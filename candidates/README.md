# Stage 1 candidates

Updated 2026-10-27T15:06:08Z by run `40527496432`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 14 | 1.43 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpcyhs0ar/) |
| CLS | 2026-10-26 19:24 | mention spike | 45 | 1.86 | 25 | 1 | wallstreetbets 45 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqfc20pq2rl/) |
| GOOG | 2026-10-27 00:43 | mention spike | 145 | 48.71 | 85 | 1 | wallstreetbets 145 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 102 | 43.86 | 46 | 0 | wallstreetbets 102 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgqawe/comment/19rqio8eel5cz/) |
| HOOD | 2026-10-27 03:54 | mention spike | 30 | 10.0 | 21 | 0 | wallstreetbets 30 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqinuqe39mo/) |
| INOD | 2026-10-27 14:48 | mention spike | 12 | 0.0 | 6 | 0 | wallstreetbets 12 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqij0lafc74/) |
| MSFT | 2026-10-27 00:09 | mention spike | 57 | 24.0 | 50 | 0 | wallstreetbets 57 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgqawe/comment/19rqio8eel5cz/) |
| RDDT | 2026-10-26 14:04 | mention spike | 73 | 18.29 | 52 | 1 | wallstreetbets 73 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| SOFI | 2026-10-27 00:43 | mention spike | 39 | 3.14 | 33 | 0 | wallstreetbets 39 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqio3cxyt8h/) |
| ANT | 2026-10-26 13:24 | mention spike | 15 | 2.57 | 15 | 0 | wallstreetbets 15 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 5 | 1.29 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpil7scjp/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.86 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| PBR | 2026-10-26 09:22 | mention spike | 8 | 4.86 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 8 | 5.14 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| EWZ | 2026-10-26 00:21 | mention spike | 15 | 7.57 | 14 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 1 | 1.71 | 1 | 0 | wallstreetbets 1 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq76zya7xxf/) |
| COIN | 2026-10-27 00:43 | mention spike | 5 | 2.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 18 | 16.57 | 18 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 2.29 | 1 | 5 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
