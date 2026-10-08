# Stage 1 candidates

Updated 2026-10-08T22:43:57Z by run `37855214775`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 13 | 3.43 | 8 | 0 | wallstreetbets 13 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11ejz/) |
| ADBE | 2026-10-08 04:07 | mention spike | 14 | 3.71 | 12 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| ASTS | 2026-10-08 21:11 | mention spike | 76 | 16.0 | 55 | 0 | wallstreetbets 75, pennystocks 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0xply/) |
| BWET | 2026-10-08 15:51 | mention spike | 19 | 5.43 | 13 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| CIFR | 2026-10-08 21:37 | mention spike | 12 | 1.14 | 7 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqflv5/) |
| CMG | 2026-10-08 19:38 | mention spike | 12 | 1.71 | 8 | 1 | wallstreetbets 11, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ym2m/) |
| DELL | 2026-10-08 17:52 | mention spike | 18 | 6.71 | 8 | 0 | wallstreetbets 16, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0sohz/comment/peqdv3y/) |
| GME | 2026-10-08 16:17 | mention spike | 30 | 12.0 | 22 | 2 | wallstreetbets 28, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 6.29 | 16 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepiqks/) |
| KEEL | 2026-10-08 03:01 | mention spike | 14 | 2.14 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peprw37/) |
| NBIS | 2026-10-08 18:05 | mention spike | 52 | 16.71 | 32 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqba7z/) |
| OKLO | 2026-10-06 18:14 | mention spike | 19 | 6.0 | 13 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/pepymiu/) |
| ORCL | 2026-10-08 17:11 | mention spike | 26 | 6.29 | 22 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq3abu/) |
| PLTR | 2026-10-08 13:12 | mention spike | 44 | 9.71 | 42 | 0 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SBUX | 2026-10-08 18:59 | mention spike | 11 | 0.29 | 8 | 0 | wallstreetbets 11 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepaboj/) |
| SKHY | 2026-10-06 18:54 | mention spike | 24 | 6.0 | 15 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq4cyg/) |
| TTWO | 2026-10-08 13:27 | mention spike | 16 | 3.43 | 7 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pepe3ix/) |
| USO | 2026-10-08 18:20 | mention spike | 24 | 8.43 | 13 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq98w3/) |
| APLD | 2026-10-05 14:23 | mention spike | 119 | 43.86 | 58 | 0 | wallstreetbets 119 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x14rdx/) |
| LEVI | 2026-10-07 20:37 | mention spike | 2 | 2.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 5.29 | 7 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peq8sdt/) |
| META | 2026-10-08 13:39 | mention spike | 35 | 19.14 | 21 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peph3d6/) |
| UUUU | 2026-10-07 20:50 | mention spike | 11 | 3.43 | 9 | 0 | wallstreetbets 11 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x10i5k/) |
| SMCI | 2026-10-07 20:50 | mention spike | 2 | 4.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoqg11/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 9.71 | 14 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peqc1al/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.14 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoii8k/) |
| HTZ | 2026-10-06 16:43 | mention spike | 25 | 33.14 | 18 | 0 | wallstreetbets 24, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 7 | 10.71 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x11464/comment/peptaaq/) |
| BIYA | 2026-10-07 16:38 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| CRWD | 2026-10-06 23:59 | mention spike | 4 | 6.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x12klg/comment/peqblr6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
