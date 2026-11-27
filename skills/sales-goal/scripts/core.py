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
round, target) -> a redirect URL that counts clicks from browsers, sale_counter(owner)
-> a URL that counts a sale when a buyer reaches it, and measured(owner, since, until,
round) -> {'clicks', 'sales', 'revenue_minor'}. Once a counter is shown to be in place
(the round's copy uses the tracked link, or the sale counter has recorded a sale), its
count replaces what the agent reports for that number, and when every number of a
goal is counted that way, auto_judge closes the round when its window ends.
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


# What each bottleneck usually looks like in the numbers, so the diagnosis rests on evidence rather than taste.
BOTTLENECK_SIGNS = {
    'audience': 'The wrong people, or too few of the right people, saw it: reach or views fell, or the people who replied are not buyers.',
    'motivation': 'The right people saw it but the want was weak: they read or watched but few acted, and replies talk about curiosity rather than need.',
    'angle': 'People saw it and did not care about this way of framing the benefit: views held while the action rate fell.',
    'message': 'The angle was right but the words did not land: people opened or read but did not act, or replies show they misunderstood.',
    'creative': 'The image or video did not stop people: low click-through or thumb-stop rate while targeting stayed the same.',
    'hook': 'The first seconds or first line lost people: views started but completion or read-through dropped early.',
    'format': 'The format did not suit the channel: the same message did better in another format before.',
    'content': 'The substance did not answer what people searched or asked for: they arrived and left quickly.',
    'query': 'The searches or keywords that triggered it were the wrong ones: impressions came from queries with no buying intent.',
    'delivery': 'It did not get delivered: low impressions, the ad or message was limited, held for review, or landed in spam.',
    'link_eligibility': 'People could not act: the link was missing, not clickable on this surface, or broken.',
    'fit': 'The people reached do not match what the product does for them.',
    'invite': 'The invitation itself put people off: too long, unclear time or value, or sent at the wrong moment.',
    'followup': 'Interest was there but nobody followed up in time, or the follow-up asked for too much.',
    'proof': 'People doubted it would work for them: questions about results, trust or quality went unanswered.',
    'partner': 'The partner or channel owner was the wrong fit or did not promote it.',
    'editor': 'The editor or journalist was the wrong one for the story.',
    'proposal': 'The offer to the partner was unclear or not worth it to them.',
    'program': 'The terms of the program (commission, payout, rules) did not motivate people.',
    'rules': 'Platform or community rules limited it: removed, hidden or restricted.',
    'data': 'The numbers themselves are doubtful: read from the wrong account or period, missing, or too few to compare. Fix the measurement before changing anything else.',
}


def _changes(goal, before, after):
    """Each metric component before and after, with the percentage change, as plain lines for the diagnosis."""
    lines = []
    for part in goal['metric']['components']:
        old = ((before or {}).get('values') or {}).get(part); new = ((after or {}).get('values') or {}).get(part)
        if old is None or new is None: continue
        change = ' (%+.0f%%)' % ((new - old) / old * 100) if old else ''
        lines.append('%s: %g -> %g%s' % (part, old, new, change))
    return lines


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
    """tried_on_a_live_product, english (every step in English) or english_and_chinese."""
    goal = goals()[goal_id]
    if goal.get('live_test'): return 'tried_on_a_live_product'
    return 'english' if all(skill(n['skill']).get('tested') for n in goal['plan']) else 'english_and_chinese'


def new_state():
    return {'status': 'no_goal', 'round': 0, 'nodes': [], 'cursor': 0, 'rounds': [], 'sources': []}


def _load(store, owner):
    """Load a state and bring one saved by an earlier version up to date: a result step that is waiting without a window
    (research playbooks before 0.1.1) gets one, and a window that an old next_step switched to 'working' is observed again."""
    state = store.load(owner)
    if state.get('status') == 'working' and state.get('nodes') and state['nodes'][state['cursor']]['measure'] == 'current' and not state.get('after'):
        if state.get('wait_until'): state['status'] = 'observing'
        else: _start_window(state, goals()[state['goal']['id']])
        store.save(owner, state)
    return state


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
    """A real, finite, non-negative number. True/False, NaN, infinity and negative counts are not measurements."""
    if not isinstance(value, (int, float)) or isinstance(value, bool): return False
    try: return math.isfinite(value) and value >= 0
    except OverflowError: return False  # an integer too large for a float


def _channel(node):
    """Which channel a measurement node belongs to, for playbooks that measure several channels in one round."""
    parts = node['node'].split('.')
    return parts[2] if len(parts) > 3 and parts[0] == 'flow' else ''


def _baseline_for(state, node):
    return (state.get('baselines') or {}).get(_channel(node)) or state.get('baseline')


def _metric(goal, values):
    spec = goal['metric']; parts = spec['components']
    if any(not _num(values.get(p)) for p in parts): return None
    if spec['formula'] == 'count': return float(values[parts[0]])
    top, bottom = float(values[parts[0]]), float(values[parts[1]])
    return None if bottom == 0 else top / bottom


def _verdict(goal, state, value, counted_this_round=False, baseline=None):
    """Did the round reach the target. counted_this_round: the count came from the engine's own counter, which
    starts at zero when the round is published, so it already is the gain and no baseline is subtracted."""
    spec = goal['metric']; target = state['goal'].get('target'); base = (baseline if baseline is not None else (state.get('baseline') or {})).get('metric')
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
    seconds = goal.get('observation_seconds', 172800)
    if state.get('window_cap'): seconds = min(seconds, state['window_cap'])  # a month target lane: one round a day
    state.update(status='observing', wait_until=state['published_at'] + seconds)


def _close_round(store, owner, state, goal, node, reading, counted):
    """Judge the round on a final reading. Steps that come after the result in the playbook (pause the ads, the next
    channel) are still handed out; the verdict takes effect when they are done. When one round measures several
    channels, each is compared with its own baseline and the round is reached if any channel reached it."""
    value = reading['metric']; channel = _channel(node); base = _baseline_for(state, node)
    reached, detail = _verdict(goal, state, value, goal['metric']['components'][0] in (reading.get('engine_counted') or []), base)
    state['current'] = reading; state.setdefault('currents', {})[channel] = reading
    store.log(owner, state['round'], node['node'], 'numbers', {'role': 'current', **reading, 'reached': reached, 'detail': detail})
    entry = {'round': state['round'], 'metric': value, 'baseline': (base or {}).get('metric'), 'verdict': 'reached' if reached else 'missed', 'detail': detail, 'at': time.time()}
    if counted is not None: entry['counted_by_engine'] = counted
    if sum(1 for n in state['nodes'] if n['measure'] == 'current') > 1: entry['channel'] = channel
    state['rounds'].append(entry)
    verdict = 'reached' if reached or state.get('after') == 'reached' else 'diagnose'
    state.update(wait_until=None, round_published_at=state.get('published_at'), published_at=None)
    if state['cursor'] + 1 < len(state['nodes']): state.update(status='working', cursor=state['cursor'] + 1, after=verdict)
    else: state.update(status=verdict, after=None)
    store.save(owner, state)
    return reached, detail


def auto_judge(store, owner, product):
    """Called by a host on a timer. When the observation window is over and every number in the metric is one the
    engine counts itself, the round is judged without anyone reading anything. Returns what happened, or None."""
    state = _load(store, owner)
    if state['status'] != 'observing' or time.time() < state.get('wait_until', 0): return None
    goal = goals()[state['goal']['id']]; node = state['nodes'][state['cursor']]
    if node['measure'] != 'current': return None
    counted = _counted(store, owner, state); values = _countable(goal, _in_place(store, owner, state, counted))
    if len(values) < len(goal['metric']['components']):
        if state.get('asked_window') == state['wait_until']: return None  # one reminder per observation window
        state['asked_window'] = state['wait_until']; store.save(owner, state)
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
                body, deadline = b'', time.time() + 20  # a page that trickles in slowly is cut off, not waited on
                while len(body) < limit and time.time() < deadline:
                    chunk = response.read(min(65536, limit - len(body)))
                    if not chunk: break
                    body += chunk
                return response.status, response.headers.get_content_type(), body, url
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
        if low.startswith('<!', lt) or low.startswith('<?', lt):  # <!doctype ...>, <?xml ...?>: not text
            end = text.find('>', lt + 2); at = size if end < 0 else end + 1; continue
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
    head = text[:2000].lower()
    if 'html' in kind or '<html' in head or head.lstrip().startswith('<!doctype html'):
        title, text = _strip_html(text)
        text = (('# ' + _html.unescape(title).strip() + '\n') if title.strip() else '') + _html.unescape(text)
    text = _DOCTYPE.sub('', text)
    lines = [' '.join(line.split()) for line in text.split('\n')]
    return '\n'.join(line for line in lines if line)


_DOCTYPE = re.compile(r'\A\s*<?!doctype[^>\n]*>?', re.I)
LITTLE_TEXT = 200  # fewer readable characters than this: a login wall or a page built by scripts

# Where a single post lives on each platform. A link on one of these hosts that matches none of its patterns is a
# profile, home, search or other page, not the post itself.
POST_PATTERNS = [
    (('threads.net', 'threads.com'), ('/post/',)),
    (('x.com', 'twitter.com'), ('/status/',)),
    (('reddit.com',), ('/comments/', '/s/')),
    (('instagram.com',), ('/p/', '/reel/')),
    (('tiktok.com',), ('/video/', '/photo/', '/t/')),
    (('youtube.com',), ('watch?v=', '/shorts/')),
    (('youtu.be',), ('/',)),
    (('linkedin.com',), ('/posts/', '/feed/update/', '/pulse/')),
    (('pinterest.com',), ('/pin/',)),
    (('facebook.com',), ('/posts/', '/permalink', 'story_fbid', '/share/p/', '/share/r/', '/share/v/', '/reel/', '/videos/', '/watch/?v=')),
    (('producthunt.com',), ('/posts/', '/products/')),
]
SHORT_POST_HOSTS = ('vm.tiktok.com', 'vt.tiktok.com', 'fb.watch')  # share links that each open a single post


def _platform_of(host):
    host = (host or '').lower().rstrip('.')
    for hosts, patterns in POST_PATTERNS:
        for name in hosts:
            if host == name or host.endswith('.' + name): return name, patterns
    return None, ()


def _not_a_post(url):
    """None when url can be a single post; otherwise the platform whose post pattern it misses. Each pattern must be
    followed by the post's own id or slug, so a listing such as linkedin.com/company/x/posts/ is not a post."""
    parts = urllib.parse.urlsplit(url)
    platform, patterns = _platform_of(parts.hostname)
    if not platform or (parts.hostname or '').lower().rstrip('.') in SHORT_POST_HOSTS: return None
    path = parts.path.lower()
    if platform == 'youtu.be': return None if re.match(r'/[\w-]+', path) else platform
    if platform == 'youtube.com':
        watch = path.rstrip('/') == '/watch' and any(urllib.parse.parse_qs(parts.query).get('v') or [])
        return None if watch or re.search(r'/(shorts|live|post)/[\w-]', path) else platform
    where = path + ('?' + parts.query.lower() if parts.query else '')
    return None if any(re.search(re.escape(p) + r'[^/?#&]', where) for p in patterns) else platform


def _link_live(url):
    """Open a published link. True: the page loaded with readable text. 'blocked': the link exists but the platform
    does not let robots read it (401, 403, 429, 999, a timeout, a redirect to a login page, a page built only by
    scripts). False: the link does not exist (no such host, connection refused, HTTP 404 or 410) or is not public."""
    parts = urllib.parse.urlsplit(url)
    try: socket.getaddrinfo(parts.hostname or '', 443, proto=socket.IPPROTO_TCP)
    except (OSError, UnicodeError): return False  # the host name does not exist
    if not parts.hostname or not _public_host(parts.hostname): return False
    try:
        status, kind, raw, final = fetch_public(url, limit=200000)
    except urllib.error.URLError as error:
        reason = getattr(error, 'reason', None)
        return False if isinstance(reason, (ConnectionRefusedError, socket.gaierror)) else 'blocked'
    except (ConnectionRefusedError, socket.gaierror):
        return False
    except Exception:
        return 'blocked'  # a timeout, a reset, too many redirects: the link exists, the platform did not answer a robot
    if status in (404, 410): return False
    if not 200 <= status < 400: return 'blocked'
    if final != url and re.search(r'/(log-?in|sign-?in|auth)\b', urllib.parse.urlsplit(final).path.lower()): return 'blocked'
    return True if len(_readable(raw, kind)) >= LITTLE_TEXT else 'blocked'


# ---------- steps ----------

def _waiting(store, owner, state):
    """The owner's to-do when the current step was submitted as blocked in this round and is still open, else None."""
    if state['status'] not in ('working', 'observing') or not state.get('nodes'): return None
    if state['status'] == 'observing' and time.time() < state.get('wait_until', 0): return None
    blocked = store.last_blocked(owner)
    if (blocked and blocked.get('round') == state['round'] and blocked['node'] == state['nodes'][state['cursor']]['node']
            and blocked.get('created', 0) >= state['goal'].get('set_at', 0)):
        return {'step': blocked['node'], 'needs': blocked['content'].get('needs'), 'since': blocked['created']}
    return None


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
                'instruction': 'The target was not reached. Look at the numbers and everything delivered so far, pick the single most likely bottleneck, and say what one thing you will change next round. already_tried lists every change made so far; a change worded the same as one of them is refused.',
                'choose_bottleneck_from': list(goal['bottleneck_routes'].keys()),
                'what_each_bottleneck_looks_like': {k: BOTTLENECK_SIGNS.get(k, '') for k in goal['bottleneck_routes']},
                'numbers_before_and_after': _changes(goal, state.get('baseline'), state.get('current')),
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
        step['other_numbers'] = 'Only ' + ', '.join(parts) + ' are judged. Any other numbers you pass in values (followers, replies, ...) are stored as context and are not judged.'
        step['if_blocked'] = [{'code': 'owner_must_read_numbers', 'do': 'If only the owner can read these numbers, call submit_step with this step_id, status "blocked" and needs saying exactly which numbers to read and where. Then call record_numbers when the owner gives them.'}]
    else:
        step.update(instruction='Do this step for the product now, in order, then call submit_step with the deliverables as a JSON object.',
                    checklist=info['steps'], deliver=info['deliver'] or ['result'], if_blocked=info['blockers'], publishes=info['needs_link'])
        if info.get('deliver_help'): step['deliver_help'] = info['deliver_help']
        step['deliver_note'] = 'Fill every key with what you actually have. If a key does not apply to how the work was done, write "not applicable" and why.'
        if info['identity']:
            step['needs_a_person'] = 'This step is about the owner\'s own account. Ask the owner to confirm the account and that they are logged in; never ask for a password. If a new sign-up needs an email, inbox_address (hosted service) gives you one and inbox_latest returns the verification code.'
        if info['needs_link']:
            step['publishing'] = ('This step puts something in public. Show the owner the exact text first. Publish with your own tools if you have them, otherwise the owner posts it. '
                                  'After it is live, pass the public https URL of the post itself (not the profile) as the first item in links. The engine opens it, and refuses a profile page or a link that does not exist.')
        elif info['writes']:
            step['publishing'] = 'This step changes or sends something outside. Show the owner exactly what will be sent before it goes out.'
        if not info['identity'] and hasattr(store, 'tracked_link'):
            step['tracked_link'] = {'url': store.tracked_link(owner, state['round'], product),
                                    'use': 'Whenever this round\'s copy, post or message points to the product, use this link instead of the bare URL, and keep it in what you deliver. It forwards to the product page and the engine counts the clicks itself (from browsers; known robots and link previews are left out). If you publish more than one version, give each its own label, for example ?v=A and ?v=B, and the engine counts clicks per version (the round is still judged on the total). Add ?p=/some/page to land on another page of the same site (combine with &). If a redirect link is not acceptable on this platform, use the product URL and read clicks from the platform instead.'}
    lessons = [{'round': r['round'], 'change': r.get('change'), 'metric': r.get('metric'), 'verdict': r.get('verdict')} for r in state['rounds']]
    step.update(delivered_so_far=_recent(store, owner), sources_read=state.get('sources', [])[-6:], lessons_from_earlier_rounds=lessons, rules=RULES)
    waiting = _waiting(store, owner, state)
    if waiting:
        step.update(state='waiting_on_owner', tell_the_owner=waiting['needs'], since=waiting['since'],
                    message='This step is waiting on the owner. Ask the owner for exactly this; when they answer, finish the step and submit it ('
                            + ('record_numbers' if node['measure'] else 'submit_step with status "done"') + '). The step details below stay the same.')
    return step


# ---------- tools ----------

def where_are_we(store, owner, product, args):
    state = _load(store, owner)
    if state['status'] == 'no_goal':
        catalog = goals()
        return {'state': 'no_goal_yet', 'product_url': product,
                'instruction': 'Read the product page with read_page, decide which goal fits what the owner wants to sell, propose it in one sentence, and call set_goal. Pick for them; do not show this whole list.',
                'good_first_goals': [{'goal_id': g, 'title': catalog[g]['title'], 'metric': catalog[g]['metric']['key'], 'status': goal_status(g)} for g in STARTERS if g in catalog],
                'all_goals': [{'goal_id': gid, 'title': g['title']} for gid, g in catalog.items()], 'rules': RULES}
    goal = goals()[state['goal']['id']]
    waiting_on_owner = _waiting(store, owner, state)
    result = {'state': 'waiting_on_owner' if waiting_on_owner else state['status'], 'product_url': product,
              'goal': {'goal_id': state['goal']['id'], 'title': goal['title'], 'title_local': goal.get('title_zh'), 'metric': goal['metric'], 'target': state['goal'].get('target')},
              'round': state['round'], 'steps_delivered': store.count_outputs(owner), 'baseline': state.get('baseline'), 'latest_numbers': state.get('current'), 'rounds': state['rounds'],
              'waiting_on_owner': waiting_on_owner, 'next': _step(store, owner, product, state)}
    if waiting_on_owner: result['tell_the_owner'] = waiting_on_owner['needs']
    return result


def set_goal(store, owner, product, args):
    goal_id = str(args.get('goal_id', '')).strip()
    if goal_id not in goals(): return {'accepted': False, 'error': 'Unknown goal_id. Call where_are_we to see the list.'}
    target = args.get('target')
    if target is not None and not _num(target): return {'accepted': False, 'error': 'target must be a finite number of 0 or more, or omitted.'}
    state = _load(store, owner)
    if state.get('goal', {}).get('id') == goal_id and state['status'] not in ('reached', 'stopped'):
        state['goal']['target'] = target if target is not None else state['goal'].get('target')  # same goal: only the target changes
    else:
        state.update(status='working', goal={'id': goal_id, 'target': target, 'set_at': time.time()}, round=1, nodes=plan_for(goal_id), cursor=0, rounds=[], baseline=None, current=None, wait_until=None,
                     published_at=None, round_published_at=None, asked_round=None, after=None)
        store.log(owner, 1, 'goal', 'goal', {'goal_id': goal_id, 'target': target, 'why': str(args.get('why', ''))[:1000]})
    store.save(owner, state)
    return {'accepted': True, 'goal': goals()[goal_id]['title'], 'target': state['goal'].get('target'),
            'target_rule': 'For a rate or cost the target is the value to reach. For a count (followers, purchases) the target is the increase over the baseline. With no target, a round succeeds when a rate is 20% better than baseline, or a count grows by 10.', 'next': _step(store, owner, product, state)}


def next_step(store, owner, product, args):
    state = _load(store, owner)
    if state['status'] == 'no_goal': return where_are_we(store, owner, product, args)
    return _step(store, owner, product, state)  # reading the step never changes the state


def submit_step(store, owner, product, args, approval=None):
    """approval: an item of a weekly batch the owner approved (month target lanes only; set by the lane wrapper)."""
    state = _load(store, owner)
    if state['status'] == 'no_goal': return {'accepted': False, 'error': 'No goal yet. Call set_goal first.'}
    step_id = str(args.get('step_id', '')); status = args.get('status', 'done'); output = args.get('output')
    if status not in ('done', 'blocked'): return {'accepted': False, 'error': 'status is "done" or "blocked".'}
    if isinstance(output, str):
        try: output = json.loads(output)
        except ValueError: output = {'result': output}
    if len(json.dumps(output, ensure_ascii=False)) > MAX_OUTPUT: return {'accepted': False, 'error': 'output is too long; keep it under %d characters.' % MAX_OUTPUT}
    goal = goals()[state['goal']['id']]
    if state['status'] == 'diagnose':
        if step_id != 'diagnose:r%d' % state['round']: return {'accepted': False, 'error': 'A different step is current.', 'next': _step(store, owner, product, state)}
        if not isinstance(output, dict) or not isinstance(output.get('bottleneck'), str) or output['bottleneck'] not in goal['bottleneck_routes'] or not isinstance(output.get('one_change'), str) or not output['one_change'].strip():
            return {'accepted': False, 'error': 'Deliver a JSON object with bottleneck (one of %s), reason and one_change.' % ', '.join(goal['bottleneck_routes'])}
        choice = output['bottleneck']; same = lambda text: ' '.join(re.findall(r'\w+', str(text).lower()))
        repeated = next((r['round'] for r in state['rounds'] if r.get('change') and same(r['change']) == same(output['one_change'][:500])), None)
        if repeated: return {'accepted': False, 'error': 'That change was already tried after round %d. Name a different one.' % repeated, 'already_tried': [r.get('change') for r in state['rounds'] if r.get('change')]}
        store.log(owner, state['round'], 'diagnose', 'output', {'title': 'Why the target was missed', 'output': output})
        stage = [n for n in plan_for(state['goal']['id']) if '.common.' not in n['node'] and 'ACCESS' not in n['skill'] and n['measure'] != 'baseline']
        route = goal['bottleneck_routes'][choice]
        state['rounds'][-1]['change'] = str(output['one_change'])[:500]
        # The next round is compared with this round's result. A count the engine made itself is a gain, not a platform
        # total, so a count goal keeps its last typed baseline when the agent will read the next result from the platform.
        counted_gain = goal['metric']['formula'] == 'count' and goal['metric']['components'][0] in ((state.get('current') or {}).get('engine_counted') or [])
        next_base = state.get('baseline') if counted_gain else state.get('current')
        next_bases = {ch: r for ch, r in (state.get('currents') or {}).items() if not (goal['metric']['formula'] == 'count' and goal['metric']['components'][0] in (r.get('engine_counted') or []))}
        state.update(round=state['round'] + 1, status='working', cursor=0, baseline=next_base, baselines={**(state.get('baselines') or {}), **next_bases}, currents={},
                     current=None, wait_until=None, round_published_at=None, after=None,
                     nodes=[{'node': 'fix.' + route, 'skill': route, 'measure': None}] + [n for n in stage if n['skill'] != route or n['measure']])
        store.save(owner, state)
        return {'accepted': True, 'message': 'Round %d opened with one change: %s' % (state['round'], state['rounds'][-1]['change']), 'next': _step(store, owner, product, state)}
    window_open = state['status'] == 'observing' and time.time() < state.get('wait_until', 0)
    if state['status'] not in ('working', 'observing') or window_open:
        return {'accepted': False, 'error': 'Nothing to submit right now.', 'next': _step(store, owner, product, state)}
    node = state['nodes'][state['cursor']]; info = skill(node['skill'])
    if step_id != '%s:r%d' % (node['node'], state['round']):
        return {'accepted': False, 'error': 'That step is not the current one (it may already be recorded). Continue with the step below.', 'next': _step(store, owner, product, state)}
    if status == 'blocked':
        needs = str(args.get('needs') or args.get('blocker') or '').strip()[:1000]
        if not needs: return {'accepted': False, 'error': 'Say in needs exactly what the owner must do, in one sentence.', 'next': _step(store, owner, product, state)}
        store.log(owner, state['round'], node['node'], 'blocked', {'title': info['title'], 'needs': needs})
        return {'accepted': True, 'state': 'waiting_on_owner', 'tell_the_owner': needs,
                'message': 'Recorded. The step stays open and nothing is lost. Ask the owner for exactly this one thing, then finish the step and '
                           + ('call record_numbers.' if node['measure'] else 'submit it as done.'),
                'next': _step(store, owner, product, state)}
    if node['measure']: return {'accepted': False, 'error': 'This step needs numbers. Call record_numbers. If only the owner can read them, submit this step with status "blocked" and needs.', 'next': _step(store, owner, product, state)}
    missing = [key for key in info['deliver'] if not (isinstance(output, dict) and output.get(key) not in (None, '', [], {}))]
    if missing: return {'accepted': False, 'error': 'Deliverables missing: ' + ', '.join(missing) + '. Submit output as a JSON object with these keys.', 'deliver': info['deliver']}
    if approval is not None:
        if not (info['needs_link'] or info['writes']):
            return {'accepted': False, 'error': 'approved_item is only for a step that publishes or sends something, and this step does not. Submit it without approved_item.', 'next': _step(store, owner, product, state)}
        if approval.get('kind') == 'template':
            links = _link_prefixes(store, owner, product, approval, state['round'])
            checked = [(text,) + _template_fill(approval['text'], text, links) for text in _texts(output)]
            sent = [text for text, fits, _ in checked if fits]
            if not sent:
                why = next((why for text, fits, why in checked if why and len(text) > 20), None)
                return {'accepted': False, 'error': 'No text in output is a message built from template %s: the fixed text unchanged and each placeholder filled with a short value of its own (%s). Put each message you sent in output as its own string.%s' % (
                            approval['id'], TEMPLATE_VALUE_RULE, ' Closest refusal: %s.' % why if why else ''),
                        'approved_template': approval['text'], 'next': _step(store, owner, product, state)}
            if len(sent) > approval['remaining_today']:
                return {'accepted': False, 'error': 'Template %s allows %d messages a day and %d were already counted today, so %d more fit today, not %d. Send the rest tomorrow.' % (
                    approval['id'], approval['daily_cap'], approval['sent_today'], approval['remaining_today'], len(sent)), 'next': _step(store, owner, product, state)}
        elif _same_text(approval['text']) not in {_same_text(text) for text in _texts(output)}:
            return {'accepted': False, 'error': 'No text in output matches approved item %s word for word. Publish exactly the approved text and put it in output, or show the owner the new text and get it approved first.' % approval['id'],
                    'approved_text': approval['text'], 'next': _step(store, owner, product, state)}
    links = args.get('links'); links = [u[:600] for u in links if isinstance(u, str)][:5] if isinstance(links, list) else []
    checked = None
    if info['needs_link']:
        if not links or not links[0].startswith('https://'):
            return {'accepted': False, 'error': 'This step publishes something. Pass the public https URL of the post itself in links. If it is not live yet, submit status "blocked" with what the owner must do.'}
        platform = _not_a_post(links[0])
        if platform:
            return {'accepted': False, 'error': 'That %s link is not a single post (it looks like a profile, home or search page). Pass the public URL of the post itself, for example the link from the post\'s share button.' % platform}
        checked = _link_live(links[0])
        if not checked:
            return {'accepted': False, 'error': 'That link does not exist (no such host, connection refused, or HTTP 404/410). Check the post is live and public and pass its URL, or submit status "blocked" with what the owner must do.'}
    logged = {'title': info['title'], 'output': output, 'links': links, 'link_read_back': checked}
    if approval is not None:
        logged['owner_approved_item'] = {key: approval.get(key) for key in ('id', 'batch_id', 'approved_by', 'approved_at')}
        if approval.get('kind') == 'template': logged['owner_approved_item'].update(kind='template', daily_cap=approval['daily_cap'], messages_counted=len(sent))
    receipt = store.log(owner, state['round'], node['node'], 'output', logged)
    last = state['cursor'] + 1 >= len(state['nodes'])
    state['cursor'] = min(state['cursor'] + 1, len(state['nodes']) - 1)
    if last and state.get('after'):  # the steps after the result are done: the recorded verdict takes effect
        state.update(status=state['after'], after=None, published_at=None)
    else:
        if info['needs_link'] or (info['writes'] and not info['identity']): state['published_at'] = time.time()
        following = state['nodes'][state['cursor']]
        if following['measure'] == 'current' and not last: _start_window(state, goal)
    store.save(owner, state)
    result = {'accepted': True, 'receipt': receipt, 'link_read_back': checked, 'next': _step(store, owner, product, state)}
    if approval is not None and approval.get('kind') == 'template':
        result['template_messages_counted'] = len(sent)
        result['owner_approval'] = 'The owner approved template %s in batch %s (up to %d messages a day, approved by %s at %s). %d message(s) counted today, %d left today. Noted in the receipt.' % (
            approval['id'], approval.get('batch_id'), approval['daily_cap'], approval.get('approved_by'), _when(approval.get('approved_at')), approval['sent_today'] + len(sent), approval['remaining_today'] - len(sent))
    elif approval is not None:
        result['owner_approval'] = 'The owner approved this exact text in batch %s (item %s, approved by %s at %s). Noted in the receipt.' % (
            approval.get('batch_id'), approval['id'], approval.get('approved_by'), time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(approval.get('approved_at') or 0)))
    return result


def record_numbers(store, owner, product, args):
    state = _load(store, owner)
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
    if lacking: return {'accepted': False, 'error': 'Missing numbers: ' + ', '.join(lacking) + '. Each must be a number of 0 or more. Unknown stays unknown; do not estimate.'}
    value = _metric(goal, values)
    reading = {'values': {k: values[k] for k in values if _num(values[k])}, 'metric': value, 'source': source, 'at': time.time()}
    if filled: reading['engine_counted'] = sorted(filled)
    if typed: reading['agent_reported_instead'] = typed
    if node['measure'] == 'baseline' and state['status'] == 'working':
        state['baseline'] = reading; state.setdefault('baselines', {})[_channel(node)] = reading; state['cursor'] += 1
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
    if not 200 <= status < 300: return {'read': False, 'http_status': status, 'url': final, 'error': 'The page answered HTTP %d.' % status}
    text = _readable(raw, kind); digest = hashlib.sha256(raw).hexdigest()
    state = _load(store, owner)
    entry = {'url': final, 'sha256': digest, 'read_at': time.time(), 'characters': len(text)}
    state['sources'] = ([s for s in state.get('sources', []) if s['url'] != final] + [entry])[-20:]
    store.save(owner, state)
    result = {'read': True, 'url': final, 'sha256': digest, 'read_at': entry['read_at'], 'text': text[:14000], 'truncated': len(text) > 14000,
              'note': 'Quote facts from this text only. Anything not here (price, results, guarantees) is unknown.'}
    if len(text) < LITTLE_TEXT:
        result['little_text'] = True
        result['note'] = ('Very little text came back (%d characters). The page may be a login wall or built only by scripts, so its real content was not read. '
                          'Do not guess what it says: ask the owner to paste the text, or use another public page. ' % len(text)) + result['note']
    return result


def tracking(store, owner, product, args):
    """The tracked link for this round, the sale counter, and what has been counted so far."""
    if not hasattr(store, 'tracked_link'):
        return {'available': False, 'note': 'This local server does not count clicks or sales. Read numbers from the platform and pass them to record_numbers. The hosted service at https://engine.nuluno.com counts them itself.'}
    state = _load(store, owner); counter = store.sale_counter(owner)
    return {'available': True, 'tracked_link': store.tracked_link(owner, max(state['round'], 1), product),
            'tracked_link_use': 'Put this link in posts, bios and messages instead of the bare product URL. Clicks from browsers are counted; known robots and link previews are left out. For several versions of a post, add ?v=A, ?v=B and so on; counted_this_round then shows clicks_by_version.',
            'sale_counter': {'image_tag': '<img src="' + counter + '.gif" width="1" height="1" alt="">', 'redirect_url': counter,
                             'use': 'Sales are counted when a buyer reaches the page shown after payment. Either the owner pastes image_tag into that page, or sets the payment provider\'s after-payment redirect to redirect_url (it forwards to the product page). Add ?value=<amount in cents>&order=<order id, URL-encoded> when known; the same order is counted once, and without an order id the same buyer is counted once a day. This needs the owner once; ask them only when the goal is about purchases.'},
            'counted_this_round': _counted(store, owner, state), 'counted_all_time': store.measured(owner, 0, time.time(), None)}


def stop_goal(store, owner, product, args):
    state = _load(store, owner)
    if state['status'] == 'no_goal': return {'stopped': False}
    state['status'] = 'stopped'; store.log(owner, state['round'], 'goal', 'goal', {'stopped': True}); store.save(owner, state)
    return {'stopped': True, 'message': 'Stopped. Everything delivered stays on record.'}


# ---------- month target ----------
#
# A month target ("100 paying customers in 30 days") is a separate record under owner + '#campaign'. It runs 1 to 5
# lanes; each lane is an ordinary goal stored under owner + '#lane:' + goal_id, so every tool works on a lane when it
# is called with lane=<goal_id>, and without lane nothing changes. The store may provide: lane_limit(owner) -> how many
# lanes the plan allows (default 5), paid_since(owner, start) -> {'count', 'revenue_minor', 'source'} or None, and
# clicks_since(owner, start) -> a count (or {'count', 'source'}) or None. Approving a batch or an ad budget is not a
# tool: only approve_batch and approve_ad_budget below do it, and only front ends the owner uses call them.

DAY = 86400
MAX_LANES = 5
MONTH_KINDS = ('paid_customers', 'revenue_minor')
ITEM_KINDS = ('post', 'reply', 'email', 'ad', 'message', 'template')
MAX_TEMPLATE_CAP = 2000  # messages a day one approved template may send
MAX_PLACEHOLDERS = 10
PLACEHOLDER_MAX_CHARS = 200  # the most a template may allow for one placeholder ({topic:200})
PLACEHOLDER_DEFAULT_CHARS = 80  # a placeholder without its own limit
NAME_PLACEHOLDER_CHARS = 40  # first_name, last_name, name, full_name, company: a name, not a sentence
TEMPLATE_VALUE_RULE = ('at most %d characters, or %d for a name, unless the template sets {name:N} up to %d; one line; no link, domain or email address '
                       'except the product link or the round\'s tracked link in a {link} placeholder; no new sentence') % (PLACEHOLDER_DEFAULT_CHARS, NAME_PLACEHOLDER_CHARS, PLACEHOLDER_MAX_CHARS)
TEMPLATE_MIN_FIXED = 20  # characters (spaces left out) a template keeps the same in every message
_PLACEHOLDER = re.compile(r'\{([A-Za-z_][A-Za-z0-9_]{0,39})(?::([0-9]{1,4}))?\}')
FUNNEL_KEYS = ('visit_to_paid', 'visit_to_signup', 'signup_to_paid')
DEFAULT_VISIT_TO_PAID = 0.02
MEASURED_MIN_VISITS = 100  # fewer visits than this are too few to measure a buying rate
MAX_BATCH_ITEMS = 50
CLICK_KEYS = {key for key, kind in ENGINE_COUNTS.items() if kind == 'clicks'} | {'qualified_clicks', 'listing_clicks'}
MONTH_NUMBERS = ('paid_customers', 'visits', 'signups')
DAILY_RHYTHM = ('One round a day per lane. Loop: month_status -> next_step with the lane it names -> do the work -> submit_step (or record_numbers) with the same lane -> month_status again. '
                'Stop when next has no lane: then wait until come_back_at, or for what the owner must do.')


def lane_owner(owner, lane):
    """The store key of one lane of a month target."""
    return owner + '#lane:' + lane


def _campaign(store, owner):
    record = store.load(owner + '#campaign')
    return record if isinstance(record, dict) and record.get('target') else None


def _save_campaign(store, owner, record): store.save(owner + '#campaign', record)


def _hook(store, name, *args):
    """Call an optional store hook. (value, None), or (None, why) when the store lacks it or it failed."""
    function = getattr(store, name, None)
    if not callable(function): return None, None
    try: return function(*args), None
    except Exception as error: return None, '%s failed (%s); it is left out.' % (name, type(error).__name__)


def _lane_limit(store, owner):
    value, _ = _hook(store, 'lane_limit', owner)
    return max(0, min(MAX_LANES, int(value))) if _num(value) else MAX_LANES


def _when(ts): return time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(ts)) if ts else None


def _ad_lane(goal_id): return goals()[goal_id]['channel'].endswith('_ads')


def _same_text(text):
    """Text compared for approval: Unicode-normalized, whitespace collapsed. Nothing else is forgiven."""
    import unicodedata
    return ' '.join(unicodedata.normalize('NFKC', str(text)).split())


def _texts(value):
    if isinstance(value, str): return [value]
    if isinstance(value, dict): return [t for v in value.values() for t in _texts(v)]
    if isinstance(value, list): return [t for v in value for t in _texts(v)]
    return []


def _count_of(value):
    """A hook answer as (count, source): a plain number or {'count', 'source'}."""
    if isinstance(value, dict) and _num(value.get('count')): return value['count'], str(value.get('source') or 'counted by the engine')
    if _num(value): return value, 'counted by the engine (tracked links)'
    return None, None


def _progress(store, owner, record):
    """Paid customers and visits since the start: counted by the store when it can, otherwise the latest recorded."""
    start = record['target']['start']; notes = []; recorded = record.get('recorded') or {}
    found, problem = _hook(store, 'paid_since', owner, start)
    if problem: notes.append(problem)
    if isinstance(found, dict) and _num(found.get('count')):
        paid = {'since_start': found['count'], 'revenue_minor': found.get('revenue_minor') if _num(found.get('revenue_minor')) else None,
                'source': str(found.get('source') or 'counted by the engine'), 'counted_by_engine': True}
    elif recorded.get('paid_customers'):
        last = recorded['paid_customers']
        paid = {'since_start': last['value'], 'revenue_minor': None, 'source': '%s (recorded %s)' % (last['source'], _when(last['at'])), 'counted_by_engine': False}
    else:
        paid = {'since_start': 0, 'revenue_minor': None, 'source': 'Nothing counted or recorded yet.', 'counted_by_engine': False}
    paid['before_start'] = record.get('current_paid') or 0
    paid['total'] = paid['since_start'] + paid['before_start']
    found, problem = _hook(store, 'clicks_since', owner, start)
    if problem: notes.append(problem)
    counted, counted_source = _count_of(found)
    typed = recorded.get('visits')
    visits = {'count': None, 'source': 'Nothing counted or recorded yet.', 'counted_by_engine': False}
    if counted is not None: visits = {'count': counted, 'source': counted_source, 'counted_by_engine': True}
    if typed and (visits['count'] is None or typed['value'] > visits['count']):  # site analytics see more visits than one tracked link
        visits = {'count': typed['value'], 'source': '%s (recorded %s)' % (typed['source'], _when(typed['at'])), 'counted_by_engine': False}
    return paid, visits, notes


def _rates(record, paid, visits):
    """Each funnel rate with its basis: measured from counted or recorded numbers, or assumed (and said so)."""
    rates = {key: dict(value) for key, value in (record.get('funnel') or {}).items() if key in FUNNEL_KEYS}
    if visits['count'] is not None and visits['count'] >= MEASURED_MIN_VISITS and paid['since_start'] >= 1:
        rates['visit_to_paid'] = {'value': paid['since_start'] / float(visits['count']), 'basis': 'measured',
                                  'source': '%g paid (%s) / %g visits (%s) since the start' % (paid['since_start'], paid['source'], visits['count'], visits['source'])}
    elif 'visit_to_paid' not in rates and 'visit_to_signup' in rates and 'signup_to_paid' in rates:
        both = rates['visit_to_signup']['basis'] == rates['signup_to_paid']['basis'] == 'measured'
        rates['visit_to_paid'] = {'value': rates['visit_to_signup']['value'] * rates['signup_to_paid']['value'], 'basis': 'measured' if both else 'assumed',
                                  'source': 'visit_to_signup x signup_to_paid'}
    if 'visit_to_paid' not in rates:
        rates['visit_to_paid'] = {'value': DEFAULT_VISIT_TO_PAID, 'basis': 'assumed',
                                  'source': 'Assumption: 2 of every 100 visitors pay. Not measured yet; it is replaced by the real rate once %d visits and 1 paid customer are counted or recorded.' % MEASURED_MIN_VISITS}
    return rates


def _lane_clicks(store, owner, record, lane):
    """(clicks since the start, closed rounds, source) for one lane."""
    found, _ = _hook(store, 'clicks_since', lane_owner(owner, lane), record['target']['start'])
    counted, source = _count_of(found)
    if counted is None:
        counted = sum(r['clicks'] for r in (record.get('lane_results') or {}).get(lane, [])); source = 'recorded with record_numbers'
    rounds = len([r for r in _load(store, lane_owner(owner, lane)).get('rounds', []) if r.get('at', 0) >= record['target']['start']])
    return counted, rounds, source


def _split(total, weights):
    """Whole numbers that add up to total, proportional to weights (largest remainder)."""
    keys = list(weights); whole = sum(weights.values())
    if not keys: return {}
    shares = {k: total * weights[k] / whole for k in keys} if whole > 0 else {k: total / float(len(keys)) for k in keys}
    out = {k: int(math.floor(shares[k])) for k in keys}
    for k in sorted(keys, key=lambda k: (-(shares[k] - out[k]), keys.index(k)))[:total - sum(out.values())]: out[k] += 1
    return out


def _math(store, owner, record, now=None):
    """The funnel worked backwards from the target: what is needed per day, at each layer, per lane."""
    now = now or time.time(); target = record['target']; price = record.get('price_minor')
    paid, visits, notes = _progress(store, owner, record)
    rates = _rates(record, paid, visits)
    if target['kind'] == 'revenue_minor':
        have = (paid['revenue_minor'] if paid['revenue_minor'] is not None else paid['since_start'] * price) + paid['before_start'] * price
        remaining = int(math.ceil(max(0, target['amount'] - have) / float(price)))
        at_start = (target['amount'] - paid['before_start'] * price) / float(price) / target['days']
    else:
        have = paid['total']; remaining = max(0, target['amount'] - have)
        at_start = (target['amount'] - paid['before_start']) / float(target['days'])
    days_left = int(math.ceil((target['end'] - now) / float(DAY) - 1e-9)) if now < target['end'] else 0
    per_day = remaining / float(days_left) if days_left else float(remaining)
    visit_rate = rates['visit_to_paid']['value']
    need = {'paid_per_day': round(per_day, 2), 'visits_per_day': int(math.ceil(per_day / visit_rate - 1e-9)) if remaining else 0}
    if 'signup_to_paid' in rates and remaining:
        need['signups_per_day'] = int(math.ceil(per_day / rates['signup_to_paid']['value'] - 1e-9))
    lanes = record.get('lanes') or []
    split_basis = 'equal split'; weights = {lane: 1.0 for lane in lanes}
    if lanes and now - (record.get('running_since') or now) >= 3 * DAY:
        per_round = {}
        for lane in lanes:
            clicks, rounds, _ = _lane_clicks(store, owner, record, lane); per_round[lane] = clicks / float(max(rounds, 1))
        if sum(per_round.values()) > 0: weights = per_round; split_basis = 'proportional to each lane\'s clicks per round so far'
    quotas = _split(need['visits_per_day'], weights)
    elapsed = min(1.0, max(0.0, (now - target['start']) / float(target['end'] - target['start'])))
    expected = target['amount'] * elapsed
    unit = 'paying customers' if target['kind'] == 'paid_customers' else 'revenue (minor units)'
    short = (expected - have) / float(price if target['kind'] == 'revenue_minor' else 1)  # in customers
    if remaining == 0: pace = {'status': 'reached', 'text': 'The target is reached.'}
    elif short < 1: pace = {'status': 'on_track', 'text': 'On track: %g %s so far, %g expected by now.' % (have, unit, round(expected, 2))}
    else:
        pace = {'status': 'behind', 'behind_by_customers': round(short, 1),
                'text': 'Behind by %.1f paying customers. %.2f paying customers a day are needed for the %d days left (%.2f a day at the start).' % (short, per_day, days_left, at_start)}
    pace.update(have=have, expected_by_now=round(expected, 2), needed_per_day_now=round(per_day, 2), needed_per_day_at_start=round(at_start, 2))
    visits_now = None
    if visits['count'] is not None and now - target['start'] >= DAY: visits_now = round(visits['count'] / ((now - target['start']) / float(DAY)), 1)
    gap = {'visits_per_day_needed': need['visits_per_day'], 'visits_per_day_now': visits_now,
           'gap': None if visits_now is None else max(0, int(math.ceil(need['visits_per_day'] - visits_now)))}
    if visits_now is None: gap['note'] = 'Visits per day so far are not known yet (less than a day, or nothing counted or recorded).'
    return {'paid': paid, 'visits': visits, 'funnel': rates, 'remaining_customers': remaining, 'days_left': days_left, 'needed_per_day': need,
            'daily_visit_quota_per_lane': quotas, 'split': split_basis, 'pace': pace, 'gap': gap, 'notes': notes}


def _plan_text(record, math_):
    target = record['target']; rate = math_['funnel']['visit_to_paid']; need = math_['needed_per_day']
    what = '%g paying customers' % target['amount'] if target['kind'] == 'paid_customers' else '%s %.2f in revenue' % (record.get('currency') or '', target['amount'] / 100.0)
    lines = ['Target: %s by %s (%d days left).' % (what, time.strftime('%Y-%m-%d', time.gmtime(target['end'])), math_['days_left']),
             'Needed: %.2f paying customers a day (%d still to win).' % (need['paid_per_day'], math_['remaining_customers']),
             'At %.1f%% of visitors paying (%s), that is %d visits a day%s.' % (rate['value'] * 100, rate['basis'], need['visits_per_day'],
                                                                             ' and %d %s a day' % (need['signups_per_day'], SIGNUP_WORD.get(record.get('preset'), 'sign-ups')) if 'signups_per_day' in need else '')]
    if math_['daily_visit_quota_per_lane']:
        lines.append('Visits a day per lane (%s): ' % math_['split'] + ', '.join('%s (%s) %d' % (goals()[lane]['title'].split(':')[0], lane, n) for lane, n in math_['daily_visit_quota_per_lane'].items()) + '.')
    if rate['basis'] == 'assumed': lines.append('The buying rate is an assumption until real visits and payments are counted; the plan is recalculated every day.')
    return ' '.join(lines)


def _summary(record):
    target = record['target']
    return {'kind': target['kind'], 'amount': target['amount'], 'days': target['days'], 'start': _when(target['start']), 'end': _when(target['end']), 'status': record['status'], 'lanes': record.get('lanes') or []}


# ---------- presets and feasibility ----------
#
# A preset is a starting plan for one kind of business: the lanes it runs (goal ids; a goal this library does not have
# is skipped and said so, and the next goal of the same kind is used), the questions only the owner can answer, and the
# rates assumed until real numbers replace them. Feasibility works out, lane by lane, how many paying customers each
# lane can bring by the end with what is known now, says honestly whether that reaches the target, and names exactly
# what would close the gap. Every rate it uses is either given, measured, or listed as assumed.

ORGANIC = {'instagram': 'G-IG-LINK-RATE', 'threads': 'G-TH-LINK-RATE', 'tiktok': 'G-TT-LINK-RATE', 'youtube': 'G-YT-SITE-CLICKS', 'x': 'G-X-LINK-RATE',
           'linkedin': 'G-LI-INQUIRIES', 'pinterest': 'G069'}
ADS = {'meta_ads': 'G-META-PURCHASE-CPA', 'google_ads': 'G-GA-PURCHASE-RATE', 'tiktok_ads': 'G-TA-CPA', 'reddit_ads': 'G095', 'pinterest_ads': 'G097',
       'microsoft_ads': 'G093', 'linkedin_ads': 'G-LA-CPA'}
COMMUNITY = {'reddit': 'G-RD-PURCHASES', 'facebook_groups': 'G072', 'threads': 'G-TH-INTENT', 'discord': 'G074', 'several': 'G065'}

# Each lane slot lists goal ids in order of preference; '@organic', '@ads', '@community' and '@acquisition' follow the
# agent's channel choice in inputs, and a slot starting with '?has_trial' is used only when the product has a trial.
PRESETS = {
    'new_brand': {'title': 'A new consumer brand with no paying customers yet', 'b2b': False,
                  'asks': ['price', 'free_trial', 'ad_daily_cap'],
                  'lanes': [['G-CREATOR-COLLAB', 'G086'], ['@organic'], ['@ads'], ['@community', 'G065']]},
    'existing_base': {'title': 'A brand with existing members or customers', 'b2b': False,
                      'asks': ['members', 'paid', 'list_size', 'message_channels', 'capacity_per_week', 'price'],
                      'lanes': [['G-BASE-REACTIVATE', 'G088'], ['G-BASE-REFERRAL', 'G086'], ['G-BASE-UPGRADE', 'G-EM-PURCHASE'], ['@acquisition']]},
    'b2b_self_serve': {'title': 'Software with a free trial or free plan and a low price', 'b2b': True,
                       'asks': ['price', 'trials_per_week', 'trial_to_paid', 'competitors'],
                       'lanes': [['G-B2B-LTD', 'G-PH-LAUNCH-PURCHASE'], ['G-B2B-ALTERNATIVES', 'G-GA-PURCHASE-RATE'], ['G-B2B-INTENT', 'G065'],
                                 ['G-B2B-TRIAL-CONVERT', 'G087'], ['G-B2B-MARKETPLACE', 'G084']],
                       'funnel': {'visit_to_signup': ('visit_to_trial', 0.04, 'visitors who start a trial'), 'signup_to_paid': ('trial_to_paid', 0.15, 'trials that become paying')}},
    'b2b_sales': {'title': 'Software sold through demos', 'b2b': True,
                  'asks': ['acv', 'sales_cycle_days', 'demos_per_week', 'has_trial'],
                  'lanes': [['G-B2B-OUTBOUND', 'G-LI-MEETINGS'], ['G-B2B-INTENT', 'G065'], ['G-B2B-ALTERNATIVES', 'G-GA-PURCHASE-RATE'], ['G-B2B-PARTNERS', 'G086'],
                            ['?has_trial', 'G-B2B-TRIAL-CONVERT', 'G087']],
                  'funnel': {'visit_to_signup': ('visit_to_demo', 0.01, 'visitors who ask for a demo'), 'signup_to_paid': ('demo_to_paid', 0.2, 'demos that become paying')}},
}

# Inputs: (type, what it is). Owner inputs are asked for by the preset; the agent decides the channels and may pass
# rates it measured. Types: number (0 or more), count (whole number), rate (above 0, at most 1), yes_no, list, url, or a
# dict of allowed choices.
INPUTS = {
    'price': ('number', 'What does one customer pay, in the main currency unit (39 for US$39)?'),
    'acv': ('number', 'What does one customer pay per year (the contract value), in the main currency unit?'),
    'free_trial': ('yes_no', 'Can buyers try it free first (a free trial or a free preview)?'),
    'has_trial': ('yes_no', 'Can buyers start a free trial without a demo?'),
    'ad_daily_cap': ('number', 'What is the most you will spend on ads per day, all channels together (0 for no ads)?'),
    'daily_send_cap': ('count', 'How many personalised messages a day do you allow, all lanes together?'),
    'members': ('count', 'How many members or contacts do you have in total?'),
    'paid': ('count', 'How many paying users do you have now?'),
    'list_size': ('count', 'How many contacts are on the member list you can message?'),
    'message_channels': ('list', 'Where can you message your members (email, LINE, WhatsApp, Instagram)?'),
    'capacity_per_week': ('count', 'How many more paying customers can you serve per week (free seats, tables or stock)?'),
    'trials_per_week': ('number', 'How many new trials start per week now?'),
    'trial_to_paid': ('rate', 'Of every 100 trials, how many become paying, if you know (0.15 means 15)?'),
    'competitors': ('list', 'Which products do buyers compare you with, if you know (otherwise the agent researches them)?'),
    'sales_cycle_days': ('count', 'How many days does it usually take from the first demo to a paid deal?'),
    'demos_per_week': ('count', 'How many demos can your team run per week?'),
    'sending_domain_verified': ('yes_no', 'Is the sending domain set up with SPF, DKIM and DMARC?'),
    'mailboxes': ('count', 'How many warmed-up mailboxes can send outreach?'),
    'ltd_live_in_days': ('count', 'In how many days does the launch deal go live on the marketplace?'),
    'ltd_listing_url': ('url', 'The public link of the launch deal once it is live.'),
    'listings_live': ('count', 'How many marketplace or directory listings are live now?'),
    'listing_urls': ('list', 'The public links of the live listings.'),
    'organic_channel': (ORGANIC, 'Agent choice: the organic channel where the buyers are.'),
    'ads_channel': (ADS, 'Agent choice: the ad channel.'),
    'community_channel': (COMMUNITY, 'Agent choice: where buyers ask for help in public.'),
    'acquisition_channel': (dict(ORGANIC, **ADS), 'Agent choice: the channel that brings new people (existing_base).'),
    'posts_per_day': ('number', 'Posts a day on the organic lane.'),
    'replies_per_day': ('number', 'Replies a day on a community lane.'),
    'visits_per_post': ('number', 'Visits one post brings, measured.'),
    'cpc': ('number', 'Cost of one ad click, in the main currency unit.'),
    'list_click_rate': ('rate', 'Share of messages to the list that get a click.'),
    'click_to_paid': ('rate', 'Share of clicks from the list that pay.'),
    'reply_rate': ('rate', 'Share of outreach messages that get a reply.'),
    'demo_to_paid': ('rate', 'Share of demos that become paying.'),
    'visit_to_trial': ('rate', 'Share of visitors who start a trial.'),
    'visit_to_demo': ('rate', 'Share of visitors who ask for a demo.'),
}
OPTIONAL_ASKS = ('trial_to_paid', 'competitors')

# Rates and amounts assumed until the owner gives them or the engine measures them. Each one used is listed in the plan.
ASSUMED = {'posts_per_day': 1, 'visits_per_post': 30, 'replies_per_day': 5, 'b2b_replies_per_day': 10, 'visits_per_reply': 4, 'reply_to_trial': 0.08,
           'cpc_usd': 1.0, 'b2b_cpc_usd': 3.0, 'list_click_rate': 0.03, 'click_to_paid': 0.08, 'list_touches': 2,
           'creator_outreach_per_day': 10, 'creator_yes_rate': 0.05, 'visits_per_creator_post': 100, 'creator_lead_days': 7,
           'referral_share_rate': 0.1, 'paid_per_sharer': 0.5, 'referral_lead_days': 3,
           'ltd_sales_low': 30, 'ltd_sales_high': 300, 'ltd_live_in_days': 21,
           'listings_planned': 3, 'installs_per_listing_per_day': 1, 'listing_lead_days': 10,
           'reply_rate': 0.05, 'reply_to_demo': 0.4, 'sends_per_mailbox': 40, 'mailboxes': 1, 'first_reply_days': 3, 'sales_cycle_days': 21,
           'partner_outreach_per_day': 5, 'partner_yes_rate': 0.1, 'paid_per_partner_per_month': 1, 'partner_lead_days': 14,
           'trial_to_paid': 0.15, 'trial_lift': 0.3, 'launch_day_visits': 800, 'launch_day_lead_days': 7}
# A brand-new consumer brand starts from accounts with few or no followers: fewer visits per post and per reply.
NEW_ACCOUNT = {'visits_per_post': 10, 'visits_per_reply': 2}
# What a sign-up is in each preset's funnel, for the plan text.
SIGNUP_WORD = {'b2b_sales': 'demo requests', 'b2b_self_serve': 'trials', 'new_brand': 'trials'}
# Main currency units per US dollar, only to turn the default cost per click into the target's currency.
CPC_FACTOR = {'USD': 1.0, 'TWD': 32.0, 'EUR': 0.95, 'GBP': 0.8, 'JPY': 150.0, 'CAD': 1.4, 'AUD': 1.5, 'SGD': 1.35, 'HKD': 7.8}
MAX_POSTS_PER_DAY, MAX_REPLIES_PER_DAY, MAX_CREATOR_OUTREACH, MAX_PARTNER_OUTREACH = 3, 20, 25, 15
STRETCH_SHARE = 0.6  # the lanes bring at least this share of what is still needed: possible but tight

# What each kind of lane does, by goal id first, then by channel.
MODEL_OF = {'G-CREATOR-COLLAB': 'creators', 'G-BASE-REACTIVATE': 'list', 'G-BASE-UPGRADE': 'list', 'G-BASE-REFERRAL': 'referral', 'G-B2B-LTD': 'launch',
            'G-B2B-ALTERNATIVES': 'ads', 'G-B2B-INTENT': 'replies', 'G-B2B-TRIAL-CONVERT': 'trials', 'G-B2B-MARKETPLACE': 'directory', 'G-B2B-OUTBOUND': 'outreach',
            'G-B2B-PARTNERS': 'partners', 'G065': 'replies', 'G-TH-INTENT': 'replies', 'G-RD-REPLIES': 'replies', 'G-YT-REQUESTS': 'replies', 'G087': 'trials',
            'G088': 'list', 'G089': 'list', 'G-LI-MEETINGS': 'outreach', 'G085': 'partners', 'G086': 'partners', 'G083': 'directory', 'G084': 'directory'}
CHANNEL_MODEL = {'email': 'list', 'line': 'list', 'whatsapp': 'list', 'reddit': 'replies', 'facebook_groups': 'replies', 'discord': 'replies', 'multi': 'replies',
                 'partnerships': 'partners', 'reviews': 'directory', 'producthunt': 'launch_day'}
INHERITED = ('list', 'referral', 'ads', 'replies', 'trials', 'directory', 'outreach')  # models a stand-in goal can take over from a missing one


def _model_of(goal_id, record=None):
    """How a lane brings customers. A goal used in place of a missing preset goal does the same job (record lane_models)."""
    kept = ((record or {}).get('lane_models') or {}).get(goal_id)
    if kept: return kept
    if goal_id in MODEL_OF: return MODEL_OF[goal_id]
    channel = goals()[goal_id].get('channel', '')
    return 'ads' if channel.endswith('_ads') else CHANNEL_MODEL.get(channel, 'posts')


def _yes(value): return value is True


def _parse_inputs(given):
    """{name: value} checked against INPUTS -> clean dict, or an error string."""
    if given in (None, {}): return {}
    if not isinstance(given, dict): return 'inputs is an object such as {"price": 9.99, "free_trial": "yes"}.'
    out = {}
    for name, value in given.items():
        if name not in INPUTS: return 'Unknown input %s. Known inputs: %s.' % (name, ', '.join(sorted(INPUTS)))
        kind = INPUTS[name][0]
        if isinstance(kind, dict):
            value = str(value or '').strip().lower()
            if value not in kind: return '%s is one of %s.' % (name, ', '.join(kind))
        elif kind == 'yes_no':
            words = {'yes': True, 'y': True, 'true': True, 'no': False, 'n': False, 'false': False}
            value = value if isinstance(value, bool) else words.get(str(value).strip().lower())
            if value is None: return '%s is yes or no.' % name
        elif kind == 'list':
            if isinstance(value, str): value = [part for part in value.split(',')]
            if not isinstance(value, list) or not all(isinstance(v, str) for v in value): return '%s is a list of words, or one comma-separated string.' % name
            value = [v.strip()[:120] for v in value if v.strip()][:20]
        elif kind == 'url':
            if not isinstance(value, str) or not value.startswith('https://') or len(value) > 600: return '%s is a public https link.' % name
        else:
            if isinstance(value, str):
                try: value = float(value.strip())
                except ValueError: return '%s is a number.' % name
            if not _num(value) or value > 1e9: return '%s is a number of 0 or more.' % name
            if kind == 'rate' and not 0 < value <= 1: return '%s is a rate above 0 and at most 1 (0.15 means 15%%).' % name
            if kind == 'count':
                if value != int(value): return '%s is a whole number.' % name
                value = int(value)
            if name in ('price', 'acv') and value <= 0: return '%s must be above 0.' % name
        out[name] = value
    return out


def _default_lanes(preset_id, inputs):
    """(lanes, skipped, models) for a preset. A goal this library does not have is skipped and the next one in its slot is used;
    when the stand-in does the same job, models keeps the missing goal's way of counting for it."""
    lanes, skipped, models = [], [], {}
    choose = {'@organic': ORGANIC[inputs.get('organic_channel') or 'instagram'], '@ads': ADS[inputs.get('ads_channel') or 'meta_ads'],
              '@community': COMMUNITY[inputs.get('community_channel') or 'reddit']}
    acquisition = inputs.get('acquisition_channel') or ('meta_ads' if (inputs.get('ad_daily_cap') or 0) > 0 else 'instagram')
    choose['@acquisition'] = ADS.get(acquisition) or ORGANIC[acquisition]
    for slot in PRESETS[preset_id]['lanes']:
        if slot[0] == '?has_trial':
            if not _yes(inputs.get('has_trial')): continue
            slot = slot[1:]
        wanted = [choose.get(goal_id, goal_id) for goal_id in slot]
        found = next((goal_id for goal_id in wanted if goal_id in goals() and goal_id not in lanes), None)
        for goal_id in wanted:
            if goal_id == found: break
            if goal_id not in goals(): skipped.append({'goal_id': goal_id, 'why': 'not in this library version', 'used_instead': found})
        if found:
            lanes.append(found)
            if found != wanted[0] and MODEL_OF.get(wanted[0]) in INHERITED: models[found] = MODEL_OF[wanted[0]]
    return lanes, skipped, models


def _preset_funnel(preset_id, inputs):
    """The funnel layers a preset assumes. A new brand with a free trial or preview counts visits -> trials -> paying
    (8 of 100 visitors start it, 25 of 100 trials pay: the same 2 of 100 visitors paying, with the trial layer to watch)."""
    if preset_id == 'new_brand':
        if not _yes(inputs.get('free_trial')): return {}
        return {'visit_to_signup': ('visit_to_trial', 0.08, 'visitors who start the free trial or preview'), 'signup_to_paid': ('trial_to_paid', 0.25, 'trials that become paying')}
    return PRESETS[preset_id].get('funnel') or {}


def _seed_funnel(record, preset_id, inputs):
    """Rates a preset works with: given by the owner (inputs) or the preset's assumption. Rates passed in funnel stay;
    a preset assumption that no longer applies (another preset, or no free trial any more) is removed."""
    funnel = record.setdefault('funnel', {}); layers = _preset_funnel(preset_id, inputs)
    for key in [key for key, value in funnel.items() if (value.get('preset_default') or value.get('from_input')) and key not in layers]: del funnel[key]
    for key, (name, default, what) in layers.items():
        if inputs.get(name) is not None:
            funnel[key] = {'value': float(inputs[name]), 'basis': 'measured', 'source': 'Given by the owner (%s).' % name, 'from_input': name}
        elif key not in funnel or funnel[key].get('preset_default'):
            funnel[key] = {'value': default, 'basis': 'assumed', 'preset_default': True,
                           'source': 'Assumption of the %s preset: %g of every 100 %s. Replaced once the owner gives it or it is measured.' % (preset_id, default * 100, what)}


def _list_size(store, owner, inputs):
    """(contacts that can be messaged, where the number comes from)."""
    found, _ = _hook(store, 'list_size', owner)
    if _num(found) and found > 0: return int(found), 'the uploaded list'
    if inputs.get('list_size'): return inputs['list_size'], 'list size given by the owner'
    if inputs.get('members'):
        rest = max(0, inputs['members'] - (inputs.get('paid') or 0))
        return rest, 'members who are not paying now (%d members - %d paying), a count given by the owner; the list itself is not uploaded yet' % (inputs['members'], inputs.get('paid') or 0)
    return 0, 'no list yet'


def _template_caps(record, lane, now=None):
    """Daily caps of the approved, unexpired message templates of one lane, added up."""
    now = now or time.time()
    return sum(item['daily_cap'] for batch in record.get('batches') or [] if now <= batch['valid_until'] for item in batch['items']
               if item['lane'] == lane and item.get('kind') == 'template' and item['state'] == 'approved')


def _context(store, owner, record, math_):
    inputs = record.get('inputs') or {}; preset = PRESETS.get(record.get('preset')) or {}; lanes = record.get('lanes') or []
    models = {lane: _model_of(lane, record) for lane in lanes}
    rates = math_['funnel']; currency = record.get('currency') or 'USD'
    budget = record.get('ad_budget') or {}
    if budget.get('approved_at'): ad_cap, ad_basis = budget['daily_cap_minor'] / 100.0, 'approved by the owner'
    elif inputs.get('ad_daily_cap') is not None: ad_cap, ad_basis = float(inputs['ad_daily_cap']), 'stated by the owner, not approved yet'
    else: ad_cap, ad_basis = 0.0, 'no ad budget given'
    b2b = bool(preset.get('b2b'))
    if inputs.get('cpc'): cpc, cpc_basis = float(inputs['cpc']), 'given'
    else:
        cpc = ASSUMED['b2b_cpc_usd' if b2b else 'cpc_usd'] * CPC_FACTOR.get(currency, 1.0); cpc_basis = 'assumed'
    signup = rates.get('signup_to_paid') or {}
    trial_to_paid = signup.get('value') or inputs.get('trial_to_paid') or ASSUMED['trial_to_paid']
    contacts, contacts_basis = _list_size(store, owner, inputs)
    defaults = dict(ASSUMED, **NEW_ACCOUNT) if record.get('preset') == 'new_brand' else ASSUMED
    return {'inputs': inputs, 'preset': record.get('preset'), 'b2b': b2b, 'days': math_['days_left'], 'models': models, 'defaults': defaults,
            'v2p': rates['visit_to_paid']['value'], 'v2p_assumed': rates['visit_to_paid']['basis'] == 'assumed',
            'to_paid': trial_to_paid, 'to_paid_assumed': not (signup.get('basis') == 'measured' or inputs.get('trial_to_paid') is not None),
            'price': record['price_minor'] / 100.0 if record.get('price_minor') else None, 'currency': currency, 'cpc': cpc, 'cpc_basis': cpc_basis,
            'ad_cap': ad_cap, 'ad_basis': ad_basis, 'ad_lanes': max(1, sum(1 for m in models.values() if m == 'ads')),
            'list_lanes': max(1, sum(1 for m in models.values() if m == 'list')), 'send_lanes': max(1, sum(1 for m in models.values() if m in ('list', 'outreach'))),
            'contacts': contacts, 'contacts_basis': contacts_basis,
            'cycle': (inputs.get('sales_cycle_days') if inputs.get('sales_cycle_days') is not None else ASSUMED['sales_cycle_days']) if record.get('preset') == 'b2b_sales' else 0}


def _lane_row(store, owner, record, ctx, lane):
    """What one lane can bring: units a day, paid customers per unit, when it starts, and every assumption used."""
    model = ctx['models'][lane]; inputs = ctx['inputs']; days = ctx['days']; assumed = []; new_account = []
    def get(name, key=None):
        if inputs.get(name) is not None: return inputs[name]
        assumed.append(name)
        if (key or name) in NEW_ACCOUNT and ctx['defaults'] is not ASSUMED: new_account.append(key or name)
        return ctx['defaults'][key or name]
    def v2p():
        if ctx['v2p_assumed']: assumed.append('visit_to_paid')
        return ctx['v2p']
    def to_paid():
        if ctx['to_paid_assumed']: assumed.append('trial_to_paid' if ctx['preset'] != 'b2b_sales' else 'demo_to_paid')
        return ctx['to_paid']
    approved = _template_caps(record, lane)
    start, extra = 0, {}
    if model == 'posts':
        posts = get('posts_per_day'); measured = None
        clicks, rounds, _ = _lane_clicks(store, owner, record, lane)
        if rounds and clicks > 0: measured = clicks / float(rounds)
        visits = measured if measured is not None else get('visits_per_post')
        units, per, unit = posts * visits, v2p(), 'visits a day'
        basis = '%g post(s) a day x %g visits per post (%s)' % (posts, round(visits, 1), 'measured' if measured is not None else
                                                                ('assumed for a new account' if 'visits_per_post' in new_account else 'given' if inputs.get('visits_per_post') is not None else 'assumed'))
        extra = {'posts': posts, 'visits_per_post': visits}
    elif model == 'replies':
        replies = get('replies_per_day', 'b2b_replies_per_day' if ctx['b2b'] else 'replies_per_day')
        if ctx['b2b']:
            per = ASSUMED['reply_to_trial'] * to_paid(); assumed.append('reply_to_trial')
            basis = '%g replies a day to people asking for this x %g%% start a trial or ask for a demo' % (replies, ASSUMED['reply_to_trial'] * 100)
        else:
            visits = get('visits_per_reply'); per = visits * v2p()
            basis = '%g helpful replies a day x %g visits each%s' % (replies, visits, ' (assumed for a new account)' if 'visits_per_reply' in new_account else '')
        units, unit = replies, 'replies a day'; extra = {'replies': replies}
    elif model == 'ads':
        cap = ctx['ad_cap'] / ctx['ad_lanes']
        if ctx['cpc_basis'] == 'assumed': assumed.append('cpc')
        units, per, unit, start = cap / ctx['cpc'], v2p(), 'visits a day from ads', 1 if cap else 0
        basis = '%s %.2f a day (%s) / %s %.2f a click' % (ctx['currency'], cap, ctx['ad_basis'], ctx['currency'], ctx['cpc'])
        extra = {'cap': cap}
    elif model == 'list':
        available = ctx['contacts'] * get('list_touches') / float(max(days, 1)) / ctx['list_lanes']
        if approved: allowed, allowed_basis = approved, 'approved template cap'
        elif inputs.get('daily_send_cap') is not None: allowed, allowed_basis = inputs['daily_send_cap'] / float(ctx['send_lanes']), 'daily send cap stated by the owner'
        else: allowed, allowed_basis = 0, 'no send volume approved yet'
        units = min(available, allowed); per = get('list_click_rate') * get('click_to_paid'); unit = 'messages a day'
        basis = '%d messages a day (%s; the list allows %d a day: %s, each contact messaged %d times)' % (units, allowed_basis, available, ctx['contacts_basis'], ASSUMED['list_touches'])
        extra = {'available': available, 'allowed': allowed}
    elif model == 'referral':
        members = inputs.get('paid') if inputs.get('paid') is not None else record.get('current_paid') or 0
        units = members * get('referral_share_rate') / 30.0; per = get('paid_per_sharer'); unit = 'members sharing an invite a day'; start = get('referral_lead_days')
        basis = '%d paying members, %g%% share an invite in a month, %g paid friend per sharer' % (members, ASSUMED['referral_share_rate'] * 100, ASSUMED['paid_per_sharer'])
    elif model == 'creators':
        outreach = approved or get('creator_outreach_per_day')
        units = outreach; per = get('creator_yes_rate') * get('visits_per_creator_post') * v2p(); unit = 'creators contacted a day'; start = get('creator_lead_days')
        basis = '%g creators contacted a day x %g%% say yes x %g visits from each one\'s post' % (outreach, ASSUMED['creator_yes_rate'] * 100, ASSUMED['visits_per_creator_post'])
        extra = {'outreach': outreach}
    elif model == 'launch':
        live_in = 0 if inputs.get('ltd_listing_url') and inputs.get('ltd_live_in_days') is None else get('ltd_live_in_days')
        low = get('ltd_sales_low'); units, per, unit, start = low / 30.0, 1.0, 'deal sales a day while live', live_in
        basis = 'A launch deal typically sells %d to %d in its first month; the plan counts the low end, live in %d days' % (low, ASSUMED['ltd_sales_high'], live_in)
        extra = {'low': low, 'live_in': live_in}
    elif model == 'launch_day':
        lead = ASSUMED['launch_day_lead_days']; visits = get('launch_day_visits')
        units, per, unit, start = visits, v2p(), 'visits on launch day', lead
        basis = 'One launch day, about %d days from now, bringing about %d visits' % (lead, visits)
        extra = {'paid_by_end': visits * per if days > lead + ctx['cycle'] else 0.0}
    elif model == 'trials':
        trials = (inputs.get('trials_per_week') or 0) / 7.0
        units, per, unit = trials, to_paid(), 'trials a day'
        basis = ('%g trials a week (given)' % inputs['trials_per_week']) if inputs.get('trials_per_week') is not None else 'trials per week not given, counted as 0'
    elif model == 'directory':
        live = inputs.get('listings_live') or 0; planned = get('listings_planned'); installs = get('installs_per_listing_per_day')
        per = to_paid() if ctx['b2b'] else 10 * v2p(); lead = ASSUMED['listing_lead_days']
        units, unit, start = (live + planned) * installs, 'installs or sign-ups a day from listings', 0 if live else lead
        basis = '%d live + %d new listings (live in about %d days) x %g installs a day each' % (live, planned, lead, installs)
        extra = {'paid_by_end': live * installs * per * days + planned * installs * per * max(0, days - lead - ctx['cycle'])}
    elif model == 'outreach':
        mailboxes = get('mailboxes'); most = get('sends_per_mailbox') * mailboxes
        if approved: allowed, allowed_basis = approved, 'approved template cap'
        elif inputs.get('daily_send_cap') is not None: allowed, allowed_basis = inputs['daily_send_cap'] / float(ctx['send_lanes']), 'daily send cap stated by the owner'
        else: allowed, allowed_basis = 0, 'no send volume approved yet'
        units = min(allowed, most); per = get('reply_rate') * ASSUMED['reply_to_demo'] * to_paid(); assumed.append('reply_to_demo'); unit = 'emails a day'
        start = ASSUMED['first_reply_days']
        basis = '%d emails a day (%s; %d mailbox(es) send at most %d) x %g%% reply x %g%% of replies book a demo' % (units, allowed_basis, mailboxes, most, ASSUMED['reply_rate'] * 100, ASSUMED['reply_to_demo'] * 100)
        extra = {'allowed': allowed, 'most': most, 'mailboxes': mailboxes}
    else:  # partners
        outreach = approved or get('partner_outreach_per_day'); lead = get('partner_lead_days')
        units, unit, start = outreach, 'partners contacted a day', lead
        per = get('partner_yes_rate') * get('paid_per_partner_per_month') / 30.0
        live = max(0, days - lead - ctx['cycle'])
        extra = {'outreach': outreach, 'paid_by_end': outreach * ASSUMED['partner_yes_rate'] * live * live / 2.0 * ASSUMED['paid_per_partner_per_month'] / 30.0}
        basis = '%g agencies or consultants contacted a day x %g%% join x %g paid customer each a month, after about %d days' % (outreach, ASSUMED['partner_yes_rate'] * 100, ASSUMED['paid_per_partner_per_month'], lead)
    if ctx['cycle'] and model not in ('trials', 'launch', 'launch_day'):
        start += ctx['cycle']; basis += '; then a %d-day sales cycle' % ctx['cycle']
    paid_by_end = extra.pop('paid_by_end') if 'paid_by_end' in extra else units * per * max(0, days - start)
    row = {'lane': lane, 'title': goals()[lane]['title'], 'model': model, 'unit': unit, 'per_day': round(units, 1), 'paid_per_unit': round(per, 5),
           'starts_after_days': start, 'paid_by_end': round(paid_by_end, 1), 'paid_per_day': round(paid_by_end / days, 2) if days else 0,
           'basis': basis + '.', 'assumed': sorted(set(assumed)), '_units': units, '_per': per, '_start': start, '_exact': paid_by_end, '_extra': extra}
    if new_account: row['new_account'] = sorted(set(new_account))
    return row


LANE_LABEL = {'G-CREATOR-COLLAB': 'Creators', 'G-BASE-REACTIVATE': 'Win-back', 'G-BASE-REFERRAL': 'Member invites', 'G-BASE-UPGRADE': 'Upgrades',
              'G-B2B-LTD': 'Launch deal', 'G-B2B-ALTERNATIVES': 'Competitor-alternative search', 'G-B2B-INTENT': 'Public requests', 'G-B2B-TRIAL-CONVERT': 'Trials',
              'G-B2B-MARKETPLACE': 'Marketplaces', 'G-B2B-OUTBOUND': 'Outbound email', 'G-B2B-PARTNERS': 'Agencies and consultants'}


def _label(lane): return LANE_LABEL.get(lane) or goals()[lane]['title'].split(':')[0].strip()


def _lever(row, text, adds, needs, ask=None, days=1, **more):
    if row: text = _label(row['lane']) + ': ' + text[0].lower() + text[1:]
    lever = {'lane': row['lane'] if row else None, 'lever': text, 'adds_by_end': None if adds is None else round(adds, 1),
             'adds_per_day': None if adds is None else round(adds / float(max(days, 1)), 2), 'needs_from_owner': needs, 'ask': ask}
    lever.update(more)
    return lever


def _row_levers(ctx, row):
    """Levers that need no ad money, for one lane: each says what it adds by the end and what the owner must do."""
    model, units, per, extra, days = row['model'], row['_units'], row['_per'], row['_extra'], ctx['days']
    live = max(0, days - row['_start']); out = []
    if model == 'posts' and extra['posts'] < MAX_POSTS_PER_DAY:
        out.append(_lever(row, 'Post %d times a day instead of %g.' % (MAX_POSTS_PER_DAY, extra['posts']), (MAX_POSTS_PER_DAY - extra['posts']) * extra['visits_per_post'] * per * live,
                          'Approve a weekly batch with %d posts a day for this lane.' % MAX_POSTS_PER_DAY, days=days))
    elif model == 'replies' and extra['replies'] < MAX_REPLIES_PER_DAY:
        out.append(_lever(row, 'Reply to up to %d matching requests a day instead of %g (each reply written for that post).' % (MAX_REPLIES_PER_DAY, extra['replies']),
                          (MAX_REPLIES_PER_DAY - extra['replies']) * per * live, 'Approve one reply template with a daily cap of %d.' % MAX_REPLIES_PER_DAY, 'approve_send_volume', days, suggested=MAX_REPLIES_PER_DAY))
    elif model == 'list':
        if ctx['contacts'] == 0:
            out.append(_lever(row, 'Give the member list so the agent can message past and free members.', None,
                              'Upload the member list (email, name, status, last purchase) or say how many contacts it has.', 'upload_list', days))
        elif extra['allowed'] < extra['available']:
            out.append(_lever(row, 'Approve up to %d messages a day from one template (now %d).' % (math.ceil(extra['available']), extra['allowed']),
                              (extra['available'] - units) * per * live, 'Approve the message template with a daily cap of %d.' % math.ceil(extra['available']),
                              'approve_send_volume', days, suggested=int(math.ceil(extra['available']))))
    elif model == 'referral' and row['_exact'] > 0:
        out.append(_lever(row, 'Give both the member and the friend a reward (for example one free session each).', row['_exact'],
                          'Approve the reward. Assumption: a reward doubles the invites that are shared.', None, days))
    elif model == 'creators' and extra['outreach'] < MAX_CREATOR_OUTREACH:
        out.append(_lever(row, 'Contact %d creators a day instead of %g.' % (MAX_CREATOR_OUTREACH, extra['outreach']), (MAX_CREATOR_OUTREACH - extra['outreach']) * per * live,
                          'Approve the creator outreach template with a daily cap of %d, and the offer (free access and an affiliate share).' % MAX_CREATOR_OUTREACH, 'approve_send_volume', days, suggested=MAX_CREATOR_OUTREACH))
    elif model == 'launch' and extra['live_in'] > 7 and ctx['inputs'].get('ltd_live_in_days') is None:
        out.append(_lever(row, 'Apply today to a launch-deal marketplace that can list within about a week.', (min(days, extra['live_in']) - min(days, 7)) * units * per,
                          'Approve the deal terms (deal price, number of codes, refund window) so the agent can apply today.', None, days))
    elif model == 'trials' and units > 0:
        out.append(_lever(row, 'Send activation and upgrade messages to every trial.', units * per * ASSUMED['trial_lift'] * days,
                          'Give the list of current trials (upload it, or connect Stripe). Assumption: these messages raise trial-to-paid by %d%%.' % (ASSUMED['trial_lift'] * 100), 'upload_list', days))
    elif model == 'directory':
        lead = ASSUMED['listing_lead_days']
        out.append(_lever(row, 'List in %d more marketplaces or directories where buyers search.' % ASSUMED['listings_planned'],
                          ASSUMED['listings_planned'] * ASSUMED['installs_per_listing_per_day'] * per * max(0, days - lead - ctx['cycle']),
                          'Create or confirm the developer or vendor accounts those listings need.', None, days))
    elif model == 'outreach' and live > 0 and per > 0:
        target = extra['most']
        if extra['allowed'] < target:
            out.append(_lever(row, 'Approve up to %d emails a day to published business contacts (now %d).' % (target, extra['allowed']), (target - units) * per * live,
                              'Approve the outreach template with a daily cap of %d, after the sending domain is verified.' % target, 'approve_send_volume', days, suggested=int(target)))
        out.append(_lever(row, 'Add 2 more warmed-up sending mailboxes (each sends about %d a day).' % ASSUMED['sends_per_mailbox'], 2 * ASSUMED['sends_per_mailbox'] * per * live,
                          'Create 2 more mailboxes on the sending domain.', None, days))
    elif model == 'partners' and extra['outreach'] < MAX_PARTNER_OUTREACH and row['_exact'] > 0:
        out.append(_lever(row, 'Contact %d agencies or consultants a day instead of %g.' % (MAX_PARTNER_OUTREACH, extra['outreach']), row['_exact'] * (MAX_PARTNER_OUTREACH / float(extra['outreach']) - 1),
                          'Approve the partner outreach template with a daily cap of %d, and the referral share.' % MAX_PARTNER_OUTREACH, 'approve_send_volume', days, suggested=MAX_PARTNER_OUTREACH))
    return [lever for lever in out if lever['adds_by_end'] is None or lever['adds_by_end'] > 0.05]


def _needed_layers(ctx, math_, remaining):
    days = ctx['days']; paid = remaining / float(days) if days else float(remaining)
    need = {'paid_per_day': round(paid, 2), 'visits_per_day': math_['needed_per_day']['visits_per_day']}
    if ctx['preset'] == 'existing_base':
        rate = (ctx['inputs'].get('list_click_rate') or ASSUMED['list_click_rate']) * (ctx['inputs'].get('click_to_paid') or ASSUMED['click_to_paid'])
        need['messages_per_day_if_all_from_the_list'] = int(math.ceil(paid / rate - 1e-9)) if remaining else 0
    if ctx['preset'] in ('b2b_self_serve', 'new_brand') and remaining and 'signup_to_paid' in math_['funnel']: need['trials_per_day'] = int(math.ceil(paid / ctx['to_paid'] - 1e-9))
    if ctx['preset'] == 'b2b_sales' and remaining:
        demos = paid / ctx['to_paid']; replies = demos / ASSUMED['reply_to_demo']
        need.update(demos_per_day=round(demos, 1), replies_per_day=round(replies, 1), outreach_emails_per_day_if_all_outbound=int(math.ceil(replies / (ctx['inputs'].get('reply_rate') or ASSUMED['reply_rate']) - 1e-9)))
    return need


def _feasibility(store, owner, record, math_):
    """Can the lanes reach the target with what is known now? Honest verdict, the gap, and the levers that close it."""
    ctx = _context(store, owner, record, math_); days = ctx['days']; remaining = math_['remaining_customers']; inputs = ctx['inputs']
    rows = [_lane_row(store, owner, record, ctx, lane) for lane in record.get('lanes') or []]
    total = sum(row['_exact'] for row in rows); limits = []
    if inputs.get('capacity_per_week') is not None:
        limits.append({'limit': 'capacity_per_week', 'most_by_end': inputs['capacity_per_week'] * days / 7.0,
                       'text': 'You can serve %d more paying customers a week (given), so at most %d by the end.' % (inputs['capacity_per_week'], inputs['capacity_per_week'] * days / 7.0)})
    if ctx['preset'] == 'b2b_sales' and inputs.get('demos_per_week') is not None:
        most = inputs['demos_per_week'] / 7.0 * ctx['to_paid'] * max(0, days - ctx['cycle'])
        limits.append({'limit': 'demos_per_week', 'most_by_end': most,
                       'text': '%d demos a week (given) x %g%% become paying, after a %d-day sales cycle: at most %d by the end.' % (inputs['demos_per_week'], ctx['to_paid'] * 100, ctx['cycle'], most)})
    ceiling = min([limit['most_by_end'] for limit in limits] or [float('inf')])
    expected = min(total, ceiling)
    for limit in limits: limit['binding'] = limit['most_by_end'] < total
    gap = max(0.0, remaining - expected)
    # The ad cap counts only as far as the stated limits leave room after the other lanes: clicks past that bring
    # customers the team cannot serve or demo. ad_cap says how much of the stated or approved cap is useful.
    ad_rows = [row for row in rows if row['model'] == 'ads']
    ads_total = sum(row['_exact'] for row in ad_rows); ad_cap = None
    if ad_rows and ctx['ad_cap'] > 0:
        room = max(0.0, ceiling - (total - ads_total))
        useful = ctx['ad_cap'] if ads_total <= room else (int(math.ceil(ctx['ad_cap'] * room / ads_total - 1e-9)) if room >= 1 else 0)
        brings = min(ads_total, room)
        per = sum(row['_per'] for row in ad_rows) / len(ad_rows)
        cost = ctx['cpc'] / per if per else None
        ad_cap = {'daily_cap': ctx['ad_cap'], 'useful_daily_cap': useful, 'brings_by_end': round(brings, 1), 'room_by_end': None if room == float('inf') else round(room, 1),
                  'limited_by': [limit['limit'] for limit in limits if limit['binding']] if ads_total > room else [],
                  'cost_per_customer': None if cost is None else round(cost, 2)}
        if ctx['price'] and cost and cost > ctx['price']:
            ad_cap['warning'] = 'At these rates each customer costs about %s %.2f in ads, more than the price %s %.2f, so this cap loses money until a higher buying rate is measured.' % (ctx['currency'], cost, ctx['currency'], ctx['price'])
        if ads_total > room:
            for row in ad_rows: row['_capped'] = row['_exact'] * room / ads_total if ads_total else 0.0
    free = [lever for row in rows for lever in _row_levers(ctx, row)]
    if ctx['cycle'] > 7 and days:
        sooner = sum(row['_units'] * row['_per'] * (max(0, days - (row['_start'] - ctx['cycle'] + 7)) - max(0, days - row['_start']))
                     for row in rows if row['model'] not in ('trials', 'launch', 'partners', 'directory'))
        if sooner > 0.05 or not rows:
            free.append(_lever(None, 'Offer a paid pilot or a monthly plan bought by card, so a deal can close in about 7 days instead of %d.' % ctx['cycle'], sooner,
                               'Approve a pilot offer (price, length, what is included).', None, days, cycle_days=7))
    free.sort(key=lambda lever: -(lever['adds_by_end'] or 0))
    # 1. Levers that bring more buyers (demand), largest first, until the lanes and these levers bring what is still needed.
    #    A lever adding less than half a customer changes nothing the owner would notice, so it is not asked for.
    demand_gap = max(0.0, remaining - total)
    plan, covered = [], 0.0
    for lever in free:
        if covered >= demand_gap: break
        if lever['adds_by_end'] and lever['adds_by_end'] >= 0.5: plan.append(lever); covered += lever['adds_by_end']
    # A paid pilot in the plan shortens the cycle, so the demos a week given reach further by the end.
    pilot = any(lever.get('cycle_days') for lever in plan)
    def most_with(limit, cycle):
        if limit['limit'] != 'demos_per_week': return limit['most_by_end']
        return inputs['demos_per_week'] / 7.0 * ctx['to_paid'] * max(0, days - cycle)
    plan_cycle = min(ctx['cycle'], 7) if pilot else ctx['cycle']
    levers = list(free)
    # 2. Ads, only as far as the stated limits (seats, stock, demos) leave room: a customer the team cannot serve or demo
    #    is not won by buying more clicks. One ad lever at most, the same in levers, closes_gap_with and asks.
    headroom = ceiling - (total + covered)
    losing = blocked = None
    if ad_rows and days - 1 - ctx['cycle'] > 0:
        live = days - 1 - ctx['cycle']; cost = ctx['cpc'] / ctx['v2p']
        def ad_lever(missing, alternative=False):
            extra = missing / float(live) / ctx['v2p'] * ctx['cpc']; cap = int(math.ceil(ctx['ad_cap'] + extra))
            text = ('Raise the daily ad cap to %s %d (now %s %.2f).' % (ctx['currency'], cap, ctx['currency'], ctx['ad_cap'])) if ctx['ad_cap'] else 'Approve a daily ad cap of %s %d.' % (ctx['currency'], cap)
            if alternative: text = text[:-1] + ', in place of the levers above.'
            lever = _lever(ad_rows[0], text, missing, 'Approve a daily ad budget cap of %s %d.' % (ctx['currency'], cap), 'approve_ad_budget', days, suggested=cap,
                           cost_per_customer=round(cost, 2))
            if alternative: lever['alternative'] = True
            if ctx['price'] and cost > ctx['price']:
                lever['warning'] = 'At these rates each customer costs about %s %.2f in ads, more than the price %s %.2f, so this lever loses money until a higher buying rate is measured.' % (ctx['currency'], cost, ctx['currency'], ctx['price'])
            return lever
        rest = min(demand_gap - covered, headroom)
        instead = min(demand_gap, ceiling - total)
        if rest >= 1:  # less than one customer is rounding, not a reason to buy ads
            lever = ad_lever(rest); levers.append(lever)
            if lever.get('warning'): losing = lever
            else: plan.append(lever); covered += rest
        elif demand_gap - covered >= 1:
            blocked = next((limit for limit in limits if limit['most_by_end'] < total + covered + 1), None)
        elif instead >= 1:
            levers.append(ad_lever(instead, alternative=True))
    # 3. Limits the owner can raise (seats, demos), sized to what the lanes and the levers above can bring.
    demand = total + covered; need = min(float(remaining), demand); after = {}
    raise_first = []
    for limit in limits:
        most = most_with(limit, plan_cycle); after[limit['limit']] = most
        if most >= need - 0.05: continue
        if limit['limit'] == 'capacity_per_week':
            per_week = int(math.ceil(need * 7.0 / max(days, 1) - inputs['capacity_per_week'])) if days else 0
            if per_week > 0:
                raise_first.append(_lever(None, 'Make room for about %d more paying customers a week (seats, tables or stock).' % per_week, need - most,
                                          'Add capacity, then tell the agent the new number (capacity_per_week).', None, days, limit='capacity_per_week', suggested=inputs['capacity_per_week'] + per_week))
                after['capacity_per_week'] = need
        elif days - plan_cycle > 0:
            per_demo = ctx['to_paid'] * (days - plan_cycle) / 7.0  # paying customers by the end from one more demo a week
            want = int(math.ceil(need / per_demo - 1e-9)); for_target = int(math.ceil(remaining / per_demo - 1e-9))
            if want > inputs['demos_per_week']:
                text = 'Run about %d demos a week instead of %d.' % (want, inputs['demos_per_week'])
                if for_target > want: text = text[:-1] + ' (all %d still needed would take about %d a week).' % (remaining, for_target)
                if plan_cycle != ctx['cycle']: text = text[:-1] + ', counting the 7-day pilot offer in this plan.'
                raise_first.append(_lever(None, text, need - most, 'Free up demo time or add a person who runs demos, then tell the agent the new number (demos_per_week).',
                                          None, days, limit='demos_per_week', suggested=want, for_target=for_target))
                after['demos_per_week'] = need
    ceiling_after = min(list(after.values()) or [float('inf')])
    plan = raise_first + plan; levers = raise_first + levers
    for lever in levers:  # a lever that brings buyers past a stated limit adds only up to that limit until it is raised
        if lever.get('limit') or not lever['adds_by_end']: continue
        cycle = min(ctx['cycle'], 7) if lever.get('cycle_days') else plan_cycle  # the pilot's own shorter cycle counts for it
        mosts = [(limit['limit'], most_with(limit, cycle)) for limit in limits]
        over = [name for name, most in mosts if most < total + lever['adds_by_end']]
        if over: lever.update(limited_by=over, adds_within_current_limits=round(max(0.0, min(lever['adds_by_end'], min(most for _, most in mosts) - total)), 1))
    reachable = min(demand, ceiling_after)
    if remaining == 0: verdict = 'on_track'
    elif expected >= remaining: verdict = 'on_track'
    elif expected >= STRETCH_SHARE * remaining: verdict = 'stretch'
    else: verdict = 'not_with_current_inputs'
    assumed = sorted({name for row in rows for name in row['assumed']})
    end = time.strftime('%Y-%m-%d', time.gmtime(record['target']['end']))
    if remaining == 0: summary = 'The target is reached.'
    elif not rows: summary = 'No lanes yet, so nothing can be counted toward the %d customers still needed.' % remaining
    else:
        summary = {'on_track': 'On paper the lanes bring about %d of the %d paying customers still needed by %s.',
                   'stretch': 'Possible but tight: the lanes bring about %d of the %d paying customers still needed by %s.',
                   'not_with_current_inputs': 'Not with the current inputs: the lanes bring about %d of the %d paying customers still needed by %s.'}[verdict] % (round(expected), remaining, end)
        if ctx['cycle'] and ctx['cycle'] + ASSUMED['first_reply_days'] >= days:
            summary += ' A deal takes about %d days to close, as long as the time left, so deals started now mostly close after the end.' % ctx['cycle']
        if verdict != 'on_track' and plan: summary += ' To close the gap: ' + ' '.join(lever['lever'] for lever in plan)
        if losing: summary += ' Ads could bring the rest only at a loss: ' + losing['warning'][0].lower() + losing['warning'][1:]
        if blocked:
            summary += ' More ad money would not help: %s' % ('the demos your team can run are the limit, so raise demos_per_week first.' if blocked['limit'] == 'demos_per_week'
                                                              else 'the customers you can serve are the limit, so raise capacity_per_week first.')
        if reachable < remaining - 0.5:
            summary += ' Even with every lever here it is about %d of %d: a longer time, a lower target or a stronger offer is needed.' % (round(reachable), remaining)
        if ctx['preset'] == 'new_brand' and (ctx['v2p_assumed'] or time.time() - record['target']['start'] < 7 * DAY):
            summary += ' These levers are estimates until the first 7 days of real visits and payments are counted; the plan is rechecked then.'
        elif assumed: summary += ' Rates not measured yet are assumed (listed in assumed); the plan is recalculated every day as real numbers come in.'
    clean = []
    for row in rows:
        out = {key: value for key, value in row.items() if not key.startswith('_')}
        if '_capped' in row:  # the ad cap past the limits brings customers nobody can serve or demo: not counted
            out.update(paid_by_end=round(row['_capped'], 1), paid_per_day=round(row['_capped'] / days, 2) if days else 0,
                       paid_by_end_before_limits=round(row['_exact'], 1), limited_by=ad_cap['limited_by'])
        clean.append(out)
    return {'verdict': verdict, 'summary': summary, 'needed': _needed_layers(ctx, math_, remaining),
            'capacity': dict({'lanes': clean, 'paid_by_end': round(expected, 1), 'paid_per_day': round(expected / days, 2) if days else 0, 'before_limits': round(total, 1), 'limits': limits},
                             **({'ad_cap': ad_cap} if ad_cap else {})),
            'gap': {'customers_by_end': round(gap, 1), 'paid_per_day': round(gap / days, 2) if days else round(gap, 1), 'share_covered': round(expected / remaining, 2) if remaining else 1.0},
            'levers': levers, 'closes_gap_with': plan, 'reachable_with_levers': round(reachable, 1), 'assumed': assumed}


def _missing_inputs(store, owner, record):
    preset = PRESETS.get(record.get('preset'))
    if not preset: return []
    inputs = record.get('inputs') or {}; missing = []
    for name in preset['asks']:
        if inputs.get(name) not in (None, '', []): continue
        if name in ('price', 'acv') and record.get('price_minor'): continue
        if name == 'paid' and record.get('current_paid'): continue
        if name == 'ad_daily_cap' and record.get('ad_budget'): continue
        if name == 'list_size' and _list_size(store, owner, inputs)[1] == 'the uploaded list': continue
        missing.append(name)
    return missing


def _where(hosted, kind, detail=''):
    if hosted:
        return {'answer': 'Tell your AI agent in the chat; it records the answer with plan_month inputs.',
                'upload_list': 'Your owner page (the private link you saved at sign-up): Upload list (CSV with email, name, status, last_purchase; up to 20,000 rows).',
                'connect_stripe': 'Your owner page: Connect Stripe (read-only).',
                'approve_send_volume': 'Your owner page: the template appears in the weekly batch with its daily cap; approve it there.',
                'approve_ad_budget': 'Your owner page: Approve ad budget.',
                'verify_sending_domain': 'Your owner page: sending-domain checklist (SPF, DKIM, DMARC at your domain host).',
                'provide_link': 'Tell your AI agent the link in the chat.'}[kind]
    return {'answer': 'Tell your AI agent, or run: python3 nuluno.py plan --input %s=<value>' % detail,
            'upload_list': 'Keep the list on your own computer; the agent sends from your own mail tool or account. Tell it how many contacts: python3 nuluno.py plan --input list_size=<number>',
            'approve_send_volume': 'After the agent hands you the template with submit_batch, run in your own terminal: python3 nuluno.py approve <batch_id> --items <template id>',
            'approve_ad_budget': 'After the agent runs request_ad_budget, run in your own terminal: python3 nuluno.py approve-budget',
            'verify_sending_domain': 'Set SPF, DKIM and DMARC at your domain host, then run: python3 nuluno.py plan --input sending_domain_verified=yes',
            'provide_link': 'Tell your AI agent, or run: python3 nuluno.py plan --input %s=https://...' % detail}[kind]


def _asks(store, owner, record, math_, feas):
    """What the owner is asked for now: answers only they have, and the approvals or connections the plan needs."""
    hosted = hasattr(store, 'tracked_link'); inputs = record.get('inputs') or {}; asks, seen = [], set()
    models = {lane: _model_of(lane, record) for lane in record.get('lanes') or []}
    def add(kind, reason, lane=None, **more):
        key = (kind, lane, more.get('input'))
        if key in seen: return
        seen.add(key); ask = {'kind': kind, 'reason': reason, 'where': _where(hosted, kind, more.get('input', ''))}
        if lane: ask['lane'] = lane
        ask.update(more); asks.append(ask)
    for name in _missing_inputs(store, owner, record):
        if name == 'list_size':
            add('upload_list', 'The lanes that message your own members need your member list (or, on your own computer, how many contacts it has).', **({} if hosted else {'input': 'list_size'}))
            continue
        add('answer', INPUTS[name][1], input=name, optional=name in OPTIONAL_ASKS)
    if hosted and not math_['paid']['counted_by_engine']:
        add('connect_stripe', 'Connecting Stripe read-only lets the engine count real paying customers itself instead of asking you.')
    for lever in feas['closes_gap_with']:
        if lever['ask'] == 'approve_send_volume':
            add('approve_send_volume', 'The agent prepares one message template for this lane; approving it with a daily cap of %d lets it send up to %d personalised messages a day.' % (lever['suggested'], lever['suggested']),
                lever['lane'], suggested=lever['suggested'], agent_does_first='submit_batch with an item of kind template (lane, text with {placeholders}, audience_rule, daily_cap %d)' % lever['suggested'])
        elif lever['ask'] == 'approve_ad_budget':
            add('approve_ad_budget', 'Ads spend only after you approve one daily cap; %s %d a day is what closes the gap at the assumed rates.' % (record.get('currency') or 'USD', lever['suggested']),
                lever['lane'], suggested=lever['suggested'], agent_does_first='request_ad_budget with daily_cap %d' % lever['suggested'], warning=lever.get('warning'))
        elif lever['ask'] == 'upload_list':
            add('upload_list', 'Messaging people already on your list is the cheapest way to more paying customers: ' + lever['needs_from_owner'], lever['lane'])
    if inputs.get('daily_send_cap') is not None:  # the plan counts the stated send cap, but nothing is sent before a template is approved
        for row in feas['capacity']['lanes']:
            if row['model'] in ('list', 'outreach') and row['per_day'] > 0 and not _template_caps(record, row['lane']):
                volume = int(math.ceil(row['per_day'] - 1e-9))
                add('approve_send_volume', 'The plan counts %d messages a day on this lane from the daily send cap you stated, but nothing is sent until you approve one message template with that daily cap.' % volume,
                    row['lane'], suggested=volume, agent_does_first='submit_batch with an item of kind template (lane, text with {placeholders}, audience_rule, daily_cap %d)' % volume)
    budget = record.get('ad_budget') or {}
    ad_cap = feas['capacity'].get('ad_cap') or {}
    if any(m == 'ads' for m in models.values()) and not budget.get('approved_at') and (inputs.get('ad_daily_cap') or 0) > 0 and ad_cap.get('useful_daily_cap'):
        # only as much of the stated cap as brings customers within the stated limits; never a cap that buys clicks for nothing
        currency, stated = record.get('currency') or 'USD', inputs['ad_daily_cap']; useful = min(stated, ad_cap['useful_daily_cap'])
        if useful < stated:
            reason = ('You said up to %s %g a day for ads, but %s %d a day already brings the about %d customers your %s leave room for; the rest would bring customers past that limit. '
                      'Nothing is spent until you approve a cap.' % (currency, stated, currency, useful, round(ad_cap['brings_by_end']),
                                                                    'demos' if ad_cap['limited_by'] == ['demos_per_week'] else 'seats or stock' if ad_cap['limited_by'] == ['capacity_per_week'] else 'demos and seats'))
        else: reason = 'You said up to %s %g a day for ads; nothing is spent until you approve that cap.' % (currency, stated)
        add('approve_ad_budget', reason, next(lane for lane, m in models.items() if m == 'ads'), suggested=useful,
            agent_does_first='request_ad_budget with daily_cap %g' % useful, warning=ad_cap.get('warning'))
    channels = [c.lower() for c in inputs.get('message_channels') or []]
    emails = any(m == 'outreach' for m in models.values()) or (any(m == 'list' for m in models.values()) and (not channels or 'email' in channels))
    if emails and not _yes(inputs.get('sending_domain_verified')):
        add('verify_sending_domain', 'Email sent in volume from a domain without SPF, DKIM and DMARC lands in spam, so this is set up once before any template is approved.')
    for lane, model in models.items():
        if model == 'launch' and not inputs.get('ltd_listing_url'):
            add('provide_link', 'When the launch deal is live, its link lets the engine count the deal sales; until then the plan assumes it goes live in %d days.' % (inputs.get('ltd_live_in_days') if inputs.get('ltd_live_in_days') is not None else ASSUMED['ltd_live_in_days']),
                lane, input='ltd_listing_url', optional=True)
        if model == 'directory' and (inputs.get('listings_live') or 0) > 0 and not inputs.get('listing_urls'):
            add('provide_link', 'The links of your live listings let the engine count what they bring.', lane, input='listing_urls')
    return asks


def set_month_target(store, owner, product, args):
    kind = str(args.get('kind') or 'paid_customers')
    if kind not in MONTH_KINDS: return {'accepted': False, 'error': 'kind is paid_customers or revenue_minor.'}
    amount, days, price = args.get('amount'), args.get('days', 30), args.get('price')
    if not _num(amount) or amount <= 0: return {'accepted': False, 'error': 'amount must be a number above 0.'}
    if not _num(days) or days != int(days) or not 7 <= days <= 90: return {'accepted': False, 'error': 'days must be a whole number from 7 to 90.'}
    if kind == 'paid_customers' and amount != int(amount): return {'accepted': False, 'error': 'amount is a whole number of paying customers.'}
    if price is not None and (not _num(price) or price <= 0): return {'accepted': False, 'error': 'price is what one customer pays in the currency\'s main unit (39 for US$39), above 0.'}
    if kind == 'revenue_minor' and price is None:
        return {'accepted': False, 'error': 'A revenue target needs price (what one customer pays, 39 for US$39) to work out how many customers a day are needed.'}
    currency = str(args.get('currency') or '').strip().upper()
    if currency and not re.fullmatch(r'[A-Z]{3}', currency): return {'accepted': False, 'error': 'currency is a three-letter code such as USD or TWD.'}
    current = args.get('current_paid', 0) or 0
    if not _num(current) or current != int(current): return {'accepted': False, 'error': 'current_paid is a whole number of 0 or more: paying customers already won toward this target.'}
    existing = _campaign(store, owner)
    if existing and existing['status'] in ('planning', 'running') and args.get('replace') is not True:
        return {'accepted': False, 'error': 'A month target is already %s. Replace it only if the owner says so: call set_month_target again with replace true.' % existing['status'], 'month_target': _summary(existing)}
    now = time.time()
    record = {'target': {'kind': kind, 'amount': int(amount), 'days': int(days), 'start': now, 'end': now + int(days) * DAY},
              'price_minor': int(round(price * 100)) if price is not None else None, 'currency': currency or None, 'current_paid': int(current),
              'why': str(args.get('why', ''))[:1000], 'funnel': {}, 'lanes': [], 'status': 'planning', 'batches': [], 'batch_seq': 0, 'ad_budget': None,
              'history': [], 'touched': {}, 'lane_results': {}, 'recorded': {}, 'alerts': [], 'created': now}
    if existing:
        for lane in existing.get('lanes') or []: stop_goal(store, lane_owner(owner, lane), product, {})
        record['previous'] = dict(_summary(existing), replaced_at=_when(now))
    _save_campaign(store, owner, record)
    store.log(owner + '#campaign', 0, 'month_target', 'goal', {'target': record['target'], 'price_minor': record['price_minor'], 'current_paid': record['current_paid'], 'why': record['why']})
    limit = _lane_limit(store, owner)
    return {'accepted': True, 'month_target': _summary(record), 'lane_limit': limit,
            'next': {'call': 'plan_month', 'instruction': 'Read the product page, then pick %s goals on different channels where this product\'s buyers are (where_are_we lists every goal) and call plan_month with their goal ids. '
                                                          'Decide yourself; tell the owner the plan it returns.' % ('3 to %d' % limit if limit >= 3 else 'up to %d' % limit),
                     'presets': {key: value['title'] for key, value in PRESETS.items()},
                     'or_preset': 'Or call plan_month with preset (the one that fits this business) and inputs you already know; it picks the lanes, '
                                  'says honestly whether the target is reachable, and lists in asks what only the owner can give.'}}


def _parse_funnel(given):
    """{key: number} or {key: {'value', 'source'}} -> {key: {'value', 'basis', 'source'}}, or an error string."""
    if given in (None, {}): return {}
    if not isinstance(given, dict): return 'funnel is an object such as {"visit_to_paid": 0.03}.'
    out = {}
    for key, value in given.items():
        if key not in FUNNEL_KEYS: return 'funnel keys are %s.' % ', '.join(FUNNEL_KEYS)
        source = ''
        if isinstance(value, dict): source = str(value.get('source') or '').strip()[:300]; value = value.get('value')
        if not _num(value) or not 0 < value <= 1: return '%s must be a rate above 0 and at most 1 (0.02 means 2%%).' % key
        out[key] = {'value': float(value), 'basis': 'measured' if source else 'assumed', 'source': source or 'Given in plan_month without a source, so treated as an assumption.'}
    return out


def plan_month(store, owner, product, args):
    record = _campaign(store, owner)
    if not record: return {'accepted': False, 'error': 'No month target yet. Call set_month_target first.'}
    if record['status'] not in ('planning', 'running'): return {'accepted': False, 'error': 'This month target has %s. Start a new one with set_month_target.' % record['status'], 'month_target': _summary(record)}
    lanes = args.get('lanes'); limit = _lane_limit(store, owner)
    preset_id = args.get('preset')
    if preset_id is not None and preset_id not in PRESETS: return {'accepted': False, 'error': 'preset is one of %s.' % ', '.join(PRESETS)}
    preset_id = preset_id or record.get('preset')
    inputs = _parse_inputs(args.get('inputs'))
    if isinstance(inputs, str): return {'accepted': False, 'error': inputs}
    inputs = dict(record.get('inputs') or {}, **inputs)
    skipped, left_out = [], []
    if lanes in (None, []) and preset_id:
        lanes, skipped, lane_models = _default_lanes(preset_id, inputs)
        record['lane_models'] = lane_models
        if not lanes: return {'accepted': False, 'skipped': skipped, 'error': 'None of the %s preset\'s goals are in this library. Pass lanes yourself.' % preset_id}
        lanes, left_out = lanes[:limit], lanes[limit:]
        if not lanes: return {'accepted': False, 'lane_limit': limit, 'error': 'This plan runs no lanes.'}
    if not isinstance(lanes, list) or not lanes or not all(isinstance(g, str) for g in lanes):
        return {'accepted': False, 'error': 'lanes is a list of 1 to %d goal ids, or pass preset (%s) to start from its lanes.' % (limit, ', '.join(PRESETS))}
    lanes = [g.strip() for g in lanes]
    unknown = [g for g in lanes if g not in goals()]
    if unknown: return {'accepted': False, 'error': 'Unknown goal ids: %s. where_are_we lists every goal.' % ', '.join(unknown)}
    if len(set(lanes)) != len(lanes): return {'accepted': False, 'error': 'Each lane is a different goal.'}
    if len(lanes) > limit:
        return {'accepted': False, 'lane_limit': limit, 'error': 'This plan runs up to %d lane%s at the same time; pick the %s most likely to bring buyers.' % (limit, '' if limit == 1 else 's', 'one' if limit == 1 else str(limit))}
    funnel = _parse_funnel(args.get('funnel'))
    if isinstance(funnel, str): return {'accepted': False, 'error': funnel}
    now = time.time()
    price = inputs.get('price') or inputs.get('acv')
    if price and not record.get('price_minor'): record['price_minor'] = int(round(price * 100))
    if preset_id: record.update(preset=preset_id); _seed_funnel(record, preset_id, inputs)
    record['inputs'] = inputs
    for old in record.get('lanes') or []:
        if old not in lanes: stop_goal(store, lane_owner(owner, old), product, {})
    for lane in lanes:
        key = lane_owner(owner, lane); state = _load(store, key)
        if (state.get('goal') or {}).get('id') != lane or state['status'] in ('reached', 'stopped', 'no_goal'):
            set_goal(store, key, product, {'goal_id': lane, 'why': 'Lane of the month target.'}); state = _load(store, key)
        state['window_cap'] = DAY
        if state['status'] == 'observing' and state.get('wait_until') and state.get('published_at'): state['wait_until'] = min(state['wait_until'], state['published_at'] + DAY)
        store.save(key, state)
    record.update(lanes=lanes, funnel=dict(record.get('funnel') or {}, **funnel), status='running', running_since=record.get('running_since') or now, planned_at=now)
    math_ = _math(store, owner, record, now)
    _snapshot(record, math_, now)
    _save_campaign(store, owner, record)
    store.log(owner + '#campaign', 0, 'month_plan', 'goal', {'lanes': lanes, 'funnel': record['funnel'], 'preset': record.get('preset'), 'inputs': inputs})
    plan_lanes = [{'lane': lane, 'title': goals()[lane]['title'], 'channel': goals()[lane]['channel'], 'daily_visit_quota': math_['daily_visit_quota_per_lane'].get(lane),
                   'round_window_hours': min(goals()[lane].get('observation_seconds', 172800), DAY) // 3600} for lane in lanes]
    feasibility = _feasibility(store, owner, record, math_)
    answer = {'accepted': True, 'status': 'running', 'tell_the_owner': _plan_text(record, math_) + ' ' + feasibility['summary'], 'plan': math_, 'lanes': plan_lanes,
              'feasibility': feasibility, 'asks': _asks(store, owner, record, math_, feasibility),
              'next': _next_lane(store, owner, product, record, now), 'daily_rhythm': DAILY_RHYTHM}
    if record.get('preset'): answer['preset'] = {'id': record['preset'], 'title': PRESETS[record['preset']]['title'], 'inputs': inputs}
    if skipped: answer['skipped_lanes'] = skipped
    if left_out: answer['left_out_lanes'] = {'lanes': left_out, 'why': 'This plan runs up to %d lane%s at the same time.' % (limit, '' if limit == 1 else 's')}
    if record.get('preset') == 'existing_base' and inputs.get('paid') and not record.get('current_paid') and record['target']['amount'] > inputs['paid']:
        answer['check_target'] = ('The target counts every paying customer from 0, but you have %d paying now. If the target is a total (for example doubling %d to %d), '
                                  'call set_month_target with amount %d, current_paid %d and replace true, then plan_month again.') % (inputs['paid'], inputs['paid'], 2 * inputs['paid'], 2 * inputs['paid'], inputs['paid'])
    return answer


def _snapshot(record, math_, now):
    day = time.strftime('%Y-%m-%d', time.gmtime(now))
    entry = {'day': day, 'paid_total': math_['paid']['total'], 'visits': math_['visits']['count'], 'needed_paid_per_day': math_['needed_per_day']['paid_per_day'],
             'needed_visits_per_day': math_['needed_per_day']['visits_per_day'], 'pace': math_['pace']['status'], 'at': now}
    history = record.setdefault('history', [])
    if history and history[-1]['day'] == day: history[-1] = entry
    else: history.append(entry)
    del history[:-120]


def _lane_view(store, owner, product, record, lane, quota):
    key = lane_owner(owner, lane); state = _load(store, key); goal = goals()[lane]
    view = {'lane': lane, 'title': goal['title'], 'channel': goal['channel'], 'today_visit_quota': quota}
    if state['status'] == 'no_goal': return dict(view, state='no_goal', status='no_goal')
    step = _step(store, key, product, state)
    view.update(status=state['status'], state=step['state'], round=state['round'], step_id=step.get('step_id'), step_title=step.get('title'),
                rounds=[{'round': r['round'], 'verdict': r['verdict'], 'metric': r.get('metric')} for r in state['rounds']])
    if step.get('come_back_at'): view.update(come_back_at=step['come_back_at'], come_back_at_text=step['come_back_at_text'])
    if step.get('tell_the_owner'): view['tell_the_owner'] = step['tell_the_owner']
    today = time.time() - time.time() % DAY
    found, _ = _hook(store, 'clicks_since', key, today)
    view['clicks_today'] = _count_of(found)[0]
    if view['clicks_today'] is None: view['clicks_today_note'] = 'Not counted here; read clicks from the platform and record them with record_numbers.'
    view['last_worked_on'] = _when((record.get('touched') or {}).get(lane))
    return view


def _next_lane(store, owner, product, record, now, views=None):
    """The lane to work on now: of the lanes with work to do, the one that has waited longest since it was last worked on."""
    if record['status'] == 'planning':
        return {'lane': None, 'state': 'planning', 'call': 'plan_month', 'message': 'No lanes yet. Pick goals on different channels and call plan_month.'}
    if record['status'] != 'running':
        return {'lane': None, 'state': record['status'], 'message': 'The month target %s; there is no lane to work on.' % {'reached': 'is reached', 'ended': 'has ended', 'stopped': 'was stopped'}.get(record['status'], record['status'])}
    views = views or [_lane_view(store, owner, product, record, lane, None) for lane in record['lanes']]
    order = {lane: i for i, lane in enumerate(record['lanes'])}; since = record.get('running_since') or 0
    ready = [v for v in views if v['state'] in ('work', 'target_missed_choose_one_change')]
    if ready:
        pick = min(ready, key=lambda v: ((record.get('touched') or {}).get(v['lane'], since), order[v['lane']]))
        return {'lane': pick['lane'], 'step_id': pick.get('step_id'), 'title': pick.get('step_title') or 'Choose one change', 'call': 'next_step', 'arguments': {'lane': pick['lane']},
                'why': 'Of the lanes with work to do, this one has waited longest (last worked on: %s).' % (pick.get('last_worked_on') or 'never'),
                'do': 'Call next_step with lane "%s", do the step, then submit it with the same lane. Then call month_status again.' % pick['lane']}
    owner_needed = [{'lane': v['lane'], 'tell_the_owner': v['tell_the_owner']} for v in views if v['state'] == 'waiting_on_owner']
    times = [v['come_back_at'] for v in views if v.get('come_back_at')]
    return {'lane': None, 'state': 'nothing_to_do_now', 'owner_needed': owner_needed, 'come_back_at': min(times) if times else None, 'come_back_at_text': _when(min(times)) if times else None,
            'message': 'No lane has work right now: every lane is waiting for results or for the owner. Ask the owner for what owner_needed lists, otherwise come back at come_back_at.'}


def _batch_state(batch, now):
    states = [item['state'] for item in batch['items']]
    if now > batch['valid_until'] and any(s in ('approved', 'awaiting_owner') for s in states): return 'expired'
    if all(s in ('approved', 'used') for s in states): return 'approved'
    if any(s in ('approved', 'used') for s in states): return 'partly_approved'
    return 'awaiting_owner'


def month_status(store, owner, product, args):
    record = _campaign(store, owner)
    if not record:
        return {'state': 'no_month_target', 'instruction': 'To work toward a number of paying customers in a set time (for example 100 in 30 days), call set_month_target, then plan_month.'}
    now = time.time(); math_ = _math(store, owner, record, now); changed = False
    if record['status'] in ('planning', 'running'):
        if math_['remaining_customers'] == 0: record.update(status='reached', ended_at=now); changed = True
        elif now >= record['target']['end']: record.update(status='ended', ended_at=now); changed = True
    if record['status'] == 'running': _snapshot(record, math_, now); changed = True
    if changed: _save_campaign(store, owner, record)
    views = [_lane_view(store, owner, product, record, lane, math_['daily_visit_quota_per_lane'].get(lane)) for lane in record.get('lanes') or []]
    for view in views:
        if _ad_lane(view['lane']): view['ad_budget'] = _ad_rule(record)
    pending = []
    for batch in record.get('batches') or []:
        waiting = [item['id'] for item in batch['items'] if item['state'] == 'awaiting_owner']
        if waiting and _batch_state(batch, now) != 'expired': pending.append({'batch_id': batch['batch_id'], 'items_waiting': len(waiting), 'what': 'weekly batch of content'})
    budget = record.get('ad_budget')
    if budget and not budget.get('approved_at'): pending.append({'ad_budget': '%s %.2f a day' % (budget['currency'], budget['daily_cap_minor'] / 100.0), 'what': 'daily ad budget cap'})
    result = {}
    alerts = [a for a in record.get('alerts') or [] if now - a['at'] < 7 * DAY]
    if alerts: result['alerts'] = alerts
    result.update(state=record['status'], target=_summary(record), days_left=math_['days_left'], paid=math_['paid'], visits=math_['visits'], pace=math_['pace'],
                  needed_per_day=math_['needed_per_day'], funnel=math_['funnel'], gap=math_['gap'], split=math_['split'], lanes=views,
                  pending_approvals=pending, ad_budget=budget, next=_next_lane(store, owner, product, record, now, views), daily_rhythm=DAILY_RHYTHM,
                  record_month_numbers='When the owner or a platform gives totals since the start, pass paid_customers and visits in record_numbers values (with lane); counted numbers from the engine replace them.')
    if math_['notes']: result['notes'] = math_['notes']
    if record['status'] in ('planning', 'running'):
        if record.get('preset'): result['preset'] = {'id': record['preset'], 'title': PRESETS[record['preset']]['title'], 'inputs': record.get('inputs') or {}}
        result['feasibility'] = _feasibility(store, owner, record, math_)
        result['asks'] = _asks(store, owner, record, math_, result['feasibility'])
    if pending: result['tell_the_owner'] = 'Waiting for your approval: ' + '; '.join(p['what'] + (' ' + p['batch_id'] if p.get('batch_id') else ' ' + p.get('ad_budget', '')) for p in pending) + '.'
    if record['status'] in ('reached', 'ended', 'stopped'):
        result['result'] = {'reached': record['status'] == 'reached', 'paid_total': math_['paid']['total'], 'target': record['target']['amount'], 'ended_at': _when(record.get('ended_at')),
                            'per_lane': [{'lane': v['lane'], 'title': v['title'], 'rounds': len(v.get('rounds') or []), 'rounds_reached': sum(1 for r in v.get('rounds') or [] if r['verdict'] == 'reached'),
                                          'clicks': _lane_clicks(store, owner, record, v['lane'])[0]} for v in views]}
        result['message'] = 'The month target %s. Tell the owner the result per lane, then offer a new one with set_month_target.' % ('is reached' if record['status'] == 'reached' else 'has ended')
    return result


def _ad_rule(record):
    budget = record.get('ad_budget') or {}
    if budget.get('approved_at'):
        return {'approved': True, 'daily_cap': budget['daily_cap_minor'] / 100.0, 'currency': budget['currency'], 'channels': budget['channels'], 'approved_at': _when(budget['approved_at']),
                'rule': 'Keep total ad spend at or below %s %.2f a day, the cap the owner approved. A higher amount needs a new request_ad_budget and the owner\'s approval.' % (budget['currency'], budget['daily_cap_minor'] / 100.0)}
    if budget: return {'approved': False, 'requested': '%s %.2f a day' % (budget['currency'], budget['daily_cap_minor'] / 100.0), 'rule': 'Requested, not approved yet. Do not start or raise any ad spend until the owner approves it.'}
    return {'approved': False, 'rule': 'No daily ad budget is approved. Call request_ad_budget with the daily cap and channels, and spend nothing until the owner approves it.'}


def submit_batch(store, owner, product, args):
    record = _campaign(store, owner)
    if not record or record['status'] != 'running': return {'accepted': False, 'error': 'A batch belongs to a running month target. Call set_month_target and plan_month first.'}
    items = args.get('items')
    if not isinstance(items, list) or not 1 <= len(items) <= MAX_BATCH_ITEMS: return {'accepted': False, 'error': 'items is a list of 1 to %d items for the coming 7 days.' % MAX_BATCH_ITEMS}
    week_of = args.get('week_of'); now = time.time(); start = now
    if week_of not in (None, ''):
        try:
            import calendar
            start = calendar.timegm(time.strptime(str(week_of), '%Y-%m-%d'))
        except ValueError: return {'accepted': False, 'error': 'week_of is a date such as 2026-11-30.'}
    if start > now + 14 * DAY or start < now - 7 * DAY: return {'accepted': False, 'error': 'week_of must be within the next two weeks.'}
    record['batch_seq'] = record.get('batch_seq', 0) + 1; batch_id = 'B%d' % record['batch_seq']; clean = []
    for number, item in enumerate(items, 1):
        if not isinstance(item, dict): return {'accepted': False, 'error': 'Item %d is not an object.' % number}
        lane, kind, channel, text = item.get('lane'), item.get('kind'), item.get('channel'), item.get('text')
        if lane not in record['lanes']: return {'accepted': False, 'error': 'Item %d: lane must be one of %s.' % (number, ', '.join(record['lanes']))}
        if kind not in ITEM_KINDS: return {'accepted': False, 'error': 'Item %d: kind is one of %s.' % (number, ', '.join(ITEM_KINDS))}
        if not isinstance(channel, str) or not channel.strip(): return {'accepted': False, 'error': 'Item %d: channel names where it goes (threads, reddit, email ...).' % number}
        if not isinstance(text, str) or not text.strip() or len(text) > 5000: return {'accepted': False, 'error': 'Item %d: text is the exact text to publish or send, up to 5000 characters.' % number}
        entry = {'id': '%s-%d' % (batch_id, number), 'batch_id': batch_id, 'lane': lane, 'kind': kind, 'channel': channel.strip()[:60], 'text': text, 'state': 'awaiting_owner'}
        if kind == 'template':
            problem = _template_problem(text)
            if problem: return {'accepted': False, 'error': 'Item %d: %s' % (number, problem)}
            rule, cap = item.get('audience_rule'), item.get('daily_cap')
            if not isinstance(rule, str) or not rule.strip() or len(rule) > 500:
                return {'accepted': False, 'error': 'Item %d: a template needs audience_rule, who it goes to, in up to 500 characters (for example "members who have not booked in 90 days").' % number}
            if not _num(cap) or cap != int(cap) or not 1 <= cap <= MAX_TEMPLATE_CAP:
                return {'accepted': False, 'error': 'Item %d: a template needs daily_cap, the most messages a day built from it, a whole number from 1 to %d.' % (number, MAX_TEMPLATE_CAP)}
            _, names, limits = _template_slots(text)
            entry.update(audience_rule=rule.strip(), daily_cap=int(cap), placeholders=names, placeholder_limits=dict(zip(names, limits)), sent_by_day={}, handed_by_day={})
        for key in ('when', 'link_target'):
            if item.get(key) not in (None, ''): entry[key] = str(item[key])[:600]
        clean.append(entry)
    batch = {'batch_id': batch_id, 'created': now, 'week_of': time.strftime('%Y-%m-%d', time.gmtime(start)), 'valid_until': max(now, start) + 7 * DAY, 'items': clean}
    record['batches'] = (record.get('batches') or []) + [batch]; del record['batches'][:-30]
    _save_campaign(store, owner, record)
    store.log(owner + '#campaign', 0, batch_id, 'batch', {'items': len(clean), 'week_of': batch['week_of']})
    kinds = {}
    for entry in clean: kinds[entry['kind']] = kinds.get(entry['kind'], 0) + 1
    templates = [entry for entry in clean if entry['kind'] == 'template']
    volume = (' Approving a template lets me send up to its daily cap of personalised messages built from it each day: ' + '; '.join(
        '%s up to %d a day to %s' % (entry['id'], entry['daily_cap'], entry['audience_rule']) for entry in templates) + '.') if templates else ''
    return {'accepted': True, 'batch_id': batch_id, 'items': len(clean), 'status': 'awaiting_owner', 'valid_until': _when(batch['valid_until']),
            'approval_needed': {'tell_the_owner': 'I prepared %d items for the next 7 days (%s), batch %s. Please read them and approve the ones you want published.' % (len(clean), ', '.join('%d %s' % (n, k) for k, n in kinds.items()), batch_id) + volume,
                                'where': 'The owner approves on their private owner page (hosted service) or runs "nuluno.py approve %s" in their own terminal (local engine). There is no tool for approving.' % batch_id,
                                'rule': 'You cannot approve. Publish an item only after batch_status shows it approved, with exactly its text, and pass its id as approved_item in submit_step.'}}


def batch_status(store, owner, product, args):
    record = _campaign(store, owner)
    if not record: return {'batches': [], 'note': 'No month target yet.'}
    now = time.time(); out = []
    for batch in reversed((record.get('batches') or [])[-10:]):
        out.append({'batch_id': batch['batch_id'], 'status': _batch_state(batch, now), 'week_of': batch['week_of'], 'valid_until': _when(batch['valid_until']),
                    'items': [_item_view(item, now) for item in batch['items']]})
    return {'batches': out, 'note': 'Publish only items in state approved, with exactly their text, and pass the id as approved_item. used means already published. '
                                    'A template stays approved for its batch week: each message built from it (placeholders filled, the rest unchanged) counts toward its daily_cap. '
                                    'Each placeholder value: ' + TEMPLATE_VALUE_RULE + '.'}


def _day(ts=None): return time.strftime('%Y-%m-%d', time.gmtime(ts or time.time()))


def _item_view(item, now=None):
    view = {key: item.get(key) for key in ('id', 'lane', 'kind', 'channel', 'text', 'when', 'link_target', 'state', 'approved_by', 'used_receipt',
                                           'audience_rule', 'daily_cap', 'placeholders', 'placeholder_limits') if item.get(key) is not None}
    if item.get('kind') == 'template':
        sent = (item.get('sent_by_day') or {}).get(_day(now), 0)
        view.update(sent_today=sent, remaining_today=max(0, item['daily_cap'] - sent))
    return view


def _template_slots(text):
    """(fixed text pieces, placeholder names, the most characters each placeholder may hold) of a template, compared
    after normalising like any approved text. {topic:120} sets a placeholder's own limit."""
    norm = _same_text(text); fixed, names, limits, at = [], [], [], 0
    for match in _PLACEHOLDER.finditer(norm):
        fixed.append(norm[at:match.start()]); names.append(match.group(1)); at = match.end()
        limits.append(int(match.group(2)) if match.group(2) else (NAME_PLACEHOLDER_CHARS if _name_like(match.group(1)) else PLACEHOLDER_DEFAULT_CHARS))
    fixed.append(norm[at:])
    return fixed, names, limits


def _template_parts(text):
    fixed, names, _ = _template_slots(text)
    return fixed, names


def _name_like(name): return name.lower() in ('first_name', 'last_name', 'name', 'full_name', 'company', 'company_name', 'name_or_handle', 'handle')
def _link_like(name): return name.lower() in ('link', 'url', 'tracked_link') or name.lower().endswith(('_link', '_url'))


def _template_problem(text):
    fixed, names, limits = _template_slots(text)
    if len(names) > MAX_PLACEHOLDERS: return 'a template has at most %d placeholders.' % MAX_PLACEHOLDERS
    if any(not piece for piece in fixed[1:-1]): return 'two placeholders cannot touch; put fixed text between them (for example "{first_name} {last_name}").'
    bad = [name for name, most in zip(names, limits) if not 1 <= most <= PLACEHOLDER_MAX_CHARS]
    if bad: return 'a placeholder limit such as {%s:120} is 1 to %d characters.' % (bad[0], PLACEHOLDER_MAX_CHARS)
    if len(''.join(''.join(fixed).split())) < TEMPLATE_MIN_FIXED:
        return 'a template keeps at least %d characters of fixed text (the words around the placeholders that the owner approves).' % TEMPLATE_MIN_FIXED
    return None


_LINE_BREAKS = '\n\r\x0b\x0c\x1c\x1d\x1e\x85  '
# A domain on any top-level domain (evil.lol, x.zip) counts as a link. A few dotted words that are not domains are
# allowed first: framework names and abbreviations.
_NOT_DOMAINS = r'(?:node\.js|vue\.js|next\.js|nuxt\.js|react\.js|asp\.net|e\.g|i\.e)(?![a-z0-9-]|\.[a-z0-9])'
_DOMAIN = r'(?<![a-z0-9-])(?!%s)[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,24}(?![a-z0-9-])' % _NOT_DOMAINS
_URLISH = re.compile(r'(?i)(?:[a-z][a-z0-9+.-]*://|www\.|%s|\b\d{1,3}(?:\.\d{1,3}){3}\b|[^\s@]+@[^\s@]+\.[^\s@]+)' % _DOMAIN)
_SENTENCE_BREAK = re.compile(r'[.!?]+["\'’”)\]]*\s+[A-Z]|[。！？]\s*\S')


def _value_problem(name, value, most, fixed, links=(), urlish=None, new_sentence=None):
    """Why one placeholder value is refused, or None. A value fills a slot: a name, a topic, a tip. It never brings
    a link (except a link placeholder holding the product's or the round's tracked link), an address, a new sentence
    or more lines, and it never repeats the template's own fixed text. urlish and new_sentence may be worked out
    beforehand for the whole text (see _template_fill)."""
    if not value.strip(): return 'an empty value'
    if len(value) > most: return '{%s} is %d characters, more than its %d' % (name, len(value), most)
    if any(ch in value for ch in _LINE_BREAKS): return '{%s} spans more than one line' % name
    if _link_like(name):
        if ' ' in value.strip() or not _allowed_link(value.strip(), links):
            return '{%s} must be exactly the product link or the round\'s tracked link' % name
        return None
    if urlish if urlish is not None else _URLISH.search(value): return '{%s} contains a link, a domain or an address' % name
    if new_sentence if new_sentence is not None else _SENTENCE_BREAK.search(value): return '{%s} starts a new sentence' % name
    if _name_like(name) and (len(value.split()) > 6 or re.search(r'[,;:!?|<>{}\[\]]', value)): return '{%s} is not a name' % name
    flat = value.lower()
    if any(len(piece.strip()) >= 8 and piece.strip().lower() in flat for piece in fixed): return '{%s} repeats the template\'s fixed text' % name
    return None


def _allowed_link(value, links):
    """value is one of links, with an optional ?query or #part; a link ending in / also allows any path below it."""
    for link in links:
        if value == link or value.startswith(link + '?') or value.startswith(link + '#'): return True
        if link.endswith('/') and value.startswith(link): return True
    return False


def _link_prefixes(store, owner, product, item, rounds=0):
    """Links a link placeholder may hold: pages of the product's site and of the item's link_target, and the lane's
    tracked links (hosted service)."""
    out = []
    url = product if isinstance(product, str) else (product.get('url') if isinstance(product, dict) else None)
    for given in (url, (item or {}).get('link_target')):
        found = re.match(r'(https://[A-Za-z0-9.-]+(?::[0-9]+)?)(?:[/?#]|$)', str(given or '').strip())
        if found: out += [found.group(1), found.group(1) + '/']
    if hasattr(store, 'tracked_link'):
        for number in range(max(1, rounds - 4), rounds + 1):
            try: link = store.tracked_link(owner, number, '')
            except Exception: link = None
            if link: out.append(str(link).split('?')[0].split('#')[0])
    return tuple(out)


def _template_fill(template, text, links=()):
    """(True, None) when text is the template with every placeholder filled by an allowed value (see _value_problem)
    and the fixed text unchanged (whitespace normalised; a line break may stand for a space in the fixed text only).
    Otherwise (False, why). Matched by walking the fixed pieces, so the time stays bounded for any input."""
    fixed, names, limits = _template_slots(template)
    import unicodedata
    marked = re.sub(r'\s+', lambda m: '\n' if any(ch in m.group() for ch in _LINE_BREAKS) else ' ', unicodedata.normalize('NFKC', str(text))).strip()
    sent = marked.replace('\n', ' ')  # the same length: a value is read from marked, the fixed text compared on sent
    if not names: return (True, None) if sent == fixed[0] else (False, 'the text is not the approved text')
    if not sent.startswith(fixed[0]): return False, 'the text does not start like the template'
    # links and sentence breaks found once in the whole text: a value is refused when one touches (link) or lies in
    # (sentence break) its span. Prefix sums keep each check constant, so adversarial input stays fast.
    import bisect
    flags = [0] * (len(marked) + 1)
    for match in _URLISH.finditer(marked):
        for i in range(match.start(), match.end()): flags[i + 1] = 1
    for i in range(len(marked)): flags[i + 1] += flags[i]
    breaks = [(m.start(), m.end()) for m in _SENTENCE_BREAK.finditer(marked)]; starts = [b[0] for b in breaks]
    def inside(at, end):  # breaks do not overlap, so the first one starting in the span is the one to check
        i = bisect.bisect_left(starts, at)
        return i < len(breaks) and breaks[i][1] <= end
    positions, why = {len(fixed[0])}, None
    for index, (name, most) in enumerate(zip(names, limits)):
        piece, last, reached = fixed[index + 1], index == len(names) - 1, set()
        for at in positions:
            for size in range(1, most + 1):
                end = at + size
                if end > len(sent): break
                fits = (end + len(piece) == len(sent) and sent.endswith(piece)) if last else sent.startswith(piece, end)
                if not fits: continue
                problem = _value_problem(name, marked[at:end], most, fixed, links, flags[end] - flags[at] > 0, inside(at, end))
                if problem: why = why or problem; continue
                if last: return True, None
                reached.add(end + len(piece))
        positions = reached
        if not positions: break
    return False, why or 'the fixed text differs from the template, or a value is longer than its limit'


def _fills_template(template, text, links=()):
    return _template_fill(template, text, links)[0]


def approve_batch(store, owner, batch_id, item_ids, by):
    """For the owner's own front end only (local command run by the owner, hosted owner page). Never a tool.
    item_ids is 'all' or a list of item ids."""
    record = _campaign(store, owner)
    batch = next((b for b in (record or {}).get('batches') or [] if b['batch_id'] == batch_id), None)
    if not batch: return {'approved': False, 'error': 'No batch %s.' % batch_id}
    now = time.time()
    if now > batch['valid_until']: return {'approved': False, 'error': 'Batch %s has expired (it covered the week of %s). Ask for a new batch.' % (batch_id, batch['week_of'])}
    if item_ids == 'all': wanted = [item['id'] for item in batch['items'] if item['state'] == 'awaiting_owner']
    elif isinstance(item_ids, (list, tuple)) and item_ids: wanted = [str(i) for i in item_ids]
    else: return {'approved': False, 'error': 'Name the item ids to approve, or all.'}
    known = {item['id']: item for item in batch['items']}
    unknown = [i for i in wanted if i not in known]
    if unknown: return {'approved': False, 'error': 'Not in batch %s: %s.' % (batch_id, ', '.join(unknown))}
    done = []
    for item_id in wanted:
        item = known[item_id]
        if item['state'] == 'awaiting_owner': item.update(state='approved', approved_at=now, approved_by=str(by)[:120]); done.append(item_id)
    _save_campaign(store, owner, record)
    store.log(owner + '#campaign', 0, batch_id, 'approval', {'approved': done, 'by': str(by)[:120]})
    return {'approved': True, 'batch_id': batch_id, 'approved_items': done, 'status': _batch_state(batch, now)}


def approve_ad_budget(store, owner, by):
    """For the owner's own front end only. Never a tool."""
    record = _campaign(store, owner); budget = (record or {}).get('ad_budget')
    if not budget: return {'approved': False, 'error': 'No ad budget was requested.'}
    if not budget.get('approved_at'):
        budget.update(approved_at=time.time(), approved_by=str(by)[:120]); _save_campaign(store, owner, record)
        store.log(owner + '#campaign', 0, 'ad_budget', 'approval', {'daily_cap_minor': budget['daily_cap_minor'], 'currency': budget['currency'], 'by': str(by)[:120]})
    return {'approved': True, 'ad_budget': budget}


def request_ad_budget(store, owner, product, args):
    record = _campaign(store, owner)
    if not record or record['status'] not in ('planning', 'running'): return {'accepted': False, 'error': 'An ad budget belongs to a month target. Call set_month_target first.'}
    cap, currency, channels = args.get('daily_cap'), str(args.get('currency') or '').strip().upper(), args.get('channels')
    if not _num(cap) or cap <= 0: return {'accepted': False, 'error': 'daily_cap is the most to spend on ads per day, all channels together, in the currency\'s main unit (10 for US$10).'}
    if not re.fullmatch(r'[A-Z]{3}', currency): return {'accepted': False, 'error': 'currency is a three-letter code such as USD or TWD.'}
    if not isinstance(channels, list) or not channels or not all(isinstance(c, str) and c.strip() for c in channels): return {'accepted': False, 'error': 'channels lists where the ads run, for example ["meta_ads"].'}
    record['ad_budget'] = {'daily_cap_minor': int(round(cap * 100)), 'currency': currency, 'channels': [c.strip()[:40] for c in channels][:8], 'requested_at': time.time(), 'approved_at': None, 'approved_by': None}
    _save_campaign(store, owner, record)
    return {'accepted': True, 'status': 'awaiting_owner', 'ad_budget': record['ad_budget'],
            'approval_needed': {'tell_the_owner': 'Please approve a daily ad budget cap of %s %.2f for %s. Ads never spend more than this a day without asking you again.' % (currency, cap, ', '.join(record['ad_budget']['channels'])),
                                'where': 'The owner approves on their private owner page (hosted service) or runs "nuluno.py approve-budget" in their own terminal (local engine). There is no tool for approving.',
                                'rule': 'Until the owner approves, do not start or raise any ad spend.'}}


def _approved(record, lane, item_id):
    """(item, None) when item_id is an approved, unused, unexpired item of this lane; else (None, why)."""
    now = time.time()
    for batch in record.get('batches') or []:
        for item in batch['items']:
            if item['id'] != str(item_id): continue
            if item['lane'] != lane: return None, 'Item %s belongs to lane %s, not %s.' % (item_id, item['lane'], lane)
            if item['state'] == 'used': return None, 'Item %s was already published (%s). Each approved item is used once.' % (item_id, item.get('used_receipt'))
            if item['state'] != 'approved': return None, 'Item %s is not approved by the owner yet. Show the owner the exact text first, or wait until batch_status shows it approved.' % item_id
            if now > batch['valid_until']: return None, 'The approval of item %s has expired (batch for the week of %s). Get the owner\'s approval again.' % (item_id, batch['week_of'])
            if item.get('kind') == 'template':
                sent = (item.get('sent_by_day') or {}).get(_day(now), 0)
                return dict(item, sent_today=sent, remaining_today=max(0, item['daily_cap'] - sent)), None
            return item, None
    return None, 'No item %s in any batch. batch_status lists them.' % item_id


def _approved_for(record, lane):
    now = time.time()
    return [{key: value for key, value in _item_view(item, now).items() if key in ('id', 'kind', 'channel', 'text', 'when', 'audience_rule', 'daily_cap', 'sent_today', 'remaining_today')}
            for batch in record.get('batches') or [] if now <= batch['valid_until'] for item in batch['items'] if item['lane'] == lane and item['state'] == 'approved'][:10]


LANE_APPROVAL_RULE = ('Required on a month target lane: a step that publishes or sends something is accepted only with approved_item, the id of an item the owner approved. '
                      'Put the exact text in submit_batch; the owner approves it on their owner page (hosted service) or by running "python3 nuluno.py approve <batch_id> --all" in their own terminal (local engine). '
                      'Then publish exactly that text and pass its id as approved_item in submit_step. Until then, submit the step with status "blocked" and needs. '
                      'For many personalised messages, submit one item of kind template instead: text with {placeholders} such as {first_name}, audience_rule and daily_cap. '
                      'Once approved, put every message you sent from it in output (one string each); each counts toward the daily cap. next_recipients gives the next people from the owner\'s list (hosted service).')


def _lane_step_sends(store, key, step_id):
    """True when step_id is the lane's current step and it publishes or sends something outside."""
    state = _load(store, key)
    if state['status'] not in ('working', 'observing') or not state.get('nodes'): return False
    if state['status'] == 'observing' and time.time() < state.get('wait_until', 0): return False
    node = state['nodes'][state['cursor']]
    if node['measure'] or str(step_id) != '%s:r%d' % (node['node'], state['round']): return False
    info = skill(node['skill'])
    return bool(info['needs_link'] or info['writes'])


def _decorate(record, lane, result):
    """Month target notes on a lane's step: approved batch items for publishing steps, the approved cap for ad lanes."""
    for step in (result, result.get('next') if isinstance(result.get('next'), dict) else None):
        if not isinstance(step, dict) or 'state' not in step: continue
        step['lane'] = lane
        if step['state'] not in ('work', 'waiting_on_owner'): continue
        if step.get('publishing'):
            step['publishing'] = step['publishing'].replace('Show the owner the exact text first. ', 'Publish only an item the owner approved in a weekly batch (see batch_approval). ').replace(
                'Show the owner exactly what will be sent before it goes out.', 'Send only an item the owner approved in a weekly batch (see batch_approval).')
            step['batch_approval'] = LANE_APPROVAL_RULE
            step['approved_items'] = _approved_for(record, lane)
        if _ad_lane(lane): step['ad_budget'] = _ad_rule(record)


def _month_numbers(store, owner, record, lane, args):
    """record_numbers on a lane: totals since the start (paid_customers, visits) go to the month target, and ad spend
    is checked against the approved daily cap. Returns flags for the answer."""
    values = args.get('values') if isinstance(args.get('values'), dict) else {}
    source = str(args.get('source', ''))[:500]; flags = {}; now = time.time(); changed = False
    if source:
        kept = [key for key in MONTH_NUMBERS if _num(values.get(key))]
        for key in kept: record.setdefault('recorded', {})[key] = {'value': values[key], 'source': source, 'at': now, 'lane': lane}
        if kept: flags['month_numbers_recorded'] = kept; changed = True
    state = _load(store, lane_owner(owner, lane))
    measuring = state['status'] in ('working', 'observing') and state.get('nodes') and state['nodes'][state['cursor']]['measure'] == 'current'
    spend = values.get('spend_minor') if _num(values.get('spend_minor')) else (values['spend'] * 100 if _num(values.get('spend')) else None)
    if _ad_lane(lane) and measuring and spend is not None:
        budget = record.get('ad_budget') or {}
        if budget.get('approved_at'):
            days = max(1, int(math.ceil((now - max(budget['approved_at'], record['target']['start'])) / float(DAY))))
            allowed = days * budget['daily_cap_minor']; why = '%d day(s) x %s %.2f approved cap' % (days, budget['currency'], budget['daily_cap_minor'] / 100.0)
        else: allowed = 0; why = 'no daily ad budget is approved'
        if spend > allowed:
            flags.update(over_budget=True, over_budget_detail='Spend %.2f is above %.2f allowed (%s). Pause or lower the ads and tell the owner.' % (spend / 100.0, allowed / 100.0, why))
            record.setdefault('alerts', []).append({'kind': 'over_budget', 'lane': lane, 'spend_minor': spend, 'allowed_minor': allowed, 'why': why, 'at': now}); del record['alerts'][:-20]
            changed = True
    if changed: _save_campaign(store, owner, record)
    return flags


def _count_day(entry, key, amount):
    days = entry.setdefault(key, {}); today = _day()
    days[today] = days.get(today, 0) + amount
    for old in sorted(days)[:-14]: del days[old]


def next_recipients(store, owner, product, args):
    """The next people to message with an approved template, from the owner's list, never more than its daily cap."""
    args = args if isinstance(args, dict) else {}
    record = _campaign(store, owner); lane = str(args.get('lane') or '').strip(); item_id = str(args.get('item_id') or '').strip()
    if not record or lane not in (record.get('lanes') or []):
        return {'accepted': False, 'error': 'lane must be one of the month target lanes: %s.' % (', '.join(record['lanes']) if record and record.get('lanes') else 'none yet')}
    item, problem = _approved(record, lane, item_id)
    if problem: return {'accepted': False, 'error': problem}
    if item.get('kind') != 'template': return {'accepted': False, 'error': 'next_recipients works with an approved item of kind template; %s is a single %s.' % (item_id, item['kind'])}
    n = args.get('n', 20)
    if not _num(n) or n != int(n) or not 1 <= n <= 200: return {'accepted': False, 'error': 'n is a whole number from 1 to 200.'}
    entry = next(e for batch in record['batches'] for e in batch['items'] if e['id'] == item['id'])
    handed = (entry.get('handed_by_day') or {}).get(_day(), 0); left = entry['daily_cap'] - handed
    base = {'item_id': item['id'], 'daily_cap': entry['daily_cap'], 'audience_rule': entry['audience_rule'], 'template': entry['text'], 'sent_today': item['sent_today']}
    if left <= 0: return dict(base, accepted=False, remaining_today=0, error='Template %s already handed out its %d recipients for today. Continue tomorrow.' % (item['id'], entry['daily_cap']))
    if not callable(getattr(store, 'next_recipients', None)):
        return dict(base, accepted=True, available=False, remaining_today=item['remaining_today'],
                    note='This engine holds no recipient list (the hosted service keeps a list the owner uploads). Use your own list of people who match audience_rule, '
                         'send at most remaining_today messages from this template today, and put each sent message in output when you submit the step with approved_item.')
    found, problem = _hook(store, 'next_recipients', owner, lane, item['id'], int(min(n, left)))
    note = problem
    if isinstance(found, dict): note = note or found.get('note'); found = found.get('recipients')
    recipients = [r for r in (found or []) if isinstance(r, dict)][:int(min(n, left))]
    if recipients:
        _count_day(entry, 'handed_by_day', len(recipients)); _save_campaign(store, owner, record)
    answer = dict(base, accepted=True, available=bool(recipients), recipients=recipients, remaining_today=left - len(recipients),
                  rule='Send each person one message built from the template (fill the placeholders from their row, leave the rest unchanged; each value: ' + TEMPLATE_VALUE_RULE + '), only through the channel the template names. '
                       'Then submit the lane step with approved_item %s and every sent message in output. Skip anyone whose row does not match audience_rule.' % item['id'])
    if not recipients: answer['note'] = note or 'No more recipients on the uploaded list for this template. The owner can upload a list on their owner page.'
    return answer


def _with_lane(name, tool):
    """Every goal tool also works on one lane of a month target (lane=<goal id>). Without lane it is unchanged."""
    def run(store, owner, product, args):
        args = args if isinstance(args, dict) else {}
        lane, item_id = args.get('lane'), args.get('approved_item')
        if lane is None:
            if item_id is not None: return {'accepted': False, 'error': 'approved_item works only on a month target lane: pass lane too.'}
            result = tool(store, owner, product, args)
            if name == 'where_are_we':
                record = _campaign(store, owner)
                if record and record['status'] in ('planning', 'running'):
                    result['month_target'] = dict(_summary(record), call='month_status', note='A month target is %s. Call month_status: it names the lane to work on now. Pass lane on every call for that lane.' % record['status'])
            return result
        args = {key: value for key, value in args.items() if key not in ('lane', 'approved_item')}
        record = _campaign(store, owner); lane = str(lane).strip()
        if not record or lane not in (record.get('lanes') or []):
            return {'accepted': False, 'error': 'lane must be one of the month target lanes: %s.' % (', '.join(record['lanes']) if record and record.get('lanes') else 'none yet (call set_month_target, then plan_month)')}
        key = lane_owner(owner, lane)
        if name == 'set_goal':
            if str(args.get('goal_id') or lane) != lane: return {'accepted': False, 'error': 'A lane works on its own goal (%s). To change lanes, call plan_month.' % lane}
            args['goal_id'] = lane
        flags = _month_numbers(store, owner, record, lane, args) if name == 'record_numbers' else {}
        item = None
        if name == 'submit_step' and item_id is not None:
            item, problem = _approved(record, lane, item_id)
            if problem:
                answer = {'accepted': False, 'error': problem, 'next': next_step(store, key, product, {})}
                _decorate(record, lane, answer); return answer
        elif name == 'submit_step' and args.get('status', 'done') == 'done' and _lane_step_sends(store, key, args.get('step_id', '')):
            answer = {'accepted': False, 'approved_item_required': True,
                      'error': ('This lane step publishes or sends something, so it needs approved_item. Hand the owner the exact text with submit_batch (lane %s), '
                                'have the owner approve it on their owner page (hosted service) or with "python3 nuluno.py approve <batch_id> --all" in their own terminal (local engine), '
                                'then publish exactly that text and submit this step with approved_item set to its id. batch_status shows what is approved. '
                                'If the owner must do something first, submit status "blocked" with needs.') % lane,
                      'next': next_step(store, key, product, {})}
            _decorate(record, lane, answer); return answer
        result = submit_step(store, key, product, args, approval=item) if item else tool(store, key, product, args)
        result = dict(result); result.update(flags); result['lane'] = lane
        if name in ('submit_step', 'record_numbers') and result.get('accepted'):
            record = _campaign(store, owner); record.setdefault('touched', {})[lane] = time.time()
            if name == 'record_numbers' and result.get('recorded_as') == 'result':
                values = args.get('values') if isinstance(args.get('values'), dict) else {}
                clicks = sum(values[k] for k in CLICK_KEYS if _num(values.get(k)))
                record.setdefault('lane_results', {}).setdefault(lane, []).append({'round': _load(store, key)['round'], 'clicks': clicks, 'at': time.time()})
                del record['lane_results'][lane][:-60]
            if item:
                for batch in record['batches']:
                    for entry in batch['items']:
                        if entry['id'] != item['id']: continue
                        if entry.get('kind') == 'template':  # a template stays approved; its messages are counted per day
                            _count_day(entry, 'sent_by_day', result.get('template_messages_counted') or 0)
                            entry['last_receipt'] = result.get('receipt')
                        else: entry.update(state='used', used_at=time.time(), used_receipt=result.get('receipt'), used_links=args.get('links') if isinstance(args.get('links'), list) else [])
            _save_campaign(store, owner, record)
        _decorate(record, lane, result)
        return result
    return run


GOAL_TOOLS = {'where_are_we': where_are_we, 'set_goal': set_goal, 'next_step': next_step, 'submit_step': submit_step,
              'record_numbers': record_numbers, 'read_page': read_page, 'stop_goal': stop_goal, 'tracking': tracking}
TOOLS = {name: _with_lane(name, tool) for name, tool in GOAL_TOOLS.items()}
TOOLS.update({'set_month_target': set_month_target, 'plan_month': plan_month, 'month_status': month_status,
              'submit_batch': submit_batch, 'batch_status': batch_status, 'request_ad_budget': request_ad_budget, 'next_recipients': next_recipients})

# Tool descriptions shared by every MCP front end.
TOOL_SPECS = [
    {'name': 'where_are_we', 'description': 'START HERE in every conversation. Returns the product, the sales goal, what was delivered most recently, the numbers so far and the next step. Nothing is lost between chats.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'read_page', 'description': 'Read one public https page (default: the product page) and get its text with a content hash. Use it to collect product facts; never invent facts that are not on a page you read. little_text means a login wall or a script-only page: ask the owner to paste the text.',
     'inputSchema': {'type': 'object', 'properties': {'url': {'type': 'string'}}, 'additionalProperties': False}},
    {'name': 'set_goal', 'description': 'Choose the sales goal (goal_id from where_are_we). Optional numeric target: for a rate or cost, the value to reach; for a count (followers, purchases), the increase over the baseline. Without one a round succeeds when a rate is 20% better than baseline or a count grows by 10. Calling it again with the same goal only changes the target.',
     'inputSchema': {'type': 'object', 'properties': {'goal_id': {'type': 'string'}, 'target': {'type': 'number'}, 'why': {'type': 'string'}}, 'required': ['goal_id'], 'additionalProperties': False}},
    {'name': 'next_step', 'description': 'Get the current step: what to do, the checklist, what to deliver, what was already delivered and lessons from earlier rounds. Call it whenever you are unsure what to do next.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'submit_step', 'description': 'Record the finished step and receive the following one. output is a JSON object with the deliverable keys the step listed. If a person is needed (login, approval, numbers only the owner can see), use status "blocked" and say in needs the one thing the owner must do. A publishing step needs the public URL of the post itself as the first item in links; the engine opens it and refuses a profile page or a link that does not exist.',
     'inputSchema': {'type': 'object', 'properties': {'step_id': {'type': 'string'}, 'status': {'type': 'string', 'enum': ['done', 'blocked']}, 'output': {'type': 'object'}, 'links': {'type': 'array', 'items': {'type': 'string'}}, 'needs': {'type': 'string'}}, 'required': ['step_id'], 'additionalProperties': False}},
    {'name': 'record_numbers', 'description': 'Record real numbers read from the platform (baseline before publishing, results after the observation window). values holds the metric components by name; source says where and when they were read. Numbers the engine counted itself (the step lists them) can be left out. The engine decides whether the target is reached; if not it opens another round.',
     'inputSchema': {'type': 'object', 'properties': {'values': {'type': 'object', 'additionalProperties': {'type': 'number'}}, 'source': {'type': 'string'}}, 'required': ['values', 'source'], 'additionalProperties': False}},
    {'name': 'tracking', 'description': 'Get the tracked link for this round, the sale counter for the page shown after payment, and the clicks and sales the engine has counted itself. Hosted service only; the local server answers that it does not count.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'stop_goal', 'description': 'Stop working on the current goal when the owner says so. Everything delivered stays on record.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'set_month_target', 'description': 'Start a month target, for example 100 paying customers in 30 days (days 7 to 90). kind paid_customers (amount = customers) or revenue_minor (amount in cents; needs price). price is what one customer pays (39 for US$39); current_paid counts customers already won toward this target. Then call plan_month.',
     'inputSchema': {'type': 'object', 'properties': {'amount': {'type': 'number'}, 'kind': {'type': 'string', 'enum': list(MONTH_KINDS)}, 'days': {'type': 'integer'}, 'price': {'type': 'number'},
                                                      'currency': {'type': 'string'}, 'current_paid': {'type': 'integer'}, 'why': {'type': 'string'}, 'replace': {'type': 'boolean'}}, 'required': ['amount'], 'additionalProperties': False}},
    {'name': 'plan_month', 'description': 'Choose the lanes of the month target: 3 to 5 goal ids on different channels (the plan may allow fewer), or a preset (new_brand, existing_base, b2b_self_serve, b2b_sales) that picks them, with inputs you know (price, members, paid, trials_per_week ...). The engine works the target back into what is needed per day at each layer, says which rates are measured and which assumed, judges honestly whether the lanes can reach it (feasibility: verdict, gap, levers), lists asks only the owner can answer, and starts every lane. Show the owner tell_the_owner. Call again with more inputs to update the plan.',
     'inputSchema': {'type': 'object', 'properties': {'lanes': {'type': 'array', 'items': {'type': 'string'}}, 'preset': {'type': 'string', 'enum': list(PRESETS)},
                                                      'inputs': {'type': 'object'}, 'funnel': {'type': 'object'}}, 'additionalProperties': False}},
    {'name': 'month_status', 'description': 'Where the month target stands: paid customers and visits so far with their source, pace, what each lane needs today, feasibility (can the lanes still reach it, the gap, the levers), asks for the owner, approvals waiting, the ad budget, and next: the lane and step to work on now.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'submit_batch', 'description': 'Hand the owner up to 50 items (posts, replies, emails, ads, messages) for the coming 7 days to approve in one go. Each item: lane, kind, channel, the exact text, optional when and link_target. A template item (kind template) is a text with {placeholders} plus audience_rule and daily_cap: approving it allows up to daily_cap personalised messages a day built from it. You cannot approve; the owner does it on their own page or terminal.',
     'inputSchema': {'type': 'object', 'properties': {'items': {'type': 'array', 'items': {'type': 'object', 'properties': {'lane': {'type': 'string'}, 'kind': {'type': 'string', 'enum': list(ITEM_KINDS)}, 'channel': {'type': 'string'},
                                                                                                                         'text': {'type': 'string'}, 'when': {'type': 'string'}, 'link_target': {'type': 'string'},
                                                                                                                         'audience_rule': {'type': 'string'}, 'daily_cap': {'type': 'integer'}}, 'required': ['lane', 'kind', 'channel', 'text']}},
                                                      'week_of': {'type': 'string'}}, 'required': ['items'], 'additionalProperties': False}},
    {'name': 'batch_status', 'description': 'List the weekly batches and the state of each item: awaiting_owner, approved (may be published with exactly its text) or used.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False}},
    {'name': 'next_recipients', 'description': 'For an approved template (item_id) on a lane: the next n people to message from the owner\'s uploaded list, never more than its daily cap a day. The local engine holds no list and says so; then use your own list that matches audience_rule.',
     'inputSchema': {'type': 'object', 'properties': {'lane': {'type': 'string'}, 'item_id': {'type': 'string'}, 'n': {'type': 'integer'}}, 'required': ['lane', 'item_id'], 'additionalProperties': False}},
    {'name': 'request_ad_budget', 'description': 'Ask the owner to approve one daily ad budget cap for the month target (all ad channels together, in the currency\'s main unit). Spend nothing until it is approved; record_numbers on an ad lane flags spend above the cap.',
     'inputSchema': {'type': 'object', 'properties': {'daily_cap': {'type': 'number'}, 'currency': {'type': 'string'}, 'channels': {'type': 'array', 'items': {'type': 'string'}}}, 'required': ['daily_cap', 'currency', 'channels'], 'additionalProperties': False}},
]

# Every goal tool also takes lane, and submit_step takes approved_item (month target only).
for _spec in TOOL_SPECS:
    if _spec['name'] in GOAL_TOOLS:
        _spec['inputSchema']['properties']['lane'] = {'type': 'string', 'description': 'Month target only: the lane to work on (its goal id, as month_status names it). Leave out otherwise.'}
    if _spec['name'] == 'submit_step':
        _spec['inputSchema']['properties']['approved_item'] = {'type': 'string', 'description': 'Month target lane only, and required there on a step that publishes or sends: the id of a batch item the owner approved; the step must publish exactly its text.'}
del _spec

INSTRUCTIONS = ('Nuluno Engine keeps a sales goal moving across conversations. Always call where_are_we first. Then repeat: next_step, do the work yourself, submit_step. '
                'Keep going without asking the owner for things you can decide. Stop only when the engine says to wait for results, the owner must do something, or the goal is reached. '
                'If where_are_we shows a month_target, call month_status and work the lane it names, passing lane on every call. '
                'Report results to the owner in their language.')
