# Nuluno Engine

**Give your AI a sales goal: it works step by step, and if the numbers fall short it changes one thing and runs another round.**

[Start free](https://engine.nuluno.com/?lang=en) · [Playbooks](playbooks/) · [Changelog](CHANGELOG.md)

[![CI](https://github.com/business-wknd/nuluno-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/business-wknd/nuluno-engine/actions/workflows/ci.yml) ![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![Agent Skills](https://img.shields.io/badge/Agent_Skills-24-black)

I kept asking Claude to help sell my side projects and getting one good answer followed by nothing. The missing piece wasn't intelligence. It was something outside the model that remembers the goal, refuses half-finished work and holds the agent to a number. This is that piece: 99 sales playbooks built from 155 reusable steps with 1,116 checklist items, packed as 24 Agent Skills, plus a small engine your AI works through. Your AI does the work; the engine needs no model key.

## Install

**Claude Code** (skills and engine tools together):

```sh
claude plugin marketplace add business-wknd/nuluno-engine
claude plugin install nuluno-engine@nuluno-engine
```

**Any agent that reads Agent Skills** (Claude Code, Codex, Cursor and others):

```sh
npx skills add business-wknd/nuluno-engine
# or only the loop plus one channel
npx skills add business-wknd/nuluno-engine --skill sales-goal threads-growth
```

Running `npx skills` from inside an agent session? Add `-a claude-code` (or your agent's name) so it installs where that agent looks.

Then say: *"Sell https://your-product.com with Nuluno Engine."* The `sales-goal` skill runs the engine from the command line (`python3 scripts/nuluno.py`, Python 3.9+, no dependencies), and progress is saved in `~/.nuluno-engine/`, so a new chat continues where the last one stopped.

**Any MCP client that starts a local command:**

```sh
claude mcp add --scope user nuluno-engine -- python3 /path/to/nuluno-engine/engine/server.py
```

The agent asks for the product URL the first time (`use_product`).

**Claude.ai, nothing to install:** get one connection address at [engine.nuluno.com](https://engine.nuluno.com/?lang=en) and add it as a custom connector. Free.

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
| [`reddit-marketing`](skills/reddit-marketing/) | 5 | Reddit: find people asking for what the product does, reply helpfully, and turn the conversations into inquiries and counted purchases |
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

## First real run (22 Nov 2026)

We added the hosted connection address to Claude.ai as a custom connector and typed only *"用 Nuluno Engine 幫我賣這個產品"* ("Use Nuluno Engine to sell this product") for Notavue, a tool that turns YouTube piano covers into sheet music. Without further prompting, Claude:

1. read the product site and chose the goal "Threads: raise the link click rate from a post to your site", because piano learners in Taiwan are active there;
2. searched the web for real complaints and picked one buyer group: adults who love a specific YouTube cover and cannot find sheet music for that version;
3. wrote three opening lines to compare, kept every claim to what the site supports, and put the round's tracked link in the post;
4. finished 7 of the 12 steps, then stopped and asked the owner which Threads account would post and who presses publish. It asked for no password and published nothing.

Round 1 result: due 23 Nov 2026; it will be added here.

## What a round looks like

```text
where_are_we      -> no goal yet. Agent reads the product page and picks a goal.
set_goal          -> "Threads: raise the link click rate from a post to your site".
                     No target given, so the round has to beat the baseline by 20%.
next_step         -> step 1 of 12: read what the product actually offers.
submit_step       -> agent delivers facts with sources. Engine returns step 2.
...               -> audience, motive, angle, the post text.
record_numbers    -> baseline before publishing: 262 views, 9 link clicks.
submit_step       -> post is live; engine opens the post's public URL.
next_step         -> "waiting for results until 2026-11-23 08:15 UTC".
record_numbers    -> results. Target reached: done. Missed: pick one bottleneck,
                     change one thing, round 2 starts.
```

Hosted only: every step that writes copy hands the agent the round's tracked link. The engine counts link clicks on it (from browsers; known robots and link previews are left out) and sales from the sale counter, and uses its own counts instead of the agent's for those two numbers. Other numbers, such as views and replies, are read from the platform. Sales are counted once per buyer per day when the buyer reaches the page shown after payment. When every number of a goal is counted that way (12 of the 99 goals), the engine judges the round by itself when the window ends, as long as the round's tracked link was used in what was published and, for sales, the sale counter has recorded a sale; otherwise the agent records the missing number.

## The rules the engine enforces

- **One step at a time, in order.** Out-of-order or repeated submissions are refused and the current step is returned.
- **Every hand-back item.** A step with any hand-back item missing or empty is refused. The engine does not judge whether the work is good; the numbers at the end of the round do.
- **Published means the post itself.** A publishing step needs the public URL of the post itself. The engine opens it, and refuses a profile page or a link that does not exist. A link the platform blocks robots from reading is accepted and recorded as blocked.
- **Numbers decide.** A round ends only on numbers recorded with a source, never on the agent saying it went well. Locally, every number is read from the platform's own dashboard by the agent or owner. On the hosted service, link clicks and sales are counted by the engine itself; for 12 of the 99 goals that covers every number in the metric.
- **One change per round.** After a miss the engine shows how each number moved. Each round names one bottleneck and one change. The engine shows every change already tried and refuses one worded the same as an earlier one.
- **Stops for the owner.** Logins, approvals and numbers only the owner can see are recorded as "waiting on the owner" with the one thing to ask; every new chat sees it until the owner answers.

## What it will not do

The playbooks and the engine's instructions tell your AI never to do these:

- It does not sign in for you, accept terms or pass identity checks; the owner does.
- It never asks for a password or copies browser cookies.
- It does not scrape, bulk-download or guess email addresses; it reads one public page at a time.
- It never publishes, sends or spends without the owner approving the exact text and amount.

The engine itself never posts, sends or spends anything.

## Tools

| Tool | What it does |
|---|---|
| `where_are_we` | Product, goal, recent deliveries, numbers so far, next step. Call first in every chat |
| `read_page` | Bounded read of a public page with a content hash, for sourced facts |
| `set_goal` | Choose one of the playbooks and an optional numeric target |
| `next_step` | The current step: checklist, hand-back items, earlier work, lessons from past rounds |
| `submit_step` | Hand in the step, or mark it blocked on the owner |
| `record_numbers` | Baseline and results; the engine judges the round |
| `tracking` | Hosted: the round's tracked link, the sale counter, and what the engine has counted. Local: says it does not count |
| `stop_goal` | Stop; the record stays |
| `use_product` | Local, when the server was started without `--product`: set the product's public https URL once |
| `add_product` | Hosted: add another product to the account (Pro: up to 5) |
| `inbox_address` | Hosted: an email address for this account that receives verification mail |
| `inbox_latest` | Hosted: wait for and return the newest code or verification link sent to that address |

## Playbooks

[`playbooks/`](playbooks/) shows all 99 goals on one page each. The engine runs [`engine/library.json`](engine/library.json); `python3 engine/pages.py` writes `playbooks/` and `python3 engine/pack.py` writes `skills/` from it.

Every playbook starts with the same research steps (product facts, buyer quotes, buyer groups, motives, the strongest motive, provable benefits, an angle test) and then adds the steps for its channel and metric. The 155 reusable steps hold 1,116 distinct checklist items; that is not a total across playbooks. Every checklist item says what counts as done, and every step says what to hand back and what to do when stuck.

The Threads link-click playbook was tried on a live product (Notavue) on 22 November 2026: the agent finished 7 of its 12 steps, then stopped to ask which Threads account would post.

The most useful contribution is running one playbook on a real product and [reporting](https://github.com/business-wknd/nuluno-engine/issues/new?template=playbook-report.md) what was unclear or wrong.

## Tests

`python3 -m unittest discover tests` runs the engine tests in [`tests/`](tests/) with the standard library only; [CI](.github/workflows/ci.yml) runs them on every push and pull request.

## How this is different

- **Agent frameworks** (LangGraph and others) give you durable graphs to build your own agent. Nuluno Engine is not a framework. It is one finished loop, selling, that plugs into the agent you already use.
- **Website optimizers** (Coframe and others) run experiments on the pages of a site you own. Nuluno Engine works off-site too: posts, replies, launches, email.
- **A prompt or a skills folder** tells an agent what to do once. These skills come with an engine that remembers the goal and the numbers across chats.

## Open source and hosted

Everything needed to run the loop is here under Apache-2.0: the engine, the MCP server, the 24 skills and every playbook. Fork it, run it locally, and edit `engine/library.json` to change a playbook (then run `engine/pages.py` and `engine/pack.py`).

| | Run it yourself (this repo) | Hosted free | Hosted Pro |
|---|---|---|---|
| Guided loop, all 99 playbooks | yes | yes | yes |
| One connection address on every device | | yes | yes |
| Tracked links and sale counter | | yes | yes |
| AI inbox for verification mail | [receiving Worker only](access-inbox/); you build the rest | 10 messages a month | 500 messages a month |
| Products | any number, one at a time | 1 | 5 |
| Price | free | free, no time limit | US$39/month, cancel any time |

The hosted server (accounts, tracked links, sale counter, inbox) is not in this repo; `engine/core.py` decides when the hosted counts replace the numbers the agent records; the counting itself (robot filter, one sale per buyer per day) runs on the hosted server. Locally there is no server, so the engine cannot count clicks or sales itself and uses the numbers you record. Pro pays for the server that stays on to count clicks and receive mail; one Pro plan covers both Engine and Access.

## Security and data

- Run locally, progress lives only in `~/.nuluno-engine/` (or the folder you pass with `--data`) on your machine.
- The hosted connection address works like a password: anyone who has it can use your account and read its inbox. Don't paste it in public chats or repos. If it leaks, open the private recovery link you were given at sign-up and press "Issue a new address"; the old one stops working at once.
- The hosted inbox keeps the sender, subject, codes and verification links for one hour, never the message body, and only your connection address can read it.

Report a security problem to support@nuluno.com; see [SECURITY.md](SECURITY.md).

Not using an AI agent? [Nuluno.com](https://nuluno.com/?ref=github) is a marketing workspace with a built-in AI team that you use in your browser.

[License](LICENSE) · [Changelog](CHANGELOG.md) · [Report a playbook](https://github.com/business-wknd/nuluno-engine/issues/new?template=playbook-report.md)
