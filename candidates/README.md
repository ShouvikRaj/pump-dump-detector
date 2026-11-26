# Stage 1 candidates

Updated 2026-11-26T14:44:10Z by run `45841674560`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SGOV | 2026-11-25 21:55 | mention spike | 20 | 6.86 | 19 | 0 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| VTI | 2026-11-26 00:54 | mention spike | 15 | 6.86 | 13 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/) |
| NRSN | 2026-11-26 00:44 | mention spike | 7 | 0.86 | 6 | 0 | pennystocks 5, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5betx/) |
| SOXS | 2026-11-26 00:44 | mention spike | 5 | 8.43 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y54kwg/comment/19t6f4f9d6200/) |
| META | 2026-11-26 00:54 | mention spike | 11 | 19.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| SOXL | 2026-11-26 00:44 | mention spike | 39 | 45.43 | 34 | 0 | wallstreetbets 39 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5uxr1/) |
| AAPL | 2026-11-26 00:54 | mention spike | 30 | 32.71 | 18 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| DELL | 2026-11-24 21:15 | mention spike | 11 | 27.14 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| BENF | 2026-11-25 00:43 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
