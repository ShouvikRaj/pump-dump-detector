# Stage 1 candidates

Updated 2026-10-09T14:12:27Z by run `37942328450`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 15 | 3.57 | 10 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ASTS | 2026-10-08 21:11 | mention spike | 154 | 14.57 | 96 | 0 | wallstreetbets 153, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 19 | 6.14 | 15 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 10 | 1.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 14 | 1.43 | 10 | 1 | wallstreetbets 13, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.14 | 9 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| GME | 2026-10-08 16:17 | mention spike | 34 | 12.0 | 25 | 1 | wallstreetbets 33, smallstreetbets 1 | NYSE | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| HUM | 2026-10-09 12:39 | mention spike | 12 | 0.43 | 5 | 0 | wallstreetbets 12 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| IBM | 2026-10-09 01:09 | mention spike | 11 | 4.14 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/peulrb8/) |
| MCD | 2026-10-09 00:16 | mention spike | 32 | 9.43 | 17 | 0 | wallstreetbets 32 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 49 | 17.29 | 30 | 0 | wallstreetbets 49 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuofil/) |
| OKLO | 2026-10-06 18:14 | mention spike | 16 | 6.43 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 5.57 | 23 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pessn6f/) |
| SBUX | 2026-10-08 18:59 | mention spike | 13 | 0.29 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 7.14 | 8 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peul5w4/) |
| SLS | 2026-10-09 13:19 | mention spike | 13 | 3.29 | 10 | 0 | wallstreetbets 10, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1kmww/) |
| SOXL | 2026-10-09 00:30 | mention spike | 50 | 16.14 | 20 | 0 | wallstreetbets 50 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuda14/) |
| TSM | 2026-10-09 12:39 | mention spike | 12 | 4.86 | 9 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| UNH | 2026-10-09 13:59 | mention spike | 10 | 1.57 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| UUUU | 2026-10-07 20:50 | mention spike | 14 | 3.43 | 12 | 0 | wallstreetbets 14 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| DAL | 2026-10-09 12:52 | mention spike | 8 | 1.0 | 4 | 0 | wallstreetbets 8 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 14 | 7.29 | 7 | 0 | wallstreetbets 11, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pestggf/) |
| IREN | 2026-10-07 19:18 | mention spike | 17 | 7.29 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peumdxv/) |
| ONDS | 2026-10-09 01:49 | mention spike | 9 | 3.86 | 8 | 0 | wallstreetbets 9 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| PLTR | 2026-10-08 13:12 | mention spike | 21 | 11.86 | 20 | 1 | wallstreetbets 21 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peujfln/) |
| TTWO | 2026-10-08 13:27 | mention spike | 10 | 3.71 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuad6o/) |
| USO | 2026-10-08 18:20 | mention spike | 17 | 10.0 | 8 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peukax8/) |
| ADBE | 2026-10-08 04:07 | mention spike | 11 | 4.71 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1m8jw/) |
| KEEL | 2026-10-08 03:01 | mention spike | 6 | 3.29 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| APLD | 2026-10-05 14:23 | mention spike | 65 | 53.43 | 36 | 0 | wallstreetbets 65 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 14 | 21.57 | 12 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |
| SMCI | 2026-10-07 20:50 | mention spike | 4 | 4.14 | 2 | 0 | wallstreetbets 4 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuku5q/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 9.86 | 11 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peumu4x/) |
| LLY | 2026-10-07 17:44 | mention spike | 3 | 2.29 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
