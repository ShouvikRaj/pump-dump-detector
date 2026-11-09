# Stage 1 candidates

Updated 2026-11-09T23:23:08Z by run `42719041616`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-09 22:18 | mention spike | 10 | 2.14 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ASTS | 2026-11-09 22:33 | mention spike | 78 | 39.29 | 50 | 0 | wallstreetbets 78 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebbc0hf9ls/) |
| CVS | 2026-11-09 13:52 | mention spike | 18 | 0.86 | 16 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| HIMS | 2026-11-09 21:25 | mention spike | 17 | 1.71 | 13 | 0 | wallstreetbets 17 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebwla01vtu/) |
| IVF | 2026-11-09 22:18 | mention spike | 16 | 0.57 | 16 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NNN | 2026-11-09 15:04 | mention spike | 14 | 4.86 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xraj53/comment/19sdtwmumgskg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1361 | 180.86 | 720 | 0 | wallstreetbets 1344, smallstreetbets 17 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs754p/) |
| NYT | 2026-11-09 11:01 | mention spike | 14 | 1.29 | 12 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 16 | 1.14 | 14 | 0 | wallstreetbets 9, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebk3yv28o4/) |
| ONDS | 2026-11-09 20:48 | mention spike | 10 | 3.43 | 6 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se49e8ob9nm/) |
| RKLB | 2026-11-09 21:25 | mention spike | 114 | 22.86 | 61 | 1 | wallstreetbets 114 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs5j87/comment/19seaxx0shexw/) |
| TTD | 2026-11-09 21:11 | mention spike | 33 | 1.86 | 23 | 0 | wallstreetbets 33 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebm5c1p6qp/) |
| MSS | 2026-11-09 23:23 | mention spike | 10 | 0.0 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4f05/comment/19sec31xztmo1/) |
| AVGO | 2026-11-09 15:56 | mention spike | 21 | 12.43 | 18 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se9cvgmuyck/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
