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

## What the hosted service connects and stores for month target mode

Everything below is managed on the owner's private page (reached through the recovery link from sign-up; the AI's connection address cannot open it):

- **Stripe:** where it is switched on, the owner presses one Connect Stripe button and approves read-only access on Stripe's own screen. The service keeps the connected account id, never a key, and uses it only to count paying customers. Nobody types a key. A restricted read-only key (`rk_live_` or `rk_test_`) pasted under the earlier version keeps working until the owner removes it; it is stored encrypted with a server-side key, and only its last four characters are ever shown.
- **Daily auto-run:** where it is switched on, it is included in Pro and runs on Nuluno's own AI account, capped per account per day. The service does not ask for or keep the owner's own AI key; keys stored under the earlier version were deleted.
- **Member list:** a CSV the owner uploads (email, name, status, last purchase; up to 20,000 rows) is stored for that product only, is used only to hand the agent the next recipients of a template the owner approved, never more than its daily cap a day, and is deleted with the Delete button.

Approving a batch, a message template or an ad budget is possible only from that page, and in a month target lane the engine refuses a publishing or sending step that does not name an approved item. The local engine stores no keys and no lists.

## Approvals on the local engine

Locally, `nuluno.py approve` and `approve-budget` run only in a real terminal and only after the owner types yes; there is no flag that skips this. Because an AI agent that can edit local files could also edit the saved state in `~/.nuluno-engine/`, local approval is a convention, not a security boundary.

The hosted service keeps what its [privacy page](https://engine.nuluno.com/privacy?lang=en) lists.
