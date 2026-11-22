---
name: search-ads
description: "Google Ads, Microsoft Ads and Google free listings: lower cost per purchase, search terms with buying intent, less wasted spend, more listing clicks and purchases. Use when the user wants these results. 8 goals, each judged by one number: Google Ads: lower the cost per conversion; Google Ads: raise the share of search terms with buying intent; Google Ads: raise the purchase rate of ad visitors; Google Ads: cut spend on irrelevant searches; Google free listings: raise clicks per product impression; Google free listings: turn listing visits into purchases; Microsoft Ads: lower the cost per purchase; Microsoft Ads: raise the share of ad views that reach the site. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.2.0
  source: https://github.com/business-wknd/nuluno-engine
---

# Google Ads, Microsoft Ads and Google free listings: sales goals

Google Ads, Microsoft Ads and Google free listings: lower cost per purchase, search terms with buying intent, less wasted spend, more listing clicks and purchases. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-GA-CPA` | Google Ads: lower the cost per conversion | `conversion_cpa` | 168 h | [playbook](references/G-GA-CPA.md) |
| `G-GA-QUERY-QUALITY` | Google Ads: raise the share of search terms with buying intent | `query_fit_rate` | 168 h | [playbook](references/G-GA-QUERY-QUALITY.md) |
| `G-GA-PURCHASE-RATE` | Google Ads: raise the purchase rate of ad visitors | `site_purchase_rate` | 168 h | [playbook](references/G-GA-PURCHASE-RATE.md) |
| `G-GA-WASTE` | Google Ads: cut spend on irrelevant searches | `irrelevant_spend_rate` | 168 h | [playbook](references/G-GA-WASTE.md) |
| `G081` | Google free listings: raise clicks per product impression | `listing_click_rate` | 168 h | [playbook](references/G081.md) |
| `G082` | Google free listings: turn listing visits into purchases | `site_purchase_rate` | 168 h | [playbook](references/G082.md) |
| `G093` | Microsoft Ads: lower the cost per purchase | `purchase_cpa` | 168 h | [playbook](references/G093.md) |
| `G094` | Microsoft Ads: raise the share of ad views that reach the site | `qualified_click_rate` | 168 h | [playbook](references/G094.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
