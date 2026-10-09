# Stage 1 candidates

Updated 2026-10-09T11:46:18Z by run `37925711266`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 16 | 3.29 | 11 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ASTS | 2026-10-08 21:11 | mention spike | 132 | 14.71 | 86 | 0 | wallstreetbets 131, pennystocks 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 21 | 5.57 | 15 | 0 | wallstreetbets 21 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 11 | 1.43 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 13 | 1.57 | 9 | 1 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| DELL | 2026-10-08 17:52 | mention spike | 18 | 7.0 | 8 | 0 | wallstreetbets 15, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pestggf/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.29 | 9 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petuv47/) |
| GME | 2026-10-08 16:17 | mention spike | 33 | 12.0 | 24 | 1 | wallstreetbets 32, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IBM | 2026-10-09 01:09 | mention spike | 10 | 4.14 | 9 | 0 | wallstreetbets 10 | NYSE | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/per79lu/) |
| IREN | 2026-10-07 19:18 | mention spike | 21 | 6.43 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0zwf6/comment/pet2ive/) |
| MCD | 2026-10-09 00:16 | mention spike | 33 | 9.14 | 18 | 0 | wallstreetbets 33 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 53 | 16.57 | 33 | 0 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petg0xq/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 5.86 | 23 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pessn6f/) |
| PLTR | 2026-10-08 13:12 | mention spike | 39 | 9.0 | 36 | 0 | wallstreetbets 39 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perv230/) |
| SBUX | 2026-10-08 18:59 | mention spike | 12 | 0.29 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1iyid/) |
| SKHY | 2026-10-06 18:54 | mention spike | 19 | 6.57 | 11 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| SOXL | 2026-10-09 00:30 | mention spike | 56 | 16.0 | 21 | 0 | wallstreetbets 56 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petlwkj/) |
| TTWO | 2026-10-08 13:27 | mention spike | 13 | 3.86 | 5 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petjsuq/) |
| UUUU | 2026-10-07 20:50 | mention spike | 14 | 3.43 | 12 | 0 | wallstreetbets 14 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| USO | 2026-10-08 18:20 | mention spike | 20 | 9.14 | 11 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmqq0/) |
| ONDS | 2026-10-09 01:49 | mention spike | 9 | 3.71 | 9 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1vlsoz5/comment/pesok7i/) |
| ADBE | 2026-10-08 04:07 | mention spike | 9 | 4.57 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pes06d2/) |
| KEEL | 2026-10-08 03:01 | mention spike | 8 | 3.0 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| OKLO | 2026-10-06 18:14 | mention spike | 16 | 6.57 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| APLD | 2026-10-05 14:23 | mention spike | 81 | 50.0 | 47 | 0 | wallstreetbets 81 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 26 | 19.86 | 18 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peshpnc/) |
| SMCI | 2026-10-07 20:50 | mention spike | 1 | 4.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 9.86 | 12 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqc1al/) |
| LLY | 2026-10-07 17:44 | mention spike | 3 | 2.71 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 17 | 34.43 | 11 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 5 | 11.14 | 4 | 1 | wallstreetbets 5 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1hco2/comment/petk2ms/) |
| BIYA | 2026-10-07 16:38 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
