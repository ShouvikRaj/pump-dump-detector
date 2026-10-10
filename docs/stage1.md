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

### Fallback while Arctic Shift is down: Reddit's RSS feeds

Arctic Shift is one person's project with no uptime promise. On 2026-10-09 at 15:45 UTC its server went down
(Cloudflare answered `522` from GitHub's runners and from elsewhere) and stayed down for more than a day, while
each run spent its whole budget retrying. Since then:

- When a request fails for good with a server or network error (a `422` query timeout doesn't count), the client
  stops asking Arctic Shift for the rest of the run. Once every stream has failed 4 runs in a row, a run tries
  Arctic Shift once without retrying, and retries again as soon as it answers.
- Each stream Arctic Shift failed reads Reddit's public Atom feed instead (`/r/SUB/new/.rss` for posts,
  `/r/SUB/comments/.rss` for comments: no key, about 100 requests per 10 minutes from a runner, checked
  2026-10-10 with the `reddit-probe` workflow), newest first, paging back with `?after=` until it reaches what is
  already stored. Feeds are read once every stream has tried Arctic Shift, r/wallstreetbets comments first since
  their feed reaches back least. Items are stored with `source=reddit_rss` and `fetch_mode=fallback`. Feeds lack `score`,
  `num_comments`, `author_fullname` and `parent_id`, leave out removed items, and give the body as rendered HTML,
  which is turned back into text.
- Reddit's budget belongs to the runner's IP address, which other GitHub users share: on 2026-10-10 one runner
  got a `429` after its first request while another had all 100 left. Once Reddit says the budget is spent, the
  reader waits for its reset (at most 10 minutes) if the run has time, else stops asking until the next run.
  While Arctic Shift is down the feeds may use the whole run, since the daily re-fetch can't.
- The Arctic Shift cursor doesn't move, so once Arctic Shift answers again it re-reads the whole stretch and
  anything the feed missed arrives then (`fetch_mode=live`), as far as Arctic Shift's own archive has it. The
  first copy of an item wins, as always.
- Spike detection counts a stream as current when Arctic Shift or the feed has caught up within 3 h. Reddit's
  listings stop at about 1000 items, which is days of r/pennystocks but only about 2 h of r/wallstreetbets
  comments, so after a long outage the first feed read can't reach back and leaves a hole (a run warning; the
  run log's `fallback` row shows `complete=0`). The feed is trusted from its next read, which reaches back to the
  first. Until Arctic Shift fills the hole, r/wallstreetbets comment counts for that stretch are short: fewer
  flags while it is in the trailing 24 h, and for the week it sits in the baseline, a ticker that was busy there
  then faces a lower bar.
- Daily mention counts and the daily re-fetch still wait for Arctic Shift.

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

`fetch_mode` records how a document arrived: `backfill` (first 9 days at start-up), `live`, `reconcile`
(picked up by the daily re-fetch after being archived late), or `fallback` (read from Reddit's RSS feed while
Arctic Shift was down; see above).

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

## Ticker extraction (`tickers.py`, version `tickers-v4`)

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

v3 (2026-10-05) followed once SEC's ticker list started loading, which added 3,266 symbols, 2,535 of them OTC. Of
the 28 SEC-only symbols that matched as bare words in the first 167k records, most were real OTC names (FNMA, FMCC,
BLGO, NLST, UURAF), but `COLA` (cost-of-living adjustment), `EMI` (loan instalment) and `ACAT` (brokerage transfer)
were jargon, so they joined `data/acronyms.txt`.

v4 (2026-10-06): bare `PMI` no longer counts on r/wallstreetbets. Candidate PMI (flagged 2026-10-05 13:55Z) came
from chatter about the ISM services PMI release: all 21 bare "PMI" on r/wallstreetbets from Sep 30 to Oct 5 meant
the purchasing managers' index, but all 4 on r/pennystocks meant Picard Medical (NYSE American: PMI), a low-float
runner (1.3M-share float, $6.16 at the flag in Stage 2's snapshot; "PMI just got halted"). Blocking it everywhere
would have hidden that, so `data/wsb_acronyms.txt` lists
symbols that don't count bare on r/wallstreetbets only; `$PMI` still counts everywhere. On the 189k records
collected Oct 4-6 the change drops exactly those 21 mentions and nothing else. The PMI episode stays in
`episodes.csv` with `extractor_version` `tickers-v3`. (ADP, the payroll report, was already excluded in v2.)

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

## Scheduling

GitHub's cron fired once in this repo's first hours (2026-10-05 01:18 UTC) and then skipped every slot, which is
common for new repositories. So collection paces itself: the last step of every `collect` run, whatever its outcome,
starts the `pace` workflow. Its job runs in the `pacer` environment, whose 13-minute wait timer (a repository
setting) delays the job without holding a runner; the job then starts the next `collect` run unless one is already
queued or running. Runs end up about 15 minutes apart. If the last `collect` run started less than 10 minutes earlier,
the timer must be missing, so `scripts/pace.sh` stops the chain rather than looping. Each pacer also queues the next
pacer, because on 2026-10-05 GitHub never gave a runner to one `collect` run (19:43 UTC), which therefore queued no
pacer and collection stopped for an hour; with collect -> pacer and pacer -> pacer, one lost run of either can't break
the chain. The `pace` concurrency group runs one pacer at a time with at most one queued behind it (a newer queued
one replaces it), and a pacer that waited under 10 minutes doesn't queue another. The cron stays on as a restart path. The nightly
build's cron is just as unreliable (it skipped its first slot), so the first pacer after 03:41 UTC starts it unless
it already ran that day.

## When collection stops

Each run checks `collection_done` first. Collection ends once there are 120 days of live data and 300
post-warm-up candidates at least 10 days old, or after 180 days regardless (`Settings.stop_*`). A finished run
fetches nothing, so it can't raise stale-data health alerts; the nightly job publishes the final SQLite as the
`dataset-final` release and disables both workflows. The check is stateless, so raising the limits and re-enabling
the workflows resumes collection where it stopped.

## For Stage 2

`candidates/episodes.csv` is the hand-off: ticker, first flag time, mentions/authors/hype vs baseline,
subreddits, example links, `exchange` and `in_universe` (from the symbol list), StockTwits rank at that moment,
and `warmup`.
