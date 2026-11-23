# Stage 1 candidates

Updated 2026-11-23T13:50:06Z by run `45186986813`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SMCI | 2026-11-23 00:51 | mention spike | 2 | 8.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19t16yy4g06dh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
