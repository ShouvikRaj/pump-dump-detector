# Stage 1 candidates

Updated 2026-10-08T18:50:36Z by run `37826540060`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 13 | 3.29 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 218 | 26.86 | 114 | 0 | wallstreetbets 218 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BWET | 2026-10-08 15:51 | mention spike | 19 | 5.43 | 13 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| DELL | 2026-10-08 17:52 | mention spike | 16 | 6.86 | 7 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peopsju/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 5.0 | 7 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peomzhz/) |
| GME | 2026-10-08 16:17 | mention spike | 37 | 10.57 | 28 | 2 | wallstreetbets 35, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 20 | 5.57 | 17 | 0 | wallstreetbets 20 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| KEEL | 2026-10-08 03:01 | mention spike | 13 | 2.29 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| LEVI | 2026-10-07 20:37 | mention spike | 11 | 1.43 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 43 | 18.86 | 28 | 0 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w9zh/comment/peodhwg/) |
| NBIS | 2026-10-08 18:05 | mention spike | 42 | 16.43 | 26 | 0 | wallstreetbets 42 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peotdhf/) |
| ORCL | 2026-10-08 17:11 | mention spike | 24 | 6.29 | 21 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peord3j/) |
| PLTR | 2026-10-08 13:12 | mention spike | 40 | 10.14 | 38 | 0 | wallstreetbets 40 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 6.29 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peohtmd/) |
| TTWO | 2026-10-08 13:27 | mention spike | 16 | 3.43 | 8 | 0 | wallstreetbets 16 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peodgv2/) |
| USO | 2026-10-08 18:20 | mention spike | 22 | 8.0 | 16 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peorx2s/) |
| OKLO | 2026-10-06 18:14 | mention spike | 14 | 6.0 | 9 | 0 | wallstreetbets 14 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoddqu/) |
| UUUU | 2026-10-07 20:50 | mention spike | 8 | 2.86 | 4 | 0 | wallstreetbets 8 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peop3i2/) |
| SMCI | 2026-10-07 20:50 | mention spike | 8 | 3.71 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 9.43 | 13 | 0 | wallstreetbets 18 | NYSE Arca | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peonwlo/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.43 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 44 | 30.0 | 32 | 0 | wallstreetbets 41, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 9 | 10.29 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| BIYA | 2026-10-07 16:38 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 7 | 5.29 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen3qry/) |
| SOXL | 2026-10-07 12:34 | mention spike | 29 | 16.86 | 16 | 0 | wallstreetbets 29 | NYSE Arca | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peooe1d/) |
| PENG | 2026-10-06 18:01 | mention spike | 2 | 7.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| AMD | 2026-10-06 14:55 | mention spike | 45 | 50.14 | 41 | 0 | wallstreetbets 44, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peorp5y/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
