# Stage 1 candidates

Updated 2026-11-01T21:10:05Z by run `41350236204`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NNN | 2026-11-01 19:38 | mention spike | 11 | 0.71 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xl8bb4/) |
| MSOS | 2026-10-31 21:03 | mention spike | 3 | 1.86 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkftz6/comment/19rzm1x4mrgbo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
