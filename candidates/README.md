# Stage 1 candidates

Updated 2026-10-12T20:45:13Z by run `38306171366`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 13 | 2.86 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfig25c/) |
| CBRS | 2026-10-12 14:20 | mention spike | 39 | 5.0 | 20 | 0 | wallstreetbets 39 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 52 | 10.29 | 41 | 0 | wallstreetbets 52 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4cb65/) |
| MU | 2026-10-12 14:20 | mention spike | 31 | 8.0 | 13 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| ONDS | 2026-10-12 14:47 | mention spike | 14 | 5.0 | 11 | 0 | wallstreetbets 14 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhgfgy/) |
| RDDT | 2026-10-12 20:18 | mention spike | 36 | 18.71 | 25 | 1 | wallstreetbets 36 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SMCI | 2026-10-12 17:00 | mention spike | 13 | 3.86 | 6 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x3tsce/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.43 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x42y1y/comment/pficid7/) |
| TSM | 2026-10-12 15:13 | mention spike | 17 | 6.71 | 12 | 0 | wallstreetbets 17 | NYSE | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| UNH | 2026-10-12 20:32 | mention spike | 11 | 3.29 | 11 | 0 | wallstreetbets 11 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pfiq0kv/) |
| WFF | 2026-10-12 18:19 | mention spike | 12 | 1.57 | 7 | 1 | wallstreetbets 8, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x3rzew/comment/pfi1zlo/) |
| MGM | 2026-10-12 06:49 | mention spike | 7 | 1.43 | 3 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
