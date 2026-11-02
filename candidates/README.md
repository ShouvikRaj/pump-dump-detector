# Stage 1 candidates

Updated 2026-11-02T18:30:06Z by run `41500330007`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-02 07:17 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| MSOS | 2026-10-31 21:03 | mention spike | 26 | 2.29 | 19 | 0 | wallstreetbets 26 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1gi1o84ew1/) |
| NNN | 2026-11-01 19:38 | mention spike | 10 | 1.86 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1d5xwhoqci/) |
| PLTR | 2026-11-02 13:09 | mention spike | 60 | 14.29 | 50 | 0 | wallstreetbets 59, smallstreetbets 1 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1himm9ok0z/) |
| RKLB | 2026-11-02 15:08 | mention spike | 22 | 9.71 | 10 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1h20agigkh/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
