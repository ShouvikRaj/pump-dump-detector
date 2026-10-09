# Stage 1 candidates

Updated 2026-10-09T15:07:46Z by run `37948977210`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 14 | 3.71 | 10 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 17 | 4.14 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1m8jw/) |
| ASTS | 2026-10-08 21:11 | mention spike | 176 | 14.86 | 105 | 0 | wallstreetbets 175, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| CIFR | 2026-10-08 21:37 | mention spike | 10 | 1.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 15 | 1.43 | 11 | 1 | wallstreetbets 14, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 5.57 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| GME | 2026-10-08 16:17 | mention spike | 36 | 12.29 | 25 | 1 | wallstreetbets 36 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| HUM | 2026-10-09 12:39 | mention spike | 11 | 0.57 | 5 | 0 | wallstreetbets 11 | NYSE | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| IBM | 2026-10-09 01:09 | mention spike | 11 | 4.0 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/peulrb8/) |
| IREN | 2026-10-07 19:18 | mention spike | 20 | 7.14 | 14 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peurpuo/) |
| MCD | 2026-10-09 00:16 | mention spike | 30 | 9.71 | 15 | 0 | wallstreetbets 30 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 47 | 17.71 | 30 | 0 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuu4c2/) |
| OKLO | 2026-10-06 18:14 | mention spike | 16 | 6.29 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| ORCL | 2026-10-08 17:11 | mention spike | 27 | 5.43 | 24 | 0 | wallstreetbets 27 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuukns/) |
| SBUX | 2026-10-08 18:59 | mention spike | 10 | 0.86 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| SKHY | 2026-10-06 18:54 | mention spike | 19 | 7.14 | 10 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peut1xp/) |
| SLS | 2026-10-09 13:19 | mention spike | 13 | 3.43 | 9 | 0 | wallstreetbets 10, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1mxkk/) |
| UNH | 2026-10-09 13:59 | mention spike | 10 | 1.57 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE | #6 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| UUUU | 2026-10-07 20:50 | mention spike | 13 | 3.57 | 11 | 0 | wallstreetbets 13 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| BWET | 2026-10-08 15:51 | mention spike | 13 | 7.0 | 11 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuhavb/) |
| SOXL | 2026-10-09 00:30 | mention spike | 40 | 17.29 | 13 | 0 | wallstreetbets 40 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuda14/) |
| TSM | 2026-10-09 12:39 | mention spike | 11 | 5.0 | 8 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| DAL | 2026-10-09 12:52 | mention spike | 8 | 1.0 | 4 | 0 | wallstreetbets 8 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 15 | 7.29 | 7 | 0 | wallstreetbets 12, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev0qtv/) |
| ONDS | 2026-10-09 01:49 | mention spike | 9 | 3.86 | 8 | 0 | wallstreetbets 9 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| PLTR | 2026-10-08 13:12 | mention spike | 20 | 12.29 | 18 | 1 | wallstreetbets 20 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/pev0r52/) |
| TTWO | 2026-10-08 13:27 | mention spike | 10 | 3.86 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuubgi/) |
| USO | 2026-10-08 18:20 | mention spike | 16 | 10.0 | 8 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peukax8/) |
| KEEL | 2026-10-08 03:01 | mention spike | 7 | 3.29 | 4 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peur70q/) |
| APLD | 2026-10-05 14:23 | mention spike | 52 | 55.29 | 33 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 13 | 21.57 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |
| SMCI | 2026-10-07 20:50 | mention spike | 4 | 4.14 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuku5q/) |
| IWM | 2026-10-06 00:59 | mention spike | 13 | 10.0 | 10 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peumu4x/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
