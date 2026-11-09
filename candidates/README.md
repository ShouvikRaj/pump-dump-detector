# Stage 1 candidates

Updated 2026-11-09T01:24:28Z by run `42544346101`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 2026-11-09 00:16 | mention spike | 413 | 141.57 | 268 | 0 | wallstreetbets 409, smallstreetbets 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xre583/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
