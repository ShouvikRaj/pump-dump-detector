# Stage 1 candidates

Updated 2026-11-16T16:34:09Z by run `43907968344`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| HOOD | 2026-11-16 15:08 | mention spike | 12 | 3.86 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq8tr43bav8/) |
| WMT | 2026-11-16 07:17 | mention spike | 17 | 3.71 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqasag026ro/) |
| ANT | 2026-11-16 16:34 | mention spike | 132 | 67.57 | 94 | 1 | wallstreetbets 129, smallstreetbets 2, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxfkdl/) |
| ASML | 2026-11-15 23:05 | mention spike | 2 | 8.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 9 | 6.0 | 8 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqaftg7cy4g/) |
| MSTR | 2026-11-13 06:20 | mention spike | 23 | 12.0 | 16 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqbgpm8hwht/) |
| COIN | 2026-11-15 21:05 | mention spike | 8 | 1.86 | 7 | 0 | wallstreetbets 8 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqawe2cja9u/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
