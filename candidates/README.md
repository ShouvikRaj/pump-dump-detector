# Stage 1 candidates

Updated 2026-10-27T00:43:06Z by run `40426924197`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 28 | 0.0 | 26 | 0 | wallstreetbets 28 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| CLS | 2026-10-26 19:24 | mention spike | 37 | 1.0 | 19 | 1 | wallstreetbets 37 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpfee8s4pmq/) |
| EWZ | 2026-10-26 00:21 | mention spike | 48 | 2.71 | 42 | 0 | wallstreetbets 47, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 40 | 0.29 | 30 | 1 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MSFT | 2026-10-27 00:09 | mention spike | 46 | 23.43 | 42 | 0 | wallstreetbets 46 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg11cu/comment/19rpe8z4woe01/) |
| PBR | 2026-10-26 09:22 | mention spike | 27 | 2.0 | 22 | 0 | wallstreetbets 27 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| RDDT | 2026-10-26 14:04 | mention spike | 88 | 12.29 | 64 | 1 | wallstreetbets 88 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgd9x7/) |
| STNE | 2026-10-26 13:24 | mention spike | 12 | 0.0 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |
| AMKR | 2026-10-27 00:43 | mention spike | 12 | 1.29 | 10 | 0 | wallstreetbets 12 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp5fimt5z9g/) |
| COIN | 2026-10-27 00:43 | mention spike | 10 | 1.43 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfvymh/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 10 | 0.43 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8g8rl21tu/) |
| GOOG | 2026-10-27 00:43 | mention spike | 115 | 46.86 | 66 | 0 | wallstreetbets 115 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| RIVN | 2026-10-27 00:43 | mention spike | 23 | 5.43 | 8 | 0 | wallstreetbets 23 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpfy6zjv7ic/) |
| SOFI | 2026-10-27 00:43 | mention spike | 10 | 3.0 | 8 | 0 | wallstreetbets 10 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpdfcgnmtol/) |
| NU | 2026-10-26 11:48 | mention spike | 18 | 0.43 | 2 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpcq1wjvjcw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
