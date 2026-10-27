# Stage 1 candidates

Updated 2026-10-27T14:10:11Z by run `40516874607`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 12 | 1.29 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp5fimt5z9g/) |
| ANT | 2026-10-26 13:24 | mention spike | 19 | 2.0 | 19 | 0 | wallstreetbets 19 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| CLS | 2026-10-26 19:24 | mention spike | 46 | 1.71 | 25 | 1 | wallstreetbets 46 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqfc20pq2rl/) |
| GOOG | 2026-10-27 00:43 | mention spike | 140 | 48.29 | 82 | 1 | wallstreetbets 140 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| MSFT | 2026-10-27 00:09 | mention spike | 55 | 23.86 | 49 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqg6fu8aumb/) |
| RDDT | 2026-10-26 14:04 | mention spike | 79 | 16.57 | 57 | 1 | wallstreetbets 79 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgd9x7/) |
| SOFI | 2026-10-27 00:43 | mention spike | 37 | 3.14 | 32 | 0 | wallstreetbets 37 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqg1ror4dq9/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 93 | 43.86 | 42 | 0 | wallstreetbets 93 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqg90v6x1tw/) |
| HOOD | 2026-10-27 03:54 | mention spike | 21 | 9.57 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqg655p6kcg/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 5 | 1.14 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8g8rl21tu/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.86 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| PBR | 2026-10-26 09:22 | mention spike | 8 | 4.86 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 9 | 4.71 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| EWZ | 2026-10-26 00:21 | mention spike | 16 | 7.43 | 15 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 1 | 1.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq76zya7xxf/) |
| COIN | 2026-10-27 00:43 | mention spike | 5 | 2.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 20 | 16.14 | 20 | 0 | wallstreetbets 19, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 2.29 | 1 | 5 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
