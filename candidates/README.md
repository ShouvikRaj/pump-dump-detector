# Stage 1 candidates

Updated 2026-10-12T17:00:06Z by run `38281184143`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CBRS | 2026-10-12 14:20 | mention spike | 37 | 5.14 | 19 | 0 | wallstreetbets 37 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 48 | 10.43 | 39 | 0 | wallstreetbets 48 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3x2u7/) |
| MU | 2026-10-12 14:20 | mention spike | 26 | 8.0 | 9 | 0 | wallstreetbets 26 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfh8enz/) |
| ONDS | 2026-10-12 14:47 | mention spike | 13 | 5.0 | 10 | 0 | wallstreetbets 13 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfgxqwg/) |
| SOXX | 2026-10-12 14:20 | mention spike | 12 | 4.14 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfh5l07/) |
| TSM | 2026-10-12 15:13 | mention spike | 14 | 6.57 | 11 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| SMCI | 2026-10-12 17:00 | mention spike | 11 | 3.71 | 5 | 0 | wallstreetbets 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x3tsce/) |
| MGM | 2026-10-12 06:49 | mention spike | 8 | 1.29 | 4 | 0 | wallstreetbets 7, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
