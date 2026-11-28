# Stage 1 candidates

Updated 2026-11-28T00:38:50Z by run `46088387401`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SAP | 2026-11-28 00:38 | mention spike | 16 | 0.0 | 16 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y6tk99/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
