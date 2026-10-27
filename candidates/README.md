# Stage 1 candidates

Updated 2026-10-27T02:38:09Z by run `40438786072`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMKR | 2026-10-27 00:43 | mention spike | 12 | 1.29 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp5fimt5z9g/) |
| ANT | 2026-10-26 13:24 | mention spike | 28 | 0.0 | 26 | 0 | wallstreetbets 28 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| CLS | 2026-10-26 19:24 | mention spike | 39 | 1.0 | 20 | 1 | wallstreetbets 39 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rpkavwyjpwi/) |
| COIN | 2026-10-27 00:43 | mention spike | 10 | 1.43 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfvymh/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 10 | 0.43 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8g8rl21tu/) |
| EWZ | 2026-10-26 00:21 | mention spike | 39 | 4.0 | 33 | 0 | wallstreetbets 38, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| GOOG | 2026-10-27 00:43 | mention spike | 117 | 46.86 | 68 | 0 | wallstreetbets 117 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgcr1g/) |
| MELI | 2026-10-26 08:42 | mention spike | 36 | 0.86 | 27 | 1 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| MSFT | 2026-10-27 00:09 | mention spike | 48 | 23.0 | 43 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgfee1/comment/19rpl7gg968n4/) |
| PBR | 2026-10-26 09:22 | mention spike | 26 | 2.14 | 22 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgavgk/) |
| RDDT | 2026-10-26 14:04 | mention spike | 95 | 12.29 | 67 | 1 | wallstreetbets 95 | NYSE | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgd9x7/) |
| RIVN | 2026-10-27 00:43 | mention spike | 24 | 5.57 | 7 | 0 | wallstreetbets 24 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rplkqmhxscj/) |
| SOFI | 2026-10-27 00:43 | mention spike | 10 | 3.0 | 8 | 0 | wallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpdfcgnmtol/) |
| STNE | 2026-10-26 13:24 | mention spike | 12 | 0.0 | 6 | 0 | wallstreetbets 12 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |
| VOO | 2026-10-27 02:38 | mention spike | 29 | 14.57 | 26 | 0 | wallstreetbets 28, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xg1dh7/) |
| NU | 2026-10-26 11:48 | mention spike | 17 | 0.57 | 1 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rpcq1wjvjcw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
