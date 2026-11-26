# Stage 1 candidates

Updated 2026-11-26T17:27:08Z by run `45867071480`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-11-26 00:54 | mention spike | 7 | 7.86 | 7 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5kdvf/comment/19t6wnyrh0mqt/) |
| SGOV | 2026-11-25 21:55 | mention spike | 8 | 8.14 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| NRSN | 2026-11-26 00:44 | mention spike | 2 | 1.57 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y5shjc/comment/19t7bcrd7hqv7/) |
| SOXS | 2026-11-26 00:44 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| META | 2026-11-26 00:54 | mention spike | 5 | 20.43 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5yin6/comment/19t85e0anl0cl/) |
| SOXL | 2026-11-26 00:44 | mention spike | 12 | 49.0 | 11 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5uxr1/) |
| AAPL | 2026-11-26 00:54 | mention spike | 11 | 34.29 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7cyzeapkh1/) |
| DELL | 2026-11-24 21:15 | mention spike | 2 | 28.43 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5io1f/comment/19t6uk9zz4wmb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
