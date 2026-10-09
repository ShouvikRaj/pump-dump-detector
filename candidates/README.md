# Stage 1 candidates

Updated 2026-10-09T15:45:30Z by run `37953967634`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 14 | 3.86 | 10 | 0 | wallstreetbets 14 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 19 | 4.14 | 14 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1nz10/) |
| ASTS | 2026-10-08 21:11 | mention spike | 254 | 15.0 | 133 | 0 | wallstreetbets 253, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| CIFR | 2026-10-08 21:37 | mention spike | 10 | 1.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 13 | 1.71 | 9 | 1 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| GME | 2026-10-08 16:17 | mention spike | 43 | 12.29 | 29 | 1 | wallstreetbets 43 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1om9v/) |
| HUM | 2026-10-09 12:39 | mention spike | 11 | 0.57 | 5 | 0 | wallstreetbets 11 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| IBM | 2026-10-09 01:09 | mention spike | 10 | 4.14 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/peulrb8/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 7.29 | 13 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peurpuo/) |
| MCD | 2026-10-09 00:16 | mention spike | 30 | 9.71 | 15 | 0 | wallstreetbets 30 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 44 | 18.14 | 27 | 0 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuu4c2/) |
| ORCL | 2026-10-08 17:11 | mention spike | 27 | 5.43 | 24 | 0 | wallstreetbets 27 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuukns/) |
| SKHY | 2026-10-06 18:54 | mention spike | 18 | 7.29 | 9 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peut1xp/) |
| SLS | 2026-10-09 13:19 | mention spike | 14 | 3.43 | 10 | 0 | wallstreetbets 11, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1mxkk/) |
| TSM | 2026-10-09 12:39 | mention spike | 12 | 5.0 | 8 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| UNH | 2026-10-09 13:59 | mention spike | 11 | 1.43 | 8 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE | #14 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| OKLO | 2026-10-06 18:14 | mention spike | 14 | 6.71 | 11 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev5yo1/) |
| UUUU | 2026-10-07 20:50 | mention spike | 12 | 3.57 | 10 | 0 | wallstreetbets 12 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| GLD | 2026-10-07 13:01 | mention spike | 12 | 6.0 | 8 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| SBUX | 2026-10-08 18:59 | mention spike | 9 | 1.0 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| BWET | 2026-10-08 15:51 | mention spike | 11 | 7.29 | 11 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuhavb/) |
| SOXL | 2026-10-09 00:30 | mention spike | 42 | 17.43 | 16 | 0 | wallstreetbets 42 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevagb5/) |
| DAL | 2026-10-09 12:52 | mention spike | 8 | 1.0 | 4 | 0 | wallstreetbets 8 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 12 | 7.71 | 6 | 0 | wallstreetbets 9, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev0qtv/) |
| ONDS | 2026-10-09 01:49 | mention spike | 8 | 4.0 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| PLTR | 2026-10-08 13:12 | mention spike | 22 | 12.43 | 19 | 1 | wallstreetbets 22 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pevaeed/) |
| TTWO | 2026-10-08 13:27 | mention spike | 10 | 3.86 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuubgi/) |
| USO | 2026-10-08 18:20 | mention spike | 14 | 10.29 | 7 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peukax8/) |
| KEEL | 2026-10-08 03:01 | mention spike | 6 | 3.43 | 3 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peur70q/) |
| APLD | 2026-10-05 14:23 | mention spike | 48 | 56.29 | 34 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 12 | 21.57 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |
| SMCI | 2026-10-07 20:50 | mention spike | 4 | 4.14 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuku5q/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
