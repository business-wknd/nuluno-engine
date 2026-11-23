# Security

Report a vulnerability to **support@nuluno.com** with the steps to reproduce it. Please keep credentials and customer content out of the report.

## What the local engine stores

When you run `engine/server.py` or `scripts/nuluno.py`, progress is kept in one JSON file per product under `~/.nuluno-engine/` (or the folder you pass with `--data`). Nothing is uploaded anywhere.

## What the local engine fetches

The engine makes outgoing requests in two cases only, and never sends your saved progress with them:

- `read_page` (`nuluno.py read`): one public https page the agent asks for, the product page by default.
- `submit_step` (`nuluno.py submit`) on a step that publishes something: the first link handed in, opened once to check it is a post that exists.

Every request is an https GET with the user agent `NulunoEngine/1.0`. The host must resolve only to public internet addresses, so pages on your own machine or private network cannot be read; each redirect is checked the same way (at most 3 redirects), and a read stops after about 400 KB or 20 seconds.

## The hosted connection address

The connection address from engine.nuluno.com works like a password: anyone who has it can use your account and read its inbox. Don't paste it in public chats, issues or repositories. If it leaks, open the private recovery link you were given at sign-up and press "Issue a new address"; the old address stops working at once.

## Keys stored by the hosted service

Month target mode on the hosted service can keep two keys the owner pastes on their private owner page (reached through the recovery link from sign-up; the AI's connection address cannot open it):

- **Stripe:** only a restricted key (`rk_live_` or `rk_test_`) with read access, used to count paying customers. Secret keys (`sk_`) are refused.
- **AI key (Pro auto-run):** the owner's own Anthropic API key, used only for the daily run, which stops at the daily spend cap the owner sets.

Both are stored encrypted with a server-side key, are never returned to any page, tool or AI (only the last four characters are shown), and are deleted with the Remove button on the owner page. On the hosted service, approving a batch or an ad budget is possible only from that page, and in a month target lane the engine refuses a publishing or sending step that does not name an approved item. The local engine stores no keys.

## Approvals on the local engine

Locally, `nuluno.py approve` and `approve-budget` run only in a real terminal and only after the owner types yes; there is no flag that skips this. Because an AI agent that can edit local files could also edit the saved state in `~/.nuluno-engine/`, local approval is a convention, not a security boundary.

The hosted service keeps what its [privacy page](https://engine.nuluno.com/privacy?lang=en) lists.
