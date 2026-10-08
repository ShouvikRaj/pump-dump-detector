# Stage 1 candidates

Updated 2026-10-08T21:24:40Z by run `37846453156`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 12 | 3.43 | 7 | 0 | wallstreetbets 12 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 14 | 3.71 | 12 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| ASTS | 2026-10-08 21:11 | mention spike | 45 | 16.0 | 35 | 0 | wallstreetbets 44, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 19 | 5.43 | 13 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.71 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 17 | 6.86 | 8 | 0 | wallstreetbets 16, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0sohz/comment/pep8d9a/) |
| GME | 2026-10-08 16:17 | mention spike | 36 | 11.0 | 27 | 2 | wallstreetbets 34, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 20 | 6.14 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepiqks/) |
| KEEL | 2026-10-08 03:01 | mention spike | 14 | 2.14 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| NBIS | 2026-10-08 18:05 | mention spike | 51 | 16.71 | 32 | 0 | wallstreetbets 51 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepqszr/) |
| OKLO | 2026-10-06 18:14 | mention spike | 19 | 6.0 | 13 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepymiu/) |
| ORCL | 2026-10-08 17:11 | mention spike | 24 | 6.29 | 21 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepdybg/) |
| PLTR | 2026-10-08 13:12 | mention spike | 42 | 10.14 | 40 | 0 | wallstreetbets 42 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 22 | 6.14 | 14 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepxl6t/) |
| TTWO | 2026-10-08 13:27 | mention spike | 17 | 3.29 | 8 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 23 | 8.43 | 13 | 0 | wallstreetbets 23 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepsix1/) |
| APLD | 2026-10-05 14:23 | mention spike | 131 | 42.0 | 64 | 0 | wallstreetbets 131 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x132j9/comment/peq0e5d/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| GLD | 2026-10-07 13:01 | mention spike | 14 | 5.29 | 6 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepv3al/) |
| META | 2026-10-08 13:39 | mention spike | 37 | 19.0 | 22 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peph3d6/) |
| UUUU | 2026-10-07 20:50 | mention spike | 10 | 3.43 | 9 | 0 | wallstreetbets 10 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| SMCI | 2026-10-07 20:50 | mention spike | 3 | 4.43 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 9.57 | 13 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepw5nk/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.14 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 31 | 32.29 | 21 | 0 | wallstreetbets 30, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 7 | 10.71 | 6 | 0 | wallstreetbets 7 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peptaaq/) |
| BIYA | 2026-10-07 16:38 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 5 | 5.71 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pep1w8z/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
