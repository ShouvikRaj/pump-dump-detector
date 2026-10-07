# Stage 1 candidates

Updated 2026-10-07T15:43:53Z by run `37646218309`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 134 | 35.0 | 109 | 0 | wallstreetbets 132, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| APLD | 2026-10-05 14:23 | mention spike | 51 | 19.57 | 32 | 1 | wallstreetbets 51 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| BULL | 2026-10-07 12:08 | mention spike | 62 | 1.14 | 24 | 0 | wallstreetbets 62 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 12 | 1.71 | 5 | 0 | pennystocks 7, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| CRWD | 2026-10-06 23:59 | mention spike | 12 | 3.86 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peetkcr/) |
| GLD | 2026-10-07 13:01 | mention spike | 14 | 4.0 | 8 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg8ue2/) |
| HTZ | 2026-10-06 16:43 | mention spike | 148 | 3.29 | 76 | 3 | wallstreetbets 129, pennystocks 18, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 8.14 | 12 | 0 | wallstreetbets 16 | NYSE Arca | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7b3s/) |
| OKLO | 2026-10-06 18:14 | mention spike | 12 | 4.43 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| PENG | 2026-10-06 18:01 | mention spike | 43 | 1.14 | 20 | 1 | wallstreetbets 43 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.29 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| SOXL | 2026-10-07 12:34 | mention spike | 41 | 12.86 | 14 | 0 | wallstreetbets 41 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg5bq3/) |
| NOK | 2026-10-06 15:49 | mention spike | 6 | 2.57 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| VOO | 2026-10-06 16:15 | mention spike | 17 | 10.71 | 16 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peeynbd/) |
| SOXS | 2026-10-07 12:08 | mention spike | 13 | 4.0 | 4 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7xf2/) |
| AVGO | 2026-10-06 19:34 | mention spike | 33 | 19.29 | 26 | 1 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg8p1r/) |
| CEG | 2026-10-06 13:36 | mention spike | 12 | 4.43 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7sww/) |
| INTC | 2026-10-06 18:28 | mention spike | 24 | 18.57 | 22 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 19 | 12.86 | 14 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 81 | 43.0 | 45 | 0 | wallstreetbets 81 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 21 | 17.14 | 17 | 0 | wallstreetbets 21 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefo6o0/) |
| NVDA | 2026-10-06 14:02 | mention spike | 132 | 71.86 | 108 | 1 | wallstreetbets 131, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefiodp/) |
| CRWV | 2026-10-06 13:49 | mention spike | 6 | 4.43 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| SPCX | 2026-10-05 14:51 | mention spike | 70 | 57.86 | 51 | 0 | wallstreetbets 70 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 12 | 3.43 | 3 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 1 | 3.0 | 1 | 0 | smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzz2zn/) |
| MRNA | 2026-10-06 14:02 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 354 | 205.86 | 183 | 2 | wallstreetbets 354 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg926f/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefuj3c/) |
| QQQ | 2026-10-06 11:49 | mention spike | 99 | 97.86 | 66 | 0 | wallstreetbets 99 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/peg66qi/) |
| VEEA | 2026-10-05 15:33 | mention spike | 10 | 7.86 | 4 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeybem/) |
| ALEC | 2026-10-05 23:41 | mention spike | 6 | 1.86 | 2 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefvj80/) |
| GME | 2026-10-05 16:24 | mention spike | 6 | 9.71 | 6 | 0 | wallstreetbets 5, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzueyi/comment/pefnzh9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
