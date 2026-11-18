# Stage 1 candidates

Updated 2026-11-18T22:20:09Z by run `44410190765`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-17 23:46 | mention spike | 14 | 2.71 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| PANW | 2026-11-18 21:40 | mention spike | 22 | 2.71 | 18 | 0 | wallstreetbets 22 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su96jkt3r9h/) |
| UNH | 2026-11-18 17:15 | mention spike | 12 | 2.14 | 8 | 0 | wallstreetbets 12 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su8gt7rh1ok/) |
| SLS | 2026-11-17 12:33 | mention spike | 13 | 62.29 | 11 | 0 | wallstreetbets 10, smallstreetbets 2, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 2 | 7.0 | 1 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su91fc87qh1/) |
| HSBC | 2026-11-17 21:20 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RCAT | 2026-11-16 22:11 | mention spike | 1 | 4.71 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xzgmm7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
