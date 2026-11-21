# Nuluno Engine

**Give your AI agent a sales goal it works on until the numbers say it is done.**

You already have Claude or ChatGPT. Ask it to "help me sell my product" and you get one long answer, then nothing. Nuluno Engine is an MCP server that turns that into a loop: it hands the agent one step at a time from a sales playbook, keeps everything the agent delivers, waits for real numbers, and if the target is missed it opens another round that changes exactly one thing.

The agent is the brain. The engine is the memory, the checklist and the referee. It needs no model key.

## Start in one minute

**Hosted, nothing to install.** Go to [engine.nuluno.com](https://engine.nuluno.com/?lang=en), paste your product URL, copy the connection address into Claude or ChatGPT as a custom connector, and say: *"Use Nuluno Engine to sell my product."* Free.

**Local, from this repo.** Python 3.9+, no dependencies:

```sh
git clone https://github.com/business-wknd/nuluno-engine.git
claude mcp add nuluno-engine -- python3 "$PWD/nuluno-engine/engine/server.py" --product https://your-product.com/
```

Any MCP client that can start a local command works the same way. Progress is saved in `~/.nuluno-engine/`, so a new chat continues where the last one stopped.

## What a round looks like

```text
where_are_we      -> no goal yet. Agent reads the product page and picks a goal.
set_goal          -> "Raise the link click rate of a Threads post", target 4%.
next_step         -> step 1 of 12: read what the product actually offers.
submit_step       -> agent delivers facts with sources. Engine returns step 2.
...               -> audience, motive, angle, the post text.
record_numbers    -> baseline before publishing: 262 views, 9 link clicks.
submit_step       -> post is live; engine reads the public URL back.
next_step         -> "waiting for results until 2026-11-23 08:15 UTC".
record_numbers    -> results. Target reached: done. Missed: pick one bottleneck,
                     change one thing, round 2 starts.
```

That example is a real run on our own product. We will publish its numbers here, good or bad.

## The rules the engine enforces

- **One step at a time, in order.** Out-of-order or repeated submissions are refused and the current step is returned.
- **Deliverables, not "done".** Each step names what must be handed back; missing pieces are rejected.
- **Published means published.** A publishing step needs the public URL, and the engine fetches it.
- **Numbers decide.** Only recorded numbers with a stated source can end a goal. No self-scoring.
- **One change per round.** After a miss the agent must name one bottleneck and one change, and cannot repeat a variant.
- **A person only when a person is needed.** Logins and approvals are recorded as "waiting on the owner" with the one thing to do; the step stays open.

## Tools

| Tool | What it does |
|---|---|
| `where_are_we` | Product, goal, everything delivered, numbers so far, next step. Call first in every chat |
| `read_page` | Bounded read of a public page with a content hash, for sourced facts |
| `set_goal` | Choose one of the playbooks and an optional numeric target |
| `next_step` | The current step: checklist, deliverables, earlier work, lessons from past rounds |
| `submit_step` | Hand in the step, or mark it blocked on the owner |
| `record_numbers` | Baseline and results; the engine judges the round |
| `stop_goal` | Stop; the record stays |

## Playbooks

[`playbooks/`](playbooks/) holds 99 goals across Threads, Instagram, X, TikTok, YouTube, Reddit, LinkedIn, Product Hunt, Meta and Google ads, email and webinars. They compile into [`engine/library.json`](engine/library.json).

Honest status:

- **In a live test: 1.** "Threads: raise the link click rate from a post to your site". Its eleven steps are rewritten in plain English and are being run on a real product right now.
- **Rewritten, not run yet: 2.** Two more Threads goals share those eleven steps.
- **Experimental: 96.** Generated drafts, in Traditional Chinese, structurally complete, never run for real. Expect rough edges.

Each playbook page says which it is.

The most useful contribution is running one playbook on a real product and sending back what was unclear or wrong.

## Open source and hosted

Everything needed to run the loop is here under Apache-2.0: the engine, the MCP server and every playbook.

The hosted service adds what needs a server that stays on: a connection address that works from any device, progress kept for you, and agent inboxes (an email address your agent can use to sign up somewhere and read back only the verification code). Paid plans, when they open, will cover the parts that cost us money to run. The code and playbooks stay free.

## Not done yet

- No customer sale has been produced by the engine yet. This is being tested in public.
- The engine does not post for the agent. The agent uses its own tools, or the owner presses publish.
- Numbers are entered by the agent or owner; automatic reading from platforms is not built.

[License](LICENSE) · Issues and playbook reports welcome
