# Stage 1 candidates

Updated 2026-11-02T23:28:07Z by run `41544573409`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 418 | 52.14 | 208 | 1 | wallstreetbets 414, smallstreetbets 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ui65xr3et/) |
| AMD | 2026-11-02 21:58 | mention spike | 192 | 57.0 | 145 | 0 | wallstreetbets 190, smallstreetbets 2 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmcf27/) |
| LITE | 2026-11-02 21:16 | mention spike | 85 | 17.14 | 61 | 0 | wallstreetbets 85 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmcf27/) |
| MRVL | 2026-11-02 21:05 | mention spike | 103 | 18.71 | 69 | 0 | wallstreetbets 102, smallstreetbets 1 | Nasdaq | #26 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmc17w/) |
| MSOS | 2026-10-31 21:03 | mention spike | 32 | 2.57 | 22 | 0 | wallstreetbets 32 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1tg9fr464l/) |
| MU | 2026-11-02 19:43 | mention spike | 30 | 9.86 | 11 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ud1tn9i4h/) |
| PLTR | 2026-11-02 13:09 | mention spike | 211 | 15.29 | 143 | 1 | wallstreetbets 210, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 33 | 9.57 | 16 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1tnw3oodmp/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 14 | 3.0 | 11 | 0 | wallstreetbets 14 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ug506babp/) |
| ASTS | 2026-11-02 21:45 | mention spike | 37 | 18.29 | 30 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1ue2bncmbn/) |
| HTZ | 2026-11-02 21:29 | mention spike | 9 | 4.14 | 8 | 0 | wallstreetbets 7, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 3 | 1.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 7 | 2.57 | 6 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1sl25iwmbk/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
