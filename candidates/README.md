# Stage 1 candidates

Updated 2026-11-01T23:49:05Z by run `41363625194`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NNN | 2026-11-01 19:38 | mention spike | 13 | 0.71 | 10 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xl8bb4/) |
| MSOS | 2026-10-31 21:03 | mention spike | 4 | 2.0 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19rzzuu00t204/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
