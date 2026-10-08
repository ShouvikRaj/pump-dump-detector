# Stage 1 candidates

Updated 2026-10-08T18:20:55Z by run `37823120901`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 15 | 2.86 | 15 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 220 | 26.71 | 115 | 0 | wallstreetbets 220 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BWET | 2026-10-08 15:51 | mention spike | 18 | 5.43 | 13 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| DELL | 2026-10-08 17:52 | mention spike | 16 | 6.86 | 7 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peopsju/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 5.0 | 7 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peomzhz/) |
| GME | 2026-10-08 16:17 | mention spike | 34 | 10.43 | 26 | 2 | wallstreetbets 32, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 21 | 5.43 | 18 | 0 | wallstreetbets 21 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| KEEL | 2026-10-08 03:01 | mention spike | 14 | 2.14 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| LEVI | 2026-10-07 20:37 | mention spike | 11 | 1.43 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 45 | 19.0 | 30 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w9zh/comment/peodhwg/) |
| NBIS | 2026-10-08 18:05 | mention spike | 40 | 16.43 | 26 | 0 | wallstreetbets 40 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peorzfu/) |
| OKLO | 2026-10-06 18:14 | mention spike | 14 | 6.0 | 9 | 0 | wallstreetbets 14 | NYSE | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoddqu/) |
| ORCL | 2026-10-08 17:11 | mention spike | 24 | 6.29 | 21 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peord3j/) |
| PLTR | 2026-10-08 13:12 | mention spike | 40 | 10.14 | 38 | 0 | wallstreetbets 40 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 6.29 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peohtmd/) |
| TTWO | 2026-10-08 13:27 | mention spike | 17 | 3.29 | 9 | 0 | wallstreetbets 17 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peodgv2/) |
| USO | 2026-10-08 18:20 | mention spike | 22 | 8.14 | 16 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peorx2s/) |
| UUUU | 2026-10-07 20:50 | mention spike | 9 | 2.71 | 5 | 0 | wallstreetbets 9 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peop3i2/) |
| SMCI | 2026-10-07 20:50 | mention spike | 9 | 4.14 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 19 | 9.29 | 13 | 0 | wallstreetbets 19 | NYSE Arca | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peonwlo/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.43 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 61 | 27.57 | 43 | 0 | wallstreetbets 57, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 9 | 10.29 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| BIYA | 2026-10-07 16:38 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 7 | 5.29 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen3qry/) |
| SOXL | 2026-10-07 12:34 | mention spike | 29 | 16.86 | 16 | 0 | wallstreetbets 29 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peooe1d/) |
| PENG | 2026-10-06 18:01 | mention spike | 2 | 7.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| AMD | 2026-10-06 14:55 | mention spike | 46 | 50.0 | 42 | 0 | wallstreetbets 45, smallstreetbets 1 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peorp5y/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
