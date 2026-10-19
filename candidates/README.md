# Stage 1 candidates

Updated 2026-10-19T00:31:17Z by run `39180975501`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-10-18 05:58 | mention spike | 14 | 2.43 | 12 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/comment/phlcwg8/) |
| SCHD | 2026-10-17 04:49 | mention spike | 10 | 5.14 | 8 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ct1y/comment/phlfr2j/) |
| NFLX | 2026-10-17 17:37 | mention spike | 5 | 9.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ct1y/comment/phkqequ/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
