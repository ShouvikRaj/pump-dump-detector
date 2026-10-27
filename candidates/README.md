# Stage 1 candidates

Updated 2026-10-27T15:33:08Z by run `40531904307`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 14 | 1.43 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpcyhs0ar/) |
| CLS | 2026-10-26 19:24 | mention spike | 45 | 1.86 | 25 | 1 | wallstreetbets 45 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqfc20pq2rl/) |
| GOOG | 2026-10-27 00:43 | mention spike | 146 | 48.57 | 86 | 1 | wallstreetbets 146 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 102 | 44.0 | 47 | 0 | wallstreetbets 102 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqjm771odxd/) |
| HOOD | 2026-10-27 03:54 | mention spike | 34 | 9.71 | 24 | 0 | wallstreetbets 34 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqjmij4l7k1/) |
| INOD | 2026-10-27 14:48 | mention spike | 12 | 0.0 | 6 | 0 | wallstreetbets 12 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqij0lafc74/) |
| MSFT | 2026-10-27 00:09 | mention spike | 57 | 23.86 | 50 | 0 | wallstreetbets 57 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgqawe/comment/19rqio8eel5cz/) |
| RDDT | 2026-10-26 14:04 | mention spike | 69 | 19.0 | 48 | 1 | wallstreetbets 69 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.71 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| SOFI | 2026-10-27 00:43 | mention spike | 40 | 3.29 | 33 | 0 | wallstreetbets 40 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqj5ih0igsk/) |
| ANT | 2026-10-26 13:24 | mention spike | 15 | 2.71 | 15 | 0 | wallstreetbets 15 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 5 | 1.29 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpil7scjp/) |
| PBR | 2026-10-26 09:22 | mention spike | 8 | 4.86 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 9 | 5.14 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| EWZ | 2026-10-26 00:21 | mention spike | 13 | 7.86 | 13 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 1 | 1.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq76zya7xxf/) |
| COIN | 2026-10-27 00:43 | mention spike | 5 | 2.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 19 | 16.57 | 19 | 0 | wallstreetbets 18, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 8 | 2.57 | 1 | 5 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
