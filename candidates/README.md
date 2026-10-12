# Stage 1 candidates

Updated 2026-10-12T14:20:59Z by run `38262124035`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| IREN | 2026-10-12 03:44 | mention spike | 40 | 10.43 | 34 | 0 | wallstreetbets 40 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3x2u7/) |
| CBRS | 2026-10-12 14:20 | mention spike | 19 | 5.14 | 7 | 0 | wallstreetbets 19 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfga55r/) |
| MU | 2026-10-12 14:20 | mention spike | 16 | 8.0 | 6 | 0 | wallstreetbets 16 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfg9u7n/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.0 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfg8y63/) |
| MGM | 2026-10-12 06:49 | mention spike | 8 | 1.29 | 4 | 0 | wallstreetbets 7, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
