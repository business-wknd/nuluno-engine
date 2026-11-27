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

VERSION = '0.4.0'

# skill name -> (channels it holds, what the user is trying to do there)
GROUPS = {
    'instagram-growth': (['instagram'], 'Instagram: more followers, profile visits, bio link clicks, saves, Reels watched to the end and qualified inquiries'),
    'tiktok-growth': (['tiktok'], 'TikTok: more followers, videos watched to the end, profile visits, website clicks and purchases'),
    'threads-growth': (['threads'], 'Threads: more followers, buyer conversations, useful replies to requests for help and clicks to the product'),
    'x-growth': (['x'], 'X (Twitter): more followers, profile visits, website clicks and buyer conversations'),
    'youtube-growth': (['youtube'], 'YouTube: more subscribers, videos watched to the end, description link clicks and real conversations'),
    'linkedin-growth': (['linkedin'], 'LinkedIn: more followers, leads in the right buyer role with verified public emails, inquiries and confirmed demos'),
    'reddit-marketing': (['reddit'], 'Reddit: find people asking for what the product does, reply helpfully, and turn the conversations into inquiries and counted purchases'),
    'pinterest-growth': (['pinterest'], 'Pinterest: more outbound clicks from Pins and more purchases from those visitors'),
    'facebook-groups': (['facebook_groups'], 'Facebook groups: more qualified replies to buyer requests and purchases from them'),
    'discord-community': (['discord'], 'Discord: more qualified replies to help answers, purchases from help conversations and members who complete tasks'),
    'messaging-apps': (['line', 'whatsapp'], 'LINE and WhatsApp: more qualified replies and purchases from targeted and template messages'),
    'email-marketing': (['email'], 'Email to an opted-in list: more buyer replies, clicks and purchases, fewer unsubscribes'),
    'webinars': (['webinar'], 'Live demos and webinars: more sign-ups who attend, one-to-one demos booked and purchases among attendees'),
    'partners-and-deals': (['partnerships'], 'Partners, creators, referrals and sales follow-up: paying customers from creators whose audience wants the product, qualified referrals, paid purchases, trials that convert, stalled deals that reply, repeat purchases and company contracts'),
    'customer-base-growth': (['customer_base'], 'Existing members and customers: win back inactive members as paying members, new paying customers from member invites, and upgrades from free or one-time use to a paid or season plan'),
    'b2b-saas-growth': (['b2b_saas', 'b2b_search_ads'], 'B2B SaaS: launch deals on SaaS deal marketplaces, trials from people searching for a competitor alternative, from public requests and from integration marketplaces, more trials that become paying, sales calls from published business contacts, and paying customers through agencies and consultants'),
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

# Extra lines for one channel skill, placed right after "How to run a goal".
NOTES = {
    'reddit-marketing': ['If `read` (`read_page`) returns little text or a login page, ask the owner to paste the thread text. Never use the Reddit API or log in.', ''],
    'customer-base-growth': [
        'Messages to members go out under one approved template: hand the owner a `template` item (the text with {placeholders}, who it goes to in `audience_rule`, and a `daily_cap`) in a batch; once approved, every message built from it counts against the cap for that day. On the hosted engine the owner uploads the member list on their owner page and `next_recipients` gives the next people to message, never more than the cap a day; locally there is no list, so use the owner\'s own list that matches `audience_rule`. Message only people who joined or bought, and honour every opt-out.', ''],
    'b2b-saas-growth': [
        'Use only business contacts published on the company\'s own pages or the person\'s public profile; never guess or buy email addresses. Before outreach, the owner verifies the sending domain (SPF, DKIM and DMARC). Messages written for each person go out under one approved `template` item with a `daily_cap`; deal terms on a marketplace and any ad budget are approved by the owner first.', ''],
}

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


def how_to_run():
    return '\n'.join([
        '## How to run a goal', '',
        '1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.',
        '2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.',
        '3. If they are not connected, run the same engine from the `%s` skill: `python3 <%s skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.' % (LOOP, LOOP),
        '4. If neither can run, open the goal\'s playbook in `references/` and work it top to bottom under the rules below.',
        '5. For a month target (several channels at once toward a number of paying customers by a date), a goal here can be one lane, or a preset picks the lanes for the kind of business: see the `%s` skill, and pass `lane` with the goal id (`--lane` on the command line).' % LOOP, ''])


def channel_skill(name, channels, summary, library):
    goals = {g: v for g, v in library['goals'].items() if v['channel'] in channels}
    titles = '; '.join(v['title'] for v in goals.values())
    description = ('%s. Use when the user wants these results. %d goals, each judged by one number: %s. Each goal is a step-by-step playbook with the number that decides success; '
                   'if a round misses, change one thing and run another. Works with the %s skill or the Nuluno Engine tools.') % (summary, len(goals), titles, LOOP)
    if len(description) > 1024: description = description[:1020].rsplit(';', 1)[0] + '...'
    rows = ['| `%s` | %s | `%s` | %d h | [playbook](references/%s.md) |' % (g, v['title'], v['metric']['key'], hours(v), g) for g, v in goals.items()]
    body = ['# ' + summary.split(':')[0] + ': sales goals', '',
            '%s. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.' % summary, '',
            how_to_run(), *NOTES.get(name, []),
            '## Goals', '', '| Goal id | Goal | Metric | Wait before judging | Steps |', '|---|---|---|---|---|'] + rows + ['', '## Rules', ''] + ['- ' + r for r in RULES]
    folder_refs = {g: pages.page(g, v, library['skills']) for g, v in goals.items()}
    return frontmatter(name, description) + '\n' + '\n'.join(body) + '\n', folder_refs


def loop_skill(library):
    by_channel = {}
    for name, (channels, summary) in GROUPS.items():
        for g, v in library['goals'].items():
            if v['channel'] in channels: by_channel.setdefault(name, []).append(g)
    description = ('When the user wants to sell a product or get more clicks, sign-ups, customers or sales, and wants the work to keep going until a real number is reached: '
                   'picks one of %d sales goals, each judged by one number, works it one step at a time, records numbers before and after, and when the target is missed names one bottleneck '
                   'and changes one thing for the next round. For a month target (for example 100 paying customers in 30 days) it plans several channels at once from a preset for a new brand, '
                   'a brand with existing customers or B2B SaaS, and says honestly whether the plan can reach it and what would close the gap. '
                   'Saves progress so a new chat continues. Includes a dependency-free engine (Python 3) that checks each step.') % len(library['goals'])
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

Global options, before or after the command: `--data <folder>` keeps progress in another folder (default `~/.nuluno-engine/`), and `--product <url>` works on a product other than the one given to `start`. For example `python3 scripts/nuluno.py --data ./nuluno-data next`.

## Loop

1. `next` prints the current step: what to do, the checklist, the keys to hand back and lessons from earlier rounds.
2. Do the work. Then hand it in:
   `python3 scripts/nuluno.py submit <step_id> --output '{"key": "value", ...}'`
   Add `--link https://...` for a step that publishes something: the public URL of the post itself. The engine opens it, and refuses a profile page or a link that does not exist; a link the platform blocks robots from reading is accepted and recorded as `link_read_back: "blocked"`. If a person is needed (login, approval), use `--blocked "the one thing the owner must do"` and ask the owner for exactly that.
3. When the step asks for numbers, read them on the platform and record them:
   `python3 scripts/nuluno.py numbers --values '{"link_clicks": 41, "views": 1200}' --source "Threads insights, 23 Nov 10:00"`
   The first reading is the baseline. The result is judged after the observation window. If only the owner can see the numbers, hand the numbers step in as blocked, `python3 scripts/nuluno.py submit <step_id> --blocked "Read link clicks and views in Threads insights"`, and ask the owner for them.
4. If the target is missed, the engine asks for a diagnosis. Hand in `{"bottleneck": ..., "reason": ..., "one_change": ...}` with a bottleneck from its list. Each round names one bottleneck and one change. The engine shows every change already tried and refuses one worded the same as an earlier one.
5. Repeat until the engine says the goal is reached, or the owner says stop (`stop`).

Every command prints one JSON object. A refusal has an `error` field and exits with code 1 (2 for a mistake in the command line); read the error and its `next`, and carry on. `cli_names` maps any tool name in the text to its command. When unsure, run `next` again.

While a blocked step is open, `next` and `status` report `state: "waiting_on_owner"` with `tell_the_owner`: the one thing to ask the owner. Ask for exactly that; when they answer, finish the step and submit it (or record the numbers). A new chat sees the same state.

The engine's messages use its tool names. On the command line they are: `where_are_we` = `status`, `read_page` = `read`, `set_goal` = `goal`, `next_step` = `next`, `submit_step` = `submit` (its `links` = `--link`, its `status: "blocked"` with `needs` = `--blocked`), `record_numbers` = `numbers`, `tracking` = `tracking`, `stop_goal` = `stop`. Counting is hosted only: on the command line `tracking` says the engine does not count clicks or sales, so read them from the platform or the owner's site analytics. `inbox_address` and `inbox_latest` exist only on the hosted engine.

## Month target

For a number of paying customers by a date (for example 100 in 30 days), run several channels at once:

```bash
python3 scripts/nuluno.py target 100 --days 30
python3 scripts/nuluno.py plan G-TH-LINK-RATE G-RD-PURCHASES G-EM-PURCHASE
python3 scripts/nuluno.py month
```

`target` starts it; add `--price 39 --currency USD` and `--current-paid N` when known. `plan` takes 1 to 5 goal ids on different channels (pick 3 to 5 yourself; a plan may allow fewer), or a preset that picks them for the kind of business:

| Preset | When | Lanes it starts with | It asks the owner |
|---|---|---|---|
| `new_brand` | A new consumer product, no paying customers yet | creators (`G-CREATOR-COLLAB`), one organic channel, ads under an approved daily cap, community requests | price, free trial or preview, ad daily cap |
| `existing_base` | A brand with members or customers | win-back (`G-BASE-REACTIVATE`), member invites (`G-BASE-REFERRAL`), upgrades (`G-BASE-UPGRADE`), one channel for new people | members, paying users now, list size, where members can be messaged, how many more customers can be served a week, price |
| `b2b_self_serve` | Software with a free trial or free plan and a low price | launch deal (`G-B2B-LTD`), competitor alternatives (`G-B2B-ALTERNATIVES`), public requests (`G-B2B-INTENT`), trial conversion (`G-B2B-TRIAL-CONVERT`), integration marketplaces (`G-B2B-MARKETPLACE`) | price, trials a week, trial to paid if known, competitors if known |
| `b2b_sales` | Software sold through demos | outbound to published contacts (`G-B2B-OUTBOUND`), public requests, competitor alternatives, agency partners (`G-B2B-PARTNERS`), trial conversion if there is a trial | contract value, sales cycle in days, demos a week, whether there is a trial |

```bash
python3 scripts/nuluno.py target 100 --days 30 --price 9.99 --currency USD
python3 scripts/nuluno.py plan --preset new_brand --input free_trial=yes --input ad_daily_cap=20
```

Pass what you know as `--input key=value` (`inputs` in `plan_month`); run `plan` again with more inputs as the owner answers. You choose the channels yourself (`organic_channel`, `ads_channel`, `community_channel`, `acquisition_channel`) and may pass rates you measured. A goal a preset names that this library lacks is replaced by the closest one and listed in `skipped_lanes`.

Each lane runs one round a day. The engine works the target back into what is needed per day at each layer (paying customers, trials or demos, visits), says which rates are measured and which are assumed (2 of every 100 visitors paying, until real numbers exist), and splits the work across the lanes. Show the owner its `tell_the_owner`.

`feasibility` is the honest check: `verdict` is `on_track`, `stretch` or `not_with_current_inputs`, with the gap and `levers`, each saying what it adds and what it needs from the owner (more posts a day, a template with a higher daily cap, a higher ad cap, a list, a marketplace listing). When ads would cost more per customer than the price, the lever carries a `warning` and is never used to close the gap. Tell the owner the verdict as it is; never promise the target.

`asks` lists what only the owner can give: an answer to a preset question, a member list, a Stripe connection (hosted), a send volume, an ad budget, a verified sending domain or a link. Each ask says why and where the owner answers it. Ask for them together, once, and do what `agent_does_first` says before the owner is asked to approve.

`month` shows progress with its source, the pace, feasibility, asks, each lane and `next`: the lane to work on now. Work it with `next`, `submit` and `numbers` plus `--lane <goal id>`, then run `month` again. When the owner or a platform gives totals since the start, add `paid_customers` and `visits` to `numbers`.

A week of content is approved in one go: write the posts, replies and emails to a file as `{"items": [{"lane": ..., "kind": "post", "channel": ..., "text": ..., "when": ...}]}` and run `batch @week.json`. `batches` shows which items the owner approved. On a lane, `submit` of a step that publishes or sends is accepted only with `--approved-item <id>`: publish an approved item with exactly its text. Any other text goes into a new batch first.

For many messages written for each person (win-back, invites, outreach, replies), hand in one item of kind `template`: the text with up to 10 `{placeholders}` such as `{first_name}` or `{their_post}`, an `audience_rule` (who it goes to) and a `daily_cap` (1 to 2000). Once the owner approves it, it stays approved for its batch week: submit the step with `--approved-item <template id>` and every message you sent in the output, each as its own string; a message counts when only the placeholders differ (each filled with 1 to 200 characters), and the engine refuses a day that would go over the cap. On the hosted engine, `next_recipients` gives the next people from the list the owner uploaded; locally there is no list, so use the owner's own list that matches `audience_rule`.

For ads, `ad-budget 10 --currency USD --channel meta_ads` asks the owner for one daily cap. Spend nothing until it is approved; spend above the cap is flagged `over_budget`.

`approve` and `approve-budget` are for the owner, in their own terminal. Never run them yourself.

Tool names: `set_month_target` = `target`, `plan_month` = `plan` (its `preset` = `--preset`, `inputs` = `--input key=value`), `month_status` = `month`, `submit_batch` = `batch`, `batch_status` = `batches`, `request_ad_budget` = `ad-budget`; `lane` = `--lane`, `approved_item` = `--approved-item`. `next_recipients` is hosted only.

## Other ways to run the same engine

- As MCP tools in Claude Code: `claude mcp add --scope user nuluno-engine -- python3 <this folder>/scripts/server.py`
- Installed as the Claude Code plugin from https://github.com/business-wknd/nuluno-engine the tools are already there.
- Hosted, for Claude.ai: one connection address from https://engine.nuluno.com/?lang=en. The hosted engine also gives a tracked link that counts clicks and a sale counter that counts purchases; those counts replace what the agent reports for link clicks and sales. Sales are counted once per buyer per day when the buyer reaches the page shown after payment. Other numbers, such as views and replies, are still read from the platform.

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
