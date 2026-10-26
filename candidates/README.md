# Stage 1 candidates

Updated 2026-10-26T07:23:09Z by run `40284902287`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 27 | 1.0 | 24 | 0 | wallstreetbets 22, smallstreetbets 5 | NYSE Arca | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfi4le/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
