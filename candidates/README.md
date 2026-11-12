# Stage 1 candidates

Updated 2026-11-12T15:08:09Z by run `43242823043`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 461 | 125.0 | 355 | 2 | wallstreetbets 453, smallstreetbets 6, pennystocks 2 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuef53/) |
| AVGO | 2026-11-09 15:56 | mention spike | 64 | 18.14 | 50 | 0 | wallstreetbets 63, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj1xlnoxtk3/) |
| LUNR | 2026-11-12 14:43 | mention spike | 15 | 5.43 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj2n3jz7ie8/) |
| NBIS | 2026-11-11 12:32 | mention spike | 431 | 60.29 | 220 | 1 | wallstreetbets 427, smallstreetbets 4 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2062 | 587.14 | 1157 | 2 | wallstreetbets 2026, smallstreetbets 34, pennystocks 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuerqj/) |
| NVDL | 2026-11-11 07:39 | mention spike | 14 | 3.29 | 11 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 16 | 0.14 | 15 | 1 | pennystocks 14, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 75 | 4.43 | 58 | 0 | wallstreetbets 75 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuedr9/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| SLI | 2026-11-12 05:40 | mention spike | 16 | 0.43 | 15 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| GME | 2026-11-12 01:54 | mention spike | 19 | 10.0 | 16 | 2 | wallstreetbets 17, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| ANT | 2026-11-10 14:52 | mention spike | 71 | 42.71 | 62 | 0 | wallstreetbets 69, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu8yp4/) |
| CRWV | 2026-11-10 20:00 | mention spike | 150 | 92.71 | 101 | 0 | wallstreetbets 149, smallstreetbets 1 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GEV | 2026-11-10 15:44 | mention spike | 5 | 5.57 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |
| MSFT | 2026-11-11 15:26 | mention spike | 77 | 55.71 | 59 | 0 | wallstreetbets 76, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
