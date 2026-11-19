# Stage 1 candidates

Updated 2026-11-19T00:09:06Z by run `44425965489`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| PANW | 2026-11-18 21:40 | mention spike | 23 | 2.71 | 19 | 0 | wallstreetbets 23 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sueijzmvk5g/) |
| UNH | 2026-11-18 17:15 | mention spike | 12 | 2.14 | 8 | 0 | wallstreetbets 12 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su8gt7rh1ok/) |
| AAOI | 2026-11-17 23:46 | mention spike | 2 | 4.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 9 | 62.86 | 8 | 0 | wallstreetbets 7, pennystocks 1, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 2 | 7.0 | 1 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su91fc87qh1/) |
| HSBC | 2026-11-17 21:20 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
