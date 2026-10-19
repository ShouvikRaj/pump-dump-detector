# Stage 1 candidates

Updated 2026-10-19T03:34:45Z by run `39195292425`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-10-18 05:58 | mention spike | 10 | 3.0 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/comment/phlcwg8/) |
| SCHD | 2026-10-17 04:49 | mention spike | 5 | 6.29 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ct1y/comment/phmf0ll/) |
| NFLX | 2026-10-17 17:37 | mention spike | 9 | 9.14 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7lpd9/comment/phmd4pj/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
