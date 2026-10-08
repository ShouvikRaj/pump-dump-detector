# Stage 1 candidates

Updated 2026-10-08T03:41:17Z by run `37723819706`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 203 | 20.29 | 105 | 0 | wallstreetbets 203 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BIYA | 2026-10-07 16:38 | mention spike | 11 | 0.0 | 8 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| BULL | 2026-10-07 12:08 | mention spike | 69 | 1.29 | 27 | 0 | wallstreetbets 69 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CRWD | 2026-10-06 23:59 | mention spike | 14 | 4.43 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 10 | 4.43 | 9 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pehzt6j/) |
| HTZ | 2026-10-06 16:43 | mention spike | 108 | 18.57 | 63 | 1 | wallstreetbets 94, pennystocks 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IREN | 2026-10-07 19:18 | mention spike | 15 | 4.57 | 15 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekabar/) |
| IWM | 2026-10-06 00:59 | mention spike | 19 | 8.71 | 11 | 0 | wallstreetbets 19 | NYSE Arca | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0de7b/comment/pejr8dw/) |
| KEEL | 2026-10-08 03:01 | mention spike | 13 | 1.57 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekb8ct/) |
| LEVI | 2026-10-07 20:37 | mention spike | 13 | 0.86 | 9 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ycv/) |
| LLY | 2026-10-07 17:44 | mention spike | 11 | 1.0 | 5 | 0 | wallstreetbets 11 | NYSE | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh0hxo/) |
| SMCI | 2026-10-07 20:50 | mention spike | 12 | 4.0 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| UUUU | 2026-10-07 20:50 | mention spike | 11 | 2.14 | 7 | 0 | wallstreetbets 11 | NYSE American | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ltz/) |
| SOXL | 2026-10-07 12:34 | mention spike | 22 | 15.43 | 11 | 0 | wallstreetbets 22 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pejret0/) |
| PENG | 2026-10-06 18:01 | mention spike | 10 | 6.29 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 8 | 2.29 | 5 | 0 | pennystocks 5, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| AMD | 2026-10-06 14:55 | mention spike | 79 | 44.0 | 70 | 0 | wallstreetbets 77, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| SKHY | 2026-10-06 18:54 | mention spike | 7 | 6.0 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekg2te/) |
| OKLO | 2026-10-06 18:14 | mention spike | 5 | 5.86 | 3 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 3 | 3.14 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcvj2/) |
| VOO | 2026-10-06 16:15 | mention spike | 11 | 11.29 | 11 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0esk4/comment/pek37kf/) |
| SOXS | 2026-10-07 12:08 | mention spike | 9 | 4.71 | 4 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek4fx6/) |
| AVGO | 2026-10-06 19:34 | mention spike | 25 | 21.29 | 18 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek7o2c/) |
| CEG | 2026-10-06 13:36 | mention spike | 6 | 5.86 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peirllx/) |
| INTC | 2026-10-06 18:28 | mention spike | 16 | 19.0 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x05wz7/) |
| MRVL | 2026-10-06 13:36 | mention spike | 10 | 14.29 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehudwc/) |
| SNDK | 2026-10-07 10:09 | mention spike | 68 | 43.71 | 42 | 0 | wallstreetbets 68 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06txo/) |
| VST | 2026-10-05 04:15 | mention spike | 15 | 19.14 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek61hl/) |
| NVDA | 2026-10-06 14:02 | mention spike | 100 | 74.86 | 80 | 1 | wallstreetbets 99, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0drw2/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
