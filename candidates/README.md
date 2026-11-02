# Stage 1 candidates

Updated 2026-11-02T20:10:09Z by run `41514885334`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-02 07:17 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| MSOS | 2026-10-31 21:03 | mention spike | 30 | 2.29 | 20 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1kmf7lffc3/) |
| MU | 2026-11-02 19:43 | mention spike | 24 | 9.86 | 8 | 0 | wallstreetbets 24 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1k8t0s9e8z/) |
| PLTR | 2026-11-02 13:09 | mention spike | 81 | 14.57 | 64 | 0 | wallstreetbets 80, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 23 | 9.71 | 11 | 0 | wallstreetbets 23 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1kr81a9qhv/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| AAPL | 2026-11-02 20:10 | mention spike | 151 | 50.57 | 90 | 0 | wallstreetbets 147, smallstreetbets 4 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1lps3nqau9/) |
| WMT | 2026-11-02 20:10 | mention spike | 12 | 3.14 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1lint8j1wi/) |
| NNN | 2026-11-01 19:38 | mention spike | 9 | 2.14 | 7 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5apu/comment/19s1id0nnp26d/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
