# Stage 1 candidates

Updated 2026-11-26T15:51:05Z by run `45852766933`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-11-26 00:54 | mention spike | 13 | 7.0 | 12 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5kdvf/comment/19t6wnyrh0mqt/) |
| SGOV | 2026-11-25 21:55 | mention spike | 18 | 7.0 | 17 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| NRSN | 2026-11-26 00:44 | mention spike | 6 | 1.0 | 5 | 0 | pennystocks 4, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5betx/) |
| SOXS | 2026-11-26 00:44 | mention spike | 3 | 8.71 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y54kwg/comment/19t6f4f9d6200/) |
| META | 2026-11-26 00:54 | mention spike | 10 | 19.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |
| SOXL | 2026-11-26 00:44 | mention spike | 24 | 47.57 | 21 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5uxr1/) |
| AAPL | 2026-11-26 00:54 | mention spike | 18 | 33.71 | 11 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| DELL | 2026-11-24 21:15 | mention spike | 7 | 27.71 | 5 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
