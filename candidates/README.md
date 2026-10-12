# Stage 1 candidates

Updated 2026-10-12T12:07:47Z by run `38247016947`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| IREN | 2026-10-12 03:44 | mention spike | 36 | 10.43 | 31 | 0 | wallstreetbets 36 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3x2u7/) |
| MGM | 2026-10-12 06:49 | mention spike | 13 | 0.57 | 6 | 0 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
