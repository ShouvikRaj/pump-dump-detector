# pump-dump-detector

Detecting US stock pump-and-dumps by combining social-media chatter with market data, validated with paper trading only.
This repository is built in stages; **Stage 1 (this code) is the social scraper**: it collects Reddit chatter with
collection timestamps and flags tickers whose mentions or hype language suddenly spike.

```
Stage 1  Reddit chatter -> ticker mentions -> spike flags -> candidate list      <- this repo, running
Stage 2  market check of candidates (float, volume vs average, price, SEC dilution filings)
Stage 3  ongoing tracking of chatter and price per candidate
Stage 4  outcome labels after N days (pump / not pump / real news), rule fixed in advance
Stage 5  feedback loop: retrain, keep only patterns that hold across periods
```

Detect and avoid only: nothing here trades, and flags are statistical, not accusations or advice.

## What runs where

Everything runs on GitHub Actions; no computer needs to stay on.

| Workflow | When | What |
|---|---|---|
| `collect` | every 15 min | fetch new posts/comments from r/pennystocks, r/smallstreetbets, r/wallstreetbets; store them; extract tickers; flag spikes; update the candidate list; open an issue if collection is unhealthy |
| `nightly` | 03:41 UTC | build a SQLite database of everything collected and attach it to the run as the `pumpdump-sqlite` artifact |
| `tests` | every push | `pytest` |

Collected data lives on the **`data` branch** (see its README). Start with `candidates/README.md` there.

## Data source

Reddit closed self-serve API keys in November 2025 and blocked unauthenticated `.json` access in May 2026, so PRAW
can't be used without Reddit's manual approval. Posts and comments come from the
[Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) Reddit archive instead: same content, archived about
20-30 seconds after posting, no key needed. Its `score`/`num_comments` are placeholders (1/0) until it refreshes them
about 36 hours later, so they are stored but must not be used as decision-time features.

StockTwits' public trending list is recorded each run as a second, independent hype signal. Ticker symbols come
from the Nasdaq Trader symbol directory and the SEC's `company_tickers_exchange.json` (refreshed daily).

## How a candidate is flagged

1. **Ticker extraction** (after Nam & Skillicorn 2025): `$CASHTAG`, `NASDAQ: XXXX` / `OTC: XXXX`, or a bare ALL-CAPS
   3-5 letter word that is a listed symbol and not a common English word or finance acronym (so `PUMP`, `MOON`,
   `CEO` only count as `$PUMP` etc.). URLs and r/ u/ links are ignored. One mention per ticker per document.
2. **Hype score**: number of hype categories a document uses (moon/rocket, squeeze, 10x, urgency, "next GME", hidden
   gem, tendies, diamond hands, low float, price targets, fire). 2+ categories = a hype document.
3. **Spike rule** (after Renault 2017): mentions in the trailing 24 h > mean + 2 sd of the previous 7 days, with at
   least 10 mentions from 5 different authors. The sd is floored at sqrt(mean) so a flat baseline doesn't flag
   10 -> 11. The same test on hype documents (at least 5 from 3 authors) flags sudden promotional language.
4. **Episodes**: the first flag of a ticker is written to `candidates/episodes.csv` with every number known at that
   moment; it stays active while it keeps flagging and closes after 24 h without a flag.

Detection only runs when every stream has 8 full days of history and caught up within the last 3 hours. The
first week's flags are marked `warmup=1` because part of their baseline was backfilled rather than collected live.

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
`candidate_episode_ends`, `daily_mention_counts`, `stocktwits_trending`, `runs`, `symbols`.

Try the extractor on any text: `python -m pumpdump scan '$ABCD to the moon 🚀 short squeeze'`.

## Development

```bash
pip install -e ".[dev]"
pytest
```

Code: `src/pumpdump/` (`tickers.py`, `hype.py`, `spikes.py`, `sources/arctic_shift.py`, `pipeline.py`, `cli.py`).
Design notes and the reasoning behind each threshold: [docs/stage1.md](docs/stage1.md).
