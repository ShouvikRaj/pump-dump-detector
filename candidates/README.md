# Stage 1 candidates

Updated 2026-10-09T00:16:58Z by run `37863888725`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 13 | 3.43 | 8 | 0 | wallstreetbets 13 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 12 | 4.0 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x03pn2/comment/pepld7v/) |
| ASTS | 2026-10-08 21:11 | mention spike | 92 | 16.0 | 67 | 0 | wallstreetbets 91, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 20 | 5.43 | 14 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 12 | 1.14 | 7 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqflv5/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.71 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 20 | 6.71 | 9 | 0 | wallstreetbets 17, smallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0crnn/comment/pequ29z/) |
| GLD | 2026-10-07 13:01 | mention spike | 16 | 5.29 | 8 | 0 | wallstreetbets 16 | NYSE Arca | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqnhlz/) |
| GME | 2026-10-08 16:17 | mention spike | 31 | 11.86 | 23 | 2 | wallstreetbets 29, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 6.29 | 16 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepiqks/) |
| KEEL | 2026-10-08 03:01 | mention spike | 14 | 2.14 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| NBIS | 2026-10-08 18:05 | mention spike | 52 | 16.71 | 32 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqba7z/) |
| OKLO | 2026-10-06 18:14 | mention spike | 19 | 6.14 | 12 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqkro0/) |
| ORCL | 2026-10-08 17:11 | mention spike | 25 | 6.43 | 21 | 0 | wallstreetbets 25 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq3abu/) |
| PLTR | 2026-10-08 13:12 | mention spike | 44 | 9.71 | 42 | 0 | wallstreetbets 44 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqjhdw/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 23 | 6.14 | 14 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| TTWO | 2026-10-08 13:27 | mention spike | 16 | 3.43 | 7 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 25 | 8.43 | 14 | 0 | wallstreetbets 25 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqq228/) |
| UUUU | 2026-10-07 20:50 | mention spike | 12 | 3.43 | 10 | 0 | wallstreetbets 12 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| MCD | 2026-10-09 00:16 | mention spike | 28 | 9.86 | 17 | 0 | wallstreetbets 28 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1379r/) |
| APLD | 2026-10-05 14:23 | mention spike | 113 | 44.86 | 56 | 0 | wallstreetbets 113 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x14rdx/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 30 | 19.71 | 20 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peph3d6/) |
| SMCI | 2026-10-07 20:50 | mention spike | 2 | 4.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 9.71 | 14 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqc1al/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.14 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 23 | 33.71 | 15 | 0 | wallstreetbets 22, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 5 | 11.0 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peptaaq/) |
| BIYA | 2026-10-07 16:38 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| CRWD | 2026-10-06 23:59 | mention spike | 4 | 6.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x12klg/comment/peqblr6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
