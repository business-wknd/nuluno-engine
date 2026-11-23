---
name: sales-goal
description: "When the user wants to sell a product or get more clicks, sign-ups, customers or sales, and wants the work to keep going until a real number is reached: picks one of 99 sales goals, each judged by one number, works it one step at a time, records numbers before and after, and when the target is missed names one bottleneck and changes one thing for the next round. Saves progress so a new chat continues. Includes a dependency-free engine (Python 3) that checks each step."
metadata:
  version: 0.3.0
  source: https://github.com/business-wknd/nuluno-engine
---

# Sales goal

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

`target` starts it; add `--price 39 --currency USD` and `--current-paid N` when known. `plan` takes 1 to 5 goal ids on different channels (pick 3 to 5 yourself; a plan may allow fewer). Each becomes a lane with one round a day. The engine works the target back into paying customers and visits per day, says which rates are measured and which are assumed (2 of every 100 visitors paying, until real numbers exist), and splits the daily visits across the lanes. Show the owner its `tell_the_owner`.

`month` shows progress with its source, the pace, each lane and `next`: the lane to work on now. Work it with `next`, `submit` and `numbers` plus `--lane <goal id>`, then run `month` again. When the owner or a platform gives totals since the start, add `paid_customers` and `visits` to `numbers`.

A week of content is approved in one go: write the posts, replies and emails to a file as `{"items": [{"lane": ..., "kind": "post", "channel": ..., "text": ..., "when": ...}]}` and run `batch @week.json`. `batches` shows which items the owner approved. On a lane, `submit` of a step that publishes or sends is accepted only with `--approved-item <id>`: publish an approved item with exactly its text. Any other text goes into a new batch first. For ads, `ad-budget 10 --currency USD --channel meta_ads` asks the owner for one daily cap. Spend nothing until it is approved; spend above the cap is flagged `over_budget`.

`approve` and `approve-budget` are for the owner, in their own terminal. Never run them yourself.

Tool names: `set_month_target` = `target`, `plan_month` = `plan`, `month_status` = `month`, `submit_batch` = `batch`, `batch_status` = `batches`, `request_ad_budget` = `ad-budget`; `lane` = `--lane`, `approved_item` = `--approved-item`.

## Other ways to run the same engine

- As MCP tools in Claude Code: `claude mcp add --scope user nuluno-engine -- python3 <this folder>/scripts/server.py`
- Installed as the Claude Code plugin from https://github.com/business-wknd/nuluno-engine the tools are already there.
- Hosted, for Claude.ai: one connection address from https://engine.nuluno.com/?lang=en. The hosted engine also gives a tracked link that counts clicks and a sale counter that counts purchases; those counts replace what the agent reports for link clicks and sales. Sales are counted once per buyer per day when the buyer reaches the page shown after payment. Other numbers, such as views and replies, are still read from the platform.

## Goals by skill

| Skill | Goals |
|---|---|
| `instagram-growth` | `G-IG-FOLLOWERS`, `G-IG-PROFILE-RATE`, `G-IG-LINK-RATE`, `G-IG-SAVES`, `G-IG-INQUIRIES`, `G-IG-REELS` |
| `tiktok-growth` | `G-TT-FOLLOWERS`, `G-TT-COMPLETION`, `G-TT-PROFILE-RATE`, `G-TT-LINK-RATE`, `G-TT-SITE-PURCHASE` |
| `threads-growth` | `G-TH-FOLLOWERS`, `G-TH-REPLIES`, `G-TH-LINK-RATE`, `G-TH-INTENT` |
| `x-growth` | `G-X-FOLLOWERS`, `G-X-PROFILE-RATE`, `G-X-LINK-RATE`, `G-X-CONVERSATIONS` |
| `youtube-growth` | `G-YT-SUBSCRIBERS`, `G-YT-COMPLETION`, `G-YT-SITE-CLICKS`, `G-YT-REQUESTS` |
| `linkedin-growth` | `G-LI-FOLLOWERS`, `G-LI-ROLES`, `G-LI-PUBLIC-EMAILS`, `G-LI-INQUIRIES`, `G-LI-MEETINGS` |
| `reddit-marketing` | `G-RD-QUALIFIED`, `G-RD-REPLIES`, `G-RD-PURCHASES`, `G-RD-STORY`, `G066` |
| `pinterest-growth` | `G069`, `G070` |
| `facebook-groups` | `G071`, `G072` |
| `discord-community` | `G073`, `G074`, `G099` |
| `messaging-apps` | `G075`, `G076`, `G077`, `G078` |
| `email-marketing` | `G-EM-REPLY`, `G-EM-CLICK`, `G-EM-PURCHASE`, `G-EM-UNSUBSCRIBE` |
| `webinars` | `G-WB-ATTEND`, `G-WB-MEETINGS`, `G-WB-PURCHASE` |
| `partners-and-deals` | `G085`, `G086`, `G087`, `G088`, `G089`, `G090` |
| `product-hunt-launch` | `G-PH-MAKERS`, `G-PH-PUBLIC-EMAILS`, `G-PH-LAUNCH-TRAFFIC`, `G-PH-LAUNCH-PURCHASE` |
| `search-visibility` | `G067`, `G068` |
| `review-directories` | `G083`, `G084` |
| `press-coverage` | `G091`, `G092` |
| `audience-research` | `G-AUD-SEGMENT`, `G-AUD-DESIRE`, `G-AUD-ANGLE`, `G-AUD-PURCHASE`, `G065` |
| `app-store-listing` | `G079`, `G080` |
| `meta-ads` | `G-META-CPA`, `G-META-PURCHASE-CPA`, `G-META-CPL`, `G-META-LINK-CTR`, `G-META-LANDING-RATE`, `G-META-ROAS`, `G-META-NET-CONTRIBUTION` |
| `search-ads` | `G-GA-CPA`, `G-GA-QUERY-QUALITY`, `G-GA-PURCHASE-RATE`, `G-GA-WASTE`, `G081`, `G082`, `G093`, `G094` |
| `social-ads` | `G-TA-CPA`, `G-TA-QUALIFIED-CPL`, `G-TA-LINK-CTR`, `G-LA-CPA`, `G-LA-QUALIFIED-CPL`, `G-LA-LINK-CTR`, `G095`, `G096`, `G097`, `G098` |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
