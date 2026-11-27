<h1 align="center">Nuluno Engine</h1>

<p align="center"><b>Your AI agent writes a marketing plan, then forgets it.<br>Nuluno Engine keeps it on one sales number until the number moves.</b></p>

<p align="center">26 Agent Skills · 110 sales playbooks · an MCP server · Python 3.9+, no dependencies · Apache-2.0</p>

<p align="center">English · <a href="README.zh-TW.md">繁體中文</a> · <a href="https://engine.nuluno.com/?lang=en">Hosted (free)</a> · <a href="playbooks/">Playbooks</a> · <a href="CHANGELOG.md">Changelog</a></p>

<p align="center"><a href="https://github.com/business-wknd/nuluno-engine/actions/workflows/ci.yml"><img src="https://github.com/business-wknd/nuluno-engine/actions/workflows/ci.yml/badge.svg" alt="CI"></a> <img src="https://img.shields.io/badge/Agent_Skills-26-black" alt="26 Agent Skills"> <img src="https://img.shields.io/badge/playbooks-110-black" alt="110 playbooks"> <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0"></p>

```sh
npx skills add business-wknd/nuluno-engine
```

Then tell your agent: **"Sell https://your-product.com with Nuluno Engine."**

**Works with** any agent that reads Agent Skills (Codex, Cursor, Claude Code, Gemini CLI and others), any MCP client, and chat apps that accept a custom MCP connector, such as Claude and ChatGPT Business, through one free connection address from [engine.nuluno.com](https://engine.nuluno.com/?lang=en).

<p align="center"><img src="docs/loop.gif" width="760" alt="The engine refuses a half-finished step and a profile link, waits for numbers, calls a miss and opens round 2 with one change"></p>

| Your agent on its own | With Nuluno Engine |
|---|---|
| Writes a plan and calls it done | Works one step at a time; a step with any hand-back item missing is refused |
| "Posted!" | Needs the post's own public URL; a profile page or a dead link is refused |
| "It went well" | A round ends only on numbers recorded with a source |
| A new chat starts over | Progress is saved; the next chat continues at the same step |
| Changes five things at once | One named change per round; a change worded like an earlier one is refused |

The engine never posts, sends or spends. Your agent does the work, and you approve every publish, send and spend.

## Month target mode

Give the engine a number for the month, such as 100 paying customers in 30 days, and it works out what each channel needs every day, and whether that can work at all.

```sh
python3 engine/nuluno.py target 100 --days 30 --price 9.99 --currency USD
python3 engine/nuluno.py plan --preset new_brand --input free_trial=yes --input ad_daily_cap=20
python3 engine/nuluno.py month
```

**Three kinds of business, three presets.** `plan_month` takes your own 1 to 5 goal ids, or a preset that picks the lanes and asks only what an AI cannot know:

| Preset | For | Lanes it starts with | Asks the owner |
|---|---|---|---|
| `new_brand` | A new consumer product with no paying customers yet | creators whose audience wants the product, one organic channel, ads under a daily cap you approve, replies to public requests | price, free trial or preview, ad daily cap |
| `existing_base` | A brand with members or customers | win back inactive members, member invites, upgrades to a paid or season plan, one channel for new people | members, paying users now, list size, where you can message them, how many more you can serve a week, price |
| `b2b_self_serve` | Software with a free trial or free plan | launch deal on SaaS deal marketplaces, competitor-alternative pages and search ads, public requests, trial conversion, integration marketplaces | price, trials a week, trial to paid if known |
| `b2b_sales` | Software sold through demos | outreach to published business contacts, public requests, competitor alternatives, agency and consultant partners, trial conversion if there is a trial | contract value, sales cycle, demos a week, whether there is a trial |

- **An honest check.** Every plan returns `feasibility`: `on_track`, `stretch` or `not_with_current_inputs`, how many customers the lanes can bring by the end, the gap, and the levers that would close it (more posts a day, a higher daily message cap, a higher ad cap, a member list, a marketplace listing), each with what it adds and what it needs from you. An ad lever that would cost more per customer than the price is marked as losing money and never used to close the gap; for software sold through demos, customers count only after the sales cycle you give, and a lever to close deals sooner (a paid pilot) is offered when the cycle is long. Rates nobody has measured are listed as assumptions (2% of visits pay by default) until real visits and payments are counted.
- **Asks, not dead ends.** `asks` turns what the engine cannot see into one list for you: answers to the preset's questions, a member list, a send volume to approve, an ad budget, a verified sending domain, a link. Each says why and where you answer it.
- **Daily numbers.** The target becomes paying customers, trials or demos, and visits per day, split across 1 to 5 goals on different channels, each run as its own lane: equally at first, from day 3 by each lane's clicks. A lane's round waits at most 24 hours for its numbers. `month_status` shows paid customers so far, pace, feasibility, asks, each lane's step and quota, and `next`: the lane to work on now. Every goal tool takes `lane`.
- **Approve once.** `submit_batch` hands you a week of posts, replies, emails and ads; `request_ad_budget` asks for one daily ad cap. For messages written for each person, you approve one template with `{placeholders}`, who it goes to and a daily cap, instead of every message; the engine counts each message built from it and refuses a day over the cap. You approve, either on your private owner page when hosted or by running `nuluno.py approve <batch_id> --all` or `nuluno.py approve-budget` yourself in a real terminal, where you type yes; there is no flag that skips this. In a month target lane, the engine refuses a publishing or sending step without an `approved_item`, and the published text must match the approved text word for word (or the approved template, with only the placeholders filled). Spend above the approved cap is flagged `over_budget`.
- **Hosted.** Free: a month plan with 1 lane and weekly approval on your owner page, counted from the sale counter and the numbers you record; visits come from tracked links. Pro: 5 products and up to 5 lanes. The pricing table on [engine.nuluno.com](https://engine.nuluno.com/?lang=en) lists what else Pro includes while it is switched on there, such as paying customers read from Stripe through one read-only Connect Stripe button.

## Install

**Any agent that reads Agent Skills:**

```sh
npx skills add business-wknd/nuluno-engine
# or only the loop plus one channel
npx skills add business-wknd/nuluno-engine --skill sales-goal threads-growth
```

Running it from inside an agent session? Add `-a <your agent>` (for example `-a claude-code` or `-a codex`) so it installs where that agent looks. The `sales-goal` skill runs the engine from the command line (`python3 scripts/nuluno.py`), and progress is saved in `~/.nuluno-engine/`.

**Claude Code plugin** (skills and engine tools together):

```sh
claude plugin marketplace add business-wknd/nuluno-engine
claude plugin install nuluno-engine@nuluno-engine
```

**Hosted, one connection address** (free at [engine.nuluno.com](https://engine.nuluno.com/?lang=en); the hosted engine also counts link clicks and sales itself):

| AI | How to add it |
|---|---|
| Claude (web and desktop) | Settings, Connectors, Add, Add custom connector; paste the address |
| ChatGPT (Business, Enterprise, Edu) | chatgpt.com/plugins, +, Add custom MCP server; paste the address, No authentication |
| Claude Code | `claude mcp add --transport http nuluno-engine YOUR_ADDRESS` |
| Codex | `codex mcp add nuluno-engine --url YOUR_ADDRESS` |
| Gemini CLI | `gemini mcp add --transport http nuluno-engine YOUR_ADDRESS` |
| Cursor, VS Code, Perplexity and other MCP clients | Add a remote MCP server (Streamable HTTP) with the address; no sign-in |

**Local MCP server** for any client that starts a command: `python3 /path/to/nuluno-engine/engine/server.py` (for example `claude mcp add --scope user nuluno-engine -- python3 /path/to/nuluno-engine/engine/server.py`). The agent is asked for the product URL the first time.

**Would rather not connect an AI at all:** [Nuluno.com](https://nuluno.com/?ref=github) has a built-in AI marketing team in your browser.

<details><summary><b>For AI agents setting this up for a user</b></summary>

1. Install with `npx skills add business-wknd/nuluno-engine -a <your agent>`, or connect the user's hosted address as an MCP server.
2. Call `where_are_we` (or run `python3 scripts/nuluno.py status`) first in every chat.
3. Ask the user only for the product's public https URL. Never ask for a password.

</details>

## Skills

| Skill | Goals | What it moves |
|---|---|---|
| [`sales-goal`](skills/sales-goal/) | all 110 | The loop itself: pick a goal, work it step by step, record numbers, change one thing after a miss. Holds the engine (`scripts/nuluno.py`) |
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
| [`partners-and-deals`](skills/partners-and-deals/) | 7 | Partners, creators, referrals and sales follow-up: paying customers from creators whose audience wants the product, qualified referrals, paid purchases, trials that convert, stalled deals that reply, repeat purchases and company contracts |
| [`customer-base-growth`](skills/customer-base-growth/) | 3 | Existing members and customers: win back inactive members as paying members, new paying customers from member invites, and upgrades from free or one-time use to a paid or season plan |
| [`b2b-saas-growth`](skills/b2b-saas-growth/) | 7 | B2B SaaS: launch deals on SaaS deal marketplaces, trials from people searching for a competitor alternative, from public requests and from integration marketplaces, more trials that become paying, sales calls from published business contacts, and paying customers through agencies and consultants |
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

Hosted only: every step that writes copy hands the agent the round's tracked link. The engine counts link clicks on it (from browsers; known robots and link previews are left out) and sales from the sale counter, and uses its own counts instead of the agent's for those two numbers. Other numbers, such as views and replies, are read from the platform. Sales are counted once per buyer per day when the buyer reaches the page shown after payment. When every number of a goal is counted that way (13 of the 110 goals), the engine judges the round by itself when the window ends, as long as the round's tracked link was used in what was published and, for sales, the sale counter has recorded a sale; otherwise the agent records the missing number.

## The rules the engine enforces

- **One step at a time, in order.** Out-of-order or repeated submissions are refused and the current step is returned.
- **Every hand-back item.** A step with any hand-back item missing or empty is refused. The engine does not judge whether the work is good; the numbers at the end of the round do.
- **Published means the post itself.** A publishing step needs the public URL of the post itself. The engine opens it, and refuses a profile page or a link that does not exist. A link the platform blocks robots from reading is accepted and recorded as blocked.
- **Numbers decide.** A round ends only on numbers recorded with a source, never on the agent saying it went well. Locally, every number is read from the platform's own dashboard by the agent or owner. On the hosted service, link clicks and sales are counted by the engine itself; for 13 of the 110 goals that covers every number in the metric.
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
| `set_month_target` | Month target mode: a number of paying customers (or revenue) in 7 to 90 days |
| `plan_month` | Choose 1 to 5 lanes (goal ids) or a preset with what you know; returns what is needed per day, each lane's daily quota, feasibility (verdict, gap, levers) and asks for the owner |
| `month_status` | Paid customers and visits so far, pace, feasibility, asks, each lane's state, approvals waiting, and the lane to work on now |
| `submit_batch` | Hand the owner up to 50 items for the coming 7 days to approve in one go, including message templates with a daily cap |
| `batch_status` | Every batch and the state of each item |
| `request_ad_budget` | Ask the owner to approve one daily ad budget cap |
| `next_recipients` | Hosted: the next people to message from the list the owner uploaded, for an approved template, within its daily cap. Local: says there is no list |
| `use_product` | Local, when the server was started without `--product`: set the product's public https URL once |
| `add_product` | Hosted: add another product to the account (Pro: up to 5) |
| `inbox_address` | Hosted: an email address for this account that receives verification mail |
| `inbox_latest` | Hosted: wait for and return the newest code or verification link sent to that address |

## Playbooks

[`playbooks/`](playbooks/) shows all 110 goals on one page each. The engine runs [`engine/library.json`](engine/library.json); `python3 engine/pages.py` writes `playbooks/` and `python3 engine/pack.py` writes `skills/` from it.

Every playbook starts with the same research steps (product facts, buyer quotes, buyer groups, motives, the strongest motive, provable benefits, an angle test) and then adds the steps for its channel and metric. The 186 reusable steps hold 1,300 distinct checklist items; that is not a total across playbooks. Every checklist item says what counts as done, and every step says what to hand back and what to do when stuck.


The most useful contribution is running one playbook on a real product and [reporting](https://github.com/business-wknd/nuluno-engine/issues/new?template=playbook-report.md) what was unclear or wrong.

## Tests

`python3 engine/demo.py` replays the run in the animation above in five seconds, with no agent and no network. `python3 -m unittest discover tests` runs the engine tests in [`tests/`](tests/) with the standard library only; [CI](.github/workflows/ci.yml) runs them on every push and pull request.

## How this is different

- **Agent frameworks** (LangGraph and others) give you durable graphs to build your own agent. Nuluno Engine is not a framework. It is one finished loop, selling, that plugs into the agent you already use.
- **Website optimizers** (Coframe and others) run experiments on the pages of a site you own. Nuluno Engine works off-site too: posts, replies, launches, email.
- Neither works back from a sales target to what has to happen today, or tells you plainly that the plan falls short and what would close the gap. Month target mode does, for a new brand, a brand with existing customers and B2B SaaS.
- **A prompt or a skills folder** tells an agent what to do once. These skills come with an engine that remembers the goal and the numbers across chats.

## Open source and hosted

Everything needed to run the loop is here under Apache-2.0: the engine, the MCP server, the 26 skills and every playbook. Fork it, run it locally, and edit `engine/library.json` to change a playbook (then run `engine/pages.py` and `engine/pack.py`).

| | Run it yourself (this repo) | Hosted free | Hosted Pro |
|---|---|---|---|
| Guided loop, all 110 playbooks | yes | yes | yes |
| One connection address on every device | | yes | yes |
| Tracked links and sale counter | | yes | yes |
| Month target mode with presets and the feasibility check | yes, up to 5 channels | 1 channel | up to 5 channels at once |
| Approve a week of content at once | yes, in your terminal | yes, on your owner page | yes, on your owner page |
| AI inbox for verification mail | [receiving Worker only](access-inbox/); you build the rest | 10 messages a month | 500 messages a month |
| Products | any number, one at a time | 1 | 5 |
| Price | free | free, no time limit | US$39/month, cancel any time |

The hosted server (accounts, tracked links, sale counter, inbox) is not in this repo; `engine/core.py` decides when the hosted counts replace the numbers the agent records; the counting itself (robot filter, one sale per buyer per day) runs on the hosted server. Locally there is no server, so the engine cannot count clicks or sales itself and uses the numbers you record. Pro pays for the server that stays on to count clicks, receive mail and keep five products and their lanes running; one Pro plan covers both Engine and Access.

## Security and data

- Run locally, progress lives only in `~/.nuluno-engine/` (or the folder you pass with `--data`) on your machine.
- The hosted connection address works like a password: anyone who has it can use your account and read its inbox. Don't paste it in public chats or repos. If it leaks, open the private recovery link you were given at sign-up and press "Issue a new address"; the old one stops working at once.
- The hosted inbox keeps the sender, subject, codes and verification links for one hour, never the message body, and only your connection address can read it.

Report a security problem to support@nuluno.com; see [SECURITY.md](SECURITY.md).

Not using an AI agent? [Nuluno.com](https://nuluno.com/?ref=github) is a marketing workspace with a built-in AI team that you use in your browser.

[License](LICENSE) · [Changelog](CHANGELOG.md) · [Report a playbook](https://github.com/business-wknd/nuluno-engine/issues/new?template=playbook-report.md)
