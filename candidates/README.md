# Stage 1 candidates

Updated 2026-11-09T06:24:07Z by run `42572100283`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 2026-11-09 00:16 | mention spike | 639 | 143.29 | 388 | 0 | wallstreetbets 633, smallstreetbets 6 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrjiih/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
