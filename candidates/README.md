# Stage 1 candidates

Updated 2026-11-02T22:59:08Z by run `41540986576`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 410 | 51.43 | 206 | 1 | wallstreetbets 406, smallstreetbets 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1tgzewuoe9/) |
| AMD | 2026-11-02 21:58 | mention spike | 180 | 57.0 | 135 | 0 | wallstreetbets 178, smallstreetbets 2 | Nasdaq | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmc17w/) |
| LITE | 2026-11-02 21:16 | mention spike | 84 | 17.14 | 60 | 0 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm91jm/) |
| MRVL | 2026-11-02 21:05 | mention spike | 102 | 18.71 | 69 | 0 | wallstreetbets 101, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmc17w/) |
| MSOS | 2026-10-31 21:03 | mention spike | 32 | 2.57 | 22 | 0 | wallstreetbets 32 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1tg9fr464l/) |
| MU | 2026-11-02 19:43 | mention spike | 29 | 9.86 | 11 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1sawuqz6rk/) |
| PLTR | 2026-11-02 13:09 | mention spike | 206 | 15.14 | 142 | 1 | wallstreetbets 205, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 29 | 9.57 | 14 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1su9gxbbb8/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 13 | 3.0 | 10 | 0 | wallstreetbets 13 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1mndjwlf8k/) |
| ASTS | 2026-11-02 21:45 | mention spike | 36 | 18.29 | 29 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pyqnc2epw/) |
| HTZ | 2026-11-02 21:29 | mention spike | 9 | 4.14 | 8 | 0 | wallstreetbets 7, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 3 | 1.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 8 | 2.43 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1sl25iwmbk/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
