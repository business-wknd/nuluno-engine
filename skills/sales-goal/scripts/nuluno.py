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

Month target (several channels at once toward a number of paying customers):

    python3 nuluno.py target 100 --days 30 [--price 39 --currency USD] [--current-paid 0]
    python3 nuluno.py plan G-TH-LINK-RATE G-RD-PURCHASES G-EM-PURCHASE
    python3 nuluno.py month
    python3 nuluno.py next --lane G-TH-LINK-RATE      (--lane works on status, goal, next, submit, numbers, read, tracking, stop)
    python3 nuluno.py batch @week.json                (a JSON object {"items": [...], "week_of": "YYYY-MM-DD"})
    python3 nuluno.py batches
    python3 nuluno.py ad-budget 10 --currency USD --channel meta_ads

For the owner only, never for an AI agent: `approve <batch_id> --all` (or --items ...) and
`approve-budget`. They ask the owner to type yes in their own terminal.

Progress is kept in ~/.nuluno-engine/ (or --data), shared with server.py, so the MCP
tools and these commands see the same goal. --data and --product may come before or
after the command.

Every command prints one JSON object. A refusal or error has an "error" field and
exits with a non-zero code (1 for a refusal, 2 for a mistake in the command line).
When the engine's text names an MCP tool, "cli_names" says which command to run instead.
"""
import argparse, json, re, sys
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
    'set_month_target': 'python3 nuluno.py target <amount> [--days 30] [--price 39 --currency USD] [--current-paid N] [--kind revenue_minor]',
    'plan_month': 'python3 nuluno.py plan <goal_id> <goal_id> ... [--funnel \'{"visit_to_paid": 0.02}\']',
    'month_status': 'python3 nuluno.py month',
    'submit_batch': 'python3 nuluno.py batch @week.json  (a JSON object {"items": [{"lane", "kind", "channel", "text", "when"}], "week_of": "YYYY-MM-DD"})',
    'batch_status': 'python3 nuluno.py batches',
    'request_ad_budget': 'python3 nuluno.py ad-budget <daily cap> --currency USD --channel meta_ads',
    'approved_item': '--approved-item <item id> on submit',
    'lane': '--lane <goal_id> on status, goal, next, submit, numbers, read, tracking, stop',
    'inbox_address': 'hosted service only (https://engine.nuluno.com); no command here',
    'inbox_latest': 'hosted service only (https://engine.nuluno.com); no command here',
}


def emit(result, code=0, names=True):
    text = json.dumps(result, ensure_ascii=False, allow_nan=False)
    named = {name: cli for name, cli in CLI_NAMES.items() if (re.search(r'\blane\b', text) if name == 'lane' else (' in links' if name == 'links' else name) in text)}
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
    laned = lambda name, text: sub.add_parser(name, help=text, parents=[common, lane])
    lane = argparse.ArgumentParser(add_help=False)
    lane.add_argument('--lane', help='month target only: the lane (its goal id) to work on')
    add('start', 'remember the product and show where things stand').add_argument('url')
    laned('status', 'the goal, the round, the numbers and the next step')
    add('goals', 'every goal id with its title and metric')
    laned('read', 'read a public page (default: the product page)').add_argument('url', nargs='?')
    goal = laned('goal', 'set the sales goal')
    goal.add_argument('goal_id'); goal.add_argument('--target', type=float); goal.add_argument('--why', default='')
    laned('next', 'the current step')
    submit = laned('submit', 'hand in the current step')
    submit.add_argument('step_id'); submit.add_argument('--output', help='JSON object with the keys the step asks for, or @file.json')
    submit.add_argument('--link', action='append', default=[], help='public https URL of the post itself (repeatable)')
    submit.add_argument('--blocked', help='the one thing the owner must do before this step can finish')
    submit.add_argument('--approved-item', help='month target lane: id of the batch item the owner approved, when this step published exactly its text')
    numbers = laned('numbers', 'record numbers read from the platform')
    numbers.add_argument('--values', required=True, help='JSON object of numbers by name, or @file.json'); numbers.add_argument('--source', required=True)
    laned('tracking', 'the tracked link and sale counter (hosted service only; here it says it does not count)')
    laned('stop', 'stop the current goal; everything stays on record')
    target = add('target', 'month target: start one, for example 100 paying customers in 30 days')
    target.add_argument('amount', type=float); target.add_argument('--days', type=int, default=30); target.add_argument('--kind', default='paid_customers', choices=core.MONTH_KINDS)
    target.add_argument('--price', type=float, help='what one customer pays, in the main unit (39 for US$39)'); target.add_argument('--currency')
    target.add_argument('--current-paid', type=int, default=0, help='paying customers already won toward this target'); target.add_argument('--why', default='')
    target.add_argument('--replace', action='store_true', help='replace a running month target (only when the owner says so)')
    plan = add('plan', 'month target: choose 1 to 5 lanes (goal ids) and get the daily plan')
    plan.add_argument('lanes', nargs='+'); plan.add_argument('--funnel', help='JSON object of known rates, e.g. {"visit_to_paid": 0.03}, or @file.json')
    add('month', 'month target: progress, pace, each lane and the lane to work on now')
    batch = add('batch', 'month target: hand the owner a week of items to approve in one go')
    batch.add_argument('items', help='@file.json or JSON text: {"items": [...], "week_of": "YYYY-MM-DD"}')
    add('batches', 'month target: every batch and the state of each item')
    budget = add('ad-budget', 'month target: ask the owner to approve a daily ad budget cap')
    budget.add_argument('daily_cap', type=float); budget.add_argument('--currency', required=True); budget.add_argument('--channel', action='append', default=[], required=True)
    approve = add('approve', 'OWNER ONLY, never an AI agent: approve items of a weekly batch')
    approve.add_argument('batch_id'); approve.add_argument('--items', nargs='+'); approve.add_argument('--all', action='store_true')
    add('approve-budget', 'OWNER ONLY, never an AI agent: approve the requested daily ad budget cap')
    return parser


def owner_confirms(lines):
    """Approvals are the owner's: show what is approved and ask for a typed yes in the owner's own terminal.
    There is no flag that skips this. Locally it is a convention (an agent that can edit files could edit the
    saved state), not a security boundary; see SECURITY.md."""
    if not sys.stdin.isatty():
        fail('Only the owner approves, in their own terminal. Run this yourself in a terminal (it asks you to type yes). An AI agent must never approve.')
    sys.stderr.write('\n'.join(lines) + '\n\nType yes to approve: '); sys.stderr.flush()
    try: answer = input()
    except EOFError: return False
    return answer.strip().lower() == 'yes'


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
    lane = {'lane': args.lane} if getattr(args, 'lane', None) else {}
    call = lambda tool, **kw: core.TOOLS[tool](store, owner, product, dict(kw, **lane))
    if args.command == 'target':
        extra = {key: value for key, value in (('price', args.price), ('currency', args.currency)) if value is not None}
        amount = int(args.amount) if args.amount == int(args.amount) else args.amount
        return call('set_month_target', amount=amount, kind=args.kind, days=args.days, current_paid=args.current_paid, why=args.why, replace=args.replace, **extra)
    if args.command == 'plan': return call('plan_month', lanes=args.lanes, **({'funnel': parse_json(args.funnel, '--funnel')} if args.funnel else {}))
    if args.command == 'month': return call('month_status')
    if args.command == 'batch':
        given = parse_json(args.items, 'items')
        return call('submit_batch', items=given.get('items'), **({'week_of': given['week_of']} if given.get('week_of') else {}))
    if args.command == 'batches': return call('batch_status')
    if args.command == 'ad-budget': return call('request_ad_budget', daily_cap=args.daily_cap, currency=args.currency, channels=args.channel)
    if args.command == 'approve':
        if not args.all and not args.items: fail('Name the items with --items, or approve every waiting item with --all.', 2)
        batch = next((b for b in core.batch_status(store, owner, product, {})['batches'] if b['batch_id'] == args.batch_id), None)
        if not batch: fail('No batch %s. Run: python3 nuluno.py batches' % args.batch_id)
        shown = [i for i in batch['items'] if i['state'] == 'awaiting_owner' and (args.all or i['id'] in args.items)]
        lines = ['Batch %s, week of %s. You approve publishing exactly these texts:' % (batch['batch_id'], batch['week_of'])] + ['\n[%s] %s on %s%s:\n%s' % (
            i['id'], i['kind'], i['channel'], ' (' + i['when'] + ')' if i.get('when') else '', i['text']) for i in shown]
        if not owner_confirms(lines): fail('Not approved.')
        return core.approve_batch(store, owner, args.batch_id, 'all' if args.all else args.items, 'owner (command line)')
    if args.command == 'approve-budget':
        budget = (core._campaign(store, owner) or {}).get('ad_budget')
        if not budget: fail('No ad budget was requested.')
        if not owner_confirms(['You approve ads spending at most %s %.2f a day in total on %s.' % (budget['currency'], budget['daily_cap_minor'] / 100.0, ', '.join(budget['channels']))]): fail('Not approved.')
        return core.approve_ad_budget(store, owner, 'owner (command line)')
    if args.command in ('start', 'status'): return call('where_are_we')
    if args.command == 'read': return call('read_page', **({'url': args.url} if args.url else {}))
    if args.command == 'goal': return call('set_goal', goal_id=args.goal_id, why=args.why, **({'target': args.target} if args.target is not None else {}))
    if args.command == 'next': return call('next_step')
    if args.command == 'submit':
        if args.blocked is not None: return call('submit_step', step_id=args.step_id, status='blocked', needs=args.blocked)
        approved = {'approved_item': args.approved_item} if args.approved_item else {}
        return call('submit_step', step_id=args.step_id, status='done', output=parse_json(args.output or '{}', '--output'), links=args.link, **approved)
    if args.command == 'numbers': return call('record_numbers', values=parse_json(args.values, '--values'), source=args.source)
    if args.command == 'tracking': return call('tracking')
    return call('stop_goal')


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'): stream.reconfigure(encoding='utf-8')
    args = build_parser().parse_args(argv)
    if not args.command: fail('Name a command: start, status, goals, read, goal, next, submit, numbers, tracking, stop, or for a month target: target, plan, month, batch, batches, ad-budget. Run: python3 nuluno.py --help', 2)
    try: result = run(args)
    except SystemExit: raise
    except Exception as error: fail('%s: %s' % (type(error).__name__, str(error)[:300]))
    emit(result, 1 if isinstance(result, dict) and result.get('error') else 0)


if __name__ == '__main__':
    main()
