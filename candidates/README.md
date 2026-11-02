# Stage 1 candidates

Updated 2026-11-02T21:45:08Z by run `41529424705`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 275 | 51.29 | 153 | 1 | wallstreetbets 271, smallstreetbets 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pyos9akg3/) |
| HTZ | 2026-11-02 21:29 | mention spike | 10 | 4.0 | 9 | 0 | wallstreetbets 8, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| LITE | 2026-11-02 21:16 | mention spike | 82 | 17.14 | 58 | 0 | wallstreetbets 82 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm91jm/) |
| MRVL | 2026-11-02 21:05 | mention spike | 97 | 18.71 | 67 | 0 | wallstreetbets 97 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm91jm/) |
| MSOS | 2026-10-31 21:03 | mention spike | 31 | 2.29 | 21 | 0 | wallstreetbets 31 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1o96v3ujc2/) |
| MU | 2026-11-02 19:43 | mention spike | 28 | 9.86 | 11 | 0 | wallstreetbets 28 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1p5z0kl7ur/) |
| PLTR | 2026-11-02 13:09 | mention spike | 172 | 14.86 | 119 | 1 | wallstreetbets 171, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 28 | 9.57 | 14 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pjz2n7mys/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 13 | 3.0 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1mndjwlf8k/) |
| ASTS | 2026-11-02 21:45 | mention spike | 41 | 17.86 | 31 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pyqnc2epw/) |
| ATC | 2026-11-02 07:17 | mention spike | 9 | 0.14 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 7 | 2.43 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5apu/comment/19s1id0nnp26d/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
