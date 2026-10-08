# Stage 1 candidates

Updated 2026-10-08T20:31:42Z by run `37839980671`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 11 | 3.57 | 6 | 0 | wallstreetbets 11 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 15 | 3.57 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 188 | 33.43 | 97 | 0 | wallstreetbets 188 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BWET | 2026-10-08 15:51 | mention spike | 19 | 5.57 | 13 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.71 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 17 | 6.86 | 8 | 0 | wallstreetbets 16, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0sohz/comment/pep8d9a/) |
| GME | 2026-10-08 16:17 | mention spike | 37 | 10.71 | 28 | 2 | wallstreetbets 35, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 21 | 6.0 | 18 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepiqks/) |
| KEEL | 2026-10-08 03:01 | mention spike | 13 | 2.14 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| NBIS | 2026-10-08 18:05 | mention spike | 51 | 16.57 | 32 | 0 | wallstreetbets 51 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepjsvy/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 6.0 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pephdlf/) |
| ORCL | 2026-10-08 17:11 | mention spike | 24 | 6.43 | 21 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepdybg/) |
| PLTR | 2026-10-08 13:12 | mention spike | 40 | 10.14 | 38 | 0 | wallstreetbets 40 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 19 | 6.14 | 14 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pephgll/) |
| TTWO | 2026-10-08 13:27 | mention spike | 17 | 3.29 | 8 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 23 | 8.29 | 14 | 0 | wallstreetbets 23 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peplm5b/) |
| LEVI | 2026-10-07 20:37 | mention spike | 3 | 2.57 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| GLD | 2026-10-07 13:01 | mention spike | 13 | 5.29 | 5 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peomzhz/) |
| META | 2026-10-08 13:39 | mention spike | 37 | 19.29 | 22 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peph3d6/) |
| UUUU | 2026-10-07 20:50 | mention spike | 10 | 3.14 | 7 | 0 | wallstreetbets 10 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| SMCI | 2026-10-07 20:50 | mention spike | 5 | 4.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 9.43 | 13 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peonwlo/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.14 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 35 | 31.57 | 23 | 0 | wallstreetbets 34, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 6 | 10.71 | 5 | 0 | wallstreetbets 6 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| BIYA | 2026-10-07 16:38 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 8 | 5.29 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pep1w8z/) |
| SOXL | 2026-10-07 12:34 | mention spike | 29 | 16.86 | 16 | 0 | wallstreetbets 29 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepeow5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
