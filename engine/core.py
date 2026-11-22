"""Nuluno Engine core: a guided sales loop for a connected AI agent.

The agent (Claude, ChatGPT, ...) does the work. The engine keeps the goal, the
playbook, every delivered result and the numbers, and always answers "what is
the next step". A goal ends only when recorded numbers reach the target;
otherwise the engine opens another round that changes exactly one thing.

This module has no dependencies and no storage of its own. A store object
provides: load(owner), save(owner, state), log(owner, round, node, kind,
content) -> receipt, outputs(owner, limit), count_outputs(owner),
last_blocked(owner).

A store may also measure for itself (the hosted service does): tracked_link(owner,
round, target) -> a redirect URL that counts human clicks, sale_counter(owner) -> a
URL that counts one sale per visit, and measured(owner, since, until, round) ->
{'clicks', 'sales', 'revenue_minor'}. With those, numbers the engine can count are never typed
in by the agent, and a round whose metric is fully countable is judged with no one
reading anything.
"""
import hashlib, ipaddress, json, math, re, socket, time, urllib.error, urllib.parse, urllib.request
from functools import lru_cache
from pathlib import Path

LIBRARY_PATH = Path(__file__).resolve().parent / 'library.json'
MAX_OUTPUT = 20000
DEFAULT_RELATIVE_GAIN = 0.2

# Goals most people mean when they say "help me sell this", by channel.
STARTERS = ['G-TH-LINK-RATE', 'G-IG-LINK-RATE', 'G-X-LINK-RATE', 'G-RD-PURCHASES', 'G-PH-LAUNCH-PURCHASE', 'G-EM-PURCHASE', 'G-META-PURCHASE-CPA', 'G-AUD-PURCHASE']

RULES = [
    'Decide what an expert marketer would decide. Do not ask the owner for things you can work out (audience, angle, sample size, timing).',
    'Use only product facts you actually read. Unknown price or results stay unknown; never invent numbers or testimonials.',
    'Ask the owner only for what needs a person: logging in, approving text before it is published, numbers only they can see.',
    'When a step is finished call submit_step immediately, then continue with the step it returns.',
]


# Metric components the engine can count itself when the store measures.
ENGINE_COUNTS = {'link_clicks': 'clicks', 'unique_link_clicks': 'clicks', 'url_clicks': 'clicks', 'website_clicks': 'clicks', 'outbound_clicks': 'clicks',
                 'attributed_sessions': 'clicks', 'external_purchases': 'sales'}


# ---------- library ----------

@lru_cache(maxsize=1)
def library():
    return json.loads(LIBRARY_PATH.read_text(encoding='utf-8'))


def goals():
    return library()['goals']


def skill(skill_id):
    found = library()['skills'].get(skill_id)
    if found: return found
    return {'title': skill_id, 'purpose': '', 'steps': [], 'deliver': ['result'], 'blockers': [], 'needs_link': False, 'writes': False, 'identity': False}


def plan_for(goal_id):
    return [dict(node) for node in goals()[goal_id]['plan']]


def goal_status(goal_id):
    """in_live_test: being run on a real product. rewritten_not_run: every step is in plain language but the goal has not been run. experimental: generated draft."""
    goal = goals()[goal_id]
    if goal.get('live_test'): return 'in_live_test'
    return 'rewritten_not_run' if all(skill(n['skill']).get('tested') for n in goal['plan']) else 'experimental'


def new_state():
    return {'status': 'no_goal', 'round': 0, 'nodes': [], 'cursor': 0, 'rounds': [], 'sources': []}


def _recent(store, owner, limit_chars=9000):
    """What has been delivered so far, oldest first, trimmed so the agent can re-read it."""
    out, used = [], 0
    for row in store.outputs(owner, 14):
        text = json.dumps(row['content'].get('output'), ensure_ascii=False)
        text = text[:1400] + ('…' if len(text) > 1400 else '')
        used += len(text)
        if used > limit_chars: break
        out.append({'round': row['round'], 'step': row['node'], 'title': row['content'].get('title'), 'output': text, 'links': row['content'].get('links') or []})
    return list(reversed(out))


# ---------- metric ----------

def _num(value):
    """A real, finite number. True/False, NaN and infinity are not measurements."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _metric(goal, values):
    spec = goal['metric']; parts = spec['components']
    if any(not _num(values.get(p)) for p in parts): return None
    if spec['formula'] == 'count': return float(values[parts[0]])
    top, bottom = float(values[parts[0]]), float(values[parts[1]])
    return None if bottom == 0 else top / bottom


def _verdict(goal, state, value, counted_this_round=False):
    """Did the round reach the target. counted_this_round: the count came from the engine's own counter, which
    starts at zero when the round is published, so it already is the gain and no baseline is subtracted."""
    spec = goal['metric']; target = state['goal'].get('target'); base = (state.get('baseline') or {}).get('metric')
    up = spec['direction'] == 'increase'
    if value is None:
        return False, {'value': None, 'note': 'The denominator is zero after the observation window: nothing happened to measure, so the round counts as a miss.'}
    if spec['formula'] == 'count':
        gained = value if counted_this_round else value - (base or 0.0)
        need = target if target is not None else 10.0
        return gained >= need, {'gained': gained, 'needed_gain': need}
    if target is not None:
        return (value >= target if up else value <= target), {'value': value, 'target': target}
    if base in (None, 0):
        return False, {'value': value, 'target': None, 'note': 'There was no baseline to beat and no target, so this round becomes the baseline. The next round has to beat it by 20%, or set a target with set_goal.'}
    needed = base * (1 + DEFAULT_RELATIVE_GAIN) if up else base * (1 - DEFAULT_RELATIVE_GAIN)
    return (value >= needed if up else value <= needed), {'value': value, 'baseline': base, 'needed': needed, 'rule': '20% better than baseline'}


def _window_end(state):
    """Counting stops at the end of the observation window, whoever judges the round and whenever they do it."""
    end = state.get('wait_until')
    return min(end, time.time()) if end else time.time()


def _counted(store, owner, state, until=None):
    """What the store counted for the current round since it was published, or None when the store does not measure."""
    since = state.get('published_at') or state.get('round_published_at')
    if not hasattr(store, 'measured') or not since: return None
    return store.measured(owner, since, until or _window_end(state), state['round'])


def _in_place(store, owner, state, counted):
    """Which counters have evidence of being in place. A zero only means zero when the tracked link was really used
    in what was published, or the sale counter has ever fired; otherwise the number must be read from the platform."""
    if counted is None: return {}
    proven = {}
    link = store.tracked_link(owner, state['round'], '')
    used = bool(link) and any(row['round'] == state['round'] and link in json.dumps(row['content'], ensure_ascii=False) for row in store.outputs(owner, 14))
    if counted['clicks'] > 0 or used: proven['clicks'] = counted['clicks']
    if counted['sales'] > 0 or store.measured(owner, 0, time.time(), None)['sales'] > 0: proven['sales'] = counted['sales']
    return proven


def _countable(goal, proven):
    """Metric components the engine can fill in itself, by component name."""
    return {part: proven[ENGINE_COUNTS[part]] for part in goal['metric']['components'] if ENGINE_COUNTS.get(part) in proven}


def _start_window(state, goal):
    """Every result is read after a waiting period. It starts when something was published, or now when the
    playbook publishes nothing (research goals)."""
    state['published_at'] = state.get('published_at') or time.time()
    state.update(status='observing', wait_until=state['published_at'] + goal.get('observation_seconds', 172800))


def _close_round(store, owner, state, goal, node, reading, counted):
    """Judge the round on a final reading. Steps that come after the result in the playbook (pause the ads, the next
    channel) are still handed out; the verdict takes effect when they are done."""
    value = reading['metric']
    reached, detail = _verdict(goal, state, value, goal['metric']['components'][0] in (reading.get('engine_counted') or []))
    state['current'] = reading
    store.log(owner, state['round'], node['node'], 'numbers', {'role': 'current', **reading, 'reached': reached, 'detail': detail})
    entry = {'round': state['round'], 'metric': value, 'baseline': (state.get('baseline') or {}).get('metric'), 'verdict': 'reached' if reached else 'missed', 'detail': detail, 'at': time.time()}
    if counted is not None: entry['counted_by_engine'] = counted
    state['rounds'].append(entry)
    verdict = 'reached' if reached else 'diagnose'
    state.update(wait_until=None, round_published_at=state.get('published_at'), published_at=None)
    if state['cursor'] + 1 < len(state['nodes']): state.update(status='working', cursor=state['cursor'] + 1, after=verdict)
    else: state.update(status=verdict, after=None)
    store.save(owner, state)
    return reached, detail


def auto_judge(store, owner, product):
    """Called by a host on a timer. When the observation window is over and every number in the metric is one the
    engine counts itself, the round is judged without anyone reading anything. Returns what happened, or None."""
    state = store.load(owner)
    if state['status'] != 'observing' or time.time() < state.get('wait_until', 0): return None
    goal = goals()[state['goal']['id']]; node = state['nodes'][state['cursor']]
    if node['measure'] != 'current': return None
    counted = _counted(store, owner, state); values = _countable(goal, _in_place(store, owner, state, counted))
    if len(values) < len(goal['metric']['components']):
        if state.get('asked_round') == state['round']: return None
        state['asked_round'] = state['round']; store.save(owner, state)
        return {'event': 'numbers_needed', 'round': state['round'], 'goal': goal['title'], 'counted_by_engine': counted,
                'still_needed': [p for p in goal['metric']['components'] if p not in values]}
    reading = {'values': values, 'metric': _metric(goal, values), 'source': 'Counted by the engine: tracked link and sale counter', 'at': time.time(), 'engine_counted': sorted(values)}
    round_number = state['round']
    reached, detail = _close_round(store, owner, state, goal, node, reading, counted)
    return {'event': 'round_judged', 'round': round_number, 'goal': goal['title'], 'reached': reached, 'metric': reading['metric'], 'detail': detail, 'counted_by_engine': counted}


# ---------- reading ----------

def _public_host(host):
    try: infos = socket.getaddrinfo(host, 443, proto=socket.IPPROTO_TCP)
    except OSError: return False
    return bool(infos) and all(ipaddress.ip_address(info[4][0]).is_global for info in infos)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs): return None


def fetch_public(url, limit=400000):
    """Bounded read of one public https page. Redirects are followed by hand so each hop is checked."""
    opener = urllib.request.build_opener(_NoRedirect)
    for _ in range(4):
        parts = urllib.parse.urlsplit(url)
        if parts.scheme != 'https' or not parts.hostname or parts.username or parts.port not in (None, 443) or not _public_host(parts.hostname):
            raise ValueError('Only public https pages can be read.')
        request = urllib.request.Request(url, headers={'user-agent': 'NulunoEngine/1.0 (+https://engine.nuluno.com)', 'accept': 'text/html,text/plain;q=0.9,*/*;q=0.5'})
        try:
            with opener.open(request, timeout=15) as response:
                return response.status, response.headers.get_content_type(), response.read(limit), url
        except urllib.error.HTTPError as error:
            if error.code in (301, 302, 303, 307, 308) and error.headers.get('location'):
                url = urllib.parse.urljoin(url, error.headers['location']); continue
            return error.code, '', b'', url
    raise ValueError('Too many redirects.')


_SKIPPED = ('script', 'style', 'noscript', 'svg', 'template')
_BREAKS = ('br', 'p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'section', 'article', 'header', 'footer')
_TAG = re.compile(r'<(/?)([a-z][a-z0-9]*)')
_LOWER = {code: code + 32 for code in range(65, 91)}


def _strip_html(text):
    """Text of an HTML page in one forward pass. Every search starts where the last one ended, so a page built to
    be slow to parse (thousands of unclosed tags) costs the same as an ordinary page of that size."""
    low = text.translate(_LOWER)  # same length as text, so positions match
    out, title, at, size = [], '', 0, len(text)
    while at < size:
        lt = text.find('<', at)
        if lt < 0: out.append(text[at:]); break
        out.append(text[at:lt])
        if low.startswith('<!--', lt):
            end = text.find('-->', lt + 4); at = size if end < 0 else end + 3; continue
        tag = _TAG.match(low, lt)
        if not tag: out.append('<'); at = lt + 1; continue
        gt = text.find('>', tag.end())
        if gt < 0: break  # an unfinished tag: nothing readable follows
        at = gt + 1; name = tag.group(2)
        if tag.group(1): out.append('\n' if name in _BREAKS else ' ')
        elif name in _SKIPPED or name == 'title':
            end = low.find('</' + name, at)
            if name == 'title' and not title: title = text[at:end if end >= 0 else at + 300]
            at = size if end < 0 else end
        else: out.append('\n' if name == 'br' else ' ')
    return title, ''.join(out)


def _readable(raw, kind):
    import html as _html
    text = raw.decode('utf-8', 'replace')
    if 'html' in kind or '<html' in text[:2000].lower():
        title, text = _strip_html(text)
        text = (('# ' + _html.unescape(title).strip() + '\n') if title.strip() else '') + _html.unescape(text)
    lines = [' '.join(line.split()) for line in text.split('\n')]
    return '\n'.join(line for line in lines if line)


def _link_live(url):
    try:
        status, _, _, _ = fetch_public(url, limit=2000)
        return 200 <= status < 400
    except Exception:
        return False


# ---------- steps ----------

def _step(store, owner, product, state):
    goal = goals()[state['goal']['id']]
    if state['status'] == 'reached':
        return {'state': 'goal_reached', 'message': 'The goal is reached and recorded. Tell the owner the result, then offer the next goal with set_goal.', 'result': state['rounds'][-1] if state['rounds'] else None}
    if state['status'] == 'stopped':
        return {'state': 'stopped', 'message': 'This goal was stopped by the owner. Use set_goal to start again.'}
    if state['status'] == 'observing' and time.time() < state.get('wait_until', 0):
        return {'state': 'waiting_for_results', 'come_back_at': state['wait_until'], 'come_back_at_text': time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(state['wait_until'])),
                'message': 'The post is live and results need time. Do not publish a new variant yet (one change per round). Until then: answer real replies, and tell the owner exactly when you will read the numbers.',
                'early_numbers': 'If the owner already has numbers you may call record_numbers now; they are stored as interim and do not end the round.',
                'counted_by_engine_so_far': _counted(store, owner, state)}
    if state['status'] == 'diagnose':
        last = state['rounds'][-1]
        return {'state': 'target_missed_choose_one_change', 'step_id': 'diagnose:r%d' % state['round'], 'numbers': last,
                'instruction': 'The target was not reached. Look at the numbers and everything delivered so far, pick the single most likely bottleneck, and say what one thing you will change next round. Do not repeat a variant that was already tried.',
                'choose_bottleneck_from': list(goal['bottleneck_routes'].keys()),
                'deliver': {'bottleneck': 'one of the keys above', 'reason': 'evidence from the numbers', 'one_change': 'the single variable that changes next round'},
                'already_tried': [r.get('change') for r in state['rounds'] if r.get('change')], 'delivered_so_far': _recent(store, owner, 6000), 'rules': RULES}
    node = state['nodes'][state['cursor']]; info = skill(node['skill'])
    step = {'state': 'work', 'step_id': '%s:r%d' % (node['node'], state['round']), 'progress': '%d of %d steps in round %d' % (state['cursor'] + 1, len(state['nodes']), state['round']),
            'title': info['title'], 'title_local': info.get('title_zh'), 'purpose': info['purpose'], 'product_url': product,
            'goal': {'title': goal['title'], 'metric': goal['metric'], 'target': state['goal'].get('target')}}
    if node['measure']:
        parts = goal['metric']['components']
        step.update(instruction=('Read the numbers BEFORE anything is published (baseline).' if node['measure'] == 'baseline' else 'Read the numbers for the same account and period AFTER the observation window.')
                    + ' Get them from the platform\'s own insights (your tools, or ask the owner to read them). Then call record_numbers with values for: ' + ', '.join(parts) + '. If the account is new and has no history, record zeros and say so in source.',
                    call='record_numbers', values_needed=parts, checklist=info['steps'])
        counted = _counted(store, owner, state) if node['measure'] == 'current' else None
        if _countable(goal, _in_place(store, owner, state, counted)):
            step['counted_by_engine'] = _countable(goal, _in_place(store, owner, state, counted))
            step['instruction'] += ' The engine already counted these itself from the tracked link and sale counter, so leave them out (the count made by the engine is the one that is used): ' + ', '.join(step['counted_by_engine']) + '.'
            step['values_needed'] = [p for p in parts if p not in step['counted_by_engine']]
    else:
        step.update(instruction='Do this step for the product now, in order, then call submit_step with the deliverables as a JSON object.',
                    checklist=info['steps'], deliver=info['deliver'] or ['result'], if_blocked=info['blockers'], publishes=info['needs_link'])
        if info.get('deliver_help'): step['deliver_help'] = info['deliver_help']
        step['deliver_note'] = 'Fill every key with what you actually have. If a key does not apply to how the work was done, write "not applicable" and why.'
        if info['identity']:
            step['needs_a_person'] = 'This step is about the owner\'s own account. Ask the owner to confirm the account and that they are logged in; never ask for a password. If a new sign-up needs an email, inbox_address (hosted service) gives you one and inbox_latest returns the verification code.'
        if info['needs_link']:
            step['publishing'] = 'This step puts something in public. Show the owner the exact text first. Publish with your own tools if you have them, otherwise the owner posts it. After it is live, pass the public URL in links so the engine can read it back.'
        elif info['writes']:
            step['publishing'] = 'This step changes or sends something outside. Show the owner exactly what will be sent before it goes out.'
        if not info['identity'] and hasattr(store, 'tracked_link'):
            step['tracked_link'] = {'url': store.tracked_link(owner, state['round'], product),
                                    'use': 'Whenever this round\'s copy, post or message points to the product, use this link instead of the bare URL, and keep it in what you deliver. It forwards to the product page and the engine counts real human clicks itself. Add ?p=/some/page to land on another page of the same site. If a redirect link is not acceptable on this platform, use the product URL and read clicks from the platform instead.'}
    lessons = [{'round': r['round'], 'change': r.get('change'), 'metric': r.get('metric'), 'verdict': r.get('verdict')} for r in state['rounds']]
    step.update(delivered_so_far=_recent(store, owner), sources_read=state.get('sources', [])[-6:], lessons_from_earlier_rounds=lessons, rules=RULES)
    return step


# ---------- tools ----------

def where_are_we(store, owner, product, args):
    state = store.load(owner)
    if state['status'] == 'no_goal':
        catalog = goals()
        return {'state': 'no_goal_yet', 'product_url': product,
                'instruction': 'Read the product page with read_page, decide which goal fits what the owner wants to sell, propose it in one sentence, and call set_goal. Pick for them; do not show this whole list.',
                'good_first_goals': [{'goal_id': g, 'title': catalog[g]['title'], 'metric': catalog[g]['metric']['key'], 'status': goal_status(g)} for g in STARTERS if g in catalog],
                'all_goals': [{'goal_id': gid, 'title': g['title']} for gid, g in catalog.items()], 'rules': RULES}
    goal = goals()[state['goal']['id']]
    blocked = store.last_blocked(owner); waiting_on_owner = None
    if blocked and state['status'] == 'working' and blocked.get('round') == state['round'] and blocked['node'] == state['nodes'][state['cursor']]['node']:
        waiting_on_owner = {'step': blocked['node'], 'needs': blocked['content'].get('needs'), 'since': blocked['created']}
    return {'state': state['status'], 'product_url': product, 'goal': {'goal_id': state['goal']['id'], 'title': goal['title'], 'title_local': goal.get('title_zh'), 'metric': goal['metric'], 'target': state['goal'].get('target')},
            'round': state['round'], 'steps_delivered': store.count_outputs(owner), 'baseline': state.get('baseline'), 'latest_numbers': state.get('current'), 'rounds': state['rounds'],
            'waiting_on_owner': waiting_on_owner, 'next': _step(store, owner, product, state)}


def set_goal(store, owner, product, args):
    goal_id = str(args.get('goal_id', '')).strip()
    if goal_id not in goals(): return {'accepted': False, 'error': 'Unknown goal_id. Call where_are_we to see the list.'}
    target = args.get('target')
    if target is not None and not _num(target): return {'accepted': False, 'error': 'target must be a finite number, or omitted.'}
    state = store.load(owner)
    if state.get('goal', {}).get('id') == goal_id and state['status'] not in ('reached', 'stopped'):
        state['goal']['target'] = target if target is not None else state['goal'].get('target')  # same goal: only the target changes
    else:
        state.update(status='working', goal={'id': goal_id, 'target': target, 'set_at': time.time()}, round=1, nodes=plan_for(goal_id), cursor=0, rounds=[], baseline=None, current=None, wait_until=None,
                     published_at=None, round_published_at=None, asked_round=None, after=None)
        store.log(owner, 1, 'goal', 'goal', {'goal_id': goal_id, 'target': target, 'why': str(args.get('why', ''))[:1000]})
    store.save(owner, state)
    return {'accepted': True, 'goal': goals()[goal_id]['title'], 'target': state['goal'].get('target'),
            'target_rule': 'With no target, a round succeeds when the metric is 20% better than baseline (counts: +10).', 'next': _step(store, owner, product, state)}


def next_step(store, owner, product, args):
    state = store.load(owner)
    if state['status'] == 'no_goal': return where_are_we(store, owner, product, args)
    return _step(store, owner, product, state)  # reading the step never changes the state


def submit_step(store, owner, product, args):
    state = store.load(owner)
    if state['status'] == 'no_goal': return {'accepted': False, 'error': 'No goal yet. Call set_goal first.'}
    step_id = str(args.get('step_id', '')); status = args.get('status', 'done'); output = args.get('output')
    if isinstance(output, str):
        try: output = json.loads(output)
        except ValueError: output = {'result': output}
    if len(json.dumps(output, ensure_ascii=False)) > MAX_OUTPUT: return {'accepted': False, 'error': 'output is too long; keep it under %d characters.' % MAX_OUTPUT}
    goal = goals()[state['goal']['id']]
    if state['status'] == 'diagnose':
        if step_id != 'diagnose:r%d' % state['round']: return {'accepted': False, 'error': 'A different step is current.', 'next': _step(store, owner, product, state)}
        if not isinstance(output, dict) or output.get('bottleneck') not in goal['bottleneck_routes'] or not isinstance(output.get('one_change'), str) or not output['one_change'].strip():
            return {'accepted': False, 'error': 'Deliver a JSON object with bottleneck (one of %s), reason and one_change.' % ', '.join(goal['bottleneck_routes'])}
        choice = output['bottleneck']; same = lambda text: ' '.join(str(text).lower().split())
        repeated = next((r['round'] for r in state['rounds'] if r.get('change') and same(r['change']) == same(output['one_change'][:500])), None)
        if repeated: return {'accepted': False, 'error': 'That change was already tried after round %d. Name a different one.' % repeated, 'already_tried': [r.get('change') for r in state['rounds'] if r.get('change')]}
        store.log(owner, state['round'], 'diagnose', 'output', {'title': 'Why the target was missed', 'output': output})
        stage = [n for n in plan_for(state['goal']['id']) if '.common.' not in n['node'] and 'ACCESS' not in n['skill'] and n['measure'] != 'baseline']
        route = goal['bottleneck_routes'][choice]
        state['rounds'][-1]['change'] = str(output['one_change'])[:500]
        state.update(round=state['round'] + 1, status='working', cursor=0, baseline=state.get('current'), current=None, wait_until=None, round_published_at=None, after=None,
                     nodes=[{'node': 'fix.' + route, 'skill': route, 'measure': None}] + [n for n in stage if n['skill'] != route or n['measure']])
        store.save(owner, state)
        return {'accepted': True, 'message': 'Round %d opened with one change: %s' % (state['round'], state['rounds'][-1]['change']), 'next': _step(store, owner, product, state)}
    if state['status'] != 'working': return {'accepted': False, 'error': 'Nothing to submit right now.', 'next': _step(store, owner, product, state)}
    node = state['nodes'][state['cursor']]; info = skill(node['skill'])
    if step_id != '%s:r%d' % (node['node'], state['round']):
        return {'accepted': False, 'error': 'That step is not the current one (it may already be recorded). Continue with the step below.', 'next': _step(store, owner, product, state)}
    if node['measure']: return {'accepted': False, 'error': 'This step needs numbers. Call record_numbers.', 'next': _step(store, owner, product, state)}
    if status == 'blocked':
        needs = str(args.get('needs') or args.get('blocker') or '')[:1000]
        if not needs: return {'accepted': False, 'error': 'Say in needs exactly what the owner must do, in one sentence.'}
        store.log(owner, state['round'], node['node'], 'blocked', {'title': info['title'], 'needs': needs})
        return {'accepted': True, 'state': 'waiting_on_owner', 'tell_the_owner': needs,
                'message': 'Recorded. The step stays open and nothing is lost. Ask the owner for exactly this one thing, then finish the step and submit it as done.'}
    missing = [key for key in info['deliver'] if not (isinstance(output, dict) and output.get(key) not in (None, '', [], {}))]
    if missing: return {'accepted': False, 'error': 'Deliverables missing: ' + ', '.join(missing) + '. Submit output as a JSON object with these keys.', 'deliver': info['deliver']}
    links = [str(u)[:600] for u in (args.get('links') or []) if isinstance(u, str)][:5]
    checked = None
    if info['needs_link']:
        if not links or not links[0].startswith('https://'):
            return {'accepted': False, 'error': 'This step publishes something. Pass the public https URL of what went live in links. If it is not live yet, submit status "blocked" with what the owner must do.'}
        checked = _link_live(links[0])
    receipt = store.log(owner, state['round'], node['node'], 'output', {'title': info['title'], 'output': output, 'links': links, 'link_read_back': checked})
    last = state['cursor'] + 1 >= len(state['nodes'])
    state['cursor'] = min(state['cursor'] + 1, len(state['nodes']) - 1)
    if last and state.get('after'):  # the steps after the result are done: the recorded verdict takes effect
        state.update(status=state['after'], after=None, published_at=None)
    else:
        if info['needs_link'] or (info['writes'] and not info['identity']): state['published_at'] = time.time()
        following = state['nodes'][state['cursor']]
        if following['measure'] == 'current' and not last: _start_window(state, goal)
    store.save(owner, state)
    return {'accepted': True, 'receipt': receipt, 'link_read_back': checked, 'next': _step(store, owner, product, state)}


def record_numbers(store, owner, product, args):
    state = store.load(owner)
    if state['status'] in ('no_goal', 'reached', 'stopped', 'diagnose'): return {'accepted': False, 'error': 'No measurement is expected right now.', 'next': next_step(store, owner, product, {})}
    goal = goals()[state['goal']['id']]; values = args.get('values') or {}; source = str(args.get('source', ''))[:500]
    if not isinstance(values, dict) or not source: return {'accepted': False, 'error': 'Pass values (numbers by name) and source (where the numbers were read).'}
    parts = goal['metric']['components']; node = state['nodes'][state['cursor']]
    counted = _counted(store, owner, state) if node['measure'] == 'current' else None
    # A number the engine counted itself is the one that is used; what the agent typed for it is kept only as a note.
    filled = _countable(goal, _in_place(store, owner, state, counted))
    typed = {part: values[part] for part in filled if _num(values.get(part)) and values[part] != filled[part]}
    values = {**values, **filled}
    lacking = [p for p in parts if not _num(values.get(p))]
    if lacking: return {'accepted': False, 'error': 'Missing numbers: ' + ', '.join(lacking) + '. Each must be a finite number. Unknown stays unknown; do not estimate.'}
    value = _metric(goal, values)
    reading = {'values': {k: values[k] for k in values if _num(values[k])}, 'metric': value, 'source': source, 'at': time.time()}
    if filled: reading['engine_counted'] = sorted(filled)
    if typed: reading['agent_reported_instead'] = typed
    if node['measure'] == 'baseline' and state['status'] == 'working':
        state['baseline'] = reading; state['cursor'] += 1
        if state['nodes'][state['cursor']]['measure'] == 'current': _start_window(state, goal)  # the result comes straight after the baseline
        store.log(owner, state['round'], node['node'], 'numbers', {'role': 'baseline', **reading}); store.save(owner, state)
        return {'accepted': True, 'recorded_as': 'baseline', 'metric': value, 'next': _step(store, owner, product, state)}
    if node['measure'] != 'current': return {'accepted': False, 'error': 'Finish the current step first.', 'next': _step(store, owner, product, state)}
    if state['status'] == 'observing' and time.time() < state.get('wait_until', 0):
        store.log(owner, state['round'], node['node'], 'numbers', {'role': 'interim', **reading})
        return {'accepted': True, 'recorded_as': 'interim', 'metric': value, 'message': 'Stored. The round is judged after the observation window.', 'next': _step(store, owner, product, state)}
    reached, detail = _close_round(store, owner, state, goal, node, reading, counted)
    return {'accepted': True, 'recorded_as': 'result', 'metric': value, 'reached': reached, 'detail': detail, 'next': _step(store, owner, product, state)}


def read_page(store, owner, product, args):
    url = str(args.get('url') or product).strip()
    try: status, kind, raw, final = fetch_public(url)
    except ValueError as error: return {'read': False, 'error': str(error)}
    except Exception: return {'read': False, 'error': 'The page could not be reached.'}
    if not 200 <= status < 300: return {'read': False, 'http_status': status, 'url': final}
    text = _readable(raw, kind); digest = hashlib.sha256(raw).hexdigest()
    state = store.load(owner)
    entry = {'url': final, 'sha256': digest, 'read_at': time.time(), 'characters': len(text)}
    state['sources'] = ([s for s in state.get('sources', []) if s['url'] != final] + [entry])[-20:]
    store.save(owner, state)
    return {'read': True, 'url': final, 'sha256': digest, 'read_at': entry['read_at'], 'text': text[:14000], 'truncated': len(text) > 14000,
            'note': 'Quote facts from this text only. Anything not here (price, results, guarantees) is unknown.'}


def tracking(store, owner, product, args):
    """The tracked link for this round, the sale counter, and what has been counted so far."""
    if not hasattr(store, 'tracked_link'):
        return {'available': False, 'note': 'This local server does not count clicks or sales. Read numbers from the platform and pass them to record_numbers. The hosted service at https://engine.nuluno.com counts them itself.'}
    state = store.load(owner); counter = store.sale_counter(owner)
    return {'available': True, 'tracked_link': store.tracked_link(owner, max(state['round'], 1), product),
            'tracked_link_use': 'Put this link in posts, bios and messages instead of the bare product URL. Human clicks are counted; link-preview robots are not.',
            'sale_counter': {'image_tag': '<img src="' + counter + '.gif" width="1" height="1" alt="">', 'redirect_url': counter,
                             'use': 'Sales are counted when a buyer reaches the page shown after payment. Either the owner pastes image_tag into that page, or sets the payment provider\'s after-payment redirect to redirect_url (it forwards to the product page). Add ?value=<amount in cents>&order=<order id> when known. This needs the owner once; ask them only when the goal is about purchases.'},
            'counted_this_round': _counted(store, owner, state), 'counted_all_time': store.measured(owner, 0, time.time(), None)}


def stop_goal(store, owner, product, args):
    state = store.load(owner)
    if state['status'] == 'no_goal': return {'stopped': False}
    state['status'] = 'stopped'; store.log(owner, state['round'], 'goal', 'goal', {'stopped': True}); store.save(owner, state)
    return {'stopped': True, 'message': 'Stopped. Everything delivered stays on record.'}


TOOLS = {'where_are_we': where_are_we, 'set_goal': set_goal, 'next_step': next_step, 'submit_step': submit_step,
         'record_numbers': record_numbers, 'read_page': read_page, 'stop_goal': stop_goal, 'tracking': tracking}

# Tool descriptions shared by every MCP front end.
TOOL_SPECS = [
    {'name': 'where_are_we', 'description': 'START HERE in every conversation. Returns the product, the sales goal, what was delivered most recently, the numbers so far and the next step. Nothing is lost between chats.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'read_page', 'description': 'Read one public https page (default: the product page) and get its text with a content hash. Use it to collect product facts; never invent facts that are not on a page you read.',
     'inputSchema': {'type': 'object', 'properties': {'url': {'type': 'string'}}, 'additionalProperties': False}},
    {'name': 'set_goal', 'description': 'Choose the sales goal (goal_id from where_are_we). Optional numeric target for the goal metric; without one a round succeeds at 20% better than baseline. Calling it again with the same goal only changes the target.',
     'inputSchema': {'type': 'object', 'properties': {'goal_id': {'type': 'string'}, 'target': {'type': 'number'}, 'why': {'type': 'string'}}, 'required': ['goal_id'], 'additionalProperties': False}},
    {'name': 'next_step', 'description': 'Get the current step: what to do, the checklist, what to deliver, what was already delivered and lessons from earlier rounds. Call it whenever you are unsure what to do next.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'submit_step', 'description': 'Record the finished step and receive the following one. output is a JSON object with the deliverable keys the step listed. If a person is needed (login, approval), use status "blocked" and say in needs the one thing the owner must do. Publishing steps need the public URL in links.',
     'inputSchema': {'type': 'object', 'properties': {'step_id': {'type': 'string'}, 'status': {'type': 'string', 'enum': ['done', 'blocked']}, 'output': {'type': 'object'}, 'links': {'type': 'array', 'items': {'type': 'string'}}, 'needs': {'type': 'string'}}, 'required': ['step_id'], 'additionalProperties': False}},
    {'name': 'record_numbers', 'description': 'Record real numbers read from the platform (baseline before publishing, results after the observation window). values holds the metric components by name; source says where and when they were read. Numbers the engine counted itself (the step lists them) can be left out. The engine decides whether the target is reached; if not it opens another round.',
     'inputSchema': {'type': 'object', 'properties': {'values': {'type': 'object', 'additionalProperties': {'type': 'number'}}, 'source': {'type': 'string'}}, 'required': ['values', 'source'], 'additionalProperties': False}},
    {'name': 'tracking', 'description': 'Get the tracked link for this round, the sale counter for the page shown after payment, and the clicks and sales the engine has counted itself. Hosted service only; the local server answers that it does not count.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'stop_goal', 'description': 'Stop working on the current goal when the owner says so. Everything delivered stays on record.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
]

INSTRUCTIONS = ('Nuluno Engine keeps a sales goal moving across conversations. Always call where_are_we first. Then repeat: next_step, do the work yourself, submit_step. '
                'Keep going without asking the owner for things you can decide. Stop only when the engine says to wait for results, the owner must do something, or the goal is reached. '
                'Report results to the owner in their language.')
