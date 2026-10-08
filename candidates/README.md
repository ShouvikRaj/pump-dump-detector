# Stage 1 candidates

Updated 2026-10-08T14:45:19Z by run `37794888832`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 14 | 2.71 | 14 | 1 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 229 | 22.57 | 116 | 0 | wallstreetbets 229 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| IREN | 2026-10-07 19:18 | mention spike | 19 | 4.86 | 19 | 0 | wallstreetbets 19 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen2fwu/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 8.86 | 11 | 0 | wallstreetbets 18 | NYSE Arca | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen7u70/) |
| KEEL | 2026-10-08 03:01 | mention spike | 10 | 2.0 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen1r7v/) |
| LEVI | 2026-10-07 20:37 | mention spike | 15 | 0.86 | 11 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| LLY | 2026-10-07 17:44 | mention spike | 10 | 1.86 | 6 | 0 | wallstreetbets 10 | NYSE | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penc8os/) |
| META | 2026-10-08 13:39 | mention spike | 47 | 19.0 | 32 | 0 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen4ywa/) |
| PLTR | 2026-10-08 13:12 | mention spike | 38 | 9.86 | 34 | 0 | wallstreetbets 38 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SMCI | 2026-10-07 20:50 | mention spike | 11 | 3.71 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| TTWO | 2026-10-08 13:27 | mention spike | 14 | 3.29 | 6 | 1 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzzgqj/) |
| HTZ | 2026-10-06 16:43 | mention spike | 92 | 22.43 | 60 | 0 | wallstreetbets 83, pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ijc4/) |
| UUUU | 2026-10-07 20:50 | mention spike | 9 | 2.14 | 5 | 0 | wallstreetbets 9 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ltz/) |
| BULL | 2026-10-07 12:08 | mention spike | 13 | 9.71 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen55ka/) |
| GLD | 2026-10-07 13:01 | mention spike | 7 | 5.14 | 6 | 0 | wallstreetbets 7 | NYSE Arca | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/penbkok/) |
| BIYA | 2026-10-07 16:38 | mention spike | 4 | 1.0 | 4 | 0 | wallstreetbets 2, pennystocks 1, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 9 | 5.14 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SOXL | 2026-10-07 12:34 | mention spike | 25 | 16.86 | 15 | 0 | wallstreetbets 25 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen979v/) |
| PENG | 2026-10-06 18:01 | mention spike | 4 | 7.14 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 3 | 3.0 | 1 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| AMD | 2026-10-06 14:55 | mention spike | 44 | 50.0 | 41 | 0 | wallstreetbets 43, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen5ajm/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.86 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pen1a7y/) |
| OKLO | 2026-10-06 18:14 | mention spike | 7 | 5.86 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 2 | 3.43 | 1 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemus3f/) |
| VOO | 2026-10-06 16:15 | mention spike | 11 | 11.57 | 11 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0de7b/comment/pelkm2s/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
