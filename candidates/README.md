# Stage 1 candidates

Updated 2026-10-07T17:57:53Z by run `37663047943`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 120 | 37.71 | 99 | 0 | wallstreetbets 118, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| APLD | 2026-10-05 14:23 | mention spike | 60 | 19.86 | 36 | 1 | wallstreetbets 60 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| BIYA | 2026-10-07 16:38 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x00v08/) |
| BULL | 2026-10-07 12:08 | mention spike | 65 | 1.14 | 26 | 0 | wallstreetbets 65 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 2.0 | 5 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| CRWD | 2026-10-06 23:59 | mention spike | 13 | 4.0 | 11 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 4.0 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peguo09/) |
| HTZ | 2026-10-06 16:43 | mention spike | 108 | 11.43 | 61 | 3 | wallstreetbets 90, pennystocks 17, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 8.57 | 12 | 0 | wallstreetbets 18 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegv1lw/) |
| LLY | 2026-10-07 17:44 | mention spike | 11 | 1.0 | 5 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh0hxo/) |
| OKLO | 2026-10-06 18:14 | mention spike | 12 | 4.43 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| PENG | 2026-10-06 18:01 | mention spike | 36 | 2.29 | 19 | 1 | wallstreetbets 36 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 14 | 5.57 | 13 | 0 | wallstreetbets 14 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh16eq/) |
| SOXL | 2026-10-07 12:34 | mention spike | 39 | 13.14 | 14 | 0 | wallstreetbets 39 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegym1x/) |
| NOK | 2026-10-06 15:49 | mention spike | 5 | 2.71 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| VOO | 2026-10-06 16:15 | mention spike | 14 | 11.0 | 14 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegoezm/) |
| SOXS | 2026-10-07 12:08 | mention spike | 13 | 3.86 | 4 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7xf2/) |
| AVGO | 2026-10-06 19:34 | mention spike | 29 | 20.29 | 22 | 1 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh5kmz/) |
| CEG | 2026-10-06 13:36 | mention spike | 6 | 5.43 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh5dvl/) |
| INTC | 2026-10-06 18:28 | mention spike | 24 | 18.43 | 21 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 16 | 13.43 | 12 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 86 | 43.0 | 48 | 0 | wallstreetbets 86 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 17 | 18.14 | 15 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh3nu5/) |
| NVDA | 2026-10-06 14:02 | mention spike | 139 | 72.43 | 110 | 1 | wallstreetbets 138, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| MSTR | 2026-10-06 08:17 | mention spike | 8 | 7.57 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh3684/) |
| CRWV | 2026-10-06 13:49 | mention spike | 7 | 4.29 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SPCX | 2026-10-05 14:51 | mention spike | 66 | 58.43 | 52 | 0 | wallstreetbets 66 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 5 | 4.43 | 1 | 0 | wallstreetbets 5 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pee6buo/) |
| QCOM | 2026-10-05 21:14 | mention spike | 2 | 2.86 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzz2zn/) |
| MRNA | 2026-10-06 14:02 | mention spike | 1 | 9.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 334 | 210.71 | 182 | 2 | wallstreetbets 334 | NYSE Arca | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh5es2/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefuj3c/) |
| QQQ | 2026-10-06 11:49 | mention spike | 89 | 99.86 | 62 | 0 | wallstreetbets 89 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peh2ctf/) |
| VEEA | 2026-10-05 15:33 | mention spike | 7 | 8.43 | 3 | 0 | pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pegci2y/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
