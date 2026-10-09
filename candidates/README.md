# Stage 1 candidates

Updated 2026-10-09T17:16:27Z by run `37963582450`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 14 | 3.86 | 10 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 18 | 4.29 | 13 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1nz10/) |
| ASTS | 2026-10-08 21:11 | mention spike | 251 | 15.29 | 131 | 0 | wallstreetbets 251 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.86 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| HUM | 2026-10-09 12:39 | mention spike | 11 | 0.57 | 5 | 0 | wallstreetbets 11 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| IBM | 2026-10-09 01:09 | mention spike | 10 | 4.14 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/peulrb8/) |
| SLS | 2026-10-09 13:19 | mention spike | 14 | 3.29 | 10 | 0 | wallstreetbets 11, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1mxkk/) |
| UNH | 2026-10-09 13:59 | mention spike | 11 | 1.29 | 8 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| UUUU | 2026-10-07 20:50 | mention spike | 12 | 3.43 | 10 | 0 | wallstreetbets 12 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| CIFR | 2026-10-08 21:37 | mention spike | 9 | 1.71 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| MCD | 2026-10-09 00:16 | mention spike | 26 | 10.29 | 12 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 40 | 18.57 | 26 | 0 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuu4c2/) |
| ORCL | 2026-10-08 17:11 | mention spike | 15 | 7.0 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuukns/) |
| GME | 2026-10-08 16:17 | mention spike | 28 | 14.43 | 21 | 1 | wallstreetbets 28 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1om9v/) |
| IREN | 2026-10-07 19:18 | mention spike | 15 | 7.43 | 11 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peurpuo/) |
| SKHY | 2026-10-06 18:54 | mention spike | 12 | 8.0 | 7 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peut1xp/) |
| TSM | 2026-10-09 12:39 | mention spike | 8 | 5.43 | 6 | 0 | wallstreetbets 7, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| OKLO | 2026-10-06 18:14 | mention spike | 8 | 7.57 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev5yo1/) |
| GLD | 2026-10-07 13:01 | mention spike | 8 | 6.57 | 6 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| SBUX | 2026-10-08 18:59 | mention spike | 8 | 1.14 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| BWET | 2026-10-08 15:51 | mention spike | 10 | 7.43 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuhavb/) |
| SOXL | 2026-10-09 00:30 | mention spike | 39 | 17.86 | 13 | 0 | wallstreetbets 39 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevagb5/) |
| DAL | 2026-10-09 12:52 | mention spike | 8 | 1.0 | 4 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 12 | 7.71 | 6 | 0 | wallstreetbets 9, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev0qtv/) |
| ONDS | 2026-10-09 01:49 | mention spike | 7 | 4.14 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| PLTR | 2026-10-08 13:12 | mention spike | 21 | 12.57 | 18 | 1 | wallstreetbets 21 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevaeed/) |
| TTWO | 2026-10-08 13:27 | mention spike | 6 | 4.43 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuubgi/) |
| USO | 2026-10-08 18:20 | mention spike | 11 | 10.57 | 4 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peukax8/) |
| KEEL | 2026-10-08 03:01 | mention spike | 6 | 3.43 | 3 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peur70q/) |
| APLD | 2026-10-05 14:23 | mention spike | 46 | 56.43 | 32 | 0 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 6 | 21.86 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
