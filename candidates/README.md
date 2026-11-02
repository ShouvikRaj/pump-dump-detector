# Stage 1 candidates

Updated 2026-11-02T22:33:09Z by run `41537308782`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 342 | 51.29 | 184 | 1 | wallstreetbets 338, smallstreetbets 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1s9gxjgjr7/) |
| AMD | 2026-11-02 21:58 | mention spike | 163 | 57.0 | 121 | 0 | wallstreetbets 162, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmb4ap/) |
| LITE | 2026-11-02 21:16 | mention spike | 83 | 17.14 | 59 | 0 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm91jm/) |
| MRVL | 2026-11-02 21:05 | mention spike | 99 | 18.71 | 67 | 0 | wallstreetbets 99 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm91jm/) |
| MSOS | 2026-10-31 21:03 | mention spike | 30 | 2.57 | 20 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1q8cz79729/) |
| MU | 2026-11-02 19:43 | mention spike | 29 | 9.86 | 11 | 0 | wallstreetbets 29 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1sawuqz6rk/) |
| PLTR | 2026-11-02 13:09 | mention spike | 188 | 15.14 | 128 | 1 | wallstreetbets 187, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 28 | 9.57 | 14 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pjz2n7mys/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 13 | 3.0 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1mndjwlf8k/) |
| ASTS | 2026-11-02 21:45 | mention spike | 37 | 18.14 | 29 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pyqnc2epw/) |
| HTZ | 2026-11-02 21:29 | mention spike | 9 | 4.14 | 8 | 0 | wallstreetbets 7, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 6 | 0.57 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 7 | 2.43 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5apu/comment/19s1id0nnp26d/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
