# Stage 1 candidates

Updated 2026-11-02T21:05:06Z by run `41523307952`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 188 | 51.0 | 109 | 0 | wallstreetbets 184, smallstreetbets 4 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1o5jx37xib/) |
| MSOS | 2026-10-31 21:03 | mention spike | 30 | 2.29 | 20 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1kmf7lffc3/) |
| MU | 2026-11-02 19:43 | mention spike | 27 | 9.86 | 10 | 0 | wallstreetbets 27 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1nlbnjg50j/) |
| PLTR | 2026-11-02 13:09 | mention spike | 97 | 14.71 | 72 | 0 | wallstreetbets 96, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 26 | 9.71 | 14 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1n141gyzj7/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 13 | 3.14 | 10 | 0 | wallstreetbets 13 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1mndjwlf8k/) |
| MRVL | 2026-11-02 21:05 | mention spike | 95 | 18.57 | 64 | 0 | wallstreetbets 95 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm91jm/) |
| ATC | 2026-11-02 07:17 | mention spike | 9 | 0.14 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| NNN | 2026-11-01 19:38 | mention spike | 9 | 2.14 | 7 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5apu/comment/19s1id0nnp26d/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
