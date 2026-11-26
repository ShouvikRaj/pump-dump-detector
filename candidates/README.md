# Stage 1 candidates

Updated 2026-11-26T01:31:28Z by run `45735645204`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| META | 2026-11-26 00:54 | mention spike | 29 | 18.0 | 16 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| NRSN | 2026-11-26 00:44 | mention spike | 12 | 0.0 | 10 | 0 | pennystocks 8, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5betx/) |
| SGOV | 2026-11-25 21:55 | mention spike | 23 | 6.57 | 22 | 0 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y56p4r/) |
| SOXL | 2026-11-26 00:44 | mention spike | 75 | 40.14 | 57 | 0 | wallstreetbets 75 | NYSE Arca | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5dxq0/) |
| SOXS | 2026-11-26 00:44 | mention spike | 18 | 7.29 | 15 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4wo51/) |
| VTI | 2026-11-26 00:54 | mention spike | 17 | 7.14 | 15 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/) |
| AAPL | 2026-11-26 00:54 | mention spike | 61 | 29.86 | 32 | 0 | wallstreetbets 61 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6t8v2m0lyd/) |
| DELL | 2026-11-24 21:15 | mention spike | 51 | 20.14 | 33 | 0 | wallstreetbets 51 | NYSE | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| BENF | 2026-11-25 00:43 | mention spike | 2 | 1.71 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y4yruq/comment/19t5y651znmkg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
