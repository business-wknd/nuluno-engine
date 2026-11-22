#!/usr/bin/env python3
"""Write the Agent Skills folder (skills/) from engine/library.json.

    python3 engine/pack.py [repo folder, default: the folder above engine/]

One skill per channel, each holding the full playbooks of its goals in references/,
plus the sales-goal skill: the loop itself, with a copy of the engine in scripts/
so it runs anywhere Python 3 runs (no MCP client needed). Run after editing the library.
"""
import json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pages

VERSION = '0.2.0'

# skill name -> (channels it holds, what the user is trying to do there)
GROUPS = {
    'instagram-growth': (['instagram'], 'Instagram: more followers, profile visits, bio link clicks, saves, Reels watched to the end and qualified inquiries'),
    'tiktok-growth': (['tiktok'], 'TikTok: more followers, videos watched to the end, profile visits, website clicks and purchases'),
    'threads-growth': (['threads'], 'Threads: more followers, buyer conversations, useful replies to requests for help and clicks to the product'),
    'x-growth': (['x'], 'X (Twitter): more followers, profile visits, website clicks and buyer conversations'),
    'youtube-growth': (['youtube'], 'YouTube: more subscribers, videos watched to the end, description link clicks and real conversations'),
    'linkedin-growth': (['linkedin'], 'LinkedIn: more followers, leads in the right buyer role with verified public emails, inquiries and confirmed demos'),
    'reddit-marketing': (['reddit'], 'Reddit: find people asking for what the product does, reply helpfully, and turn the conversations into inquiries and verified purchases'),
    'pinterest-growth': (['pinterest'], 'Pinterest: more outbound clicks from Pins and more purchases from those visitors'),
    'facebook-groups': (['facebook_groups'], 'Facebook groups: more qualified replies to buyer requests and purchases from them'),
    'discord-community': (['discord'], 'Discord: more qualified replies to help answers, purchases from help conversations and members who complete tasks'),
    'messaging-apps': (['line', 'whatsapp'], 'LINE and WhatsApp: more qualified replies and purchases from targeted and template messages'),
    'email-marketing': (['email'], 'Email to an opted-in list: more buyer replies, clicks and purchases, fewer unsubscribes'),
    'webinars': (['webinar'], 'Live demos and webinars: more sign-ups who attend, one-to-one demos booked and purchases among attendees'),
    'partners-and-deals': (['partnerships'], 'Partners, referrals and sales follow-up: qualified referrals, paid purchases, trials that convert, stalled deals that reply, repeat purchases and company contracts'),
    'product-hunt-launch': (['producthunt'], 'Product Hunt: makers who fit the product with sourced public emails, then more tracked visits and purchases from the launch'),
    'search-visibility': (['search'], 'Search and AI answers: more qualified visits from outside articles and AI answers that cite the brand correctly'),
    'review-directories': (['reviews'], 'Review directories: more qualified inquiries and purchases from listing visits'),
    'press-coverage': (['earned_media'], 'Press, podcasts and newsletters: more qualified inquiries and purchases from coverage'),
    'audience-research': (['audience', 'multi'], 'Finding who buys and why: the buyer group, outcome and sales angle that bring real inquiries and kept purchases, and useful replies to public requests'),
    'app-store-listing': (['app_store', 'google_play'], 'App Store and Google Play: more listing visitors who download or install'),
    'meta-ads': (['meta_ads'], 'Meta ads (Facebook and Instagram): lower cost per conversion, purchase and lead, more link clicks and page loads, higher return on ad spend and net profit per customer'),
    'search-ads': (['google_ads', 'microsoft_ads', 'merchant_center'], 'Google Ads, Microsoft Ads and Google free listings: lower cost per purchase, search terms with buying intent, less wasted spend, more listing clicks and purchases'),
    'social-ads': (['tiktok_ads', 'linkedin_ads', 'reddit_ads', 'pinterest_ads'], 'TikTok, LinkedIn, Reddit and Pinterest ads: lower cost per conversion, lead and purchase, and higher click rates'),
}

LOOP = 'sales-goal'

RULES = [
    'One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.',
    'Use only facts you read on the product\'s pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.',
    'Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.',
    'Never publish, send or spend without the owner\'s approval of the exact text and amount. Never ask for a password.',
    'Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.',
    'If the target is missed, name one bottleneck from the playbook\'s list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.',
]


def hours(goal): return goal.get('observation_seconds', 172800) // 3600


def frontmatter(name, description):
    return '---\nname: %s\ndescription: %s\nmetadata:\n  version: %s\n  source: https://github.com/business-wknd/nuluno-engine\n---\n' % (name, json.dumps(description, ensure_ascii=False), VERSION)


def how_to_run(example):
    return '\n'.join([
        '## How to run a goal', '',
        '1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.',
        '2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine refuses unfinished steps, reads published links back, waits out the observation window and judges the round.',
        '3. If they are not connected, run the same engine from the `%s` skill: `python3 <%s skill folder>/scripts/nuluno.py goal %s`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.' % (LOOP, LOOP, example),
        '4. If neither can run, open the goal\'s playbook in `references/` and work it top to bottom under the rules below.', ''])


def channel_skill(name, channels, summary, library):
    goals = {g: v for g, v in library['goals'].items() if v['channel'] in channels}
    titles = '; '.join(v['title'] for v in goals.values())
    description = ('%s. Use when the user wants these results. %d measured goals: %s. Each goal is a step-by-step playbook with the number that decides success; '
                   'if a round misses, change one thing and run another. Works with the %s skill or the Nuluno Engine tools.') % (summary, len(goals), titles, LOOP)
    if len(description) > 1024: description = description[:1020].rsplit(';', 1)[0] + '...'
    first = next(iter(goals))
    rows = ['| `%s` | %s | `%s` | %d h | [playbook](references/%s.md) |' % (g, v['title'], v['metric']['key'], hours(v), g) for g, v in goals.items()]
    body = ['# ' + summary.split(':')[0] + ': measured goals', '',
            '%s. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.' % summary, '',
            how_to_run(first),
            '## Goals', '', '| Goal id | Goal | Metric | Wait before judging | Steps |', '|---|---|---|---|---|'] + rows + ['', '## Rules', ''] + ['- ' + r for r in RULES]
    folder_refs = {g: pages.page(g, v, library['skills']) for g, v in goals.items()}
    return frontmatter(name, description) + '\n' + '\n'.join(body) + '\n', folder_refs


def loop_skill(library):
    by_channel = {}
    for name, (channels, summary) in GROUPS.items():
        for g, v in library['goals'].items():
            if v['channel'] in channels: by_channel.setdefault(name, []).append(g)
    description = ('When the user wants to sell a product or get more clicks, sign-ups, customers or sales, and wants the work to keep going until a real number is reached: '
                   'picks one of 99 measured sales goals, works it one step at a time, records numbers before and after, and when the target is missed names one bottleneck '
                   'and changes one thing for the next round. Saves progress so a new chat continues. Includes a dependency-free engine (Python 3) that checks each step.')
    index = ['| Skill | Goals |', '|---|---|'] + ['| `%s` | %s |' % (name, ', '.join('`%s`' % g for g in ids)) for name, ids in by_channel.items()]
    body = '''# Sales goal

Work a sales goal until the numbers say it is done. You do the work; the engine in `scripts/` keeps the goal, the current step, everything handed in and the numbers, and decides when a round passed.

## Start

`scripts/` is inside this skill's folder; from another folder, use its full path. Progress is saved in `~/.nuluno-engine/`.

```bash
python3 scripts/nuluno.py start https://the-product.com/
python3 scripts/nuluno.py read
python3 scripts/nuluno.py goal G-TH-LINK-RATE
python3 scripts/nuluno.py next
```

`start` remembers the product. `read` fetches the product page; quote facts only from what it returns. `goal` sets the goal: pick it yourself from the channel skills below and tell the owner in one sentence. `status` shows where things stand at any time.

## Loop

1. `next` prints the current step: what to do, the checklist, the keys to hand back and lessons from earlier rounds.
2. Do the work. Then hand it in:
   `python3 scripts/nuluno.py submit <step_id> --output '{"key": "value", ...}'`
   Add `--link https://...` for a step that publishes something; the engine reads the page back. If a person is needed (login, approval), use `--blocked "the one thing the owner must do"` and ask the owner for exactly that.
3. When the step asks for numbers, read them on the platform and record them:
   `python3 scripts/nuluno.py numbers --values '{"link_clicks": 41, "views": 1200}' --source "Threads insights, 23 Nov 10:00"`
   The first reading is the baseline. The result is judged after the observation window.
4. If the target is missed, the engine asks for a diagnosis. Hand in `{"bottleneck": ..., "reason": ..., "one_change": ...}` with a bottleneck from its list. The next round starts with that one change; a change that was already tried is refused.
5. Repeat until the engine says the goal is reached, or the owner says stop (`stop`).

Every command prints JSON. Follow its `next` field; when unsure, run `next` again.

The engine's messages use its tool names. On the command line they are: `where_are_we` = `status`, `read_page` = `read`, `set_goal` = `goal`, `next_step` = `next`, `submit_step` = `submit`, `record_numbers` = `numbers`, `stop_goal` = `stop`.

## Other ways to run the same engine

- As MCP tools in Claude Code: `claude mcp add --scope user nuluno-engine -- python3 <this folder>/scripts/server.py`
- Installed as the Claude Code plugin from https://github.com/business-wknd/nuluno-engine the tools are already there.
- Hosted, for Claude.ai: one connection address from https://engine.nuluno.com/?lang=en. The hosted engine also counts clicks and sales itself through a tracked link, so the agent's own report is not what decides the round.

## Goals by skill

''' + '\n'.join(index) + '\n\n## Rules\n\n' + '\n'.join('- ' + r for r in RULES) + '\n'
    return frontmatter(LOOP, description) + '\n' + body


def write(repo):
    library = json.loads((HERE / 'library.json').read_text(encoding='utf-8'))
    covered = {c for channels, _ in GROUPS.values() for c in channels}
    missing = {v['channel'] for v in library['goals'].values()} - covered
    if missing: raise SystemExit('channels with no skill: %s' % ', '.join(sorted(missing)))
    out = Path(repo) / 'skills'
    if out.exists(): shutil.rmtree(out)
    for name, (channels, summary) in GROUPS.items():
        text, refs = channel_skill(name, channels, summary, library)
        folder = out / name; (folder / 'references').mkdir(parents=True)
        (folder / 'SKILL.md').write_text(text, encoding='utf-8')
        for goal_id, page in refs.items(): (folder / 'references' / (goal_id + '.md')).write_text(page, encoding='utf-8')
    loop = out / LOOP; (loop / 'scripts').mkdir(parents=True)
    (loop / 'SKILL.md').write_text(loop_skill(library), encoding='utf-8')
    for name in ('core.py', 'server.py', 'nuluno.py', 'library.json'): shutil.copyfile(HERE / name, loop / 'scripts' / name)
    print(len(GROUPS) + 1, 'skills ->', out)


if __name__ == '__main__':
    write(sys.argv[1] if len(sys.argv) > 1 else HERE.parent)
