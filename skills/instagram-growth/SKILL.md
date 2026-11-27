---
name: instagram-growth
description: "Instagram: more followers, profile visits, bio link clicks, saves, Reels watched to the end and qualified inquiries. Use when the user wants these results. 6 goals, each judged by one number: Instagram: grow net new followers; Instagram: turn more post reach into profile visits; Instagram: raise bio link clicks per profile visit; Instagram: get more saves per account reached; Instagram: get more qualified product inquiries; Instagram: get more Reels viewers to watch to the end. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.4.0
  source: https://github.com/business-wknd/nuluno-engine
---

# Instagram: sales goals

Instagram: more followers, profile visits, bio link clicks, saves, Reels watched to the end and qualified inquiries. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.
5. For a month target (several channels at once toward a number of paying customers by a date), a goal here can be one lane, or a preset picks the lanes for the kind of business: see the `sales-goal` skill, and pass `lane` with the goal id (`--lane` on the command line).

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-IG-FOLLOWERS` | Instagram: grow net new followers | `net_followers` | 48 h | [playbook](references/G-IG-FOLLOWERS.md) |
| `G-IG-PROFILE-RATE` | Instagram: turn more post reach into profile visits | `profile_visit_rate` | 48 h | [playbook](references/G-IG-PROFILE-RATE.md) |
| `G-IG-LINK-RATE` | Instagram: raise bio link clicks per profile visit | `profile_link_rate` | 48 h | [playbook](references/G-IG-LINK-RATE.md) |
| `G-IG-SAVES` | Instagram: get more saves per account reached | `save_rate` | 48 h | [playbook](references/G-IG-SAVES.md) |
| `G-IG-INQUIRIES` | Instagram: get more qualified product inquiries | `qualified_inquiries` | 48 h | [playbook](references/G-IG-INQUIRIES.md) |
| `G-IG-REELS` | Instagram: get more Reels viewers to watch to the end | `completion_rate` | 48 h | [playbook](references/G-IG-REELS.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
