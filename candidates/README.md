# Stage 1 candidates

Updated 2026-11-03T02:59:09Z by run `41568702730`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-03 00:57 | mention spike | 19 | 7.57 | 10 | 1 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| AAPL | 2026-11-02 20:10 | mention spike | 420 | 55.43 | 215 | 1 | wallstreetbets 417, smallstreetbets 3 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s23j1aflq81/) |
| AMD | 2026-11-02 21:58 | mention spike | 216 | 60.0 | 157 | 1 | wallstreetbets 215, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmcf27/) |
| ASTS | 2026-11-02 21:45 | mention spike | 51 | 17.14 | 39 | 0 | wallstreetbets 51 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s23wx4a5wqs/) |
| LITE | 2026-11-02 21:16 | mention spike | 92 | 17.14 | 65 | 0 | wallstreetbets 92 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| MRVL | 2026-11-02 21:05 | mention spike | 108 | 18.86 | 71 | 0 | wallstreetbets 107, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmc17w/) |
| MSOS | 2026-10-31 21:03 | mention spike | 38 | 2.71 | 25 | 0 | wallstreetbets 38 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkftz6/comment/19s241f4nl4kk/) |
| MU | 2026-11-02 19:43 | mention spike | 29 | 10.0 | 10 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ud1tn9i4h/) |
| PLTR | 2026-11-02 13:09 | mention spike | 221 | 16.43 | 142 | 1 | wallstreetbets 221 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 28 | 10.0 | 17 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkmhzj/comment/19s1xa1zryg05/) |
| SMCI | 2026-11-02 18:46 | mention spike | 18 | 5.29 | 17 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 16 | 3.0 | 12 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1zm3ks48ar/) |
| HTZ | 2026-11-02 21:29 | mention spike | 8 | 4.14 | 8 | 0 | wallstreetbets 6, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 1 | 1.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 9 | 2.57 | 8 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
