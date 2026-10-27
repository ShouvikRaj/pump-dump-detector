# Stage 1 candidates

Updated 2026-10-27T14:48:09Z by run `40523107579`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 14 | 1.43 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpcyhs0ar/) |
| CLS | 2026-10-26 19:24 | mention spike | 45 | 1.86 | 25 | 1 | wallstreetbets 45 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqfc20pq2rl/) |
| GOOG | 2026-10-27 00:43 | mention spike | 143 | 48.43 | 84 | 1 | wallstreetbets 143 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 99 | 43.71 | 43 | 0 | wallstreetbets 99 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqi1h0j5tvl/) |
| MSFT | 2026-10-27 00:09 | mention spike | 55 | 24.0 | 49 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgi7gw/comment/19rqh6drqa3j4/) |
| RDDT | 2026-10-26 14:04 | mention spike | 76 | 17.57 | 55 | 1 | wallstreetbets 76 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgteg0/) |
| SOFI | 2026-10-27 00:43 | mention spike | 38 | 3.14 | 32 | 0 | wallstreetbets 38 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqgpceyuzk5/) |
| INOD | 2026-10-27 14:48 | mention spike | 11 | 0.0 | 5 | 0 | wallstreetbets 11 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhvshnyhs0/) |
| ANT | 2026-10-26 13:24 | mention spike | 15 | 2.57 | 15 | 0 | wallstreetbets 15 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| HOOD | 2026-10-27 03:54 | mention spike | 25 | 10.0 | 17 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqi091xzr7p/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 5 | 1.29 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpil7scjp/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.86 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| PBR | 2026-10-26 09:22 | mention spike | 8 | 4.86 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 7 | 5.14 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| EWZ | 2026-10-26 00:21 | mention spike | 16 | 7.43 | 15 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 1 | 1.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq76zya7xxf/) |
| COIN | 2026-10-27 00:43 | mention spike | 5 | 2.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 18 | 16.43 | 18 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 2.29 | 1 | 5 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
