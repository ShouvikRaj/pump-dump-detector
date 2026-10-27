# Stage 1 candidates

Updated 2026-10-27T00:27:41Z by run `40425504522`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 25 | 0.0 | 23 | 0 | wallstreetbets 25 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| CLS | 2026-10-26 19:24 | mention spike | 28 | 1.0 | 14 | 1 | wallstreetbets 28 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpfee8s4pmq/) |
| EWZ | 2026-10-26 00:21 | mention spike | 46 | 2.43 | 39 | 0 | wallstreetbets 45, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 38 | 0.14 | 30 | 1 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MSFT | 2026-10-27 00:09 | mention spike | 40 | 23.43 | 38 | 0 | wallstreetbets 40 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg11cu/comment/19rpe8z4woe01/) |
| PBR | 2026-10-26 09:22 | mention spike | 27 | 2.0 | 22 | 0 | wallstreetbets 27 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| RDDT | 2026-10-26 14:04 | mention spike | 85 | 12.29 | 62 | 1 | wallstreetbets 85 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgd9x7/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |
| NU | 2026-10-26 11:48 | mention spike | 16 | 0.43 | 2 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpcq1wjvjcw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
