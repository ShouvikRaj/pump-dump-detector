# Stage 1 candidates

Updated 2026-11-26T04:34:44Z by run `45755627855`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NRSN | 2026-11-26 00:44 | mention spike | 12 | 0.0 | 10 | 0 | pennystocks 8, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5betx/) |
| SGOV | 2026-11-25 21:55 | mention spike | 23 | 6.29 | 22 | 0 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y56p4r/) |
| VTI | 2026-11-26 00:54 | mention spike | 17 | 7.0 | 15 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/) |
| SOXS | 2026-11-26 00:44 | mention spike | 11 | 7.86 | 10 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y54kwg/comment/19t6f4f9d6200/) |
| META | 2026-11-26 00:54 | mention spike | 26 | 18.43 | 14 | 0 | wallstreetbets 26 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| SOXL | 2026-11-26 00:44 | mention spike | 63 | 41.86 | 50 | 0 | wallstreetbets 63 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5dxq0/) |
| AAPL | 2026-11-26 00:54 | mention spike | 54 | 30.57 | 30 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6t8v2m0lyd/) |
| DELL | 2026-11-24 21:15 | mention spike | 40 | 22.14 | 30 | 0 | wallstreetbets 40 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| BENF | 2026-11-25 00:43 | mention spike | 2 | 1.71 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y4yruq/comment/19t5y651znmkg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
