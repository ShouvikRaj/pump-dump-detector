# Stage 4 design notes: labels

Stage 4 gives every Stage 2 snapshot (each candidate and its two matched controls) a label once enough trading
sessions have passed: **pump**, **real news** or **not pump**, plus a separate **crash** label for the "avoid"
signal. Candidates and controls go through exactly the same rule.

The rule below (version `label-v1`) was written down and committed on 2026-10-05, before any outcome rows were
opened (see "What had been seen" at the end). shouvik chose the two price labels the same day (21:30 UTC, "Both"):
his own example as the main label and the crash rule as a second one.

## Inputs

Everything comes from what Stage 2 and Stage 3 recorded; Stage 4 fetches nothing.

- `market/snapshots.csv` (Stage 2): `price_at_flag` (the base for every return), `cik`, and the last 8-K/6-K and
  the last dilution filing accepted **before** the flag (`last_current_report_at`, `last_current_report_items`,
  `last_dilution_at`).
- `track/outcomes.csv`, `track/daily.csv`, `track/filings.csv` (Stage 3): sessions after the flag in flag-time
  prices (session `k = 1` is the first regular session whose close comes after the flag), and SEC filings accepted
  **after** the flag.
- `candidates/episodes.csv` (Stage 1): `warmup`, copied onto each row (controls take their candidate's value).

## The rule (`label-v1`)

| Label | Definition |
|---|---|
| `pump_dump` | The highest high over sessions 1-5 is at least **50% above** the flag price (Stage 3's `ret_max_5 >= 0.50`), **and** the lowest low over the 10 sessions after that peak's session is at least **40% below** that peak (`drop_from_peak_10 <= -0.40`). Stage 3's columns, unchanged. |
| `crash_10` | Any close in sessions 1-10 is at or below **60% of the flag price** (40% or more below it). |
| `real_news` | The company filed material news with the SEC between **72 hours before the flag** and the **close of session 5**: an 8-K with item 2.02 (results), 2.01 (completed acquisition or disposal), 5.01 (change in control), 1.03 (bankruptcy), or 1.01 (material definitive agreement) unless that 8-K also lists item 2.03 or 3.02, or a dilution filing (S-1, S-3, F-1, F-3, 424B, Reg A and their variants: Stage 2's list) was accepted within 48 hours of it. |
| `label` | `real_news` if `real_news = 1`; otherwise `pump` if `pump_dump = 1`; otherwise `not_pump`. |

Why each part is the way it is:

- **pump_dump** is the example in the project brief, measured with highs and lows as Stage 3 already does. Daily
  bars can't say whether a session's low came before its high, so the drop is measured only over sessions after the
  peak's.
- **crash_10** uses closes, not lows: one stray print on an illiquid stock can set a daily low, while a close is
  where a holder actually stood at the end of a day. It counts stocks that fall right after the flag without rising
  first, which `pump_dump` misses and the brief's safer first test ("does the flag predict a crash within 10 days?")
  needs. It is reported next to `label`, not folded into it.
- **real_news** takes precedence over pump: a move with a legitimate catalyst (earnings, a buyout, a deal) is not
  called a pump-and-dump. Only filings that are costly to fake count. 8-Ks with only items 7.01 or 8.01 are press
  releases, which promoters use too, and 6-Ks (foreign issuers' reports) carry no item codes, so neither counts;
  both are listed in `news_filings` for a later text classifier. A material agreement that comes with a share sale
  is a financing, which is the dump's supply, not news. 8-K/A amendments don't count (they re-report old events).
  The 72 hours before the flag cover news released on a Friday that is talked about on Monday.

## When a label is final

Each part settles as soon as its window has closed, and its value never changes after that (unless Yahoo revises a
bar or the SEC re-dates a filing):

- `pump_dump`: after 5 sessions if the 5-session rise is under 50%; otherwise once the 10 sessions after the peak
  are in (15 sessions at most).
- `crash_10`: as soon as a close crosses the line; otherwise after 10 sessions.
- `real_news`: as soon as a qualifying 8-K appears; otherwise after 10 sessions. The window closes at session 5;
  the extra sessions give Stage 3's daily re-read of EDGAR time to catch filings a failed fetch missed. A company
  with no CIK (not an SEC filer, as most OTC Pink companies) has `real_news = 0` straight away.

So N, the wait before a label is final, is 10 trading sessions (two weeks) for most snapshots and 15 at most. Until
then `label` is `pending`. When tracking ends before the rule can be evaluated (Stage 2 had no price, Yahoo has no
data, or the stock stopped trading and fewer sessions than needed came in within Stage 3's 45 days), `label` is
`unknown` and `note` says why and after how many sessions; a stock that stopped trading after rising 50% says so,
since halts and delistings are common after a dump.

## Outputs (on the `data` branch)

| Path | What |
|---|---|
| `labels/labels.csv` | rebuilt every run: one row per snapshot with `label`, `pump_dump`, `crash_10`, `real_news`, the numbers behind them (`ret_max_5`, `peak_k_5`, `drop_from_peak_10`, `min_close_10`, `ret_min_close_10`), `news_filings`, `peak_maybe_before_flag`, `warmup`, `note`, `label_version` |
| `labels/README.md` | counts per archetype and role, and the rows labeled so far |

The archetypes are reported separately (`low_float_runner`, `otc_penny`, `other`), as the brief asks. The first
result to look at is the crash rate of candidates against their controls within each archetype. Candidates labeled
`not_pump` are the brief's second control group (chatter but no pump); the matched controls are the first (no
chatter). `python -m pumpdump build-db` loads the labels as the `labels` table.

## When it runs

The `label` workflow runs once a day, an hour after Stage 3's `track` run: `scripts/pace.sh` starts it at the first
pacer after 23:41 UTC, with a `41 23 * * *` cron as backup. It reads only the files above and writes only
`labels/`. Once collection has finished, every snapshot has been tracked and no label is pending, it turns itself
off.

## Changing the rule

Write the new rule and the reason here first, as `label-v2`, before looking at what it produces, and keep the
`label-v1` results next to it. Never tune the thresholds on the labels.

## Known gaps

- When the flag came during session 1 (`flag_in_session_1 = 1`), that session's high can predate the flag. A pump
  whose peak is session 1 is marked `peak_maybe_before_flag = 1`.
- News means SEC filings only. Non-SEC filers can never be `real_news`, and news released only on a newswire or
  under item 8.01 (FDA decisions, contract wins) isn't recognised: reading those texts is a job for the modeling
  stage's text classifier.
- Stage 2 kept only the last 8-K before the flag, so a qualifying 8-K in the 72 hours before is missed when a later
  non-qualifying one followed it before the flag.
- Daily bars only: a pump-and-dump that fully reverses within one session is not a pump here.
- No trading suspensions or SEC litigation releases yet (the brief lists both as label sources).

## What had been seen before the rule was written

One outcome: the card that asked shouvik to pick the rule mentioned that SDEV closed 42% below its flag price on its
first session, which is why the crash label was proposed. No other outcome rows (`track/outcomes.csv`,
`track/daily.csv`, `track/README.md`) were opened before this file was committed.
