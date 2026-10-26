# Stage 1 candidates

Updated 2026-10-26T09:22:08Z by run `40298298162`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 31 | 1.0 | 27 | 0 | wallstreetbets 25, smallstreetbets 6 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfi4le/) |
| MELI | 2026-10-26 08:42 | mention spike | 14 | 0.29 | 12 | 0 | wallstreetbets 14 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfpzai/comment/19rob3465nyde/) |
| PBR | 2026-10-26 09:22 | mention spike | 10 | 1.57 | 8 | 0 | wallstreetbets 7, smallstreetbets 3 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19robgg6uq3j9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
