# Stage 1 candidates

Updated 2026-10-09T09:33:33Z by run `37911985857`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 16 | 3.43 | 11 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ASTS | 2026-10-08 21:11 | mention spike | 122 | 14.71 | 82 | 0 | wallstreetbets 121, pennystocks 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 22 | 5.43 | 16 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 11 | 1.43 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.57 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 19 | 6.86 | 8 | 0 | wallstreetbets 16, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pestggf/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.14 | 9 | 0 | wallstreetbets 19 | NYSE Arca | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pernwav/) |
| GME | 2026-10-08 16:17 | mention spike | 33 | 12.0 | 24 | 1 | wallstreetbets 32, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IBM | 2026-10-09 01:09 | mention spike | 10 | 4.57 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/per79lu/) |
| IREN | 2026-10-07 19:18 | mention spike | 21 | 6.43 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0zwf6/comment/pet2ive/) |
| MCD | 2026-10-09 00:16 | mention spike | 33 | 9.29 | 18 | 0 | wallstreetbets 33 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 53 | 16.71 | 33 | 0 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 5.86 | 23 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pessn6f/) |
| PLTR | 2026-10-08 13:12 | mention spike | 42 | 8.71 | 39 | 0 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perv230/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 19 | 6.71 | 11 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| SOXL | 2026-10-09 00:30 | mention spike | 54 | 16.29 | 21 | 0 | wallstreetbets 54 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesvqr1/) |
| TTWO | 2026-10-08 13:27 | mention spike | 14 | 3.57 | 6 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 24 | 8.57 | 12 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmqq0/) |
| UUUU | 2026-10-07 20:50 | mention spike | 14 | 3.43 | 12 | 0 | wallstreetbets 14 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| ONDS | 2026-10-09 01:49 | mention spike | 9 | 3.71 | 9 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1vlsoz5/comment/pesok7i/) |
| ADBE | 2026-10-08 04:07 | mention spike | 9 | 4.57 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pes06d2/) |
| KEEL | 2026-10-08 03:01 | mention spike | 8 | 3.0 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| OKLO | 2026-10-06 18:14 | mention spike | 16 | 6.57 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pesmjxq/) |
| APLD | 2026-10-05 14:23 | mention spike | 86 | 49.14 | 49 | 0 | wallstreetbets 86 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1da4b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 29 | 19.43 | 19 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peshpnc/) |
| SMCI | 2026-10-07 20:50 | mention spike | 1 | 4.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 9.86 | 12 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqc1al/) |
| LLY | 2026-10-07 17:44 | mention spike | 4 | 2.57 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 19 | 34.14 | 12 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 4 | 11.14 | 3 | 0 | wallstreetbets 4 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pet9131/) |
| BIYA | 2026-10-07 16:38 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| CRWD | 2026-10-06 23:59 | mention spike | 3 | 6.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x12klg/comment/peqblr6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
