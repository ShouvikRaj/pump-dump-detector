# Stage 1 candidates

Updated 2026-10-08T07:01:11Z by run `37740767023`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 10 | 2.71 | 10 | 1 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 203 | 21.14 | 105 | 0 | wallstreetbets 203 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BIYA | 2026-10-07 16:38 | mention spike | 11 | 0.0 | 8 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| BULL | 2026-10-07 12:08 | mention spike | 71 | 1.29 | 29 | 0 | wallstreetbets 71 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CRWD | 2026-10-06 23:59 | mention spike | 14 | 4.43 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 10 | 4.43 | 9 | 0 | wallstreetbets 10 | NYSE Arca | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pehzt6j/) |
| HTZ | 2026-10-06 16:43 | mention spike | 106 | 19.0 | 61 | 0 | wallstreetbets 94, pennystocks 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ijc4/) |
| IREN | 2026-10-07 19:18 | mention spike | 15 | 4.57 | 15 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekabar/) |
| KEEL | 2026-10-08 03:01 | mention spike | 12 | 1.71 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekb8ct/) |
| LEVI | 2026-10-07 20:37 | mention spike | 13 | 0.86 | 9 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ycv/) |
| LLY | 2026-10-07 17:44 | mention spike | 13 | 1.0 | 5 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pel7j4b/) |
| SMCI | 2026-10-07 20:50 | mention spike | 12 | 4.0 | 11 | 0 | wallstreetbets 12 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| UUUU | 2026-10-07 20:50 | mention spike | 11 | 2.14 | 7 | 0 | wallstreetbets 11 | NYSE American | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ltz/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 9.14 | 10 | 0 | wallstreetbets 16 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0de7b/comment/pejr8dw/) |
| SOXL | 2026-10-07 12:34 | mention spike | 22 | 15.43 | 12 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekov0i/) |
| PENG | 2026-10-06 18:01 | mention spike | 10 | 6.29 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 8 | 2.29 | 5 | 0 | pennystocks 5, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| AMD | 2026-10-06 14:55 | mention spike | 80 | 44.86 | 71 | 0 | wallstreetbets 78, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| SKHY | 2026-10-06 18:54 | mention spike | 7 | 5.86 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekg2te/) |
| OKLO | 2026-10-06 18:14 | mention spike | 7 | 5.86 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 3 | 3.14 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcvj2/) |
| VOO | 2026-10-06 16:15 | mention spike | 13 | 11.29 | 13 | 0 | wallstreetbets 12, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0esk4/comment/pel0e0o/) |
| SOXS | 2026-10-07 12:08 | mention spike | 11 | 4.71 | 4 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pel7opf/) |
| AVGO | 2026-10-06 19:34 | mention spike | 25 | 21.43 | 18 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pektqos/) |
| CEG | 2026-10-06 13:36 | mention spike | 6 | 5.86 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peirllx/) |
| INTC | 2026-10-06 18:28 | mention spike | 16 | 19.0 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x05wz7/) |
| MRVL | 2026-10-06 13:36 | mention spike | 10 | 14.29 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehudwc/) |
| SNDK | 2026-10-07 10:09 | mention spike | 65 | 43.71 | 38 | 0 | wallstreetbets 65 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06txo/) |
| VST | 2026-10-05 04:15 | mention spike | 14 | 19.29 | 14 | 0 | wallstreetbets 14 | NYSE | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek61hl/) |
| NVDA | 2026-10-06 14:02 | mention spike | 93 | 76.57 | 74 | 0 | wallstreetbets 93 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0drw2/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
