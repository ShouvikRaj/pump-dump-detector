# Stage 1 candidates

Updated 2026-10-09T13:59:05Z by run `37940684557`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 15 | 3.57 | 10 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ASTS | 2026-10-08 21:11 | mention spike | 149 | 14.43 | 93 | 0 | wallstreetbets 148, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 22 | 5.71 | 16 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 10 | 1.57 | 6 | 0 | wallstreetbets 10 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 14 | 1.43 | 10 | 1 | wallstreetbets 13, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| DAL | 2026-10-09 12:52 | mention spike | 10 | 0.71 | 5 | 0 | wallstreetbets 10 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 16 | 7.29 | 7 | 0 | wallstreetbets 13, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pestggf/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.14 | 9 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| GME | 2026-10-08 16:17 | mention spike | 34 | 12.0 | 25 | 1 | wallstreetbets 33, smallstreetbets 1 | NYSE | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| HUM | 2026-10-09 12:39 | mention spike | 12 | 0.43 | 5 | 0 | wallstreetbets 12 | NYSE | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| IBM | 2026-10-09 01:09 | mention spike | 11 | 4.14 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/peulrb8/) |
| MCD | 2026-10-09 00:16 | mention spike | 32 | 9.29 | 18 | 0 | wallstreetbets 32 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 48 | 17.29 | 30 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peulae6/) |
| OKLO | 2026-10-06 18:14 | mention spike | 16 | 6.43 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 5.71 | 23 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pessn6f/) |
| SBUX | 2026-10-08 18:59 | mention spike | 13 | 0.29 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 7.14 | 8 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peul5w4/) |
| SLS | 2026-10-09 13:19 | mention spike | 13 | 3.29 | 10 | 0 | wallstreetbets 10, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1kmww/) |
| SOXL | 2026-10-09 00:30 | mention spike | 54 | 15.86 | 20 | 0 | wallstreetbets 54 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuda14/) |
| UUUU | 2026-10-07 20:50 | mention spike | 14 | 3.43 | 12 | 0 | wallstreetbets 14 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| UNH | 2026-10-09 13:59 | mention spike | 10 | 1.57 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| IREN | 2026-10-07 19:18 | mention spike | 17 | 7.14 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peugx74/) |
| ONDS | 2026-10-09 01:49 | mention spike | 9 | 3.86 | 8 | 0 | wallstreetbets 9 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| TSM | 2026-10-09 12:39 | mention spike | 11 | 4.86 | 9 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| PLTR | 2026-10-08 13:12 | mention spike | 26 | 11.14 | 24 | 1 | wallstreetbets 26 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peujfln/) |
| TTWO | 2026-10-08 13:27 | mention spike | 10 | 4.0 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuad6o/) |
| USO | 2026-10-08 18:20 | mention spike | 18 | 9.86 | 8 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peukax8/) |
| ADBE | 2026-10-08 04:07 | mention spike | 8 | 4.71 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pes06d2/) |
| KEEL | 2026-10-08 03:01 | mention spike | 6 | 3.29 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| APLD | 2026-10-05 14:23 | mention spike | 67 | 53.0 | 37 | 0 | wallstreetbets 67 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 15 | 21.43 | 12 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |
| SMCI | 2026-10-07 20:50 | mention spike | 4 | 4.14 | 2 | 0 | wallstreetbets 4 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuku5q/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 9.86 | 11 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peudieu/) |
| LLY | 2026-10-07 17:44 | mention spike | 3 | 2.29 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
