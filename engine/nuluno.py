#!/usr/bin/env python3
"""Nuluno Engine from the command line: the same engine as the MCP server, for agents
that run shell commands (Claude Code, Codex, Cursor, ...) without connecting anything.

    python3 nuluno.py start https://your-product.com/
    python3 nuluno.py read
    python3 nuluno.py goal G-TH-LINK-RATE
    python3 nuluno.py next
    python3 nuluno.py submit <step_id> --output '{"key": "value"}' [--link https://...]
    python3 nuluno.py submit <step_id> --blocked "what the owner must do"
    python3 nuluno.py numbers --values '{"link_clicks": 41}' --source "where and when"
    python3 nuluno.py status | goals | tracking | stop

Progress is kept in ~/.nuluno-engine/ (or --data), shared with server.py, so the MCP
tools and these commands see the same goal. --data and --product may come before or
after the command.

Every command prints one JSON object. A refusal or error has an "error" field and
exits with a non-zero code (1 for a refusal, 2 for a mistake in the command line).
When the engine's text names an MCP tool, "cli_names" says which command to run instead.
"""
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import core
from server import FileStore, check_product, owner_of, saved_product, save_product

# The engine speaks in MCP tool names; these are the same actions on the command line.
CLI_NAMES = {
    'where_are_we': 'python3 nuluno.py status',
    'read_page': 'python3 nuluno.py read [url]',
    'set_goal': 'python3 nuluno.py goal <goal_id> [--target N] [--why "..."]',
    'next_step': 'python3 nuluno.py next',
    'submit_step': 'python3 nuluno.py submit <step_id> --output \'{...}\' [--link https://...]  or  --blocked "what the owner must do"',
    'links': '--link https://... (repeat for more; the first is the post itself)',
    'record_numbers': 'python3 nuluno.py numbers --values \'{"name": 0}\' --source "where and when"',
    'stop_goal': 'python3 nuluno.py stop',
    'tracking': 'python3 nuluno.py tracking',
    'use_product': 'python3 nuluno.py start <product url>',
    'inbox_address': 'hosted service only (https://engine.nuluno.com); no command here',
    'inbox_latest': 'hosted service only (https://engine.nuluno.com); no command here',
}


def emit(result, code=0, names=True):
    text = json.dumps(result, ensure_ascii=False, allow_nan=False)
    named = {name: cli for name, cli in CLI_NAMES.items() if (' in links' if name == 'links' else name) in text}
    if names and named and isinstance(result, dict): result = {**result, 'cli_names': named}
    print(json.dumps(result, ensure_ascii=False, indent=1, allow_nan=False))
    raise SystemExit(code)


def fail(message, code=1): emit({'error': str(message)}, code, names=False)


class Parser(argparse.ArgumentParser):
    def error(self, message): fail(message + '. Run: python3 nuluno.py --help', 2)


def parse_json(text, what):
    if text.startswith('@'):
        try: text = Path(text[1:]).read_text(encoding='utf-8')
        except (OSError, UnicodeError) as error: fail('%s file could not be read: %s' % (what, error), 2)
    try: value = json.loads(text)
    except ValueError as error: fail('%s is not valid JSON: %s' % (what, error), 2)
    if not isinstance(value, dict): fail('%s must be a JSON object' % what, 2)
    return value


def build_parser():
    common = argparse.ArgumentParser(add_help=False)  # also accepted after the command; SUPPRESS keeps a value given before it
    common.add_argument('--data', default=argparse.SUPPRESS, help='folder for saved progress (default ~/.nuluno-engine)')
    common.add_argument('--product', default=argparse.SUPPRESS, help='product URL (default: the one given to start)')
    parser = Parser(prog='nuluno.py', description='Nuluno Engine: work a sales goal step by step until the numbers say done.', parents=[common])
    sub = parser.add_subparsers(dest='command', parser_class=Parser)
    add = lambda name, text: sub.add_parser(name, help=text, parents=[common])
    add('start', 'remember the product and show where things stand').add_argument('url')
    add('status', 'the goal, the round, the numbers and the next step')
    add('goals', 'every goal id with its title and metric')
    add('read', 'read a public page (default: the product page)').add_argument('url', nargs='?')
    goal = add('goal', 'set the sales goal')
    goal.add_argument('goal_id'); goal.add_argument('--target', type=float); goal.add_argument('--why', default='')
    add('next', 'the current step')
    submit = add('submit', 'hand in the current step')
    submit.add_argument('step_id'); submit.add_argument('--output', help='JSON object with the keys the step asks for, or @file.json')
    submit.add_argument('--link', action='append', default=[], help='public https URL of the post itself (repeatable)')
    submit.add_argument('--blocked', help='the one thing the owner must do before this step can finish')
    numbers = add('numbers', 'record numbers read from the platform')
    numbers.add_argument('--values', required=True, help='JSON object of numbers by name, or @file.json'); numbers.add_argument('--source', required=True)
    add('tracking', 'the tracked link and sale counter (hosted service only; here it says it does not count)')
    add('stop', 'stop the current goal; everything stays on record')
    return parser


def run(args):
    store = FileStore(getattr(args, 'data', '~/.nuluno-engine'))
    if args.command == 'goals':
        return {'goals': [{'goal_id': g, 'title': v['title'], 'channel': v['channel'], 'metric': v['metric']['key'], 'wait_hours': v.get('observation_seconds', 172800) // 3600}
                          for g, v in core.goals().items()]}
    try:
        if args.command == 'start': product = check_product(args.url); save_product(store, product)
        else: product = check_product(args.product) if getattr(args, 'product', None) else saved_product(store)
    except SystemExit as error: fail(str(error))
    if not product: fail('No product yet. Run: python3 nuluno.py start https://your-product.com/')
    owner = owner_of(product)
    call = lambda tool, **kw: core.TOOLS[tool](store, owner, product, kw)
    if args.command in ('start', 'status'): return call('where_are_we')
    if args.command == 'read': return call('read_page', **({'url': args.url} if args.url else {}))
    if args.command == 'goal': return call('set_goal', goal_id=args.goal_id, why=args.why, **({'target': args.target} if args.target is not None else {}))
    if args.command == 'next': return call('next_step')
    if args.command == 'submit':
        if args.blocked is not None: return call('submit_step', step_id=args.step_id, status='blocked', needs=args.blocked)
        return call('submit_step', step_id=args.step_id, status='done', output=parse_json(args.output or '{}', '--output'), links=args.link)
    if args.command == 'numbers': return call('record_numbers', values=parse_json(args.values, '--values'), source=args.source)
    if args.command == 'tracking': return call('tracking')
    return call('stop_goal')


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'): stream.reconfigure(encoding='utf-8')
    args = build_parser().parse_args(argv)
    if not args.command: fail('Name a command: start, status, goals, read, goal, next, submit, numbers, tracking or stop. Run: python3 nuluno.py --help', 2)
    try: result = run(args)
    except SystemExit: raise
    except Exception as error: fail('%s: %s' % (type(error).__name__, str(error)[:300]))
    emit(result, 1 if isinstance(result, dict) and result.get('error') else 0)


if __name__ == '__main__':
    main()
