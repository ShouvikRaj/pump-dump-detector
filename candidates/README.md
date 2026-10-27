# Stage 1 candidates

Updated 2026-10-27T10:33:07Z by run `40488544347`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 12 | 1.29 | 10 | 0 | wallstreetbets 12 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp5fimt5z9g/) |
| ANT | 2026-10-26 13:24 | mention spike | 30 | 0.0 | 28 | 0 | wallstreetbets 30 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgh236/) |
| CLS | 2026-10-26 19:24 | mention spike | 41 | 1.0 | 21 | 1 | wallstreetbets 41 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rps251q9cqo/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 10 | 0.43 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8g8rl21tu/) |
| GOOG | 2026-10-27 00:43 | mention spike | 121 | 46.14 | 69 | 0 | wallstreetbets 121 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| HOOD | 2026-10-27 03:54 | mention spike | 22 | 8.86 | 17 | 0 | wallstreetbets 22 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq6dcqs788y/) |
| MELI | 2026-10-26 08:42 | mention spike | 23 | 2.71 | 19 | 1 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MSFT | 2026-10-27 00:09 | mention spike | 48 | 23.43 | 43 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpw24l2s3ib/) |
| PBR | 2026-10-26 09:22 | mention spike | 19 | 3.43 | 16 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| RDDT | 2026-10-26 14:04 | mention spike | 101 | 12.14 | 73 | 1 | wallstreetbets 101 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgd9x7/) |
| RIVN | 2026-10-27 00:43 | mention spike | 24 | 5.57 | 7 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| SOFI | 2026-10-27 00:43 | mention spike | 12 | 3.0 | 10 | 0 | wallstreetbets 12 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rq2a96a4lac/) |
| EWZ | 2026-10-26 00:21 | mention spike | 28 | 5.57 | 22 | 0 | wallstreetbets 28 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| STNE | 2026-10-26 13:24 | mention spike | 6 | 0.86 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |
| COIN | 2026-10-27 00:43 | mention spike | 7 | 1.86 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfvymh/) |
| VOO | 2026-10-27 02:38 | mention spike | 24 | 15.86 | 22 | 0 | wallstreetbets 23, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 13 | 1.14 | 1 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpcq1wjvjcw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
