# Stage 1 candidates

Updated 2026-11-22T23:14:08Z by run `45081619045`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NYT | 2026-11-22 00:48 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| MSTR | 2026-11-22 00:48 | mention spike | 2 | 22.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y2gl1m/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
