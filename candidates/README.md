# Stage 1 candidates

Updated 2026-11-24T00:28:09Z by run `45296626001`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SMCI | 2026-11-23 00:51 | mention spike | 1 | 8.14 | 1 | 0 | smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y3l69h/comment/19t2ww7qh2bfn/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
