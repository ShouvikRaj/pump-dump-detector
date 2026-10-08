# Stage 1 candidates

Updated 2026-10-08T15:11:19Z by run `37798559841`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 14 | 2.71 | 14 | 1 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 234 | 23.0 | 118 | 0 | wallstreetbets 234 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 4.86 | 19 | 0 | wallstreetbets 19 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen2fwu/) |
| IWM | 2026-10-06 00:59 | mention spike | 19 | 8.71 | 11 | 0 | wallstreetbets 19 | NYSE Arca | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/peni8lj/) |
| KEEL | 2026-10-08 03:01 | mention spike | 10 | 2.0 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen1r7v/) |
| LEVI | 2026-10-07 20:37 | mention spike | 15 | 0.86 | 11 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 48 | 18.43 | 32 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penctyh/) |
| PLTR | 2026-10-08 13:12 | mention spike | 39 | 9.71 | 35 | 0 | wallstreetbets 39 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SMCI | 2026-10-07 20:50 | mention spike | 11 | 3.71 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| TTWO | 2026-10-08 13:27 | mention spike | 14 | 3.29 | 6 | 1 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzzgqj/) |
| UUUU | 2026-10-07 20:50 | mention spike | 10 | 2.14 | 5 | 0 | wallstreetbets 10 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penhmsp/) |
| LLY | 2026-10-07 17:44 | mention spike | 9 | 2.0 | 6 | 0 | wallstreetbets 9 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penc8os/) |
| HTZ | 2026-10-06 16:43 | mention spike | 88 | 23.14 | 58 | 0 | wallstreetbets 80, pennystocks 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0tauh/) |
| BULL | 2026-10-07 12:08 | mention spike | 12 | 9.86 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| GLD | 2026-10-07 13:01 | mention spike | 9 | 4.86 | 6 | 0 | wallstreetbets 9 | NYSE Arca | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penhrb7/) |
| BIYA | 2026-10-07 16:38 | mention spike | 3 | 1.14 | 3 | 0 | pennystocks 1, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 9 | 5.14 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SOXL | 2026-10-07 12:34 | mention spike | 25 | 16.71 | 15 | 0 | wallstreetbets 25 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen979v/) |
| PENG | 2026-10-06 18:01 | mention spike | 3 | 7.29 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| AMD | 2026-10-06 14:55 | mention spike | 45 | 49.86 | 42 | 0 | wallstreetbets 44, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penhkk3/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.86 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen1a7y/) |
| OKLO | 2026-10-06 18:14 | mention spike | 6 | 6.0 | 3 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0esk4/comment/pekl2k5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
