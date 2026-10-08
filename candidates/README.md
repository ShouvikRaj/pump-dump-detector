# Stage 1 candidates

Updated 2026-10-08T12:18:59Z by run `37775907689`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 13 | 2.71 | 13 | 1 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 214 | 21.71 | 108 | 0 | wallstreetbets 214 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BIYA | 2026-10-07 16:38 | mention spike | 10 | 0.14 | 8 | 0 | pennystocks 6, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| BULL | 2026-10-07 12:08 | mention spike | 59 | 3.14 | 21 | 0 | wallstreetbets 59 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| GLD | 2026-10-07 13:01 | mention spike | 11 | 4.43 | 10 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pem5tfj/) |
| IREN | 2026-10-07 19:18 | mention spike | 14 | 4.71 | 14 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekabar/) |
| KEEL | 2026-10-08 03:01 | mention spike | 10 | 1.86 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekb8ct/) |
| LEVI | 2026-10-07 20:37 | mention spike | 14 | 0.86 | 10 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemh2j2/) |
| SMCI | 2026-10-07 20:50 | mention spike | 12 | 3.86 | 11 | 0 | wallstreetbets 12 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| UUUU | 2026-10-07 20:50 | mention spike | 11 | 2.0 | 7 | 0 | wallstreetbets 11 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ltz/) |
| HTZ | 2026-10-06 16:43 | mention spike | 104 | 19.71 | 60 | 0 | wallstreetbets 94, pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ijc4/) |
| CRWD | 2026-10-06 23:59 | mention spike | 8 | 5.29 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| LLY | 2026-10-07 17:44 | mention spike | 12 | 1.43 | 4 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pem2x4w/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 9.29 | 9 | 0 | wallstreetbets 15 | NYSE Arca | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pelfbys/) |
| SOXL | 2026-10-07 12:34 | mention spike | 17 | 16.14 | 11 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekov0i/) |
| PENG | 2026-10-06 18:01 | mention spike | 8 | 6.57 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 8 | 2.29 | 5 | 0 | pennystocks 5, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| AMD | 2026-10-06 14:55 | mention spike | 58 | 47.29 | 53 | 0 | wallstreetbets 56, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| SKHY | 2026-10-06 18:54 | mention spike | 9 | 5.86 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pels36u/) |
| OKLO | 2026-10-06 18:14 | mention spike | 7 | 5.86 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcvj2/) |
| VOO | 2026-10-06 16:15 | mention spike | 11 | 11.71 | 11 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0de7b/comment/pelkm2s/) |
| SOXS | 2026-10-07 12:08 | mention spike | 13 | 5.0 | 4 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pem0r2m/) |
| AVGO | 2026-10-06 19:34 | mention spike | 23 | 22.0 | 17 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemem0c/) |
| CEG | 2026-10-06 13:36 | mention spike | 5 | 6.0 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peirllx/) |
| INTC | 2026-10-06 18:28 | mention spike | 9 | 19.86 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x05wz7/) |
| MRVL | 2026-10-06 13:36 | mention spike | 10 | 14.0 | 5 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemgxax/) |
| SNDK | 2026-10-07 10:09 | mention spike | 48 | 45.71 | 33 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06txo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
