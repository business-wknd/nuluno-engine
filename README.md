# Nuluno Engine

**Give your AI a sales goal: it works step by step, and if the numbers fall short it changes one thing and runs another round.**

[Start free](https://engine.nuluno.com/?lang=en) · [Use the Nuluno.com team](https://nuluno.com/?ref=github)

![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![MCP server](https://img.shields.io/badge/MCP-server-black)

You already have an AI assistant. Ask it to "help me sell my product" and you get one long answer, then nothing. Nuluno Engine is an MCP server that turns that into a loop: it hands the agent one step at a time from a sales playbook, keeps everything the agent delivers, waits for real numbers, and if the target is missed it opens another round that changes exactly one thing.

Your AI does the work. The engine keeps the goal, the steps, everything delivered and the numbers, and it needs no model key.

**Three ways to use it**

1. **Hosted (recommended):** [engine.nuluno.com](https://engine.nuluno.com/?lang=en), nothing to install, free.
2. **Run it yourself:** clone this repository and add one line to Claude Code or any MCP client that starts a local command. Clicks and sales are not counted locally; your agent reads them from the platform.
3. **Nuluno.com:** a built-in AI marketing team you can use in your browser, if you would rather not connect an AI or run code. [nuluno.com](https://nuluno.com/?ref=github)

## Start in one minute

**Hosted, nothing to install.** Go to [engine.nuluno.com](https://engine.nuluno.com/?lang=en), paste your product URL, add the connection address to Claude as a custom connector, and say: *"Use Nuluno Engine to sell my product."* Free.

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

## A real run, from one sentence

On 22 Nov 2026 we added the hosted connection address to Claude.ai as a custom connector and typed only *"用 Nuluno Engine 幫我賣這個產品"* ("Use Nuluno Engine to sell this product") for Notavue, a tool that turns YouTube piano covers into sheet music. Without further prompting, Claude:

1. read the product site and chose the goal "Threads: raise the link click rate", because piano learners in Taiwan are active there;
2. searched public forums for real complaints and picked one buyer group: adults who love a specific YouTube cover and cannot find sheet music for that version;
3. wrote three opening lines to compare, kept every claim to what the site supports, and put the round's tracked link in the post;
4. finished 7 of the 12 steps, then stopped and asked the owner which Threads account would post and who presses publish. It asked for no password and published nothing.

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
```

Hosted only: every step that writes copy hands the agent the round's tracked link.
Clicks on it from browsers (known robots and link previews are left out) and sales
recorded by the sale counter on your thank-you page are counted by the engine and
used in place of whatever the agent reports. When every number of a goal is counted
that way (12 of the 99 goals), the engine judges the round by itself when the
window ends.

## The rules the engine enforces

- **One step at a time, in order.** Out-of-order or repeated submissions are refused and the current step is returned.
- **Deliverables, not "done".** Each step names what must be handed back; missing pieces are rejected.
- **Published means a public URL.** A publishing step is not accepted without the https URL of what went live. The engine fetches it and records whether it could be read.
- **Numbers decide.** Only recorded numbers with a stated source can end a goal. No self-scoring. On the hosted service, clicks and sales counted by the engine replace whatever the agent reports for them.
- **One change per round.** After a miss the engine shows the agent how each number moved and what each possible bottleneck looks like in numbers. The agent names one bottleneck and one change, and the same change cannot be submitted twice.
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

[`playbooks/`](playbooks/) holds 99 goals across Threads, Instagram, X, TikTok, YouTube, Reddit, LinkedIn, Product Hunt, Meta and Google ads, email and webinars. The engine runs [`engine/library.json`](engine/library.json); `python3 engine/pages.py` writes the pages in `playbooks/` from it.

Every playbook is written step by step in plain English: 155 skills and 1,116 steps. Every step says what counts as done, and every skill says what to hand back and what to do when stuck. The Threads link-click playbook is running on a live product.

The most useful contribution is running one playbook on a real product and sending back what was unclear or wrong.

## How this is different

- **Agent frameworks** (LangGraph and others) give you durable graphs to build your own agent. Nuluno Engine is not a framework. It is one finished loop, selling, that plugs into the agent you already use over MCP. There is nothing to build.
- **Website optimizers** (Coframe and others) run experiments on copy on a site you own. Nuluno Engine works off-site too: posts, replies, launches, email. The experiment discipline is the same: a baseline, one change per round, numbers decide.
- **A prompt or a skills folder** tells an agent what to do once. The engine remembers across chats, refuses a step until everything it asks for is handed in, and ends a round only on recorded numbers.

## Open source and hosted

Everything needed to run the loop is here under Apache-2.0: the engine, the MCP server and every playbook. Fork it, run it locally, and edit `engine/library.json` to change a playbook (then run `engine/pages.py`).

| | Run it yourself (this repo) | Hosted free (recommended) | Hosted Pro |
|---|---|---|---|
| Guided loop, all 99 playbooks | yes | yes | yes |
| One connection address on every device | | yes | yes |
| Tracked links and sale counter; countable rounds judged by the engine | | yes | yes |
| AI inbox for verification mail | [receiving Worker only](access-inbox/); you build the rest | 10 messages a month | 500 messages a month |
| Products | one per `--product` | 1 | 5 |
| Price | free | free, no time limit | US$39/month, cancel any time |

Pro pays for the server that stays on to count clicks and receive mail; one Pro plan covers both Engine and Access. The code and the playbooks stay free.

## Security and data

- Run locally, progress lives only in `~/.nuluno-engine/` on your machine.
- The engine never asks for a password. Logins are the owner's job and are recorded as "waiting on the owner" with the one thing to do.
- Before anything goes public, the engine tells the agent to show the owner the exact text. The engine itself never posts, sends or spends.
- The hosted agent inbox keeps the sender, subject, codes and verification links for one hour, never the message body, and only your connection address can read it.

Report a security problem to support@nuluno.com; see [SECURITY.md](SECURITY.md).

If the engine helped you, a star helps others find it.

[License](LICENSE) · [Report a playbook](https://github.com/business-wknd/nuluno-engine/issues/new?template=playbook-report.md)
