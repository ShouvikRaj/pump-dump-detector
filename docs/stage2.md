# Stage 2 design notes

Stage 2 takes a market snapshot of every Stage 1 candidate as of the moment it was flagged: price and volume
against its own history, float and shares outstanding, short interest, recent dilution filings, exchange and
which pump archetype it fits. The same snapshot is taken of two matched tickers nobody was talking about, so later
stages have a control group. Like Stage 1, the priorities are no lookahead and keeping what free sources lose.

## When it runs

Every `collect` run ends by starting the `market` workflow, the same way it starts `pace` (GitHub's `workflow_run`
event would be neater, but it doesn't fire for runs started with `GITHUB_TOKEN`, and the pacer starts most of
them). It reads `candidates/episodes.csv`, snapshots each candidate that has no snapshot yet, and pushes to the
`data` branch. A candidate is therefore snapshotted a minute or two after its flag. Snapshots never change once
written.

Each snapshot is computed **as of the flag time** (`as_of` = `first_flagged_at`): only price bars that had finished,
filings that had been accepted and data that had been published by then count. The fetch itself happens a little
later (`snapshot_at`, `lag_s`); values that free sources only serve as "current" (float, shares outstanding,
insider holdings) are as of `snapshot_at`, which is why the lag is recorded.

## Sources

Checked from GitHub's runners on 2026-10-05 (two probe runs). None needs a key; all are free.

| Source | What | Notes |
|---|---|---|
| Yahoo Finance chart API | 2 years of daily bars with split events; 5-minute bars incl. pre/post market around the flag | plain `requests` with a browser User-Agent; `404 No data found` for unknown or delisted symbols |
| Yahoo Finance quoteSummary | float, shares outstanding, insider/institution %, sector, exchange | needs a cookie + crumb (`fc.yahoo.com`, `getcrumb`); values are current, not historical |
| SEC EDGAR submissions | every filing with its acceptance time; former names; filer category | needs the `SEC_USER_AGENT` secret (see Stage 1); only for tickers with a CIK |
| SEC EDGAR XBRL `dei:EntityCommonStockSharesOutstanding` | shares outstanding from each 10-K/10-Q/20-F cover page, with filing date | point-in-time: the value as filed before the flag |
| FINRA consolidated short interest API | twice-monthly short interest for listed **and** OTC stocks | Yahoo's short interest for OTC names can be years old (FNMA: 2010), FINRA's is current |
| Nasdaq screener API | once a day: last price, volume and market cap of all ~7,000 listed stocks | lags by a session or two; used to price-match controls, and kept as a daily cross-section |

Not usable from GitHub's runners: OTC Markets' API (bot wall) and Stooq (JavaScript challenge). Not needed: the
`yfinance` library (works, but pulls pandas/numpy/curl_cffi for what two plain requests do).

## What a snapshot records (`market/snapshots.csv`, version `market-v1`)

One row per snapshot; `role` is `candidate` or `control`, `episode_id` joins to `candidates/episodes.csv` for both.
Prices are split-adjusted as Yahoo serves them; ratios are unaffected by splits.

| Group | Columns | Definition |
|---|---|---|
| timing | `as_of`, `snapshot_at`, `lag_s` | flag time; when the data was fetched; the gap |
| venue | `exchange`, `yahoo_exchange`, `venue`, `quote_type` | `venue` = `listed`, `otc` or `unknown` (Yahoo's exchange first, then the Stage 1 symbol list) |
| price | `price_at_flag`, `price_time_utc`, `price_source` | close of the last 5-minute bar (pre/post market included) that ended by `as_of`; the last daily close if there is none |
| last session | `last_session`, `last_close`, `move_since_close` | the last regular session that closed (16:00 ET) before `as_of`; `price_at_flag / last_close - 1` |
| returns | `ret_1d`, `ret_5d`, `ret_20d` | last close vs the close 1/5/20 sessions earlier |
| volume | `vol_last`, `avg_vol_20d`, `rel_vol_last` | last session's volume vs the mean of the 20 sessions before it |
| volume today | `vol_today`, `rel_vol_today` | volume of the regular-session 5-minute bars on the flag's ET date up to `as_of`, vs `avg_vol_20d`; 0 if the stock hasn't traded since the open (Yahoo skips bars without trades); blank until the first bar ends at 09:35 ET, on weekends and NYSE holidays (Yahoo serves no pre/post-market volume), or when the 5-minute fetch failed |
| liquidity | `dollar_vol_20d`, `volatility_20d` | mean close x volume and sd of daily log returns over the last 20 sessions |
| range | `high_52w`, `low_52w`, `pct_from_52w_high`, `n_sessions`, `first_trade_date` | over up to 252 sessions; `first_trade_date` flags recent listings |
| splits | `reverse_splits_1y`, `last_split_date`, `last_split_ratio` | reverse splits often precede pumps |
| shares | `shares_outstanding`, `float_shares`, `insider_pct`, `institution_pct` | Yahoo, as of `snapshot_at` |
| shares (SEC) | `sec_shares_outstanding`, `sec_shares_as_of`, `sec_shares_filed` | latest cover-page value filed before the flag date |
| derived | `market_cap`, `turnover_last`, `turnover_today` | price x shares; volume / float |
| short interest | `si_settlement_date`, `si_shares`, `si_prev_shares`, `si_days_to_cover`, `si_pct_float` | latest FINRA settlement assumed published by `as_of` (settlement + 8 business days) |
| dilution | `dilution_filings_90d`, `dilution_filings_365d`, `last_dilution_form`, `last_dilution_at`, `offerings_424b_30d` | S-1, S-3, F-1, F-3 (and amendments, MEF, ASR), 424B prospectuses, Reg A (1-A, 253G); accepted before `as_of` |
| other filings | `current_reports_30d`, `last_current_report_at`, `last_current_report_items`, `unregistered_sales_90d`, `late_filing_notices_365d`, `last_name_change` | 8-K/6-K count (news); the latest one's acceptance time and 8-K items (an 8-K just before the spike points to real news); 8-Ks with item 3.02 (private share sales); NT 10-K/10-Q; most recent former-name end date |
| issuer | `cik`, `sic`, `sec_category`, `state_of_incorporation`, `name`, `sector`, `industry`, `country` | |
| archetype | `archetype`, `archetype_version` | see below |
| quality | `errors` | `source: message` for every source that failed; the row is still written |

The raw responses behind each row (bars, quote fields, filings list, short interest rows) are saved to
`market/raw/YYYY/MM/DD/<snapshot>.json.gz`, so features can be recomputed with different rules later, and the
price history survives the ticker being delisted or reverse-split.

## Archetypes (`archetype-v1`)

From the project brief, decided before any results:

| Archetype | Rule |
|---|---|
| `low_float_runner` | listed (Nasdaq, NYSE, NYSE American, Arca, Cboe, IEX), price $1-10, float <= 20M shares (shares outstanding if float is unknown) |
| `otc_penny` | OTC, price < $1 |
| `other` | everything else (large caps, listed sub-dollar stocks, OTC above $1, ETFs) |
| `unknown` | no price |

20M is the upper end of what traders call low float; the raw float is in the row, so a stricter cut (10M) can be
applied in analysis without a new version.

## Controls

The brief asks for control groups: random low-float tickers with no chatter, and tickers with chatter that did
not pump. The second comes from candidates that don't pump. For the first, each candidate with price data gets two
controls snapshotted at the same `as_of`:

- same venue: listed candidates draw from the latest Nasdaq screener file, OTC candidates from the SEC's OTC
  ticker list;
- no chatter: not mentioned at all on Reddit in the 7 days before (`daily/mention_counts/`) and not a candidate;
- similar size: listed controls are within 0.5-2x of the candidate's price and market cap (widened to price only,
  then to all listed stocks, while fewer than 10 qualify);
- same archetype: a low-float runner's controls are low-float runners, an OTC penny stock's are OTC penny stocks,
  checked on each control's own snapshot (there is no free OTC price list to filter on beforehand);
- drawn with a random generator seeded by the episode id, so the draw is reproducible; a draw with no Yahoo data or
  the wrong archetype is replaced, up to 10 tries, so a candidate can end up with fewer than two.

Leuz et al. match on price level and pre-campaign run-up. Price and size are matched here; run-up can be matched in
analysis from `market_universe` (daily prices of every listed stock) and the controls' own price history.

## Failures and retries

- A source failing never stops a run. Its message goes into `errors` and the run summary.
- A candidate whose snapshot crashes (odd data or a bug) is treated like an outage below, so it can't block the
  candidates after it; if it still crashes after 12 hours it is written with the crash message.
- A host that still fails after retries twice in a row is skipped for the rest of the run, so a hanging source
  can't push a run past its time limit (the run's work would be lost).
- If Yahoo's daily chart (the core of the snapshot) fails with a network error, 429 or 5xx, the candidate stays
  pending and is retried on the next runs for 12 hours (`market/state.json` counts attempts); after that it is
  written with whatever was fetched. A `404 No data found` is final at once: the ticker is not on Yahoo (often an
  unlisted cashtag that isn't a real symbol), which is itself useful to know.
- Historical bars don't change, so a snapshot taken late still has correct price features; the current-only values
  (float, shares) are the ones `lag_s` qualifies.

## Data layout (on the `data` branch)

| Path | What |
|---|---|
| `market/README.md` | latest snapshots, human readable |
| `market/snapshots.csv` | one row per snapshot (candidates and controls), append-only |
| `market/raw/YYYY/MM/DD/*.json.gz` | raw source data per snapshot, by snapshot date |
| `market/universe/YYYY/MM/YYYY-MM-DD.csv.gz` | daily listed-stock cross-section from the Nasdaq screener, named by its price date |
| `market/state.json` | retry bookkeeping (internal) |

`python -m pumpdump build-db` loads `market_snapshots` and `market_universe` tables next to the Stage 1 ones.

## Known gaps

- Float and insider holdings are Yahoo's current values, not point-in-time; a snapshot taken hours late can see an
  update the flag time could not (rare; check `lag_s`).
- Non-reporting OTC pinks have no CIK, so no SEC data; their dilution shows up only as a rising share count.
- OTC controls come from the SEC's OTC ticker list, so they are all SEC reporters; non-reporting pinks are never
  drawn as controls, while some OTC candidates are non-reporting. Compare like with like (`cik` blank or not).
- Yahoo's pre/post-market bars only exist for listed stocks; OTC prices at flag time come from regular-session bars.
- The session close is taken as 16:00 ET, so on half days the last session is recognised up to 3 hours late.
- Short-interest publication dates are approximated (settlement + 8 business days), not read from FINRA's calendar.
