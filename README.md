# Collected data (branch `data`)

Written by the `collect` workflow every 15 minutes. Code and docs live on `main`.

| Path | What |
|---|---|
| `candidates/README.md` | Current candidates, human readable |
| `candidates/episodes.csv` | One row per candidate, written the moment it was first flagged (never edited) |
| `candidates/episode_ends.csv` | When each candidate went quiet, with its peak numbers |
| `candidates/active.csv` | Candidates flagged in the last 24 hours |
| `raw/reddit/YYYY/MM/DD/*.jsonl.gz` | Every post and comment, one file per run (huge runs split into `_pNN` parts), partitioned by the UTC date it was collected |
| `daily/mention_counts/YYYY-MM.csv` | Mentions per ticker per UTC day, for all tickers (control groups) |
| `stocktwits/trending/YYYY-MM.csv` | StockTwits trending list at each run |
| `logs/runs/YYYY-MM.csv` | What each run fetched, lags and errors |
| `reports/health.json` | Latest health check (an issue opens automatically when it fails) |
| `ref/symbols.csv` | US ticker list (Nasdaq Trader + SEC); git history gives past versions |
| `state/state.json` | Cursors and open episodes (internal) |
| `market/README.md` | Stage 2: each candidate's market data at its flag time, human readable (written by the `market` workflow) |
| `market/snapshots.csv` | Stage 2: one row per market snapshot, candidates and their controls |
| `market/raw/YYYY/MM/DD/*.json.gz` | Stage 2: raw source data behind each snapshot (price bars, filings, short interest) |
| `market/universe/YYYY/MM/*.csv.gz` | Stage 2: daily prices of all listed stocks (Nasdaq screener), named by price date |

Every record carries `created_utc` (when it was posted) and `collected_at`
(when the collector received it). Build a SQLite database with
`python -m pumpdump build-db --datastore <checkout of this branch>`, or
download the `pumpdump-sqlite` artifact from the latest `nightly` run.
