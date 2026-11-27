---
name: partners-and-deals
description: "Partners, creators, referrals and sales follow-up: paying customers from creators whose audience wants the product, qualified referrals, paid purchases, trials that convert, stalled deals that reply, repeat purchases and company contracts. Use when the user wants these results. 7 goals, each judged by one number: Partners: raise the share of referrals who qualify; Referral partners: raise paid purchases per qualified referral; Trials and inquiries: raise the share that become paying; Stalled deals: raise the share of buyers who reply again; Existing customers: raise repeat purchases after refunds; Company sales: raise paid contracts from demos and pilots; Creators: get paying customers through creators whose audience wants the product. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.4.0
  source: https://github.com/business-wknd/nuluno-engine
---

# Partners, creators, referrals and sales follow-up: sales goals

Partners, creators, referrals and sales follow-up: paying customers from creators whose audience wants the product, qualified referrals, paid purchases, trials that convert, stalled deals that reply, repeat purchases and company contracts. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.
5. For a month target (several channels at once toward a number of paying customers by a date), a goal here can be one lane, or a preset picks the lanes for the kind of business: see the `sales-goal` skill, and pass `lane` with the goal id (`--lane` on the command line).

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G085` | Partners: raise the share of referrals who qualify | `qualified_referral_rate` | 168 h | [playbook](references/G085.md) |
| `G086` | Referral partners: raise paid purchases per qualified referral | `referral_purchase_rate` | 168 h | [playbook](references/G086.md) |
| `G087` | Trials and inquiries: raise the share that become paying | `trial_purchase_rate` | 168 h | [playbook](references/G087.md) |
| `G088` | Stalled deals: raise the share of buyers who reply again | `reactivation_rate` | 168 h | [playbook](references/G088.md) |
| `G089` | Existing customers: raise repeat purchases after refunds | `repeat_purchase_rate` | 168 h | [playbook](references/G089.md) |
| `G090` | Company sales: raise paid contracts from demos and pilots | `procurement_purchase_rate` | 168 h | [playbook](references/G090.md) |
| `G-CREATOR-COLLAB` | Creators: get paying customers through creators whose audience wants the product | `creator_paid_customers` | 168 h | [playbook](references/G-CREATOR-COLLAB.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
