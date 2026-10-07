# Crypto track: exchange pump data and public Telegram channels

A separate dataset next to the stock pipeline (shouvik, 2026-10-06: crypto exchanges see pumps and rug pulls more
often, so more data). Nothing here feeds the stock labels (`label-v1`), the stock model (`model-v2`) or the stock
hold-out: crypto events have their own flag rules, their own label rule and live under `crypto/` on the `data`
branch. Paper trading only.

The rules in this file (`tg-v1`, `scan-v1`, `crypto-label-v1`) were written and committed on 2026-10-07 before
any crypto price outcome was computed or looked at. What had been seen by then is listed at the end. Change a rule
only with a new version written here first.

## Where the events come from

| Source | What | Period | Exchanges |
|---|---|---|---|
| `history` | Public lists of Telegram pump announcements: PumpSense (Mahrous et al., ICBC 2026, MIT, 2,246 hand-labelled announcements in 355k messages of 39 channels), La Morgia et al. 2020/2023 (MIT, 1,109), Ardia & Bluteau 2024 (1,160, Binance BTC pairs; cite the paper and DOI 10.5281/zenodo.12019080) | 2017 to 2023 | Binance and KuCoin get price bars (Binance's public bulk files, KuCoin's API); Yobit, Cryptopia, Bittrex, Hotbit and the rest are listed with `no_data`, since no free history exists for them |
| `telegram` | Messages of public Telegram channels read from their public web preview (`https://t.me/s/NAME`), hourly | live, from 2026-10-07 | the exchange the message names, else the first of MEXC, KuCoin, Gate, Binance that lists the coin against USDT |
| `scan` | Every USDT spot pair on MEXC, Gate, KuCoin and Binance, checked hourly for price spikes on unusual volume | live, from 2026-10-07 | those four |

The three history lists overlap. Duplicates (same exchange and coin, announcement times within 3 hours) are merged,
taking the time from Ardia & Bluteau (exact UTC seconds) first, then La Morgia (GMT minute), then PumpSense.
PumpSense's timestamps are the exporter's local time: matched against the other two lists they sit 2 hours ahead in
about three quarters of matches and 3 hours in the rest, with no clean daylight-saving pattern, so PumpSense-only
events are shifted by -2 hours and marked `time_source = pumpsense_minus_2h` (their time can be an hour off).

### Telegram: how it is read

The papers read Telegram in three ways: Mirtaheri et al. ran a Telethon crawler (Telegram's MTProto API, which needs
a phone-registered account and API keys) and snowballed from seed channels through `t.me` links; Ardia & Bluteau used
the same API on channels they had joined; Xu & Livshits and Nghiem et al. bought nothing from Telegram at all and took
PumpOlymp's list of pumps, which PumpOlymp's staff found by keyword search on Telegram aggregators (tgstat.com,
telegramcryptogroups.com) and cross-promotion. La Morgia et al. read channel histories by hand.

This project takes the one route that needs no account and joins nothing: a public channel's web preview at
`https://t.me/s/NAME`, which anyone can open in a browser. It shows the newest ~20 posts and pages back with
`?before=ID`. Private groups and invite links are never followed, and nothing is posted.

- **Channels**: seeded from the channels named in Nghiem et al. (appendix table), La Morgia's `groups.csv`, the
  channels most linked in PumpSense's messages, and channels found by a web search on 2026-10-07. New channels come
  from `t.me/NAME` links in collected posts (the papers' snowball), at most 10 new ones per run, added only if their
  preview is public and their title or recent posts match the pump keywords below. A channel whose preview is gone
  (or that hasn't posted for 180 days) is marked and checked again only weekly.
- **Classification `tg-v1`** (a rule, no model; `src/pumpdump/crypto/telegram.py`): each post's text is checked in
  this order:
  1. `announcement`: the post names a coin as the pump target. Either a phrase such as "the coin (we are pumping /
     we have picked ... / for today / to pump) is", "coin is", "coin:", "coin name", "pump coin", "pump alert",
     "today's coin" followed within 20 symbols by a ticker (also spelled out, "A P P C"), in a post that is not a
     results post, a teaser, a reminder or a cancellation and has no entry range or stop loss; or a post that is only
     a ticker (`#XYZ`, `$XYZ`, `XYZ`, `XYZ/BTC`) or only an exchange trade link (`.../trade/XYZ_USDT`) within 15
     minutes after a countdown post ("10 minutes left", "next post will be the coin") in the same channel.
  2. `call`: a ticker (`XYZ/USDT`, a trade link, `#XYZ` or `$XYZ`) together with buy words ("buy", "entry",
     "long") and a target ("target", "TP", "sell"): an ordinary signal, kept as its own kind because it is the same
     playbook at a slower pace.
  3. `other`: everything else (results, countdowns, ads, news), stored but not an event.
  A post that is itself a countdown ("24 hours left until our pump ... watch for the coin name") is never an
  announcement. The named exchange is the first exchange name or link in the post. If the post names one, the coin
  must be listed against USDT there (and that exchange must be one of the four read here); if it names none, the
  first of MEXC, KuCoin, Gate, Binance that lists it is used; otherwise the event is kept with exchange `unmatched` (or the named exchange, e.g. `yobit`, `solana`) and gets
  no bars.
- **tg-v1 check** against PumpSense's hand labels (2026-10-07; the rule was adjusted on 2017-2019 posts and then
  scored once on 2020-2023 posts it was not adjusted on): on 2020-2023 posts with text, 72% of the labelled
  announcements are found (617 of 860) and 99% of those get the right coin; 72% of the posts tg-v1 calls
  announcements are labelled ones. That precision is understated: PumpSense labels one post per pump, and many of
  the "false" hits are the same pump's second post or a real announcement it left unlabelled. 299 labelled
  announcements were images with no text, which no text rule can read.
- An event's `t0` is the post's own timestamp (Telegram's, to the second).

### `scan-v1`: market-wide spike flags

Each hourly run reads all tickers of each exchange in one call. Pairs whose 24-hour high is at least 1.2x their
24-hour low get their last 48 hourly bars fetched, and each completed hour `h` not checked before is flagged when
all of these hold:

- `high[h] >= 1.20 x close[h-1]` (a 20% spike inside the hour),
- `quote_volume[h] >= 5 x` the median hourly quote volume of the 24 hours before `h`,
- `quote_volume[h] >= 10,000 USDT` and that 24-hour median `>= 100 USDT` (dead pairs excluded),
- the base is not a stablecoin, a leveraged token (`3L`, `3S`, `5L`, `UP`, `DOWN`, `BULL`, `BEAR` suffixes) or a
  tokenised stock (`ON`/`X` suffix tickers Gate and Bitget list for US shares),
- the same pair was not flagged in the 72 hours before (one episode).

`t0` is the start of hour `h`. The rule uses only bars up to and including `h`; the flag is known only once `h`
has closed, which the label rule below accounts for with an entry price after the flag hour. Pairs that were
delisted before a run saw them are missed (the hourly runs keep that window small).

## What is stored per event

`crypto/events.csv` holds one row per event: id, source, kind (`announcement`, `call`, `spike`), exchange, base,
quote, `t0`, `collected_at`, the channel and post link (telegram), the spike's size and volume ratio (scan), the
list and time source (history). `crypto/bars/` holds each event's bars as fetched: 1-minute bars from 60 minutes
before `t0` to 4 hours after, and hourly bars from 48 hours before to 7 days after (exchange time in UTC
milliseconds, open, high, low, close, base volume, quote volume). Live events get their minute bars at the first
run 4 hours after `t0` (Gate only keeps about a week of minute bars) and their hourly bars at the first run 7 days
after; history events get both at once.

## `crypto-label-v1`

Prices in the event's quote currency. `p0` is the reference price before the event; `p_entry` is the first price a
follower could realistically get.

| Field | Definition |
|---|---|
| `p0` | announcement/call: close of the last 1-minute bar that ends at or before `t0`. spike: close of hour `h-1`. |
| `p_entry` | announcement/call: the price 2 minutes after `t0` (the last 1-minute close at or before the first minute boundary 2 minutes after `t0`; minutes without trades have no bar, so prices carry forward, as `p0` does). spike: close of hour `h` (the flag hour). |
| `peak_ret_1h` | highest 1-minute high from `t0` to `t0 + 60 min`, over `p0`, minus 1. Spikes use the flag hour's high. |
| `pump` | `peak_ret_1h >= 0.10` (the price moved at least 10% within the hour: the pump happened). |
| `pump_dump` | `peak_ret_1h >= 0.20` **and** within 24 hours after the peak the price trades at or below `p0 + 0.5 x (peak - p0)` (it gave back at least half the rise). The low after the peak is taken from 1-minute bars to `t0 + 4 h`, then hourly bars from the next full hour to the peak + 24 h. |
| `crash_7d` | any hourly close in the 7 days after `t0` at or below `0.6 x p0` (40% or more below the pre-event price): the "avoid" label, as for stocks. |
| `ret_entry_1h`, `ret_entry_24h`, `ret_entry_7d` | close 1 hour, 24 hours and 7 days after `t0` over `p_entry`, minus 1 (what a follower who bought at `p_entry` would hold). Hourly closes after the minute window. |
| `max_ret_entry_24h`, `min_ret_entry_24h` | highest high and lowest low in the 24 hours after the entry bar, over `p_entry`, minus 1. |
| `minutes_to_peak` | minutes from `t0` to the 1-minute bar with the peak in the first hour. |

An event is `settled` once its 7-day bars are in; `partial` if the pair stopped trading or the exchange stopped
returning bars before that (the fields that can be computed are filled, `delisted = 1` if the pair is gone from the
exchange's tickers); `no_data` if no bars around `t0` exist; `pending` until then. Fees and slippage are not in
these fields: they are returns of prices, and the trading research adds costs on top.

Why these numbers: the Telegram pumps in the papers peak within seconds to minutes and give back most of the move
within the hour (Xu & Livshits; La Morgia et al.), so the stock rule's 5-day and 10-day windows become 1 hour and
24 hours here. 10% is the smallest move any of the papers calls a pump; 20% plus a half give-back separates a
pump-and-dump from a coin that rerated and stayed. `p_entry` two minutes after the post (and the close of the spike
hour) keeps the follower honest: nobody buys at `p0`.

## Running and stopping

`crypto.yml` runs hourly (started by `scripts/pace.sh` at the first pacer at least 55 minutes after the last crypto
run; cron at minute 17 as backup) and does, within a 20-minute budget: Telegram, scan, then bars and outcomes of
events whose time has come; `crypto/outcomes.csv` is rebuilt every run. A `history` run (manual dispatch,
resumable) builds the history events and their bars.

It stops collecting when the stock collection stops (Reddit collector finished, ~Feb to Apr 2027) or 180 days after
its first live run, whichever is first; it keeps fetching bars until every event is settled, then turns itself off.

## What had been seen before these rules were written

- The three history lists themselves (coins, channels, exchanges, announcement times, counts by year) and a time
  check of PumpSense against the other two lists. No price data of any event. (Later the same day, before any outcome was computed: `p_entry`'s wording was made exact for minutes without trades, and tg-v1's wording below was updated to the rule as built and checked.)
- A reachability probe (2026-10-07, run 37619315867): which exchange APIs answer from GitHub's runners, and the last
  ~20 posts of 40 seed channels' previews (some channels still post pumps and calls in 2026: `mexcpumpcoins`,
  `kucoin_pump_group`, `mega_pump_group`, `cryptoprofitcoach`). One results post claimed "$LIGHT went up 10% after our
  signal"; no price of it was looked up.
