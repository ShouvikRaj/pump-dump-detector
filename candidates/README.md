# Stage 1 candidates

Updated 2026-11-10T01:10:09Z by run `42732801238`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-09 22:18 | mention spike | 10 | 2.14 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ASTS | 2026-11-09 22:33 | mention spike | 81 | 39.57 | 53 | 0 | wallstreetbets 81 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19see0c2s7m1v/) |
| CVS | 2026-11-09 13:52 | mention spike | 19 | 0.86 | 17 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| HIMS | 2026-11-09 21:25 | mention spike | 17 | 1.71 | 13 | 0 | wallstreetbets 17 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebwla01vtu/) |
| IVF | 2026-11-09 22:18 | mention spike | 17 | 0.57 | 17 | 0 | wallstreetbets 16, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NNN | 2026-11-09 15:04 | mention spike | 14 | 5.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sefeqdyfrl1/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1310 | 198.0 | 701 | 0 | wallstreetbets 1294, smallstreetbets 16 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs8wgz/) |
| NYT | 2026-11-09 11:01 | mention spike | 12 | 1.57 | 10 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 16 | 1.14 | 14 | 0 | wallstreetbets 9, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebk3yv28o4/) |
| ONDS | 2026-11-09 20:48 | mention spike | 10 | 3.43 | 6 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se49e8ob9nm/) |
| RKLB | 2026-11-09 21:25 | mention spike | 122 | 22.86 | 67 | 1 | wallstreetbets 122 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19seg7rsw3lgk/) |
| TTD | 2026-11-09 21:11 | mention spike | 41 | 2.0 | 27 | 0 | wallstreetbets 41 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sefi5nmas84/) |
| MSS | 2026-11-09 23:23 | mention spike | 9 | 0.14 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4f05/comment/19sec31xztmo1/) |
| AVGO | 2026-11-09 15:56 | mention spike | 22 | 12.43 | 19 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ylt/comment/19seeb52rh3gk/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
