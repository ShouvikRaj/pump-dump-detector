# Stage 1 design notes

Stage 1 turns Reddit chatter into a timestamped candidate list. Everything later (market checks, labels, models)
reads its outputs, so the priorities were: never lose data, never let later information leak into an earlier
decision, and keep running unattended.

## Source: Arctic Shift instead of PRAW

The original plan was PRAW. Checked on 2026-10-04:

- Reddit stopped self-serve OAuth app creation on 2025-11-11 ("Responsible Builder Policy": manual approval,
  hobby projects rarely approved) and blocked unauthenticated `.json` endpoints around 2026-05-28.
- The [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) archive serves the same posts and comments
  through a free API. Live check: `retrieved_on - created_utc` was 19-29 s for new r/pennystocks posts and comments,
  so it is effectively real time. It needs no key and is not blocked from cloud IPs.

Caveats handled in code:

- `score` and `num_comments` are 1/0 at archive time and refreshed ~36 h later. They are stored as received but are
  not decision-time features.
- Rate limits are dynamic and undocumented. The client waits 1 s between requests, honours `429` +
  `X-RateLimit-Reset`, retries 5xx/network errors with backoff, and drops `limit=auto` to 100 if a heavy query
  times out.
- The API only serves a fixed list of `fields` (no `permalink`, `removed_by_category`, `edited`, `upvote_ratio`).
  Permalinks are rebuilt from the IDs, and the other fields are not stored at all, so an empty value never
  pretends to mean "not removed". If the API stops accepting a field (`400 'x' is not a valid field`), the client
  drops it, carries on and the run summary warns.
- Reddit is moving away from monotonic comment IDs, so cursors use `created_utc`, never IDs.

If Reddit ever grants API access, a PRAW source can be added next to `sources/arctic_shift.py`; nothing else
depends on where records come from (each record carries `source`).

## Storage: append-only files on a `data` branch

A SQLite file can't be committed every 15 minutes (binary churn, GitHub's 100 MB file limit). Instead each run
writes one gzipped JSON-lines file of the records it newly saw:

```
raw/reddit/YYYY/MM/DD/HHMMSSZ_<run_id>.jsonl.gz   (date = UTC collection date)
```

The first backfill run collects a few hundred thousand records, so files are split every 50,000 records
(`HHMMSSZ_<run_id>_p00.jsonl.gz`, `_p01`, ...) to stay far below GitHub's per-file limits.

Files are never rewritten, so they form a log of what the collector knew and when. Each run sparse-checks-out
only the last 9 days of files plus small state/candidate/log files, rebuilds an in-memory SQLite database from
them, and pushes its new file. The full database is built nightly (or locally) with `pumpdump build-db`.

Volume (Arctic Shift time series, late Sep 2026): r/wallstreetbets ~22-26k comments per weekday, ~9k weekend
days; r/pennystocks ~400-600; r/smallstreetbets smaller. That is roughly 3 MB/day gzipped, ~1 GB/year, which a
GitHub repo handles fine for a couple of years. Clone with `--single-branch` to skip it.

## Timestamps and lookahead

Every record keeps three times:

| Field | Meaning |
|---|---|
| `created_utc` | when it was posted on Reddit |
| `source_retrieved_at` | when Arctic Shift archived it |
| `collected_at` | when our collector first received it (time the API page arrived) |

`db.window_counts(conn, as_of, strict=True)` only counts documents with `collected_at <= as_of`, so replaying
the detector over history reproduces what it could have known at each moment. The first copy of a document
wins; later re-fetches never overwrite it.

`fetch_mode` records how a document arrived: `backfill` (first 9 days at start-up), `live`, or `reconcile`
(picked up by the daily re-fetch after being archived late).

## Collection loop

Six streams: {posts, comments} x {pennystocks, smallstreetbets, wallstreetbets}. Each keeps a cursor (newest
`created_utc` seen). A run fetches everything created after `cursor - overlap` (3 h for posts, 30 min for
comments), oldest first, paging with `limit=auto` and re-reading the boundary second so ties across pages are not
lost. Known IDs are skipped. wallstreetbets comments run last so a slow catch-up there can't starve the rest.

After 00:30 UTC the first run of the day re-fetches the whole previous UTC day for every stream, stores anything
missing, then writes that day's per-ticker mention counts (all tickers, for control groups). If a busy day doesn't
fit in one run, the next run resumes the re-fetch where it stopped instead of starting over. Days that never get
this rollover (the backfilled days, or days missed while the collector was down) get their counts once every
stream has completed a fetch after the day ended, so rows in `daily/mention_counts/` are not in date order.

On the very first run every stream backfills 9 days (1 current + 7 baseline + 1 spare), which can take more
than one run for r/wallstreetbets; cursors make it resume.

## Ticker extraction (`tickers.py`, version `tickers-v2`)

Nam & Skillicorn (2025) used regex candidates checked against exchange symbol lists. Same idea, three forms:

| Form | Example | Accepted when |
|---|---|---|
| exchange prefix | `(NASDAQ: ABCD)`, `OTC: ABCDF`, `TSXV: XYZ` | always (US exchanges as `ABCD`, foreign ones as `TSXV:XYZ`) |
| cashtag | `$ABCD`, `$abcd`, `$BRK.B` | listed; or unlisted with 3+ letters and not a currency/crypto coin |
| bare | `ABCD` | ALL CAPS, 3-5 letters, listed, not a common English word (wordfreq Zipf >= 4.0) or finance acronym/slang, not part of a hyphenated compound (`GLP-1`) |

Unlisted cashtags are kept (`in_universe=0`) because non-reporting OTC pinks, the classic pump targets, are in
neither symbol list. Known gaps: company names ("GameStop") are not matched; two-letter tickers only count as
cashtags; tickers that are English words (`WOLF`, `OPEN`) only count as cashtags, except a short allowlist
(`data/bare_allow.txt`: SPY, HOOD, ARM, COIN, APP) that in caps on Reddit almost always means the ticker.
Documents by AutoModerator and the WSB bots are skipped.

v2 came from reading the bare matches in the first 165k live records: the most-mentioned "tickers" included
`TACO` (the Trump meme), `MAGA`, `GPT`, `DRAM`/`HBM` (memory chips), `WTI` (oil), `BYD` (the carmaker, not Boyd
Gaming), `HYSA`, `DEI`, `GLP` (from GLP-1) and SPY was missing entirely. About 45 such collisions were added to
`data/acronyms.txt`; they still count as `$TACO` etc. Real small caps found in the same review (SOAR, SDEV, GOW,
TGE, GYGY, WCT) were kept.

## Hype score (`hype.py`, version `hype-v1`)

Thirteen regex categories (moon, rocket, squeeze, multibagger, urgency, next_big, explosive, gem, wealth,
diamond, low_float, price_target, fire). A document with 2+ categories is a hype document; one rocket emoji is
ordinary WSB noise. This is a stand-in for the LLM classifier planned for later stages.

## Spike rule (`spikes.py`, version `spikes-v1`)

Renault (2017) flags an OTC stock when its daily tweet count exceeds the previous 7-day mean + 2 sd, with at
least 20 tweets from 20 users. Adapted:

| Parameter | Value | Why |
|---|---|---|
| window | trailing 24 h, evaluated every run | flags within 15 min instead of once a day |
| baseline | the seven 24 h windows before it | Renault's 7 days |
| threshold | mean + 2 x sd_eff | Renault |
| sd_eff | max(sample sd, sqrt(mean)) | a flat baseline (sd 0) would otherwise flag +1 changes; sqrt(mean) is the Poisson noise of a count |
| min mentions / authors | 10 / 5 | three subreddits are far quieter than all of Twitter; Stage 2 filters the extra candidates with market data |
| hype spike | same test on hype documents, min 5 from 3 authors | catches promotional language when total chatter is steady |
| episode gap | 24 h | one candidate row per burst, not one per run |

These values were set before looking at any results; change them only with a new `DETECTOR_VERSION`.
Large caps (TSLA, NVDA) will sometimes trip the 2-sd rule on news days; Stage 2's float and price filters
separate them from pump candidates, and the two archetypes (low-float Nasdaq runner, OTC penny) are told apart by
the `exchange` column.

## Health and self-monitoring

Each run writes `reports/health.json`. A stream is unhealthy when it hasn't completed a fetch for 3 h, hasn't
caught up 6 h after starting, or failed 4 runs in a row. The workflow keeps one GitHub issue (label
`collector-health`) open while unhealthy, which emails the repo owner, and closes it on recovery.

A source outage does not fail the run: the errors are saved in the state and pushed, and the checks above decide
when to alert. Only a crash, or a failed checkout or push, fails a run; three failed runs in a row (cancelled ones
skipped) also open the issue. The `nightly` workflow re-enables the schedules so GitHub's 60-day inactivity rule
can't switch them off.

## For Stage 2

`candidates/episodes.csv` is the hand-off: ticker, first flag time, mentions/authors/hype vs baseline,
subreddits, example links, `exchange` and `in_universe` (from the symbol list), StockTwits rank at that moment,
and `warmup`.
