# Stage 1 candidates

Updated 2026-11-22T10:25:10Z by run `45011887426`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NYT | 2026-11-22 00:48 | mention spike | 23 | 9.14 | 22 | 0 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y273h3/comment/19szo09q6zq4g/) |
| MSTR | 2026-11-22 00:48 | mention spike | 16 | 22.14 | 14 | 0 | wallstreetbets 16 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y2gl1m/) |
| CRWD | 2026-11-21 00:55 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| ORCL | 2026-11-20 17:56 | mention spike | 8 | 7.43 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19szjecd6s4lf/) |
| VWAV | 2026-11-21 00:46 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SNDK | 2026-11-21 00:46 | mention spike | 22 | 56.71 | 14 | 0 | wallstreetbets 20, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y259ja/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
