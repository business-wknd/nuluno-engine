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

The hosted service keeps what its [privacy page](https://engine.nuluno.com/privacy?lang=en) lists.
