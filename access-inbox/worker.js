// Cloudflare Email Worker for Nuluno Access agent inboxes.
// Mail to <label>.<inbox code>@nuluno.com is handed to the Nuluno host with a tag only this
// Worker can produce. The host confirms each delivery by asking this Worker's /verify endpoint
// over TLS, so the signing secret never leaves Cloudflare. Other addresses are rejected.
const ADDRESS = /^([a-z0-9][a-z0-9-]{0,31})\.([a-z0-9]{10})@nuluno\.com$/;
const hex = bytes => [...new Uint8Array(bytes)].map(b => b.toString(16).padStart(2, '0')).join('');

async function readAll(stream, limit) {
  const reader = stream.getReader(); const chunks = []; let size = 0;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    size += value.length;
    if (size > limit) { chunks.push(value.subarray(0, value.length - (size - limit))); break; }
    chunks.push(value);
  }
  const out = new Uint8Array(chunks.reduce((n, c) => n + c.length, 0)); let at = 0;
  for (const c of chunks) { out.set(c, at); at += c.length; }
  return out;
}

async function tagFor(secret, stamp, digest) {
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return hex(await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(stamp + '.' + digest)));
}

export default {
  async email(message, env) {
    const to = String(message.to || '').toLowerCase();
    if (!ADDRESS.test(to)) { message.setReject('Address not found'); return; }
    const raw = await readAll(message.raw, 256 * 1024);
    let binary = ''; for (let i = 0; i < raw.length; i += 0x8000) binary += String.fromCharCode.apply(null, raw.subarray(i, i + 0x8000));
    const body = JSON.stringify({ to, from: String(message.from || '').slice(0, 320), subject: String(message.headers.get('subject') || '').slice(0, 500), received: Date.now(), raw_base64: btoa(binary) });
    const stamp = String(Date.now());
    const digest = hex(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(body)));
    const answer = await fetch(env.HOST_ORIGIN + '/inbound/email', {
      method: 'POST', headers: { 'content-type': 'application/json', 'x-nuluno-time': stamp, 'x-nuluno-signature': await tagFor(env.INBOX_SECRET, stamp, digest) }, body,
    });
    if (answer.status === 404) { message.setReject('Address not found'); return; }
    if (!answer.ok) throw new Error('host ' + answer.status); // Cloudflare retries temporary failures.
  },
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method !== 'POST' || url.pathname !== '/verify') return new Response('Nuluno Access inbox', { status: 200 });
    let claim; try { claim = await request.json(); } catch { return Response.json({ valid: false }, { status: 400 }); }
    const { stamp, digest, tag } = claim || {};
    if (!/^\d{10,16}$/.test(stamp || '') || !/^[0-9a-f]{64}$/.test(digest || '') || !/^[0-9a-f]{64}$/.test(tag || '')) return Response.json({ valid: false });
    const expected = await tagFor(env.INBOX_SECRET, stamp, digest);
    let same = expected.length === tag.length ? 0 : 1; for (let i = 0; i < expected.length && i < tag.length; i++) same |= expected.charCodeAt(i) ^ tag.charCodeAt(i);
    return Response.json({ valid: same === 0 && Math.abs(Date.now() - Number(stamp)) < 10 * 60 * 1000 });
  },
};
