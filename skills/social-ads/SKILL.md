---
name: social-ads
description: "TikTok, LinkedIn, Reddit and Pinterest ads: lower cost per conversion, lead and purchase, and higher click rates. Use when the user wants these results. 10 goals, each judged by one number: TikTok Ads: lower the cost per conversion; TikTok Ads: lower the cost per qualified lead; TikTok Ads: raise the link click rate of video ads; LinkedIn Ads: lower the cost per conversion; LinkedIn Ads: lower the cost per qualified lead; LinkedIn Ads: raise the link click rate; Reddit Ads: lower the cost per purchase; Reddit Ads: raise the share of ad views that reach the site; Pinterest Ads: lower the cost per purchase; Pinterest Ads: raise the qualified click rate. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.3.0
  source: https://github.com/business-wknd/nuluno-engine
---

# TikTok, LinkedIn, Reddit and Pinterest ads: sales goals

TikTok, LinkedIn, Reddit and Pinterest ads: lower cost per conversion, lead and purchase, and higher click rates. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.
5. For a month target (several channels at once toward a number of paying customers by a date), a goal here can be one lane: see the `sales-goal` skill, and pass `lane` with the goal id (`--lane` on the command line).

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-TA-CPA` | TikTok Ads: lower the cost per conversion | `conversion_cpa` | 168 h | [playbook](references/G-TA-CPA.md) |
| `G-TA-QUALIFIED-CPL` | TikTok Ads: lower the cost per qualified lead | `qualified_lead_cpl` | 168 h | [playbook](references/G-TA-QUALIFIED-CPL.md) |
| `G-TA-LINK-CTR` | TikTok Ads: raise the link click rate of video ads | `link_ctr` | 168 h | [playbook](references/G-TA-LINK-CTR.md) |
| `G-LA-CPA` | LinkedIn Ads: lower the cost per conversion | `conversion_cpa` | 168 h | [playbook](references/G-LA-CPA.md) |
| `G-LA-QUALIFIED-CPL` | LinkedIn Ads: lower the cost per qualified lead | `qualified_lead_cpl` | 168 h | [playbook](references/G-LA-QUALIFIED-CPL.md) |
| `G-LA-LINK-CTR` | LinkedIn Ads: raise the link click rate | `link_ctr` | 168 h | [playbook](references/G-LA-LINK-CTR.md) |
| `G095` | Reddit Ads: lower the cost per purchase | `purchase_cpa` | 168 h | [playbook](references/G095.md) |
| `G096` | Reddit Ads: raise the share of ad views that reach the site | `qualified_click_rate` | 168 h | [playbook](references/G096.md) |
| `G097` | Pinterest Ads: lower the cost per purchase | `purchase_cpa` | 168 h | [playbook](references/G097.md) |
| `G098` | Pinterest Ads: raise the qualified click rate | `qualified_click_rate` | 168 h | [playbook](references/G098.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
