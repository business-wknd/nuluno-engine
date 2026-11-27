---
name: b2b-saas-growth
description: "B2B SaaS: launch deals on SaaS deal marketplaces, trials from people searching for a competitor alternative, from public requests and from integration marketplaces, more trials that become paying, sales calls from published business contacts, and paying customers through agencies and consultants. Use when the user wants these results. 7 goals, each judged by one number: B2B SaaS: sell a launch deal on SaaS deal marketplaces; B2B SaaS: win trials from people searching for a competitor alternative; B2B SaaS: turn public requests and complaints into trials; B2B SaaS: raise the share of trials that become paying; B2B SaaS: get sign-ups from integration marketplaces and software directories; B2B SaaS: book sales calls by emailing published business contacts; B2B SaaS: get paying customers through agencies and consultants. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.4.0
  source: https://github.com/business-wknd/nuluno-engine
---

# B2B SaaS: sales goals

B2B SaaS: launch deals on SaaS deal marketplaces, trials from people searching for a competitor alternative, from public requests and from integration marketplaces, more trials that become paying, sales calls from published business contacts, and paying customers through agencies and consultants. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine accepts only the current step, only with every hand-back item filled in. A publishing step needs the public URL of the post itself; the engine opens it, and refuses a profile page or a link that does not exist. It then waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py start <product url>`, then `... goal <your goal id>`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.
5. For a month target (several channels at once toward a number of paying customers by a date), a goal here can be one lane, or a preset picks the lanes for the kind of business: see the `sales-goal` skill, and pass `lane` with the goal id (`--lane` on the command line).

Use only business contacts published on the company's own pages or the person's public profile; never guess or buy email addresses. Before outreach, the owner verifies the sending domain (SPF, DKIM and DMARC). Messages written for each person go out under one approved `template` item with a `daily_cap`; deal terms on a marketplace and any ad budget are approved by the owner first.

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-B2B-LTD` | B2B SaaS: sell a launch deal on SaaS deal marketplaces | `deals_sold` | 168 h | [playbook](references/G-B2B-LTD.md) |
| `G-B2B-ALTERNATIVES` | B2B SaaS: win trials from people searching for a competitor alternative | `alternative_trial_signups` | 168 h | [playbook](references/G-B2B-ALTERNATIVES.md) |
| `G-B2B-INTENT` | B2B SaaS: turn public requests and complaints into trials | `intent_trial_signups` | 72 h | [playbook](references/G-B2B-INTENT.md) |
| `G-B2B-TRIAL-CONVERT` | B2B SaaS: raise the share of trials that become paying | `trial_to_paid_rate` | 168 h | [playbook](references/G-B2B-TRIAL-CONVERT.md) |
| `G-B2B-MARKETPLACE` | B2B SaaS: get sign-ups from integration marketplaces and software directories | `marketplace_signups` | 336 h | [playbook](references/G-B2B-MARKETPLACE.md) |
| `G-B2B-OUTBOUND` | B2B SaaS: book sales calls by emailing published business contacts | `outbound_meetings` | 168 h | [playbook](references/G-B2B-OUTBOUND.md) |
| `G-B2B-PARTNERS` | B2B SaaS: get paying customers through agencies and consultants | `partner_paid_customers` | 336 h | [playbook](references/G-B2B-PARTNERS.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
