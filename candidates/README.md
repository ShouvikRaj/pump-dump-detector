# Stage 1 candidates

Updated 2026-10-26T23:20:10Z by run `40418054013`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 23 | 0.0 | 21 | 0 | wallstreetbets 23 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| CLS | 2026-10-26 19:24 | mention spike | 24 | 1.0 | 13 | 0 | wallstreetbets 24 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8i1qi8blx/) |
| EWZ | 2026-10-26 00:21 | mention spike | 59 | 0.57 | 47 | 0 | wallstreetbets 53, smallstreetbets 6 | NYSE Arca | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 38 | 0.14 | 30 | 1 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| NU | 2026-10-26 11:48 | mention spike | 19 | 0.0 | 5 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpcq1wjvjcw/) |
| PBR | 2026-10-26 09:22 | mention spike | 30 | 1.57 | 24 | 0 | wallstreetbets 27, smallstreetbets 3 | NYSE | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| RDDT | 2026-10-26 14:04 | mention spike | 79 | 12.29 | 57 | 0 | wallstreetbets 79 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpce3p56hfm/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
