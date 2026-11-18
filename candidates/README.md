# Stage 1 candidates

Updated 2026-11-18T21:30:06Z by run `44401186526`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-17 23:46 | mention spike | 14 | 2.71 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| UNH | 2026-11-18 17:15 | mention spike | 11 | 2.14 | 8 | 0 | wallstreetbets 11 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stx62yn4z7n/) |
| SLS | 2026-11-17 12:33 | mention spike | 16 | 61.86 | 13 | 0 | wallstreetbets 11, smallstreetbets 3, pennystocks 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 1 | 7.0 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwoi0t4abn/) |
| HSBC | 2026-11-17 21:20 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RCAT | 2026-11-16 22:11 | mention spike | 1 | 4.71 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xzgmm7/) |
| VOO | 2026-11-17 00:31 | mention spike | 5 | 17.29 | 5 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwe2hbffb7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
