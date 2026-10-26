# Stage 1 candidates

Updated 2026-10-26T10:51:08Z by run `40310381213`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 35 | 0.86 | 31 | 0 | wallstreetbets 29, smallstreetbets 6 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfi4le/) |
| MELI | 2026-10-26 08:42 | mention spike | 18 | 0.14 | 14 | 0 | wallstreetbets 18 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19rod29yuanaa/) |
| PBR | 2026-10-26 09:22 | mention spike | 15 | 1.57 | 11 | 0 | wallstreetbets 12, smallstreetbets 3 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfc7de/comment/19rocrj62tun7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
