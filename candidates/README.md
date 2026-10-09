# Stage 1 candidates

Updated 2026-10-09T02:55:59Z by run `37876829146`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 14 | 3.43 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 12 | 4.0 | 11 | 0 | wallstreetbets 12 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pepld7v/) |
| ASTS | 2026-10-08 21:11 | mention spike | 111 | 15.71 | 76 | 0 | wallstreetbets 110, pennystocks 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 22 | 5.43 | 16 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 11 | 1.43 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perh3ga/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.71 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 20 | 6.57 | 9 | 0 | wallstreetbets 17, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0crnn/comment/pequ29z/) |
| GLD | 2026-10-07 13:01 | mention spike | 19 | 5.29 | 9 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pernwav/) |
| GME | 2026-10-08 16:17 | mention spike | 33 | 11.86 | 25 | 2 | wallstreetbets 31, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IBM | 2026-10-09 01:09 | mention spike | 11 | 4.86 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/per79lu/) |
| IREN | 2026-10-07 19:18 | mention spike | 17 | 6.57 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepiqks/) |
| MCD | 2026-10-09 00:16 | mention spike | 35 | 9.43 | 20 | 0 | wallstreetbets 35 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| NBIS | 2026-10-08 18:05 | mention spike | 52 | 16.86 | 32 | 0 | wallstreetbets 52 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/perqsbh/) |
| ONDS | 2026-10-09 01:49 | mention spike | 11 | 3.71 | 10 | 0 | wallstreetbets 10, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x180e6/comment/pernf8p/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 6.43 | 22 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x173ex/comment/per8ca2/) |
| PLTR | 2026-10-08 13:12 | mention spike | 45 | 9.14 | 42 | 0 | wallstreetbets 45 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peroprb/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 23 | 6.14 | 14 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| SOXL | 2026-10-09 00:30 | mention spike | 34 | 16.43 | 17 | 0 | wallstreetbets 34 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x16gek/comment/per4kv3/) |
| TTWO | 2026-10-08 13:27 | mention spike | 14 | 3.71 | 6 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 24 | 8.57 | 13 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqq228/) |
| UUUU | 2026-10-07 20:50 | mention spike | 13 | 3.43 | 11 | 0 | wallstreetbets 13 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| KEEL | 2026-10-08 03:01 | mention spike | 10 | 2.71 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 6.29 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqkro0/) |
| APLD | 2026-10-05 14:23 | mention spike | 98 | 47.14 | 52 | 0 | wallstreetbets 98 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x14rdx/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 30 | 19.86 | 20 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peri1iy/) |
| SMCI | 2026-10-07 20:50 | mention spike | 1 | 4.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 17 | 9.71 | 13 | 0 | wallstreetbets 17 | NYSE Arca | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqc1al/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.14 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 21 | 34.0 | 14 | 0 | wallstreetbets 20, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 5 | 11.0 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peptaaq/) |
| BIYA | 2026-10-07 16:38 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| CRWD | 2026-10-06 23:59 | mention spike | 4 | 6.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x12klg/comment/peqblr6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
