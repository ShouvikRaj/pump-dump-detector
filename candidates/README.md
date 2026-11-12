# Stage 1 candidates

Updated 2026-11-12T13:21:07Z by run `43225005717`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 424 | 134.43 | 327 | 2 | wallstreetbets 416, smallstreetbets 6, pennystocks 2 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9rfx/) |
| AVGO | 2026-11-09 15:56 | mention spike | 64 | 17.43 | 51 | 0 | wallstreetbets 63, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sivs9dg24md/) |
| NBIS | 2026-11-11 12:32 | mention spike | 368 | 58.29 | 189 | 1 | wallstreetbets 365, smallstreetbets 3 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1860 | 575.57 | 1047 | 2 | wallstreetbets 1830, smallstreetbets 29, pennystocks 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xua9iu/) |
| NVDL | 2026-11-11 07:39 | mention spike | 14 | 3.29 | 11 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 16 | 0.14 | 15 | 1 | pennystocks 14, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 74 | 4.43 | 57 | 0 | wallstreetbets 74 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu7xyx/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| SLI | 2026-11-12 05:40 | mention spike | 15 | 0.43 | 14 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| GME | 2026-11-12 01:54 | mention spike | 20 | 10.0 | 17 | 2 | wallstreetbets 18, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| ANT | 2026-11-10 14:52 | mention spike | 79 | 41.43 | 68 | 0 | wallstreetbets 77, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu8yp4/) |
| CRWV | 2026-11-10 20:00 | mention spike | 172 | 89.71 | 113 | 0 | wallstreetbets 171, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 8 | 5.29 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |
| MSFT | 2026-11-11 15:26 | mention spike | 75 | 57.29 | 58 | 0 | wallstreetbets 74, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 7 | 5.57 | 5 | 0 | wallstreetbets 7 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
