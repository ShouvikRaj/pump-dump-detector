# Stage 1 candidates

Updated 2026-11-26T00:44:35Z by run `45729421991`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 2026-11-24 21:15 | mention spike | 56 | 8.71 | 36 | 0 | wallstreetbets 56 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| SGOV | 2026-11-25 21:55 | mention spike | 21 | 6.14 | 20 | 0 | wallstreetbets 21 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y56p4r/) |
| NRSN | 2026-11-26 00:44 | mention spike | 12 | 0.0 | 10 | 0 | pennystocks 8, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5betx/) |
| SOXL | 2026-11-26 00:44 | mention spike | 78 | 37.14 | 57 | 0 | wallstreetbets 78 | NYSE Arca | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y5dxq0/) |
| SOXS | 2026-11-26 00:44 | mention spike | 18 | 6.71 | 15 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4wo51/) |
| BENF | 2026-11-25 00:43 | mention spike | 2 | 1.71 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y4yruq/comment/19t5y651znmkg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
