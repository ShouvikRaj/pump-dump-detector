# Stage 1 candidates

Updated 2026-10-07T17:18:10Z by run `37657898774`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 119 | 37.57 | 98 | 0 | wallstreetbets 117, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| APLD | 2026-10-05 14:23 | mention spike | 56 | 19.57 | 33 | 1 | wallstreetbets 56 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| BIYA | 2026-10-07 16:38 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x00v08/) |
| BULL | 2026-10-07 12:08 | mention spike | 64 | 1.14 | 25 | 0 | wallstreetbets 64 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 11 | 1.86 | 5 | 0 | pennystocks 6, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| CRWD | 2026-10-06 23:59 | mention spike | 12 | 4.0 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 4.0 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peguo09/) |
| HTZ | 2026-10-06 16:43 | mention spike | 116 | 9.71 | 66 | 3 | wallstreetbets 98, pennystocks 17, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IWM | 2026-10-06 00:59 | mention spike | 19 | 8.43 | 13 | 0 | wallstreetbets 19 | NYSE Arca | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegv1lw/) |
| OKLO | 2026-10-06 18:14 | mention spike | 12 | 4.43 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| PENG | 2026-10-06 18:01 | mention spike | 44 | 1.14 | 21 | 1 | wallstreetbets 44 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.43 | 12 | 0 | wallstreetbets 13 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegbq6w/) |
| SOXL | 2026-10-07 12:34 | mention spike | 39 | 13.0 | 14 | 0 | wallstreetbets 39 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegeue5/) |
| NOK | 2026-10-06 15:49 | mention spike | 5 | 2.71 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| VOO | 2026-10-06 16:15 | mention spike | 16 | 10.86 | 15 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegoezm/) |
| SOXS | 2026-10-07 12:08 | mention spike | 13 | 4.0 | 4 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7xf2/) |
| AVGO | 2026-10-06 19:34 | mention spike | 30 | 19.71 | 24 | 1 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegc8y1/) |
| CEG | 2026-10-06 13:36 | mention spike | 8 | 5.0 | 4 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7sww/) |
| INTC | 2026-10-06 18:28 | mention spike | 24 | 18.71 | 21 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 16 | 13.43 | 13 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 84 | 43.0 | 46 | 0 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 19 | 17.71 | 15 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegv9dg/) |
| NVDA | 2026-10-06 14:02 | mention spike | 134 | 72.57 | 109 | 1 | wallstreetbets 133, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefiodp/) |
| CRWV | 2026-10-06 13:49 | mention spike | 7 | 4.29 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SPCX | 2026-10-05 14:51 | mention spike | 67 | 58.43 | 53 | 0 | wallstreetbets 67 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 6 | 4.29 | 2 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pee6buo/) |
| QCOM | 2026-10-05 21:14 | mention spike | 2 | 2.86 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzz2zn/) |
| MRNA | 2026-10-06 14:02 | mention spike | 1 | 9.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 337 | 209.86 | 178 | 2 | wallstreetbets 337 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegv7rh/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefuj3c/) |
| QQQ | 2026-10-06 11:49 | mention spike | 92 | 99.86 | 64 | 0 | wallstreetbets 92 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegv47n/) |
| VEEA | 2026-10-05 15:33 | mention spike | 10 | 8.0 | 4 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pegci2y/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
