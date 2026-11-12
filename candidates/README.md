# Stage 1 candidates

Updated 2026-11-12T15:22:08Z by run `43245219791`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 462 | 124.71 | 358 | 2 | wallstreetbets 453, smallstreetbets 7, pennystocks 2 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| AVGO | 2026-11-09 15:56 | mention spike | 66 | 18.14 | 50 | 0 | wallstreetbets 65, smallstreetbets 1 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj33jxl32e8/) |
| GME | 2026-11-12 01:54 | mention spike | 20 | 9.71 | 17 | 2 | wallstreetbets 18, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| LUNR | 2026-11-12 14:43 | mention spike | 15 | 5.43 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj2n3jz7ie8/) |
| NBIS | 2026-11-11 12:32 | mention spike | 434 | 60.57 | 221 | 1 | wallstreetbets 429, smallstreetbets 5 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuf16g/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2090 | 587.29 | 1170 | 2 | wallstreetbets 2053, smallstreetbets 35, pennystocks 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf8dj/) |
| NVDL | 2026-11-11 07:39 | mention spike | 14 | 3.29 | 11 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 16 | 0.14 | 15 | 1 | pennystocks 14, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 76 | 4.43 | 59 | 0 | wallstreetbets 76 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| SLI | 2026-11-12 05:40 | mention spike | 16 | 0.43 | 15 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| ANT | 2026-11-10 14:52 | mention spike | 71 | 42.86 | 62 | 0 | wallstreetbets 69, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| CRWV | 2026-11-10 20:00 | mention spike | 141 | 94.14 | 96 | 0 | wallstreetbets 140, smallstreetbets 1 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GEV | 2026-11-10 15:44 | mention spike | 5 | 5.57 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |
| MSFT | 2026-11-11 15:26 | mention spike | 74 | 55.43 | 57 | 0 | wallstreetbets 73, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
