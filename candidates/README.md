# Stage 1 candidates

Updated 2026-10-07T14:47:57Z by run `37639642849`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 152 | 32.43 | 121 | 0 | wallstreetbets 150, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| BULL | 2026-10-07 12:08 | mention spike | 62 | 1.0 | 25 | 1 | wallstreetbets 62 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 1.57 | 5 | 0 | pennystocks 7, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefpeuv/) |
| CRWD | 2026-10-06 23:59 | mention spike | 12 | 3.86 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peetkcr/) |
| GLD | 2026-10-07 13:01 | mention spike | 13 | 4.0 | 7 | 0 | wallstreetbets 13 | NYSE Arca | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peftp0o/) |
| HTZ | 2026-10-06 16:43 | mention spike | 134 | 3.29 | 70 | 3 | wallstreetbets 118, pennystocks 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| NOK | 2026-10-06 15:49 | mention spike | 12 | 1.71 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| OKLO | 2026-10-06 18:14 | mention spike | 12 | 4.29 | 8 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 44 | 0.86 | 21 | 1 | wallstreetbets 44 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.29 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| SOXL | 2026-10-07 12:34 | mention spike | 39 | 13.29 | 13 | 0 | wallstreetbets 39 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefpum3/) |
| VOO | 2026-10-06 16:15 | mention spike | 18 | 10.57 | 17 | 0 | wallstreetbets 18 | NYSE Arca | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peeynbd/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 8.14 | 9 | 0 | wallstreetbets 14 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefjr8u/) |
| SOXS | 2026-10-07 12:08 | mention spike | 12 | 4.29 | 4 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pef8xla/) |
| AVGO | 2026-10-06 19:34 | mention spike | 36 | 18.57 | 28 | 1 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefp21y/) |
| CEG | 2026-10-06 13:36 | mention spike | 13 | 4.14 | 8 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| INTC | 2026-10-06 18:28 | mention spike | 28 | 18.0 | 26 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 22 | 12.43 | 17 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 82 | 42.86 | 46 | 0 | wallstreetbets 82 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 26 | 16.43 | 21 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefo6o0/) |
| NVDA | 2026-10-06 14:02 | mention spike | 127 | 71.0 | 102 | 1 | wallstreetbets 126, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| APLD | 2026-10-05 14:23 | mention spike | 38 | 19.43 | 28 | 1 | wallstreetbets 38 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 8.14 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefiodp/) |
| CRWV | 2026-10-06 13:49 | mention spike | 5 | 4.71 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| SPCX | 2026-10-05 14:51 | mention spike | 76 | 58.14 | 54 | 0 | wallstreetbets 76 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 16 | 2.86 | 4 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRNA | 2026-10-06 14:02 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 372 | 202.57 | 190 | 2 | wallstreetbets 370, smallstreetbets 2 | NYSE Arca | #16 | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefuj3c/) |
| QQQ | 2026-10-06 11:49 | mention spike | 105 | 97.0 | 68 | 0 | wallstreetbets 105 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefvhy7/) |
| VEEA | 2026-10-05 15:33 | mention spike | 11 | 7.71 | 4 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeybem/) |
| ALEC | 2026-10-05 23:41 | mention spike | 6 | 1.86 | 2 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefvj80/) |
| GME | 2026-10-05 16:24 | mention spike | 6 | 9.71 | 6 | 0 | wallstreetbets 5, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzueyi/comment/pefnzh9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
