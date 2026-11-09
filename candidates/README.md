# Stage 1 candidates

Updated 2026-11-09T11:01:09Z by run `42604791590`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 2026-11-09 00:16 | mention spike | 775 | 142.86 | 447 | 0 | wallstreetbets 768, smallstreetbets 7 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrmwf3/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 1.14 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xr90c7/comment/19sdex1i7co84/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
