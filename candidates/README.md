# Stage 1 candidates

Updated 2026-11-27T01:38:31Z by run `45923118597`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-11-26 00:54 | mention spike | 3 | 9.29 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5anxn/comment/19t7dty9hzk69/) |
| SGOV | 2026-11-25 21:55 | mention spike | 2 | 9.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y66lyf/comment/19t8luxnmyxxc/) |
| NRSN | 2026-11-26 00:44 | mention spike | 2 | 2.14 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y6grk8/) |
| SOXS | 2026-11-26 00:44 | mention spike | 3 | 9.29 | 3 | 0 | wallstreetbets 3 | NYSE Arca | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5yin6/comment/19t82niyhi8eb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
