---
name: sales-goal
description: "When the user wants to sell a product or get more clicks, sign-ups, customers or sales, and wants the work to keep going until a real number is reached: picks one of 99 measured sales goals, works it one step at a time, records numbers before and after, and when the target is missed names one bottleneck and changes one thing for the next round. Saves progress so a new chat continues. Includes a dependency-free engine (Python 3) that checks each step."
metadata:
  version: 0.2.0
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
