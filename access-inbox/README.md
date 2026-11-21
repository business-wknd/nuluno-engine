# Agent inbox (Cloudflare Email Worker)

Gives an AI agent email addresses it can use to sign up somewhere, and hands back only the verification code or link.

`worker.js` is the receiving half. Cloudflare Email Routing delivers mail for `<label>.<inbox code>@your-domain` to the Worker. The Worker forwards it to your host at `HOST_ORIGIN/inbound/email` with a tag made from `INBOX_SECRET`. The host confirms each delivery by calling the Worker's `/verify` endpoint over TLS, so the secret never leaves Cloudflare.

To run it on your own domain:

1. Change the domain in the `ADDRESS` pattern at the top of `worker.js`.
2. Deploy it as a Worker with two bindings: `INBOX_SECRET` (a random secret) and `HOST_ORIGIN` (your receiving service).
3. In Email Routing, send the catch-all address to this Worker. Addresses that do not match the pattern are rejected.
4. On your host, accept `POST /inbound/email`, verify with `POST <worker>/verify` (`{stamp, digest, tag}` returns `{valid}`), then keep only sender, subject, codes and links.

The hosted Nuluno service runs this for you; see [engine.nuluno.com](https://engine.nuluno.com/?lang=en).
