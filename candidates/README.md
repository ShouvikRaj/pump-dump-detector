# Stage 1 candidates

Updated 2026-10-07T14:08:24Z by run `37634078577`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 158 | 30.57 | 124 | 0 | wallstreetbets 156, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| BULL | 2026-10-07 12:08 | mention spike | 61 | 1.0 | 24 | 1 | wallstreetbets 61 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CRWD | 2026-10-06 23:59 | mention spike | 13 | 3.71 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peetkcr/) |
| GLD | 2026-10-07 13:01 | mention spike | 11 | 4.0 | 6 | 0 | wallstreetbets 11 | NYSE Arca | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pef7yx6/) |
| HTZ | 2026-10-06 16:43 | mention spike | 127 | 3.29 | 67 | 3 | wallstreetbets 112, pennystocks 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzn9uv/) |
| IWM | 2026-10-06 00:59 | mention spike | 17 | 7.71 | 11 | 0 | wallstreetbets 17 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefjr8u/) |
| NOK | 2026-10-06 15:49 | mention spike | 12 | 1.71 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| OKLO | 2026-10-06 18:14 | mention spike | 13 | 4.14 | 9 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 42 | 0.86 | 19 | 1 | wallstreetbets 42 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.43 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| SOXL | 2026-10-07 12:34 | mention spike | 37 | 13.57 | 11 | 0 | wallstreetbets 37 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefkguh/) |
| SOXS | 2026-10-07 12:08 | mention spike | 13 | 4.29 | 5 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pef8xla/) |
| AVGO | 2026-10-06 19:34 | mention spike | 40 | 18.0 | 33 | 1 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peffpgw/) |
| CEG | 2026-10-06 13:36 | mention spike | 14 | 4.0 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| INTC | 2026-10-06 18:28 | mention spike | 34 | 17.43 | 31 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 26 | 11.71 | 22 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| VOO | 2026-10-06 16:15 | mention spike | 18 | 10.57 | 17 | 0 | wallstreetbets 18 | NYSE Arca | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peeynbd/) |
| SNDK | 2026-10-07 10:09 | mention spike | 84 | 41.0 | 46 | 0 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 27 | 16.29 | 23 | 0 | wallstreetbets 27 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefjsxo/) |
| NVDA | 2026-10-06 14:02 | mention spike | 127 | 71.0 | 104 | 1 | wallstreetbets 126, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| APLD | 2026-10-05 14:23 | mention spike | 36 | 18.86 | 27 | 1 | wallstreetbets 36 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 1.43 | 4 | 0 | pennystocks 6, wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefk5bs/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 8.14 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefiodp/) |
| CRWV | 2026-10-06 13:49 | mention spike | 4 | 5.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| SPCX | 2026-10-05 14:51 | mention spike | 85 | 57.14 | 57 | 0 | wallstreetbets 85 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 18 | 2.57 | 4 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRNA | 2026-10-06 14:02 | mention spike | 6 | 8.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 361 | 202.86 | 187 | 2 | wallstreetbets 359, smallstreetbets 2 | NYSE Arca | #16 | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| QQQ | 2026-10-06 11:49 | mention spike | 98 | 96.43 | 64 | 0 | wallstreetbets 98 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefl0u2/) |
| VEEA | 2026-10-05 15:33 | mention spike | 11 | 7.71 | 4 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeybem/) |
| ALEC | 2026-10-05 23:41 | mention spike | 4 | 1.86 | 1 | 0 | pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeexod/) |
| GME | 2026-10-05 16:24 | mention spike | 5 | 9.71 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecyki8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
