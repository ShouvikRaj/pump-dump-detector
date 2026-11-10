# Stage 1 candidates

Updated 2026-11-10T02:40:08Z by run `42743745493`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-09 22:18 | mention spike | 10 | 2.14 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ASTS | 2026-11-09 22:33 | mention spike | 84 | 39.71 | 55 | 0 | wallstreetbets 84 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpjj4e/comment/19seku7m42b1c/) |
| CVS | 2026-11-09 13:52 | mention spike | 18 | 1.14 | 16 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sei8viswold/) |
| HIMS | 2026-11-09 21:25 | mention spike | 17 | 1.71 | 13 | 0 | wallstreetbets 17 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebwla01vtu/) |
| IVF | 2026-11-09 22:18 | mention spike | 17 | 0.57 | 17 | 0 | wallstreetbets 16, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NNN | 2026-11-09 15:04 | mention spike | 14 | 5.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sefeqdyfrl1/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1249 | 212.0 | 683 | 0 | wallstreetbets 1233, smallstreetbets 16 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsaj5s/) |
| NYT | 2026-11-09 11:01 | mention spike | 11 | 1.86 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 16 | 1.14 | 14 | 0 | wallstreetbets 9, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebk3yv28o4/) |
| RKLB | 2026-11-09 21:25 | mention spike | 123 | 22.14 | 68 | 1 | wallstreetbets 123 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sehhk7flyzo/) |
| TTD | 2026-11-09 21:11 | mention spike | 42 | 2.0 | 28 | 0 | wallstreetbets 42 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sei2raj6cf9/) |
| ONDS | 2026-11-09 20:48 | mention spike | 9 | 3.71 | 6 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sejep6ua8gy/) |
| MSS | 2026-11-09 23:23 | mention spike | 7 | 0.43 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4f05/comment/19sec31xztmo1/) |
| AVGO | 2026-11-09 15:56 | mention spike | 20 | 12.29 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ylt/comment/19seeb52rh3gk/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
