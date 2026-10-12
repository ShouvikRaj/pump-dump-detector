# Stage 1 candidates

Updated 2026-10-12T14:34:06Z by run `38263762788`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CBRS | 2026-10-12 14:20 | mention spike | 21 | 5.14 | 8 | 0 | wallstreetbets 21 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgbenv/) |
| IREN | 2026-10-12 03:44 | mention spike | 40 | 10.43 | 34 | 0 | wallstreetbets 40 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3x2u7/) |
| SOXX | 2026-10-12 14:20 | mention spike | 12 | 4.0 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgc6ou/) |
| MU | 2026-10-12 14:20 | mention spike | 16 | 8.0 | 6 | 0 | wallstreetbets 16 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfg9u7n/) |
| MGM | 2026-10-12 06:49 | mention spike | 8 | 1.29 | 4 | 0 | wallstreetbets 7, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
