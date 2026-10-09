# Stage 1 candidates

Updated 2026-10-09T04:42:36Z by run `37885073620`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 14 | 3.43 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ASTS | 2026-10-08 21:11 | mention spike | 115 | 15.57 | 80 | 0 | wallstreetbets 114, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 22 | 5.43 | 16 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 11 | 1.43 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.57 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 18 | 6.86 | 8 | 0 | wallstreetbets 15, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0crnn/comment/pequ29z/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.29 | 9 | 0 | wallstreetbets 19 | NYSE Arca | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pernwav/) |
| GME | 2026-10-08 16:17 | mention spike | 33 | 11.86 | 25 | 2 | wallstreetbets 31, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IBM | 2026-10-09 01:09 | mention spike | 11 | 4.71 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/per79lu/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 6.57 | 16 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pes8s2e/) |
| MCD | 2026-10-09 00:16 | mention spike | 34 | 9.29 | 19 | 0 | wallstreetbets 34 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 51 | 17.0 | 32 | 0 | wallstreetbets 51 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pes9hpr/) |
| ONDS | 2026-10-09 01:49 | mention spike | 11 | 3.43 | 10 | 0 | wallstreetbets 10, pennystocks 1 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x180e6/comment/pernf8p/) |
| ORCL | 2026-10-08 17:11 | mention spike | 25 | 6.29 | 22 | 0 | wallstreetbets 25 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/per8ca2/) |
| PLTR | 2026-10-08 13:12 | mention spike | 45 | 8.57 | 42 | 0 | wallstreetbets 45 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perv230/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 22 | 6.29 | 14 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| TTWO | 2026-10-08 13:27 | mention spike | 14 | 3.71 | 6 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 24 | 8.57 | 13 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqq228/) |
| UUUU | 2026-10-07 20:50 | mention spike | 13 | 3.43 | 11 | 0 | wallstreetbets 13 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| ADBE | 2026-10-08 04:07 | mention spike | 12 | 4.14 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pes06d2/) |
| SOXL | 2026-10-09 00:30 | mention spike | 34 | 16.57 | 16 | 0 | wallstreetbets 34 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pes8zct/) |
| KEEL | 2026-10-08 03:01 | mention spike | 8 | 3.0 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| OKLO | 2026-10-06 18:14 | mention spike | 15 | 6.71 | 11 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqkro0/) |
| APLD | 2026-10-05 14:23 | mention spike | 91 | 48.0 | 50 | 0 | wallstreetbets 91 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x14rdx/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 29 | 19.71 | 19 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peri1iy/) |
| SMCI | 2026-10-07 20:50 | mention spike | 1 | 4.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 17 | 9.71 | 13 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqc1al/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.14 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 21 | 33.86 | 14 | 0 | wallstreetbets 20, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 3 | 11.14 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peptaaq/) |
| BIYA | 2026-10-07 16:38 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| CRWD | 2026-10-06 23:59 | mention spike | 3 | 6.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x12klg/comment/peqblr6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
