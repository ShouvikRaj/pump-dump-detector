# Stage 1 candidates

Updated 2026-11-26T23:51:08Z by run `45912868586`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-11-26 00:54 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca | #23 |  |
| SGOV | 2026-11-25 21:55 | mention spike | 2 | 9.14 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y66lyf/comment/19t8luxnmyxxc/) |
| NRSN | 2026-11-26 00:44 | mention spike | 1 | 1.71 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y5shjc/comment/19t7bcrd7hqv7/) |
| SOXS | 2026-11-26 00:44 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| META | 2026-11-26 00:54 | mention spike | 2 | 20.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y68xxq/) |
| SOXL | 2026-11-26 00:44 | mention spike | 2 | 49.29 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5uxr1/) |
| AAPL | 2026-11-26 00:54 | mention spike | 2 | 34.86 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y68xxq/) |
| DELL | 2026-11-24 21:15 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
