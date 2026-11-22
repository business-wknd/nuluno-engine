# Nuluno Engine

**Give your AI a sales goal: it works step by step, and if the numbers fall short it changes one thing and runs another round.**

[Start free](https://engine.nuluno.com/?lang=en) · [Use the Nuluno.com team](https://nuluno.com/?ref=github)

![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![MCP server](https://img.shields.io/badge/MCP-server-black) ![Agent Skills](https://img.shields.io/badge/Agent_Skills-24-black)

Marketing skills tell an agent how to do a task once. Nuluno Engine adds what they leave out: a goal with a number, one step at a time, real numbers before and after, and another round with one change when the number falls short. It is 24 Agent Skills holding 99 sales playbooks with 1,116 steps, plus a small engine that checks every step. Your AI does the work; the engine needs no model key.

## Install

**Claude Code** (skills and engine tools together):

```sh
claude plugin marketplace add business-wknd/nuluno-engine
claude plugin install nuluno-engine@nuluno-engine
```

**Any agent that reads Agent Skills** (Claude Code, Codex, Cursor and others):

```sh
npx skills add business-wknd/nuluno-engine
```

Then say: *"Sell https://your-product.com with Nuluno Engine."* The `sales-goal` skill runs the engine from the command line (`python3 scripts/nuluno.py`, Python 3.9+, no dependencies), and progress is saved in `~/.nuluno-engine/`, so a new chat continues where the last one stopped.

**Claude.ai, nothing to install:** get one connection address at [engine.nuluno.com](https://engine.nuluno.com/?lang=en) and add it as a custom connector. The hosted engine also counts clicks and sales itself, so the agent's own report is not what decides a round. Free.

**Would rather not connect an AI at all:** [Nuluno.com](https://nuluno.com/?ref=github) is a built-in AI marketing team in your browser.

**Just want to see it? Five seconds, no agent, no network:**

```sh
git clone https://github.com/business-wknd/nuluno-engine.git
python3 nuluno-engine/engine/demo.py
```

A scripted agent works one goal and you watch the engine refuse a half-finished step, refuse skipping ahead, wait for numbers, call a miss, and open round 2 with one change.

## Skills

| Skill | Goals | What it moves |
|---|---|---|
| [`sales-goal`](skills/sales-goal/) | all 99 | The loop itself: pick a goal, work it step by step, record numbers, change one thing after a miss. Holds the engine (`scripts/nuluno.py`) |
| [`instagram-growth`](skills/instagram-growth/) | 6 | Instagram: more followers, profile visits, bio link clicks, saves, Reels watched to the end and qualified inquiries |
| [`tiktok-growth`](skills/tiktok-growth/) | 5 | TikTok: more followers, videos watched to the end, profile visits, website clicks and purchases |
| [`threads-growth`](skills/threads-growth/) | 4 | Threads: more followers, buyer conversations, useful replies to requests for help and clicks to the product |
| [`x-growth`](skills/x-growth/) | 4 | X (Twitter): more followers, profile visits, website clicks and buyer conversations |
| [`youtube-growth`](skills/youtube-growth/) | 4 | YouTube: more subscribers, videos watched to the end, description link clicks and real conversations |
| [`linkedin-growth`](skills/linkedin-growth/) | 5 | LinkedIn: more followers, leads in the right buyer role with verified public emails, inquiries and confirmed demos |
| [`reddit-marketing`](skills/reddit-marketing/) | 5 | Reddit: find people asking for what the product does, reply helpfully, and turn the conversations into inquiries and verified purchases |
| [`pinterest-growth`](skills/pinterest-growth/) | 2 | Pinterest: more outbound clicks from Pins and more purchases from those visitors |
| [`facebook-groups`](skills/facebook-groups/) | 2 | Facebook groups: more qualified replies to buyer requests and purchases from them |
| [`discord-community`](skills/discord-community/) | 3 | Discord: more qualified replies to help answers, purchases from help conversations and members who complete tasks |
| [`messaging-apps`](skills/messaging-apps/) | 4 | LINE and WhatsApp: more qualified replies and purchases from targeted and template messages |
| [`email-marketing`](skills/email-marketing/) | 4 | Email to an opted-in list: more buyer replies, clicks and purchases, fewer unsubscribes |
| [`webinars`](skills/webinars/) | 3 | Live demos and webinars: more sign-ups who attend, one-to-one demos booked and purchases among attendees |
| [`partners-and-deals`](skills/partners-and-deals/) | 6 | Partners, referrals and sales follow-up: qualified referrals, paid purchases, trials that convert, stalled deals that reply, repeat purchases and company contracts |
| [`product-hunt-launch`](skills/product-hunt-launch/) | 4 | Product Hunt: makers who fit the product with sourced public emails, then more tracked visits and purchases from the launch |
| [`search-visibility`](skills/search-visibility/) | 2 | Search and AI answers: more qualified visits from outside articles and AI answers that cite the brand correctly |
| [`review-directories`](skills/review-directories/) | 2 | Review directories: more qualified inquiries and purchases from listing visits |
| [`press-coverage`](skills/press-coverage/) | 2 | Press, podcasts and newsletters: more qualified inquiries and purchases from coverage |
| [`audience-research`](skills/audience-research/) | 5 | Finding who buys and why: the buyer group, outcome and sales angle that bring real inquiries and kept purchases, and useful replies to public requests |
| [`app-store-listing`](skills/app-store-listing/) | 2 | App Store and Google Play: more listing visitors who download or install |
| [`meta-ads`](skills/meta-ads/) | 7 | Meta ads (Facebook and Instagram): lower cost per conversion, purchase and lead, more link clicks and page loads, higher return on ad spend and net profit per customer |
| [`search-ads`](skills/search-ads/) | 8 | Google Ads, Microsoft Ads and Google free listings: lower cost per purchase, search terms with buying intent, less wasted spend, more listing clicks and purchases |
| [`social-ads`](skills/social-ads/) | 10 | TikTok, LinkedIn, Reddit and Pinterest ads: lower cost per conversion, lead and purchase, and higher click rates |

Each channel skill lists its goals with the metric and how long to wait before judging, and keeps every full playbook in `references/`. The skills are written from [`engine/library.json`](engine/library.json) by `python3 engine/pack.py`.

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

[`playbooks/`](playbooks/) shows all 99 goals on one page each. The engine runs [`engine/library.json`](engine/library.json); `python3 engine/pages.py` writes `playbooks/` and `python3 engine/pack.py` writes `skills/` from it.

To add the engine as MCP tools in any client that starts a local command: `claude mcp add --scope user nuluno-engine -- python3 /path/to/nuluno-engine/engine/server.py`. The agent is asked for the product URL the first time.

Every playbook is written step by step in plain English: 1,116 steps in 155 reusable step groups. Every step says what counts as done, and every step group says what to hand back and what to do when stuck. The Threads link-click playbook is running on a live product.

The most useful contribution is running one playbook on a real product and sending back what was unclear or wrong.

## How this is different

- **Agent frameworks** (LangGraph and others) give you durable graphs to build your own agent. Nuluno Engine is not a framework. It is one finished loop, selling, that plugs into the agent you already use over MCP. There is nothing to build.
- **Website optimizers** (Coframe and others) run experiments on copy on a site you own. Nuluno Engine works off-site too: posts, replies, launches, email. The experiment discipline is the same: a baseline, one change per round, numbers decide.
- **A prompt or a skills folder** tells an agent what to do once. These skills come with an engine that remembers across chats, refuses a step until everything it asks for is handed in, and ends a round only on recorded numbers.

## Open source and hosted

Everything needed to run the loop is here under Apache-2.0: the engine, the MCP server, the 24 skills and every playbook. Fork it, run it locally, and edit `engine/library.json` to change a playbook (then run `engine/pages.py` and `engine/pack.py`).

| | Run it yourself (this repo) | Hosted free (recommended) | Hosted Pro |
|---|---|---|---|
| Guided loop, all 99 playbooks | yes | yes | yes |
| One connection address on every device | | yes | yes |
| Tracked links and sale counter; countable rounds judged by the engine | | yes | yes |
| AI inbox for verification mail | [receiving Worker only](access-inbox/); you build the rest | 10 messages a month | 500 messages a month |
| Products | any number, one at a time | 1 | 5 |
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
