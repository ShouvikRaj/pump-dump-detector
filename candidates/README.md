# Stage 1 candidates

Updated 2026-10-07T13:50:43Z by run `37631601900`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 158 | 31.14 | 125 | 0 | wallstreetbets 156, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| AVGO | 2026-10-06 19:34 | mention spike | 42 | 17.86 | 34 | 1 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peffpgw/) |
| BULL | 2026-10-07 12:08 | mention spike | 61 | 1.0 | 24 | 1 | wallstreetbets 61 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CEG | 2026-10-06 13:36 | mention spike | 15 | 3.86 | 10 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| CRWD | 2026-10-06 23:59 | mention spike | 13 | 3.86 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peetkcr/) |
| GLD | 2026-10-07 13:01 | mention spike | 11 | 4.0 | 6 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pef7yx6/) |
| HTZ | 2026-10-06 16:43 | mention spike | 123 | 3.29 | 66 | 3 | wallstreetbets 108, pennystocks 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzn9uv/) |
| INTC | 2026-10-06 18:28 | mention spike | 36 | 17.14 | 31 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 33 | 10.29 | 27 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| NOK | 2026-10-06 15:49 | mention spike | 12 | 1.71 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| OKLO | 2026-10-06 18:14 | mention spike | 14 | 4.0 | 9 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 41 | 0.86 | 18 | 1 | wallstreetbets 41 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.43 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| SOXL | 2026-10-07 12:34 | mention spike | 35 | 14.0 | 11 | 0 | wallstreetbets 35 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefhhpx/) |
| SOXS | 2026-10-07 12:08 | mention spike | 14 | 4.14 | 5 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pef8xla/) |
| VOO | 2026-10-06 16:15 | mention spike | 19 | 10.57 | 18 | 0 | wallstreetbets 19 | NYSE Arca | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peeynbd/) |
| SNDK | 2026-10-07 10:09 | mention spike | 81 | 40.14 | 46 | 0 | wallstreetbets 81 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 28 | 16.14 | 24 | 0 | wallstreetbets 28 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peez38u/) |
| NVDA | 2026-10-06 14:02 | mention spike | 126 | 71.0 | 103 | 1 | wallstreetbets 125, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| APLD | 2026-10-05 14:23 | mention spike | 36 | 18.86 | 27 | 1 | wallstreetbets 36 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| CIRC | 2026-10-06 17:21 | mention spike | 9 | 1.43 | 3 | 0 | pennystocks 5, wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefbygr/) |
| MSTR | 2026-10-06 08:17 | mention spike | 5 | 8.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefhpwf/) |
| CRWV | 2026-10-06 13:49 | mention spike | 4 | 5.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| SPCX | 2026-10-05 14:51 | mention spike | 84 | 56.71 | 57 | 0 | wallstreetbets 84 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 18 | 2.57 | 4 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 1 | 2.86 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| MRNA | 2026-10-06 14:02 | mention spike | 10 | 8.43 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 379 | 199.14 | 198 | 2 | wallstreetbets 377, smallstreetbets 2 | NYSE Arca | #25 | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| QQQ | 2026-10-06 11:49 | mention spike | 105 | 95.14 | 66 | 0 | wallstreetbets 105 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefhzh4/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 7.86 | 11 | 0 | wallstreetbets 16 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peet20r/) |
| VEEA | 2026-10-05 15:33 | mention spike | 11 | 7.71 | 4 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeybem/) |
| ALEC | 2026-10-05 23:41 | mention spike | 5 | 1.71 | 1 | 0 | pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeexod/) |
| GME | 2026-10-05 16:24 | mention spike | 5 | 9.71 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecyki8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
