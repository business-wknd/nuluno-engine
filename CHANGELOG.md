# Changelog

## 0.3.0 (2026-11-23)

**Month target mode**
- New tools: `set_month_target` (a number of paying customers, or revenue, in 7 to 90 days), `plan_month` (1 to 5 lanes, one goal each), `month_status`, `submit_batch`, `batch_status` and `request_ad_budget`. Command line: `target`, `plan`, `month`, `batch @file`, `batches`, `ad-budget`; `--lane` on status, read, goal, next, submit, numbers, tracking and stop, and `--approved-item` on submit.
- The plan works the target back into paying customers, sign-ups and visits per day and splits the visits across lanes: equally at first, from day 3 by each lane's clicks per round. Unmeasured rates are marked as assumptions (visit to paid 2% by default) until 100 visits and one paying customer are counted or recorded.
- Each lane is a normal goal stored on its own; every goal tool takes an optional `lane`. A lane's observation window is at most 24 hours. `month_status().next` names the lane with work to do that has waited longest.
- Approvals: a weekly batch of up to 50 items and one daily ad budget cap. The agent can only ask; the owner approves on the hosted owner page, or with `approve <batch_id> --all|--items ...` and `approve-budget`, which show the texts and ask for a typed "yes" in a real terminal (no flag skips it). On a lane, a step that publishes or sends is refused without an `approved_item`; it is accepted only if the published text matches the approved text, and the approval is written into the receipt. Outside a month target nothing changes. Ad spend recorded above the approved cap is accepted and flagged `over_budget`.
- Optional store hooks `lane_limit`, `paid_since` and `clicks_since` let a hosted store set the lane limit and count paying customers and visits itself.
- Without `lane` every tool behaves as in 0.2.0. 16 new tests.

## 0.2.0 (2026-11-23)

**Install as Agent Skills**
- 24 Agent Skills in `skills/`: 23 channel skills, each with its goals and full playbooks in `references/`, and `sales-goal`, the loop itself. Written from `engine/library.json` by `engine/pack.py`.
- Claude Code plugin and marketplace (`.claude-plugin/`) and a Codex plugin manifest (`.codex-plugin/`). Installs with `claude plugin install nuluno-engine@nuluno-engine` or `npx skills add business-wknd/nuluno-engine`.
- Command-line engine `engine/nuluno.py` (copied into `skills/sales-goal/scripts/`): `start`, `status`, `goals`, `read`, `goal`, `next`, `submit`, `numbers`, `tracking`, `stop`. `--data` and `--product` work before or after the command; errors print as JSON with exit code 1 (refusal) or 2 (command line); `cli_names` maps MCP tool names to commands. Same engine and saved progress as the MCP server; no MCP client needed.
- `use_product` tool: the local MCP server started without `--product` asks for the product URL once and remembers it.

**Engine**
- Publishing check: a publishing step needs the public URL of the post itself. The engine opens it, and refuses a profile, home or search page on a known platform, or a link that does not exist (no such host, connection refused, HTTP 404 or 410). A link the platform blocks robots from reading is accepted and recorded as `link_read_back: "blocked"`.
- Waiting on the owner: any step, including a numbers step, can be submitted as blocked with the one thing the owner must do. `next_step` and `where_are_we` then report `state: "waiting_on_owner"` with `tell_the_owner`, and every blocked response includes `next`.
- Tests in `tests/` (standard library `unittest`) and a GitHub Actions workflow that runs them on every push and pull request.

**Library**
- Fixes from the first real run (22 Nov 2026) and a review: purchase goals say "counted purchases", the angle step publishes one chosen angle and compares it with the baseline, examples no longer carry product claims, and Reddit playbooks were corrected.

## 0.1.x (2026-11-21 to 2026-11-22)

- 0.1.0: the guided sales loop over MCP (`engine/core.py`, `engine/server.py`) with 99 playbooks in `engine/library.json`, the five-second `engine/demo.py`, and the `tracking` tool for the hosted engine's tracked links and sale counter.
- Later 0.1 changes: steps handed out in order, every result waits out its observation window, engine counts replace typed numbers only when the counters were in place, repeated changes refused, clicks counted per post version (`?v=A`), the page generator `engine/pages.py`, and all 99 playbooks rewritten in plain English (155 reusable steps, 1,116 checklist items).
