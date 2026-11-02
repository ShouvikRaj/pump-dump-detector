# Stage 1 candidates

Updated 2026-11-02T20:49:07Z by run `41521301303`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 174 | 50.86 | 103 | 0 | wallstreetbets 170, smallstreetbets 4 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1ninq0byp0/) |
| ATC | 2026-11-02 07:17 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| MSOS | 2026-10-31 21:03 | mention spike | 30 | 2.29 | 20 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1kmf7lffc3/) |
| MU | 2026-11-02 19:43 | mention spike | 26 | 9.86 | 10 | 0 | wallstreetbets 26 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1n141gyzj7/) |
| PLTR | 2026-11-02 13:09 | mention spike | 91 | 14.71 | 71 | 0 | wallstreetbets 90, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 26 | 9.71 | 14 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1n141gyzj7/) |
| SMCI | 2026-11-02 18:46 | mention spike | 15 | 5.29 | 14 | 0 | wallstreetbets 15 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 13 | 3.14 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1mndjwlf8k/) |
| NNN | 2026-11-01 19:38 | mention spike | 9 | 2.14 | 7 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5apu/comment/19s1id0nnp26d/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
