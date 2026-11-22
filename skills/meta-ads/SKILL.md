---
name: meta-ads
description: "Meta ads (Facebook and Instagram): lower cost per conversion, purchase and lead, more link clicks and page loads, higher return on ad spend and net profit per customer. Use when the user wants these results. 7 measured goals: Meta Ads: lower the cost per conversion; Meta Ads: lower the cost per verified outside purchase; Meta Ads: lower the cost per qualified lead; Meta Ads: raise the link click rate; Meta Ads: get more ad clicks to load the website; Meta Ads: raise return on ad spend after refunds; Meta Ads: raise net profit per customer after all costs. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.2.0
  source: https://github.com/business-wknd/nuluno-engine
---

# Meta ads (Facebook and Instagram): measured goals

Meta ads (Facebook and Instagram): lower cost per conversion, purchase and lead, more link clicks and page loads, higher return on ad spend and net profit per customer. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine refuses unfinished steps, reads published links back, waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py goal G-META-CPA`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-META-CPA` | Meta Ads: lower the cost per conversion | `conversion_cpa` | 72 h | [playbook](references/G-META-CPA.md) |
| `G-META-PURCHASE-CPA` | Meta Ads: lower the cost per verified outside purchase | `purchase_cpa` | 72 h | [playbook](references/G-META-PURCHASE-CPA.md) |
| `G-META-CPL` | Meta Ads: lower the cost per qualified lead | `qualified_lead_cpl` | 72 h | [playbook](references/G-META-CPL.md) |
| `G-META-LINK-CTR` | Meta Ads: raise the link click rate | `link_ctr` | 72 h | [playbook](references/G-META-LINK-CTR.md) |
| `G-META-LANDING-RATE` | Meta Ads: get more ad clicks to load the website | `landing_rate` | 72 h | [playbook](references/G-META-LANDING-RATE.md) |
| `G-META-ROAS` | Meta Ads: raise return on ad spend after refunds | `refund_adjusted_roas` | 72 h | [playbook](references/G-META-ROAS.md) |
| `G-META-NET-CONTRIBUTION` | Meta Ads: raise net profit per customer after all costs | `net_per_customer` | 72 h | [playbook](references/G-META-NET-CONTRIBUTION.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
