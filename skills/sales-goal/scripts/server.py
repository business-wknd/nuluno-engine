#!/usr/bin/env python3
"""Nuluno Engine, local single-user MCP server (stdio). No dependencies.

    python3 server.py [--product https://your-product.com/]

Add it to any MCP client that can start a local command, for example:

    claude mcp add --scope user nuluno-engine -- python3 /path/to/engine/server.py

Without --product it uses the product given to `nuluno.py start`, or asks the agent to
call use_product with the owner's product URL.

Everything the agent delivers is kept in one JSON file per product under
~/.nuluno-engine/ (or --data DIR), so a new chat continues where the last one stopped.

Every tool in core.TOOLS is served, including the month target tools; goal tools take
lane. Approving a weekly batch or an ad budget is not a tool: the owner runs
`nuluno.py approve` or `nuluno.py approve-budget` in their own terminal.
"""
import argparse, hashlib, json, os, re, sys, tempfile, time, urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import core

VERSION = '0.3.0'
PROTOCOLS = ('2025-06-18', '2025-03-26', '2024-11-05')


class FileStore:
    """One JSON file per product: the current state plus an append-only log."""
    def __init__(self, folder):
        self.folder = Path(folder).expanduser(); self.folder.mkdir(parents=True, exist_ok=True)
        try: os.chmod(self.folder, 0o700)
        except OSError: pass

    def _path(self, owner):  # readable name plus a hash, so two products can never share a file
        return self.folder / (re.sub(r'[^a-z0-9.-]+', '-', owner.lower()).strip('-')[:60] + '-' + hashlib.sha256(owner.encode()).hexdigest()[:8] + '.json')

    def _read(self, owner):
        path = self._path(owner)
        legacy = self.folder / (re.sub(r'[^a-z0-9.-]+', '-', owner.lower()).strip('-')[:80] + '.json')  # file name used by 0.1.0
        if not path.exists() and legacy.exists(): legacy.rename(path)
        return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'state': core.new_state(), 'log': []}

    def _write(self, owner, data):
        path = self._path(owner)
        handle, temporary = tempfile.mkstemp(dir=str(self.folder), suffix='.tmp')
        with os.fdopen(handle, 'w', encoding='utf-8') as out: json.dump(data, out, ensure_ascii=False, indent=1)
        os.replace(temporary, path)

    def load(self, owner): return self._read(owner)['state']

    def save(self, owner, state):
        data = self._read(owner); data['state'] = state; self._write(owner, data)

    def log(self, owner, round_number, node, kind, content):
        data = self._read(owner)
        digest = hashlib.sha256(json.dumps(content, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        data['log'].append({'round': round_number, 'node': node, 'kind': kind, 'content': content, 'sha256': digest, 'created': time.time()})
        self._write(owner, data)
        return digest[:16]

    def outputs(self, owner, limit):
        rows = [row for row in self._read(owner)['log'] if row['kind'] == 'output']
        return list(reversed(rows))[:limit]

    def count_outputs(self, owner):  # outputs of the current goal only, as on the hosted service
        data = self._read(owner); since = (data['state'].get('goal') or {}).get('set_at') or 0
        return sum(1 for row in data['log'] if row['kind'] == 'output' and row.get('created', 0) >= since)

    def last_blocked(self, owner):
        rows = [row for row in self._read(owner)['log'] if row['kind'] == 'blocked']
        return rows[-1] if rows else None


def check_product(url):
    """The product must be a public https URL; returns it unchanged or exits with the reason."""
    parts = urllib.parse.urlsplit(str(url))
    if parts.scheme != 'https' or not parts.hostname or '.' not in parts.hostname or parts.username or parts.password or re.search(r'\s', str(url)):
        raise SystemExit('The product must be a public https URL, for example https://your-product.com/')
    return str(url)


def owner_of(product): return re.sub(r'^https?://', '', product).strip('/')


def saved_product(store):
    path = store.folder / 'current-product'
    return path.read_text(encoding='utf-8').strip() if path.exists() else None


def save_product(store, product): (store.folder / 'current-product').write_text(product + '\n', encoding='utf-8')


USE_PRODUCT = {'name': 'use_product', 'description': 'Set the product to sell: its public https URL. Needed once; later conversations remember it.',
               'inputSchema': {'type': 'object', 'properties': {'url': {'type': 'string'}}, 'required': ['url'], 'additionalProperties': False}}


def serve(product, store):
    fixed = product
    def reply(message_id, result=None, error=None):
        body = {'jsonrpc': '2.0', 'id': message_id}
        body.update({'error': error} if error else {'result': result})
        sys.stdout.write(json.dumps(body, ensure_ascii=False) + '\n'); sys.stdout.flush()
    for stream in (sys.stdin, sys.stdout):  # the library is UTF-8 whatever the system locale says (Windows)
        if hasattr(stream, 'reconfigure'): stream.reconfigure(encoding='utf-8')
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try: message = json.loads(line)
        except ValueError:
            reply(None, error={'code': -32700, 'message': 'Parse error'}); continue
        if not isinstance(message, dict):
            reply(None, error={'code': -32600, 'message': 'Send one JSON-RPC object per line; batches are not supported.'}); continue
        method, message_id, params = message.get('method'), message.get('id'), message.get('params')
        if not isinstance(method, str) or message_id is None: continue  # notifications and stray responses need no answer
        if not isinstance(params, dict): params = {}
        if method == 'initialize':
            asked = params.get('protocolVersion')
            reply(message_id, {'protocolVersion': asked if asked in PROTOCOLS else PROTOCOLS[0], 'capabilities': {'tools': {}},
                               'serverInfo': {'name': 'nuluno-engine', 'version': VERSION}, 'instructions': core.INSTRUCTIONS})
        elif method == 'ping':
            reply(message_id, {})
        elif method == 'tools/list':
            reply(message_id, {'tools': core.TOOL_SPECS + ([] if fixed else [USE_PRODUCT])})
        elif method == 'tools/call':
            name, arguments = params.get('name'), params.get('arguments')
            if not isinstance(arguments, dict): arguments = {}
            if not fixed and name == 'use_product':
                try: chosen = check_product(str(arguments.get('url', '')).strip())
                except SystemExit as error: value = {'accepted': False, 'error': str(error)}
                else:
                    save_product(store, chosen)
                    value = {'accepted': True, 'product_url': chosen, 'next': core.where_are_we(store, owner_of(chosen), chosen, {})}
                reply(message_id, {'content': [{'type': 'text', 'text': json.dumps(value, ensure_ascii=False)}], 'structuredContent': value, 'isError': False}); continue
            if not isinstance(name, str) or name not in core.TOOLS:
                reply(message_id, error={'code': -32602, 'message': 'Unknown tool: ' + str(name)}); continue
            product = fixed or saved_product(store)
            if not product:
                value = {'state': 'no_product_yet', 'instruction': 'Ask the owner for the public https URL of the product to sell, then call use_product with it.'}
                reply(message_id, {'content': [{'type': 'text', 'text': json.dumps(value)}], 'structuredContent': value, 'isError': False}); continue
            try:
                value = core.TOOLS[name](store, owner_of(product), product, arguments)
                reply(message_id, {'content': [{'type': 'text', 'text': json.dumps(value, ensure_ascii=False, allow_nan=False)}], 'structuredContent': value, 'isError': False})
            except Exception as error:  # the agent gets a readable failure instead of a dead connection
                reply(message_id, {'content': [{'type': 'text', 'text': json.dumps({'error': type(error).__name__ + ': ' + str(error)[:300]})}], 'isError': True})
        else:
            reply(message_id, error={'code': -32601, 'message': 'Method not found: ' + str(method)})


def main():
    parser = argparse.ArgumentParser(description='Nuluno Engine local MCP server')
    parser.add_argument('--product', help='public https URL of the product to sell (default: the saved one, or ask)')
    parser.add_argument('--data', default='~/.nuluno-engine', help='folder for saved progress')
    args = parser.parse_args()
    serve(check_product(args.product) if args.product else None, FileStore(args.data))


if __name__ == '__main__':
    main()
