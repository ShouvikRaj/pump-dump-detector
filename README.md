# pump-dump-detector

Detecting US stock pump-and-dumps by combining social-media chatter with market data, validated with paper trading only.
This repository is built in stages. **Stage 1 is the social scraper**: it collects Reddit chatter with collection
timestamps and flags tickers whose mentions or hype language suddenly spike. **Stage 2 is the market check**: each
flagged ticker's market data as of the moment it was flagged, next to two matched tickers nobody was talking about.
**Stage 3 is tracking**: every flagged ticker and control is followed for 20 trading sessions afterwards. **Stage 4 is
labeling**: once its windows have closed, each one is labeled pump, real news or not pump (plus a separate crash label),
by a rule written down before any results were looked at. **Stage 5 is the model**: every new candidate is scored
for crash and pump risk by a LightGBM model retrained each week on the labels so far, validated walk-forward and,
once, on a locked hold-out period.

```
Stage 1  Reddit chatter -> ticker mentions -> spike flags -> candidate list      <- running
Stage 2  market check of candidates (float, volume vs average, price, SEC dilution filings)   <- running
Stage 3  ongoing tracking of price, filings and chatter per candidate and control (20 sessions)   <- running
Stage 4  outcome labels after 10-15 sessions (pump / real news / not pump, and crash), rule fixed in advance   <- running
Stage 5  model + feedback loop: weekly retraining, walk-forward checks, weak feature groups pruned   <- running
```

Detect and avoid only: nothing here trades, and flags are statistical, not accusations or advice.

## What runs where

Everything runs on GitHub Actions; no computer needs to stay on.

| Workflow | When | What |
|---|---|---|
| `collect` | about every 15 min | fetch new posts/comments from r/pennystocks, r/smallstreetbets, r/wallstreetbets; store them; extract tickers; flag spikes; update the candidate list; open an issue if collection is unhealthy |
| `pace` | after each `collect` run | wait 13 minutes in the `pacer` environment, then start the next `collect` run (GitHub's cron fires rarely for this repo, so collection paces itself; the cron stays as a backup) |
| `market` | after each `collect` run | snapshot each new candidate's market data as of its flag time, plus two matched controls (Stage 2) |
| `track` | daily after the US close (started by `pace` after 22:41 UTC; cron backup) | record each candidate's and control's new trading sessions and SEC filings since its flag, for 20 sessions, and rebuild `track/outcomes.csv` (Stage 3) |
| `label` | daily after `track` (started by `pace` after 23:21 UTC; cron backup) | label every candidate and control whose windows have closed and rebuild `labels/labels.csv` (Stage 4) |
| `model` | daily after `label` (started by `pace` after 00:11 UTC; cron backup) | rate new candidates' chatter (text features and LLM labels), retrain the weekly models, score each new candidate once into `model/predictions.csv` and rewrite `model/README.md` (Stage 5) |
| `llm-eval` | by hand (Actions, then Run workflow) | test the LLM step's prompt, or another open-weights model, against the hand-labelled documents in `docs/stage5-llm-gold.json`; writes nothing (Stage 5) |
| `nightly` | 03:41 UTC (started by `pace` when GitHub's cron misses it) | build a SQLite database of everything collected and attach it to the run as the `pumpdump-sqlite` artifact; once collection has finished, publish it as the `dataset-final` release and turn collection off |
| `tests` | every push | `pytest` |

Collected data lives on the **`data` branch** (see its README). Start with `candidates/README.md` there,
`market/README.md` for the market snapshots, `track/README.md` for what happened next, `labels/README.md` for the
labels and `model/README.md` for the model's scores and results.

The `pacer` environment's wait timer (13 minutes, set under Settings > Environments) is what spaces the runs; it holds
no runner while waiting. Each wait shows up as a deployment to `pacer`. If the timer is removed, `pace` stops the
chain instead of looping, and collection falls back to the cron.

## How long it runs

Collection stops by itself once there is enough data for the planned analysis: **120 days** of live collection
**and** **300 candidates** flagged after the warm-up week that are at least 10 days old (so each one's follow-up
chatter has been collected). It stops after **180 days** regardless.

120 days gives a few months for walk-forward validation plus a locked hold-out month, and covers the 60-120 days
that promotion campaigns run (Leuz et al.); 300 settled candidates leave a usable number of pumps even under the
strict label rule, which few candidates will meet. The 180-day cap keeps the data branch around 550 MB. When it
stops, the collector fetches nothing more and marks `candidates/README.md`, and the next nightly run publishes the
final database as the [`dataset-final` release](https://github.com/ShouvikRaj/pump-dump-detector/releases/tag/dataset-final) and turns collection off (all three workflows; `market`
stops with them, since it runs after `collect`).

The data can be analysed at any time before that. To collect for longer, raise the `stop_*` values in `Settings`
(`src/pumpdump/pipeline.py`) and re-enable both workflows in the Actions tab; `python -m pumpdump status
--datastore <data branch checkout>` says whether collection has finished.

## Data source

Reddit closed self-serve API keys in November 2025 and blocked unauthenticated `.json` access in May 2026, so PRAW
can't be used without Reddit's manual approval. Posts and comments come from the
[Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) Reddit archive instead: same content, archived about
20-30 seconds after posting, no key needed. Its `score`/`num_comments` are placeholders (1/0) until it refreshes them
about 36 hours later, so they are stored but must not be used as decision-time features.

StockTwits' public trending list is recorded each run as a second, independent hype signal. Ticker symbols come
from the Nasdaq Trader symbol directory and the SEC's `company_tickers_exchange.json` (refreshed daily, or after
2 hours if a source failed). The SEC refuses requests whose User-Agent doesn't name a reachable contact, and GitHub
no-reply addresses don't count, so its list is fetched only once the repository secret `SEC_USER_AGENT` holds one
(e.g. `pump-dump-detector you@example.com`), starting with the next run after the secret is added. A secret stays
out of the public logs, and the address is sent to sec.gov only. OTC tickers missing from both lists still count when written as `$TICKER`.

## How a candidate is flagged

1. **Ticker extraction** (after Nam & Skillicorn 2025): `$CASHTAG`, `NASDAQ: XXXX` / `OTC: XXXX`, or a bare ALL-CAPS
   3-5 letter word that is a listed symbol and not a common English word or finance acronym/slang (so `PUMP`,
   `MOON`, `CEO`, `TACO` only count as `$PUMP` etc.). URLs and r/ u/ links are ignored. One mention per ticker per
   document.
2. **Hype score**: number of hype categories a document uses (moon/rocket, squeeze, 10x, urgency, "next GME", hidden
   gem, tendies, diamond hands, low float, price targets, fire). 2+ categories = a hype document.
3. **Spike rule** (after Renault 2017): mentions in the trailing 24 h > mean + 2 sd of the previous 7 days, with at
   least 10 mentions from 5 different authors. The sd is floored at sqrt(mean) so a flat baseline doesn't flag
   10 -> 11. The same test on hype documents (at least 5 from 3 authors) flags sudden promotional language.
4. **Episodes**: the first flag of a ticker is written to `candidates/episodes.csv` with every number known at that
   moment; it stays active while it keeps flagging and closes after 24 h without a flag.

Detection only runs when every stream has 8 full days of history and caught up within the last 3 hours. The
first week's flags are marked `warmup=1` because part of their baseline was backfilled rather than collected live.

## Stage 2: market snapshots

A minute or two after a candidate is flagged, the `market` workflow records what the market looked like **at the
flag time**: price (including pre/post-market), returns, volume against the 20-day average, 52-week range, reverse
splits, float and shares outstanding (Yahoo, and SEC cover pages as filed), FINRA short interest, and SEC filings
(S-1/S-3/F-1/F-3 registrations, 424B prospectuses, 8-K item 3.02 share sales, late-filing notices, name changes).
Only data that existed before the flag counts. Each candidate gets an archetype, decided before any results:
`low_float_runner` (listed, $1-10, float <= 20M) or `otc_penny` (OTC, under $1), else `other`. Two controls with no
Reddit mentions in the previous 7 days are snapshotted at the same moment: same venue and archetype, and for listed
stocks a similar price and market cap. The raw source data is kept too, so price history survives delistings and
reverse splits.

All sources are free and keyless (Yahoo Finance, SEC EDGAR, FINRA, Nasdaq's screener); SEC uses the same
`SEC_USER_AGENT` secret as Stage 1. Every column, rule and known gap: [docs/stage2.md](docs/stage2.md).

## Stage 3: tracking

Once a day after the close, the `track` workflow appends each finished trading session of every candidate and control
(open/high/low/close/volume, kept in flag-time prices across splits) and every SEC filing made since the flag, each
stamped with when it was collected. From those it rebuilds `track/outcomes.csv`: the 5-session peak, the drop from that
peak over the next 10 sessions, returns after 1/5/10/20 sessions, 8-Ks and dilution filings, and Reddit mentions in the
days after. Each ticker is followed for 20 sessions and then left alone; the label rule is Stage 4's. Details:
[docs/stage3.md](docs/stage3.md).

## Stage 4: labels

Once a day after tracking, the `label` workflow labels every candidate and control with the same rule, written down
and committed before any outcome was looked at (version `label-v1`, chosen by shouvik):

- **pump**: up 50% or more within 5 sessions after the flag, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy, or a material agreement that isn't
  a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it takes precedence over pump
- **not pump**: neither, once the windows have closed
- **crash**, a separate label for the "avoid" signal: a close 40% or more below the flag price within 10 sessions

A label is final 10 sessions after the flag (15 after a 50% rise) and never changes after that. `labels/README.md` on
the data branch counts them per archetype for candidates and controls side by side; the crash rate of candidates
against their controls is the first test of the avoid signal. Rule, reasons and gaps: [docs/stage4.md](docs/stage4.md).

## Stage 5: the model

Once a day after labeling, the `model` workflow (rule `model-v2`, written down and committed before any model was
trained: [docs/stage5.md](docs/stage5.md)):

- reads the Reddit posts and comments behind each new flag and turns them into text features (one author dominating,
  copy-paste and reworded copies across authors, promotional and squeeze language, news and dilution talk, outside
  links) and LLM labels from a small open-weights model that llama.cpp runs on the workflow's own runner (no account
  or key): which posts are not about the company at all, which pitch it, which warn about it and which state a
  company event, with a copied quote the code checks, so every label can be checked against the posts;
- adds how often the same stock was flagged, and crashed, before;
- trains one LightGBM model per week and target (**crash** first, the avoid signal; then **pump**) on every candidate
  and control whose label was settled before the week began, recent ones weighted more, once 50 rows and 5 positives
  exist;
- scores each new candidate once with its week's model and appends the score to `model/predictions.csv`, the
  prospective log (signal-only paper trading, phase 1); a candidate is flagged at twice the base rate;
- replays every development week (flags before 2027-01-04) the same way and reports precision, recall, F1, lift,
  average precision and five robustness checks (separate periods, per pump type, against the controls, after 1-3%
  slippage), and drops feature groups that don't help once there are 20 positive candidates;
- leaves the hold-out (flags from 2027-01-04) locked until collection has ended and its labels have settled, then
  evaluates it once into `model/holdout.md` and turns itself off.

## Safeguards built in

- **No lookahead**: every record stores `created_utc` and `collected_at`; counting functions take an `as_of` time
  and only see documents collected by then. Raw files are append-only and partitioned by collection date.
- **Control groups**: all tickers' daily mention counts are kept (`daily/mention_counts/`), not just flagged ones.
- **Late data**: each run re-reads 30 min (comments) / 3 h (posts) before its cursor, and every day after 00:30 UTC
  the previous day is re-fetched in full; anything archived late is stored with its real (late) `collected_at`.
- **Versioned rules**: candidate rows carry `detector_version` and `extractor_version`.

## Use the data locally

```bash
git clone --branch data --single-branch https://github.com/ShouvikRaj/pump-dump-detector.git datastore
pip install .
python -m pumpdump build-db --datastore datastore --out pumpdump.sqlite
sqlite3 pumpdump.sqlite "select ticker, first_flagged_at_utc, mentions_24h, reasons from candidate_episodes order by first_flagged_at desc limit 20"
```

Tables: `docs` (posts + comments), `mentions` (one row per document x ticker, with hype score), `candidate_episodes`,
`candidate_episode_ends`, `daily_mention_counts`, `stocktwits_trending`, `runs`, `symbols`, `market_snapshots`
(Stage 2, candidates and controls; join on `episode_id`), `market_universe` (daily prices of all listed stocks),
`track_daily`, `track_filings`, `track_outcomes` (Stage 3; join on `snapshot_id`), `labels` (Stage 4; join on `snapshot_id`),
`model_text`, `model_llm` (Stage 5; join on `episode_id`), `model_predictions`, `model_walkforward` (Stage 5; join on
`snapshot_id`).

Try the extractor on any text: `python -m pumpdump scan '$ABCD to the moon 🚀 short squeeze'`. See what a market
snapshot would record right now (needs internet; nothing is saved):
`python -m pumpdump market --datastore datastore --dry-run ABCD`.

## Development

```bash
pip install -e ".[dev]"
pytest
```

Code: `src/pumpdump/`. Stage 1: `tickers.py`, `hype.py`, `spikes.py`, `sources/arctic_shift.py`, `pipeline.py`.
Stage 2: `market.py` (the run), `features.py` (point-in-time features), `sources/` (Yahoo, EDGAR, FINRA, Nasdaq).
Stage 3: `track.py`. Stage 4: `label.py`. Stage 5: `text.py` (text features, LLM ratings), `model.py`. Command line:
`cli.py`. Design notes and the reasoning behind each threshold: [docs/stage1.md](docs/stage1.md),
[docs/stage2.md](docs/stage2.md), [docs/stage3.md](docs/stage3.md), [docs/stage4.md](docs/stage4.md),
[docs/stage5.md](docs/stage5.md).
