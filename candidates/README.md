# Stage 1 candidates

Updated 2026-10-10T16:58:10Z by run `38069422959`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| ADBE | 2026-10-08 04:07 | mention spike | 1 | 6.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x21cyd/) |
| ASTS | 2026-10-08 21:11 | mention spike | 5 | 47.86 | 5 | 0 | wallstreetbets 4, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1ve6y/comment/pf2bpek/) |
| IBM | 2026-10-09 01:09 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SLS | 2026-10-09 13:19 | mention spike | 2 | 5.14 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x1kb5x/comment/pf2d4kr/) |
| UNH | 2026-10-09 13:59 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| CMG | 2026-10-08 19:38 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HUM | 2026-10-09 12:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| UUUU | 2026-10-07 20:50 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
