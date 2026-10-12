# Stage 1 candidates

Updated 2026-10-12T18:06:31Z by run `38288586993`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 12 | 2.86 | 9 | 0 | wallstreetbets 12 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhp9bo/) |
| CBRS | 2026-10-12 14:20 | mention spike | 37 | 5.14 | 19 | 0 | wallstreetbets 37 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 48 | 10.43 | 39 | 0 | wallstreetbets 48 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3x2u7/) |
| MU | 2026-10-12 14:20 | mention spike | 28 | 8.0 | 10 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhotvc/) |
| ONDS | 2026-10-12 14:47 | mention spike | 14 | 5.0 | 11 | 0 | wallstreetbets 14 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhgfgy/) |
| SMCI | 2026-10-12 17:00 | mention spike | 14 | 3.71 | 6 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x3tsce/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.29 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfh5l07/) |
| TSM | 2026-10-12 15:13 | mention spike | 14 | 6.71 | 11 | 0 | wallstreetbets 14 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| MGM | 2026-10-12 06:49 | mention spike | 8 | 1.29 | 4 | 0 | wallstreetbets 7, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
