# Stage 1 candidates

Updated 2026-10-12T15:13:58Z by run `38268605054`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CBRS | 2026-10-12 14:20 | mention spike | 23 | 5.14 | 8 | 0 | wallstreetbets 23 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgk62b/) |
| IREN | 2026-10-12 03:44 | mention spike | 43 | 10.43 | 37 | 0 | wallstreetbets 43 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3x2u7/) |
| MU | 2026-10-12 14:20 | mention spike | 18 | 8.0 | 8 | 0 | wallstreetbets 18 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgm6ta/) |
| ONDS | 2026-10-12 14:47 | mention spike | 11 | 5.0 | 9 | 0 | wallstreetbets 11 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgez65/) |
| SOXX | 2026-10-12 14:20 | mention spike | 12 | 4.0 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgc6ou/) |
| TSM | 2026-10-12 15:13 | mention spike | 14 | 6.71 | 11 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| MGM | 2026-10-12 06:49 | mention spike | 8 | 1.29 | 4 | 0 | wallstreetbets 7, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
