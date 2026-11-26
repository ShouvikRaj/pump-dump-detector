# Stage 1 candidates

Updated 2026-11-26T10:20:08Z by run `45799534271`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NRSN | 2026-11-26 00:44 | mention spike | 13 | 0.0 | 11 | 0 | pennystocks 9, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5betx/) |
| SGOV | 2026-11-25 21:55 | mention spike | 24 | 6.29 | 23 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y56p4r/) |
| VTI | 2026-11-26 00:54 | mention spike | 16 | 7.0 | 14 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/) |
| SOXS | 2026-11-26 00:44 | mention spike | 6 | 8.57 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y54kwg/comment/19t6f4f9d6200/) |
| META | 2026-11-26 00:54 | mention spike | 19 | 19.14 | 13 | 0 | wallstreetbets 19 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| SOXL | 2026-11-26 00:44 | mention spike | 46 | 45.0 | 40 | 0 | wallstreetbets 46 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5uxr1/) |
| AAPL | 2026-11-26 00:54 | mention spike | 50 | 30.71 | 27 | 0 | wallstreetbets 50 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| DELL | 2026-11-24 21:15 | mention spike | 24 | 25.29 | 21 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| BENF | 2026-11-25 00:43 | mention spike | 2 | 1.71 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y4yruq/comment/19t5y651znmkg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
