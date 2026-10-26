# Stage 1 candidates

Updated 2026-10-26T09:48:06Z by run `40301716213`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 32 | 1.0 | 28 | 0 | wallstreetbets 26, smallstreetbets 6 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfi4le/) |
| MELI | 2026-10-26 08:42 | mention spike | 16 | 0.29 | 13 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19roc9er8b0bk/) |
| PBR | 2026-10-26 09:22 | mention spike | 14 | 1.57 | 11 | 0 | wallstreetbets 11, smallstreetbets 3 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19rocesraeoo0/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
