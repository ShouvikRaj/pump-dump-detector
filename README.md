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

Every record carries `created_utc` (when it was posted) and `collected_at`
(when the collector received it). Build a SQLite database with
`python -m pumpdump build-db --datastore <checkout of this branch>`, or
download the `pumpdump-sqlite` artifact from the latest `nightly` run.
