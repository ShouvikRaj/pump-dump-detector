# Crypto track

Exchange pump events and public Telegram channels, kept apart from the stock pipeline. Rules, sources and
field definitions: docs/crypto.md on main (tg-v1, scan-v1, crypto-label-v1).

Live since 2026-10-07T12:32:05Z.

| Events | Count |
|---|---|
| history / announcement | 2471 |
| scan / spike | 109 |
| telegram / announcement | 151 |
| telegram / call | 1960 |

| Outcome status | Count |
|---|---|
| no_data | 475 |
| not_covered | 1562 |
| partial | 5 |
| pending | 115 |
| settled | 2534 |

- `events.csv`: one row per event; `outcomes.csv`: crypto-label-v1 per event, rebuilt every run.
- `bars/<source>/<event_id>.json.gz`: the event's 1-minute and hourly bars [open time ms, open, high, low,
  close, base volume, quote volume] and when they were fetched.
- `telegram/channels.csv`, `telegram/posts/`: every public post read, with its tg-v1 class.
