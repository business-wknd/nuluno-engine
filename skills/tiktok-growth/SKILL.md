---
name: tiktok-growth
description: "TikTok: more followers, videos watched to the end, profile visits, website clicks and purchases. Use when the user wants these results. 5 goals, each judged by one number: TikTok: grow net followers with short videos; TikTok: raise the share of viewers who watch to the end; TikTok: turn more video views into profile visits; TikTok: raise website clicks from profile visits; TikTok: turn more site visits from TikTok into purchases. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.4.0
  source: https://github.com/business-wknd/nuluno-engine
---

# TikTok: sales goals

TikTok: more followers, videos watched to the end, profile visits, website clicks and purchases. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.
5. For a month target (several channels at once toward a number of paying customers by a date), a goal here can be one lane, or a preset picks the lanes for the kind of business: see the `sales-goal` skill, and pass `lane` with the goal id (`--lane` on the command line).

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-TT-FOLLOWERS` | TikTok: grow net followers with short videos | `net_followers` | 48 h | [playbook](references/G-TT-FOLLOWERS.md) |
| `G-TT-COMPLETION` | TikTok: raise the share of viewers who watch to the end | `completion_rate` | 48 h | [playbook](references/G-TT-COMPLETION.md) |
| `G-TT-PROFILE-RATE` | TikTok: turn more video views into profile visits | `profile_visit_rate` | 48 h | [playbook](references/G-TT-PROFILE-RATE.md) |
| `G-TT-LINK-RATE` | TikTok: raise website clicks from profile visits | `profile_link_rate` | 48 h | [playbook](references/G-TT-LINK-RATE.md) |
| `G-TT-SITE-PURCHASE` | TikTok: turn more site visits from TikTok into purchases | `site_purchase_rate` | 48 h | [playbook](references/G-TT-SITE-PURCHASE.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
