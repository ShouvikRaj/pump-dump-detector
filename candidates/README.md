# Stage 1 candidates

Updated 2026-11-09T15:04:07Z by run `42639113159`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CVS | 2026-11-09 13:52 | mention spike | 12 | 1.0 | 11 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1126 | 143.71 | 611 | 0 | wallstreetbets 1115, smallstreetbets 11 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrtr5l/) |
| NYT | 2026-11-09 11:01 | mention spike | 11 | 1.0 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| NNN | 2026-11-09 15:04 | mention spike | 13 | 5.57 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19sdnwg3fl31e/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
