# Stage 1 candidates

Updated 2026-10-27T14:37:09Z by run `40520974658`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 13 | 1.29 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqgjthgyyyt/) |
| ANT | 2026-10-26 13:24 | mention spike | 18 | 2.14 | 18 | 0 | wallstreetbets 18 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| CLS | 2026-10-26 19:24 | mention spike | 45 | 1.86 | 25 | 1 | wallstreetbets 45 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqfc20pq2rl/) |
| GOOG | 2026-10-27 00:43 | mention spike | 141 | 48.43 | 82 | 1 | wallstreetbets 141 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| MSFT | 2026-10-27 00:09 | mention spike | 55 | 24.0 | 49 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgi7gw/comment/19rqh6drqa3j4/) |
| RDDT | 2026-10-26 14:04 | mention spike | 77 | 17.14 | 56 | 1 | wallstreetbets 77 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgteg0/) |
| SOFI | 2026-10-27 00:43 | mention spike | 38 | 3.14 | 32 | 0 | wallstreetbets 38 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqgpceyuzk5/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 97 | 43.71 | 42 | 0 | wallstreetbets 97 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqh1lt46ohu/) |
| HOOD | 2026-10-27 03:54 | mention spike | 19 | 10.0 | 15 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhgvyad7k0/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 5 | 1.14 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8g8rl21tu/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.86 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| PBR | 2026-10-26 09:22 | mention spike | 8 | 4.86 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 7 | 5.14 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| EWZ | 2026-10-26 00:21 | mention spike | 16 | 7.43 | 15 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 1 | 1.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rq76zya7xxf/) |
| COIN | 2026-10-27 00:43 | mention spike | 5 | 2.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 18 | 16.43 | 18 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 2.29 | 1 | 5 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
