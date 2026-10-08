# Stage 1 candidates

Updated 2026-10-08T17:24:30Z by run `37816208724`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 15 | 2.71 | 15 | 1 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 225 | 25.57 | 120 | 0 | wallstreetbets 225 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BWET | 2026-10-08 15:51 | mention spike | 16 | 5.43 | 11 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| GME | 2026-10-08 16:17 | mention spike | 29 | 10.43 | 21 | 1 | wallstreetbets 27, smallstreetbets 2 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w4yb/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 5.43 | 17 | 0 | wallstreetbets 19 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoaqrt/) |
| KEEL | 2026-10-08 03:01 | mention spike | 11 | 2.0 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penlp2w/) |
| LEVI | 2026-10-07 20:37 | mention spike | 14 | 1.0 | 10 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 49 | 18.57 | 32 | 0 | wallstreetbets 49 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0w9zh/comment/peodhwg/) |
| OKLO | 2026-10-06 18:14 | mention spike | 15 | 5.86 | 9 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoddqu/) |
| ORCL | 2026-10-08 17:11 | mention spike | 16 | 6.29 | 15 | 0 | wallstreetbets 16 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoevx6/) |
| PLTR | 2026-10-08 13:12 | mention spike | 37 | 10.14 | 36 | 0 | wallstreetbets 37 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SKHY | 2026-10-06 18:54 | mention spike | 19 | 5.86 | 16 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoawsb/) |
| TTWO | 2026-10-08 13:27 | mention spike | 17 | 3.43 | 9 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peodgv2/) |
| UUUU | 2026-10-07 20:50 | mention spike | 10 | 2.43 | 5 | 0 | wallstreetbets 10 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peofg8w/) |
| GLD | 2026-10-07 13:01 | mention spike | 14 | 5.14 | 6 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penza6f/) |
| SMCI | 2026-10-07 20:50 | mention spike | 9 | 4.0 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 9.43 | 12 | 0 | wallstreetbets 16 | NYSE Arca | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoek2a/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.29 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penc8os/) |
| HTZ | 2026-10-06 16:43 | mention spike | 70 | 26.29 | 47 | 0 | wallstreetbets 65, pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 10 | 10.14 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| BIYA | 2026-10-07 16:38 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 8 | 5.14 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen3qry/) |
| SOXL | 2026-10-07 12:34 | mention spike | 26 | 16.71 | 16 | 0 | wallstreetbets 26 | NYSE Arca | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoci9i/) |
| PENG | 2026-10-06 18:01 | mention spike | 2 | 7.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| AMD | 2026-10-06 14:55 | mention spike | 44 | 49.57 | 40 | 0 | wallstreetbets 43, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peoex5i/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
