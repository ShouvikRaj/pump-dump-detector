# Stage 1 candidates

Updated 2026-10-07T16:10:36Z by run `37649869613`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 135 | 35.0 | 110 | 0 | wallstreetbets 133, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| APLD | 2026-10-05 14:23 | mention spike | 50 | 19.86 | 30 | 1 | wallstreetbets 50 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| BULL | 2026-10-07 12:08 | mention spike | 62 | 1.14 | 24 | 0 | wallstreetbets 62 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 12 | 1.71 | 5 | 0 | pennystocks 7, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| CRWD | 2026-10-06 23:59 | mention spike | 11 | 4.0 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peetkcr/) |
| GLD | 2026-10-07 13:01 | mention spike | 14 | 4.0 | 8 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg8ue2/) |
| HTZ | 2026-10-06 16:43 | mention spike | 152 | 3.57 | 77 | 3 | wallstreetbets 132, pennystocks 19, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IWM | 2026-10-06 00:59 | mention spike | 17 | 8.29 | 11 | 0 | wallstreetbets 17 | NYSE Arca | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegd6x7/) |
| OKLO | 2026-10-06 18:14 | mention spike | 12 | 4.43 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| PENG | 2026-10-06 18:01 | mention spike | 43 | 1.14 | 20 | 1 | wallstreetbets 43 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 14 | 5.29 | 12 | 0 | wallstreetbets 14 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegbq6w/) |
| SOXL | 2026-10-07 12:34 | mention spike | 41 | 13.0 | 14 | 0 | wallstreetbets 41 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegeue5/) |
| NOK | 2026-10-06 15:49 | mention spike | 6 | 2.57 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeuz2k/) |
| VOO | 2026-10-06 16:15 | mention spike | 15 | 11.0 | 14 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/peeynbd/) |
| SOXS | 2026-10-07 12:08 | mention spike | 13 | 4.0 | 4 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7xf2/) |
| AVGO | 2026-10-06 19:34 | mention spike | 32 | 19.57 | 26 | 1 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegc8y1/) |
| CEG | 2026-10-06 13:36 | mention spike | 12 | 4.43 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7sww/) |
| INTC | 2026-10-06 18:28 | mention spike | 24 | 18.57 | 22 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 19 | 12.86 | 14 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 84 | 43.0 | 47 | 0 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 20 | 17.29 | 16 | 0 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefo6o0/) |
| NVDA | 2026-10-06 14:02 | mention spike | 134 | 72.0 | 110 | 1 | wallstreetbets 133, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 6 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefiodp/) |
| CRWV | 2026-10-06 13:49 | mention spike | 6 | 4.43 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| SPCX | 2026-10-05 14:51 | mention spike | 71 | 58.0 | 53 | 0 | wallstreetbets 71 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 10 | 3.71 | 3 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 1 | 3.0 | 1 | 0 | smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzz2zn/) |
| MRNA | 2026-10-06 14:02 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 353 | 207.14 | 180 | 2 | wallstreetbets 353 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegfmpw/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefuj3c/) |
| QQQ | 2026-10-06 11:49 | mention spike | 100 | 98.57 | 69 | 0 | wallstreetbets 100 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegfnld/) |
| VEEA | 2026-10-05 15:33 | mention spike | 11 | 7.86 | 4 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pegci2y/) |
| ALEC | 2026-10-05 23:41 | mention spike | 6 | 1.86 | 2 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/pefvj80/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
