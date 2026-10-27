# Stage 1 candidates

Updated 2026-10-27T13:39:08Z by run `40512918380`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 12 | 1.29 | 10 | 0 | wallstreetbets 12 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp5fimt5z9g/) |
| ANT | 2026-10-26 13:24 | mention spike | 20 | 1.71 | 20 | 0 | wallstreetbets 20 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgh236/) |
| CLS | 2026-10-26 19:24 | mention spike | 46 | 1.57 | 25 | 1 | wallstreetbets 46 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf0hfrcayt/) |
| GOOG | 2026-10-27 00:43 | mention spike | 137 | 47.0 | 80 | 1 | wallstreetbets 137 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| HOOD | 2026-10-27 03:54 | mention spike | 24 | 9.14 | 18 | 0 | wallstreetbets 24 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqdlmh38fwk/) |
| MSFT | 2026-10-27 00:09 | mention spike | 55 | 23.71 | 50 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqeybxx8w3o/) |
| RDDT | 2026-10-26 14:04 | mention spike | 103 | 12.86 | 73 | 1 | wallstreetbets 103 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgd9x7/) |
| SOFI | 2026-10-27 00:43 | mention spike | 36 | 3.14 | 31 | 0 | wallstreetbets 36 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqez2v7lgg1/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 101 | 42.57 | 48 | 0 | wallstreetbets 101 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf4jjb1ldu/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 5 | 1.14 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8g8rl21tu/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.86 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| PBR | 2026-10-26 09:22 | mention spike | 10 | 4.57 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 12 | 4.29 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| EWZ | 2026-10-26 00:21 | mention spike | 18 | 7.14 | 16 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq76zya7xxf/) |
| COIN | 2026-10-27 00:43 | mention spike | 6 | 2.14 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 22 | 16.14 | 22 | 0 | wallstreetbets 21, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 12 | 2.0 | 1 | 5 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
