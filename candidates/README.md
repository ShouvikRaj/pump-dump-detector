# Stage 1 candidates

Updated 2026-11-27T12:01:08Z by run `45994413552`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-11-26 00:54 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| SGOV | 2026-11-25 21:55 | mention spike | 1 | 9.57 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y66lyf/comment/19t8luxnmyxxc/) |
| NRSN | 2026-11-26 00:44 | mention spike | 3 | 2.29 | 3 | 0 | pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y6grk8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
