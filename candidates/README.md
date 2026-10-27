# Stage 1 candidates

Updated 2026-10-27T16:48:08Z by run `40542863893`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 14 | 1.43 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpcyhs0ar/) |
| CLS | 2026-10-26 19:24 | mention spike | 46 | 1.86 | 26 | 1 | wallstreetbets 46 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqkq67n3mv6/) |
| GOOG | 2026-10-27 00:43 | mention spike | 138 | 50.57 | 81 | 1 | wallstreetbets 138 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 98 | 44.71 | 48 | 0 | wallstreetbets 98 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqm8gx1djlw/) |
| HOOD | 2026-10-27 03:54 | mention spike | 34 | 9.71 | 25 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqmqbx3o5mr/) |
| INOD | 2026-10-27 14:48 | mention spike | 15 | 0.0 | 7 | 0 | wallstreetbets 15 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqm0jp9975w/) |
| MSFT | 2026-10-27 00:09 | mention spike | 49 | 25.29 | 45 | 0 | wallstreetbets 49 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rql4chldfno/) |
| RDDT | 2026-10-26 14:04 | mention spike | 67 | 19.71 | 45 | 1 | wallstreetbets 67 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| RIVN | 2026-10-27 00:43 | mention spike | 22 | 5.29 | 5 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| SOFI | 2026-10-27 00:43 | mention spike | 46 | 3.14 | 37 | 0 | wallstreetbets 46 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqmhi882n41/) |
| ANT | 2026-10-26 13:24 | mention spike | 15 | 2.86 | 15 | 0 | wallstreetbets 15 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 4 | 1.43 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqhpil7scjp/) |
| PBR | 2026-10-26 09:22 | mention spike | 8 | 4.86 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MELI | 2026-10-26 08:42 | mention spike | 7 | 5.43 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| EWZ | 2026-10-26 00:21 | mention spike | 9 | 8.43 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqev9w6jf5w/) |
| STNE | 2026-10-26 13:24 | mention spike | 2 | 1.71 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqko5wd67pg/) |
| COIN | 2026-10-27 00:43 | mention spike | 4 | 2.43 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqc950zqglh/) |
| VOO | 2026-10-27 02:38 | mention spike | 17 | 16.57 | 17 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqiov8rwtq9/) |
| NU | 2026-10-26 11:48 | mention spike | 7 | 2.71 | 1 | 5 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgodye/comment/19rqf3uemth1c/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
