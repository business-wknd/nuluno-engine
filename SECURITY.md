# Security

Report a vulnerability to **support@nuluno.com** with the steps to reproduce it. Please keep credentials and customer content out of the report.

What this repository stores: when you run `engine/server.py`, progress is kept in one JSON file per product under `~/.nuluno-engine/` (or the folder you pass with `--data`). Nothing is sent anywhere except the public pages your agent asks `read_page` to fetch and the public URL handed in on a publishing step, which the engine reads back once.

The hosted service at engine.nuluno.com keeps what its [privacy page](https://engine.nuluno.com/privacy?lang=en) lists.
