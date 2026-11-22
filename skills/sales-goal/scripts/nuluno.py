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
    python3 nuluno.py status | goals | stop

Progress is kept in ~/.nuluno-engine/ (or --data), shared with server.py, so the MCP
tools and these commands see the same goal. Every command prints JSON.
"""
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import core
from server import FileStore, check_product, owner_of, saved_product, save_product


def parse_json(text, what):
    if text.startswith('@'): text = Path(text[1:]).read_text(encoding='utf-8')
    try: value = json.loads(text)
    except ValueError as error: raise SystemExit('%s is not valid JSON: %s' % (what, error))
    if not isinstance(value, dict): raise SystemExit('%s must be a JSON object' % what)
    return value


def main(argv=None):
    parser = argparse.ArgumentParser(prog='nuluno.py', description='Nuluno Engine: work a sales goal step by step until the numbers say done.')
    parser.add_argument('--data', default='~/.nuluno-engine', help='folder for saved progress')
    parser.add_argument('--product', help='product URL (default: the one given to start)')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('start', help='remember the product and show where things stand').add_argument('url')
    sub.add_parser('status', help='the goal, the round, the numbers and the next step')
    sub.add_parser('goals', help='every goal id with its title and metric')
    sub.add_parser('read', help='read a public page (default: the product page)').add_argument('url', nargs='?')
    goal = sub.add_parser('goal', help='set the sales goal')
    goal.add_argument('goal_id'); goal.add_argument('--target', type=float); goal.add_argument('--why', default='')
    sub.add_parser('next', help='the current step')
    submit = sub.add_parser('submit', help='hand in the current step')
    submit.add_argument('step_id'); submit.add_argument('--output', help='JSON object with the keys the step asks for, or @file.json')
    submit.add_argument('--link', action='append', default=[], help='public https URL of what went live (repeatable)')
    submit.add_argument('--blocked', help='the one thing the owner must do before this step can finish')
    numbers = sub.add_parser('numbers', help='record numbers read from the platform')
    numbers.add_argument('--values', required=True, help='JSON object of numbers by name, or @file.json'); numbers.add_argument('--source', required=True)
    sub.add_parser('stop', help='stop the current goal; everything stays on record')
    args = parser.parse_args(argv)

    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'): stream.reconfigure(encoding='utf-8')
    store = FileStore(args.data)
    if args.command == 'goals':
        result = {'goals': [{'goal_id': g, 'title': v['title'], 'channel': v['channel'], 'metric': v['metric']['key'], 'wait_hours': v.get('observation_seconds', 172800) // 3600}
                            for g, v in core.goals().items()]}
        print(json.dumps(result, ensure_ascii=False, indent=1)); return
    if args.command == 'start':
        product = check_product(args.url); save_product(store, product)
    else:
        product = check_product(args.product) if args.product else saved_product(store)
        if not product: raise SystemExit('No product yet. Run: python3 nuluno.py start https://your-product.com/')
    owner = owner_of(product)
    call = lambda tool, **kw: core.TOOLS[tool](store, owner, product, kw)
    if args.command in ('start', 'status'): result = call('where_are_we')
    elif args.command == 'read': result = call('read_page', **({'url': args.url} if args.url else {}))
    elif args.command == 'goal': result = call('set_goal', goal_id=args.goal_id, why=args.why, **({'target': args.target} if args.target is not None else {}))
    elif args.command == 'next': result = call('next_step')
    elif args.command == 'submit':
        if args.blocked: result = call('submit_step', step_id=args.step_id, status='blocked', needs=args.blocked)
        else: result = call('submit_step', step_id=args.step_id, status='done', output=parse_json(args.output or '{}', '--output'), links=args.link)
    elif args.command == 'numbers': result = call('record_numbers', values=parse_json(args.values, '--values'), source=args.source)
    else: result = call('stop_goal')
    print(json.dumps(result, ensure_ascii=False, indent=1, allow_nan=False))


if __name__ == '__main__':
    main()
