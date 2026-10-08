# Stage 1 candidates

Updated 2026-10-08T16:31:44Z by run `37809343959`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 14 | 2.71 | 14 | 1 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 229 | 24.86 | 120 | 0 | wallstreetbets 229 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BWET | 2026-10-08 15:51 | mention spike | 16 | 5.43 | 11 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0sclo/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 5.0 | 7 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penza6f/) |
| GME | 2026-10-08 16:17 | mention spike | 26 | 10.57 | 19 | 1 | wallstreetbets 24, smallstreetbets 2 | NYSE | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x0si4h/) |
| IREN | 2026-10-07 19:18 | mention spike | 18 | 5.14 | 18 | 0 | wallstreetbets 18 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peo2cyq/) |
| KEEL | 2026-10-08 03:01 | mention spike | 11 | 2.0 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penlp2w/) |
| LEVI | 2026-10-07 20:37 | mention spike | 15 | 0.86 | 11 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 49 | 18.14 | 32 | 0 | wallstreetbets 49 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penu7l4/) |
| PLTR | 2026-10-08 13:12 | mention spike | 37 | 10.0 | 36 | 0 | wallstreetbets 37 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 5.86 | 15 | 0 | wallstreetbets 17 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penxsag/) |
| SMCI | 2026-10-07 20:50 | mention spike | 10 | 3.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| TTWO | 2026-10-08 13:27 | mention spike | 15 | 3.43 | 7 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pentqr4/) |
| UUUU | 2026-10-07 20:50 | mention spike | 10 | 2.29 | 5 | 0 | wallstreetbets 10 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penqf2d/) |
| IWM | 2026-10-06 00:59 | mention spike | 13 | 9.71 | 10 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pennl1r/) |
| LLY | 2026-10-07 17:44 | mention spike | 7 | 2.29 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penc8os/) |
| HTZ | 2026-10-06 16:43 | mention spike | 75 | 25.43 | 48 | 0 | wallstreetbets 70, pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 12 | 9.86 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| BIYA | 2026-10-07 16:38 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 9 | 5.0 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SOXL | 2026-10-07 12:34 | mention spike | 23 | 16.86 | 14 | 0 | wallstreetbets 23 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penjrp1/) |
| PENG | 2026-10-06 18:01 | mention spike | 3 | 7.29 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| AMD | 2026-10-06 14:55 | mention spike | 44 | 49.57 | 40 | 0 | wallstreetbets 43, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peo0xvo/) |
| OKLO | 2026-10-06 18:14 | mention spike | 13 | 5.86 | 8 | 0 | wallstreetbets 13 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penxxnp/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
