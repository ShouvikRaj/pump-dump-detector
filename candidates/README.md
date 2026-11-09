# Stage 1 candidates

Updated 2026-11-09T14:36:08Z by run `42634794559`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CVS | 2026-11-09 13:52 | mention spike | 11 | 1.0 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1013 | 143.86 | 552 | 0 | wallstreetbets 1003, smallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrt5lp/) |
| NYT | 2026-11-09 11:01 | mention spike | 11 | 1.0 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
