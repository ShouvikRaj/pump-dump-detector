# Stage 1 candidates

Updated 2026-11-03T00:50:22Z by run `41554403119`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 419 | 54.71 | 211 | 1 | wallstreetbets 415, smallstreetbets 4 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1y8miv816r/) |
| AMD | 2026-11-02 21:58 | mention spike | 200 | 58.14 | 149 | 0 | wallstreetbets 198, smallstreetbets 2 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmcf27/) |
| ASTS | 2026-11-02 21:45 | mention spike | 48 | 18.0 | 38 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1xuth43dhh/) |
| LITE | 2026-11-02 21:16 | mention spike | 90 | 17.14 | 64 | 0 | wallstreetbets 90 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmcf27/) |
| MRVL | 2026-11-02 21:05 | mention spike | 107 | 18.71 | 70 | 0 | wallstreetbets 106, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmc17w/) |
| MSOS | 2026-10-31 21:03 | mention spike | 36 | 2.71 | 23 | 0 | wallstreetbets 36 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1xf6dbdp1d/) |
| MU | 2026-11-02 19:43 | mention spike | 29 | 10.0 | 10 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ud1tn9i4h/) |
| PLTR | 2026-11-02 13:09 | mention spike | 216 | 15.86 | 141 | 1 | wallstreetbets 215, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 33 | 9.43 | 17 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkmhzj/comment/19s1xa1zryg05/) |
| SMCI | 2026-11-02 18:46 | mention spike | 18 | 5.29 | 17 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 14 | 3.0 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ug506babp/) |
| HTZ | 2026-11-02 21:29 | mention spike | 9 | 4.14 | 8 | 0 | wallstreetbets 7, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 2 | 1.14 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 8 | 2.57 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1vn6vd9s02/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
