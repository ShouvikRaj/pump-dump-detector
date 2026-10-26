# Stage 1 candidates

Updated 2026-10-26T09:35:07Z by run `40299999152`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 32 | 1.0 | 28 | 0 | wallstreetbets 26, smallstreetbets 6 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfi4le/) |
| MELI | 2026-10-26 08:42 | mention spike | 15 | 0.29 | 13 | 0 | wallstreetbets 15 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19roc2214g600/) |
| PBR | 2026-10-26 09:22 | mention spike | 12 | 1.57 | 9 | 0 | wallstreetbets 9, smallstreetbets 3 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19roc2214g600/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
