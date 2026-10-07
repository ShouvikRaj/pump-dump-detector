# Stage 1 candidates

Updated 2026-10-07T14:21:42Z by run `37635901766`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 160 | 30.86 | 127 | 0 | wallstreetbets 158, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| BULL | 2026-10-07 12:08 | mention spike | 61 | 1.0 | 24 | 1 | wallstreetbets 61 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 1.57 | 5 | 0 | pennystocks 7, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefpeuv/) |
| CRWD | 2026-10-06 23:59 | mention spike | 13 | 3.71 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peetkcr/) |
| GLD | 2026-10-07 13:01 | mention spike | 12 | 4.0 | 7 | 0 | wallstreetbets 12 | NYSE Arca | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefp0vg/) |
| HTZ | 2026-10-06 16:43 | mention spike | 131 | 3.29 | 69 | 3 | wallstreetbets 116, pennystocks 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| NOK | 2026-10-06 15:49 | mention spike | 12 | 1.71 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| OKLO | 2026-10-06 18:14 | mention spike | 13 | 4.14 | 9 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 43 | 0.86 | 20 | 1 | wallstreetbets 43 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.43 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| SOXL | 2026-10-07 12:34 | mention spike | 38 | 13.57 | 12 | 0 | wallstreetbets 38 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefnj68/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 7.86 | 10 | 0 | wallstreetbets 16 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefjr8u/) |
| SOXS | 2026-10-07 12:08 | mention spike | 12 | 4.43 | 4 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pef8xla/) |
| AVGO | 2026-10-06 19:34 | mention spike | 38 | 18.57 | 30 | 1 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefp21y/) |
| CEG | 2026-10-06 13:36 | mention spike | 13 | 4.14 | 8 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| INTC | 2026-10-06 18:28 | mention spike | 33 | 17.57 | 31 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 24 | 12.0 | 20 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| VOO | 2026-10-06 16:15 | mention spike | 18 | 10.57 | 17 | 0 | wallstreetbets 18 | NYSE Arca | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peeynbd/) |
| SNDK | 2026-10-07 10:09 | mention spike | 80 | 41.86 | 45 | 0 | wallstreetbets 80 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 27 | 16.43 | 22 | 0 | wallstreetbets 27 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefo6o0/) |
| NVDA | 2026-10-06 14:02 | mention spike | 125 | 71.0 | 101 | 1 | wallstreetbets 124, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| APLD | 2026-10-05 14:23 | mention spike | 34 | 19.14 | 25 | 1 | wallstreetbets 34 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 8.14 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefiodp/) |
| CRWV | 2026-10-06 13:49 | mention spike | 5 | 5.14 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| SPCX | 2026-10-05 14:51 | mention spike | 80 | 58.0 | 56 | 0 | wallstreetbets 80 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 17 | 2.71 | 4 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRNA | 2026-10-06 14:02 | mention spike | 4 | 9.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 365 | 203.57 | 185 | 2 | wallstreetbets 363, smallstreetbets 2 | NYSE Arca | #16 | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| QQQ | 2026-10-06 11:49 | mention spike | 99 | 96.86 | 64 | 0 | wallstreetbets 99 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefnayn/) |
| VEEA | 2026-10-05 15:33 | mention spike | 11 | 7.71 | 4 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeybem/) |
| ALEC | 2026-10-05 23:41 | mention spike | 4 | 1.86 | 1 | 0 | pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeexod/) |
| GME | 2026-10-05 16:24 | mention spike | 6 | 9.71 | 6 | 0 | wallstreetbets 5, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzueyi/comment/pefnzh9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
