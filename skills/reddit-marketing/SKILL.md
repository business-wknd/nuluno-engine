---
name: reddit-marketing
description: "Reddit: find people asking for what the product does, reply helpfully, and turn the conversations into inquiries and verified purchases. Use when the user wants these results. 5 measured goals: Reddit: find more posts from people with a matching need; Reddit: turn helpful replies into buyer conversations; Reddit: turn request replies into verified purchases in 48 hours; Reddit: get qualified inquiries from a true founder story; Reddit: turn buyer conversations into verified purchases in a week. Each goal is a step-by-step playbook with the number that decides success; if a round misses, change one thing and run another. Works with the sales-goal skill or the Nuluno Engine tools."
metadata:
  version: 0.2.0
  source: https://github.com/business-wknd/nuluno-engine
---

# Reddit: measured goals

Reddit: find people asking for what the product does, reply helpfully, and turn the conversations into inquiries and verified purchases. Each goal below is a playbook: ordered steps, what to hand back at each one, the number that decides success, and what to change when a round misses.

## How to run a goal

1. Pick the goal below that matches what the owner wants. Decide yourself and say it in one sentence; do not ask the owner to choose from a list.
2. If the Nuluno Engine tools are connected (`where_are_we`, `set_goal`, `next_step`), call `set_goal` with the goal id and follow `next_step`. The engine refuses unfinished steps, reads published links back, waits out the observation window and judges the round.
3. If they are not connected, run the same engine from the `sales-goal` skill: `python3 <sales-goal skill folder>/scripts/nuluno.py goal G-RD-QUALIFIED`, then `next`, `submit`, `numbers` as that skill explains. Progress is saved, so a new chat continues where the last one stopped.
4. If neither can run, open the goal's playbook in `references/` and work it top to bottom under the rules below.

## Goals

| Goal id | Goal | Metric | Wait before judging | Steps |
|---|---|---|---|---|
| `G-RD-QUALIFIED` | Reddit: find more posts from people with a matching need | `qualified_request_rate` | 48 h | [playbook](references/G-RD-QUALIFIED.md) |
| `G-RD-REPLIES` | Reddit: turn helpful replies into buyer conversations | `qualified_reply_rate` | 48 h | [playbook](references/G-RD-REPLIES.md) |
| `G-RD-PURCHASES` | Reddit: turn request replies into verified purchases in 48 hours | `external_purchases` | 48 h | [playbook](references/G-RD-PURCHASES.md) |
| `G-RD-STORY` | Reddit: get qualified inquiries from a true founder story | `qualified_inquiries` | 168 h | [playbook](references/G-RD-STORY.md) |
| `G066` | Reddit: turn buyer conversations into verified purchases in a week | `external_purchases` | 168 h | [playbook](references/G066.md) |

## Rules

- One step at a time. A step is finished only when every "Done when" line is true and every item under "Hand back" exists.
- Use only facts you read on the product's pages or got from the owner. An unknown price or result stays unknown; never invent numbers, quotes or testimonials.
- Decide what an expert marketer would decide (audience, angle, timing, sample size). Ask the owner only for what needs a person: logging in, approving text before it goes public, numbers only they can see.
- Never publish, send or spend without the owner's approval of the exact text and amount. Never ask for a password.
- Record the starting numbers before publishing. Read the result only after the waiting time. Numbers come from the platform, not from estimates.
- If the target is missed, name one bottleneck from the playbook's list, say what in the numbers shows it, and change exactly one thing for the next round. Never repeat a change that was already tried.
