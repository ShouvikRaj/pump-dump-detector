# Stage 1 candidates

Updated 2026-10-09T13:46:46Z by run `37939059021`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 14 | 3.57 | 10 | 0 | wallstreetbets 14 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ASTS | 2026-10-08 21:11 | mention spike | 139 | 14.43 | 89 | 0 | wallstreetbets 138, pennystocks 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 23 | 5.57 | 17 | 0 | wallstreetbets 23 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 11 | 1.43 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 13 | 1.43 | 9 | 1 | wallstreetbets 12, pennystocks 1 | NYSE | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| DAL | 2026-10-09 12:52 | mention spike | 10 | 0.71 | 5 | 0 | wallstreetbets 10 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peu5bx6/) |
| DELL | 2026-10-08 17:52 | mention spike | 18 | 7.0 | 8 | 0 | wallstreetbets 15, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pestggf/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.29 | 9 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| GME | 2026-10-08 16:17 | mention spike | 33 | 12.0 | 24 | 1 | wallstreetbets 32, smallstreetbets 1 | NYSE | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| HUM | 2026-10-09 12:39 | mention spike | 12 | 0.43 | 5 | 0 | wallstreetbets 12 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf3d9/) |
| IBM | 2026-10-09 01:09 | mention spike | 10 | 4.14 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/per79lu/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 6.86 | 15 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peugx74/) |
| MCD | 2026-10-09 00:16 | mention spike | 32 | 9.43 | 18 | 0 | wallstreetbets 32 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 49 | 17.29 | 31 | 0 | wallstreetbets 49 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peufwvz/) |
| OKLO | 2026-10-06 18:14 | mention spike | 16 | 6.43 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| ONDS | 2026-10-09 01:49 | mention spike | 10 | 3.71 | 9 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuf7it/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 5.71 | 23 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pessn6f/) |
| SBUX | 2026-10-08 18:59 | mention spike | 13 | 0.29 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 6.86 | 10 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| SLS | 2026-10-09 13:19 | mention spike | 12 | 3.29 | 9 | 0 | wallstreetbets 9, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1kmww/) |
| SOXL | 2026-10-09 00:30 | mention spike | 54 | 15.86 | 20 | 0 | wallstreetbets 54 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuda14/) |
| TSM | 2026-10-09 12:39 | mention spike | 12 | 4.71 | 9 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x1dn0y/) |
| UUUU | 2026-10-07 20:50 | mention spike | 14 | 3.43 | 12 | 0 | wallstreetbets 14 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| PLTR | 2026-10-08 13:12 | mention spike | 26 | 11.14 | 24 | 1 | wallstreetbets 26 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peui13l/) |
| TTWO | 2026-10-08 13:27 | mention spike | 10 | 4.0 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuad6o/) |
| USO | 2026-10-08 18:20 | mention spike | 17 | 9.86 | 8 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuhp9v/) |
| ADBE | 2026-10-08 04:07 | mention spike | 8 | 4.71 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pes06d2/) |
| KEEL | 2026-10-08 03:01 | mention spike | 7 | 3.14 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| APLD | 2026-10-05 14:23 | mention spike | 71 | 52.29 | 41 | 0 | wallstreetbets 71 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| META | 2026-10-08 13:39 | mention spike | 16 | 21.43 | 12 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peuckp5/) |
| SMCI | 2026-10-07 20:50 | mention spike | 1 | 4.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 9.86 | 11 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/peudieu/) |
| LLY | 2026-10-07 17:44 | mention spike | 3 | 2.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
