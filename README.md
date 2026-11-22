# Nuluno Engine

**Give your AI agent a sales goal it works on until the numbers say it is done.**

You already have Claude or ChatGPT. Ask it to "help me sell my product" and you get one long answer, then nothing. Nuluno Engine is an MCP server that turns that into a loop: it hands the agent one step at a time from a sales playbook, keeps everything the agent delivers, waits for real numbers, and if the target is missed it opens another round that changes exactly one thing.

The agent is the brain. The engine is the memory, the checklist and the referee. It needs no model key.

## Start in one minute

**Hosted, nothing to install.** Go to [engine.nuluno.com](https://engine.nuluno.com/?lang=en), paste your product URL, copy the connection address into Claude or ChatGPT as a custom connector, and say: *"Use Nuluno Engine to sell my product."* Free.

**Local, from this repo.** Python 3.9+, no dependencies:

```sh
git clone https://github.com/business-wknd/nuluno-engine.git
claude mcp add --scope user nuluno-engine -- python3 "$PWD/nuluno-engine/engine/server.py" --product https://your-product.com/
```

Any MCP client that can start a local command works the same way. Progress is saved in `~/.nuluno-engine/`, so a new chat continues where the last one stopped.

**Just want to see it? Five seconds, no agent, no network:**

```sh
python3 nuluno-engine/engine/demo.py
```

A scripted agent works one goal and you watch the engine refuse a half-finished step, refuse skipping ahead, wait for numbers, call a miss, and open round 2 with one change.

## What a round looks like

```text
where_are_we      -> no goal yet. Agent reads the product page and picks a goal.
set_goal          -> "Threads: raise the link click rate". No target given, so the round
                     has to beat the baseline by 20%.
next_step         -> step 1 of 12: read what the product actually offers.
submit_step       -> agent delivers facts with sources. Engine returns step 2.
...               -> audience, motive, angle, the post text.
record_numbers    -> baseline before publishing: 262 views, 9 link clicks.
submit_step       -> post is live; engine reads the public URL back.
next_step         -> "waiting for results until 2026-11-23 08:15 UTC".
record_numbers    -> results. Target reached: done. Missed: pick one bottleneck,
                     change one thing, round 2 starts.

Hosted only: every step hands the agent a tracked link for the round. Human clicks
on it, and sales on your thank-you page once the sale counter is on it, are counted
by the engine and used in place of whatever the agent reports. When the whole metric
is countable that way (12 of the 99 goals), the engine judges the round by itself
when the window ends.
```

The baseline numbers are from a real run on our own product.

## The rules the engine enforces

- **One step at a time, in order.** Out-of-order or repeated submissions are refused and the current step is returned.
- **Deliverables, not "done".** Each step names what must be handed back; missing pieces are rejected.
- **Published means a public URL.** A publishing step is not accepted without the https URL of what went live. The engine fetches it and records whether it could be read.
- **Numbers decide.** Only recorded numbers with a stated source can end a goal. No self-scoring. On the hosted service, clicks and sales counted by the engine replace whatever the agent reports for them.
- **One change per round.** After a miss the agent must name one bottleneck and one change, and a change that was already tried is refused.
- **A person only when a person is needed.** Logins and approvals are recorded as "waiting on the owner" with the one thing to do; the step stays open.

## Tools

| Tool | What it does |
|---|---|
| `where_are_we` | Product, goal, recent deliveries, numbers so far, next step. Call first in every chat |
| `read_page` | Bounded read of a public page with a content hash, for sourced facts |
| `set_goal` | Choose one of the playbooks and an optional numeric target |
| `next_step` | The current step: checklist, deliverables, earlier work, lessons from past rounds |
| `submit_step` | Hand in the step, or mark it blocked on the owner |
| `record_numbers` | Baseline and results; the engine judges the round |
| `tracking` | Hosted: the round's tracked link, the sale counter, and what the engine has counted. Local: says it does not count |
| `stop_goal` | Stop; the record stays |

## Playbooks

[`playbooks/`](playbooks/) holds 99 goals across Threads, Instagram, X, TikTok, YouTube, Reddit, LinkedIn, Product Hunt, Meta and Google ads, email and webinars. The engine runs [`engine/library.json`](engine/library.json); the pages in `playbooks/` are generated from it for reading.

The research and messaging steps that the playbooks share are written in plain English. The Threads link-click playbook is in English end to end and is running on a live product. In the other channels, the channel-specific steps are in Traditional Chinese. Each page shows its language.

The most useful contribution is running one playbook on a real product and sending back what was unclear or wrong.

## How this is different

- **Agent frameworks** (LangGraph and others) give you durable graphs to build your own agent. Nuluno Engine is not a framework. It is one finished loop, selling, that plugs into the agent you already use over MCP. There is nothing to build.
- **Website optimizers** (Coframe and others) run experiments on copy on a site you own. Nuluno Engine works off-site too, where most small products actually find buyers: posts, replies, launches, email. The experiment discipline is the same: a baseline, one change per round, numbers decide.
- **A prompt or a skills folder** tells an agent what to do once. The engine remembers across chats, refuses work that is not finished, and ends a round only on recorded numbers.

## Open source and hosted

Everything needed to run the loop is here under Apache-2.0: the engine, the MCP server and every playbook. Fork it, run it locally, and edit `engine/library.json` to change a playbook.

The hosted service at [engine.nuluno.com](https://engine.nuluno.com/?lang=en) adds what needs a server that stays on:

| | Local (this repo) | Hosted, free |
|---|---|---|
| Guided loop, all 99 playbooks | yes | yes |
| One connection address that works from any device | | yes |
| Tracked links and sale counter; countable rounds judged by the engine | | yes |
| Agent inbox for verification mail | [mail Worker included](access-inbox/) | 10 messages a month |

The free plan has no time limit. The code and the playbooks stay free.

[License](LICENSE) · Issues and playbook reports welcome
