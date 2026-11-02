# Stage 1 candidates

Updated 2026-11-02T19:03:07Z by run `41504518119`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-02 07:17 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| MSOS | 2026-10-31 21:03 | mention spike | 28 | 2.29 | 20 | 0 | wallstreetbets 28 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1hxwl0vh40/) |
| NNN | 2026-11-01 19:38 | mention spike | 10 | 2.0 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5apu/comment/19s1id0nnp26d/) |
| PLTR | 2026-11-02 13:09 | mention spike | 62 | 14.43 | 52 | 0 | wallstreetbets 61, smallstreetbets 1 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1i10feyc80/) |
| RKLB | 2026-11-02 15:08 | mention spike | 23 | 9.71 | 11 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1ift17ssx0/) |
| SMCI | 2026-11-02 18:46 | mention spike | 14 | 5.29 | 13 | 0 | wallstreetbets 14 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
