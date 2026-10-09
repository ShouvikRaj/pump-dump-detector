# Stage 1 candidates

Updated 2026-10-09T18:22:28Z by run `37971365695`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 13 | 4.0 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 17 | 4.43 | 12 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1nz10/) |
| ASTS | 2026-10-08 21:11 | mention spike | 245 | 16.0 | 128 | 0 | wallstreetbets 245 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevavn6/) |
| IBM | 2026-10-09 01:09 | mention spike | 10 | 4.14 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/peulrb8/) |
| SLS | 2026-10-09 13:19 | mention spike | 14 | 3.29 | 10 | 0 | wallstreetbets 11, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1mxkk/) |
| UNH | 2026-10-09 13:59 | mention spike | 10 | 1.43 | 7 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE | #29 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| CMG | 2026-10-08 19:38 | mention spike | 9 | 2.29 | 7 | 1 | wallstreetbets 8, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| HUM | 2026-10-09 12:39 | mention spike | 8 | 1.0 | 5 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| UUUU | 2026-10-07 20:50 | mention spike | 10 | 3.71 | 8 | 0 | wallstreetbets 10 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| CIFR | 2026-10-08 21:37 | mention spike | 7 | 1.86 | 4 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| MCD | 2026-10-09 00:16 | mention spike | 23 | 10.29 | 11 | 0 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 29 | 19.71 | 21 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuu4c2/) |
| ORCL | 2026-10-08 17:11 | mention spike | 6 | 8.14 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuukns/) |
| GME | 2026-10-08 16:17 | mention spike | 23 | 15.14 | 17 | 0 | wallstreetbets 23 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1om9v/) |
| IREN | 2026-10-07 19:18 | mention spike | 13 | 7.57 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peurpuo/) |
| SKHY | 2026-10-06 18:54 | mention spike | 11 | 7.71 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peut1xp/) |
| TSM | 2026-10-09 12:39 | mention spike | 7 | 5.57 | 6 | 0 | wallstreetbets 6, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| OKLO | 2026-10-06 18:14 | mention spike | 8 | 7.57 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev5yo1/) |
| GLD | 2026-10-07 13:01 | mention spike | 7 | 6.71 | 5 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| SBUX | 2026-10-08 18:59 | mention spike | 5 | 1.57 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| BWET | 2026-10-08 15:51 | mention spike | 8 | 7.57 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuhavb/) |
| SOXL | 2026-10-09 00:30 | mention spike | 35 | 18.0 | 12 | 0 | wallstreetbets 35 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevagb5/) |
| DAL | 2026-10-09 12:52 | mention spike | 8 | 1.0 | 4 | 0 | wallstreetbets 8 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 7 | 8.14 | 5 | 0 | wallstreetbets 4, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev0qtv/) |
| ONDS | 2026-10-09 01:49 | mention spike | 7 | 4.14 | 6 | 0 | wallstreetbets 7 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| PLTR | 2026-10-08 13:12 | mention spike | 18 | 13.0 | 15 | 1 | wallstreetbets 18 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevaeed/) |
| TTWO | 2026-10-08 13:27 | mention spike | 6 | 4.43 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuubgi/) |
| USO | 2026-10-08 18:20 | mention spike | 10 | 10.14 | 4 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peukax8/) |
| KEEL | 2026-10-08 03:01 | mention spike | 2 | 4.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peur70q/) |
| APLD | 2026-10-05 14:23 | mention spike | 42 | 56.86 | 31 | 0 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 6 | 21.86 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
