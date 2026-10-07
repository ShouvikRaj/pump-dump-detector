# Stage 3 design notes

Stage 3 follows every Stage 2 snapshot (each candidate and its two matched controls) after the flag, so Stage 4 can
label what happened. It records only what happened **after** `as_of`, stamps every row with when it was collected,
and never feeds back into the flag-time features: these rows are outcomes, not inputs.

## When it runs and when it stops

The `track` workflow runs once a day after the US close: `scripts/pace.sh` starts it at the first pacer after
22:41 UTC (as it does the nightly build; GitHub's cron fires rarely here), with a `41 22 * * *` cron as backup. Each
snapshot is followed for **20 trading sessions** after its flag. After that, or 45 calendar days after the flag
(delisted, halted, no data), or once Yahoo answers `404 No data found`, it is left alone. When collection has
finished (README, "How long it runs") the pacer stops, the cron keeps tracking going for the last candidates, and once
nothing is left to follow the workflow turns itself off. A run that misses a day loses nothing: daily bars are
history, so the next run records every session it missed (with the later `collected_at`).

## Sessions

Session `k = 1` is the first regular session whose close (16:00 ET) comes after the flag. For a flag during market
hours that is the flag's own session (`flag_in_session_1 = 1`), so its high and low can include trading from before
the flag; a flag after the close or at the weekend starts with the next session. A session is recorded once its close
is an hour old, so partial bars are never stored.

Prices are kept **in flag-time terms**: Yahoo re-adjusts its whole history after a split, so each bar is divided by
`adj_factor`, the product of `denominator / numerator` over splits after the flag (a 1-for-10 reverse split has
factor 10). Without it a reverse split mid-pump (common) would read as a +900% move against `price_at_flag`.

## Files (on the `data` branch)

| Path | What |
|---|---|
| `track/daily.csv` | append-only: one row per snapshot x session, `k`, OHLCV in flag-time terms, `adj_factor`, `collected_at` |
| `track/filings.csv` | append-only: SEC filings accepted after the flag (form, acceptance time, 8-K items); `k` is the first session that could react to it |
| `track/outcomes.csv` | rebuilt every run from the two files above: one row per snapshot, see below |
| `track/README.md` | the outcomes, human readable |
| `track/state.json` | snapshots Yahoo no longer knows (internal) |

## Outcomes (`track/outcomes.csv`, version `track-v1`)

Returns are against `base_price` = Stage 2's `price_at_flag`. A column stays blank until all the sessions it needs
have been recorded, so a value never changes once it appears (unless Yahoo revises a bar).

| Column | Definition |
|---|---|
| `status` | `active`, `done` (20 sessions), `expired` (45 days), `no_data` (not on Yahoo), `no_price` (Stage 2 had no price) |
| `max_high_5`, `ret_max_5`, `peak_k_5` | highest high over sessions 1-5, its return, and which session |
| `min_low_10_after_peak`, `drop_from_peak_10` | lowest low over the 10 sessions after that peak, and its fall from the peak's high |
| `ret_close_1/5/10/20` | close of session k vs the flag price |
| `current_reports_10` | 8-K/6-K filings accepted between the flag and session 10's close (news) |
| `dilution_filings_20` | S-1/S-3/F-1/F-3/424B/Reg A filings between the flag and session 20's close (the dump's supply) |
| `mentions_next_5d/20d` | Reddit mentions on the 5 / 20 UTC days after the flag's day (Stage 1's daily counts) |

These columns are chosen to evaluate the example rule in the brief (+50% within 5 days, then -40% from the peak
within 10) and its variants, but **the label rule itself is Stage 4's** and must be written down before anyone looks
at these numbers. Daily highs and lows can't say whether the peak came before the drop within one session, which is
why the drop is measured only over sessions after the peak's.

`python -m pumpdump build-db` loads `track_daily`, `track_filings` and `track_outcomes`.

## Known gaps

- Daily bars only: intraday pumps that fully reverse within a session show up only as a long upper wick.
- OTC tickers that stop trading have no bars; they expire after 45 days with fewer than 20 sessions.
- data.sec.gov serves a filing's `acceptanceDateTime` 4 hours later (5 in winter) once the filing is no longer new:
  16 filings read on 2026-10-05 came back +4 h on 2026-10-06, some of them later than the moment we had first read
  them, so the first value is the right one. `track/filings.csv` therefore keys filings on their `accession` number and
  keeps the time first seen; a filing that is skipped because Stage 2 already saw it before the flag (its
  `last_current_report_at` / `last_dilution_at`, 4-5 h earlier) is not recorded. A filing first read only after the
  shift still carries the extra hours. Rows from before 2026-10-07 had no accession number: their shifted copies were
  dropped and the rest matched to accession numbers on the next read.
- Session closes are taken as 16:00 ET, so half days are recorded one session late at worst.
