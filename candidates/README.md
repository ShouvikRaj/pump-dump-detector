# Stage 1 candidates

Updated 2026-10-07T18:37:53Z by run `37668183728`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 119 | 38.14 | 98 | 0 | wallstreetbets 117, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| APLD | 2026-10-05 14:23 | mention spike | 61 | 20.0 | 37 | 1 | wallstreetbets 61 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| BIYA | 2026-10-07 16:38 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x00v08/) |
| BULL | 2026-10-07 12:08 | mention spike | 65 | 1.14 | 26 | 0 | wallstreetbets 65 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 2.0 | 5 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| CRWD | 2026-10-06 23:59 | mention spike | 13 | 4.0 | 11 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 3.86 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peguo09/) |
| HTZ | 2026-10-06 16:43 | mention spike | 104 | 13.86 | 61 | 3 | wallstreetbets 87, pennystocks 16, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 8.57 | 11 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehdomd/) |
| LLY | 2026-10-07 17:44 | mention spike | 11 | 1.0 | 5 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh0hxo/) |
| PENG | 2026-10-06 18:01 | mention spike | 33 | 2.71 | 18 | 1 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 14 | 5.71 | 13 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh6kle/) |
| SOXL | 2026-10-07 12:34 | mention spike | 38 | 13.0 | 14 | 0 | wallstreetbets 38 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegym1x/) |
| OKLO | 2026-10-06 18:14 | mention spike | 7 | 5.29 | 6 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 6 | 2.71 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcvj2/) |
| VOO | 2026-10-06 16:15 | mention spike | 14 | 10.86 | 14 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegoezm/) |
| SOXS | 2026-10-07 12:08 | mention spike | 12 | 3.71 | 4 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peg7xf2/) |
| AVGO | 2026-10-06 19:34 | mention spike | 27 | 20.71 | 20 | 1 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehdtqb/) |
| CEG | 2026-10-06 13:36 | mention spike | 3 | 5.86 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh5dvl/) |
| INTC | 2026-10-06 18:28 | mention spike | 24 | 18.43 | 21 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 14 | 13.71 | 11 | 0 | wallstreetbets 14 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 88 | 43.0 | 50 | 0 | wallstreetbets 88 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 14 | 18.71 | 12 | 0 | wallstreetbets 14 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehdegq/) |
| NVDA | 2026-10-06 14:02 | mention spike | 140 | 71.86 | 111 | 1 | wallstreetbets 139, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| MSTR | 2026-10-06 08:17 | mention spike | 7 | 7.71 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh3684/) |
| CRWV | 2026-10-06 13:49 | mention spike | 6 | 4.43 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SPCX | 2026-10-05 14:51 | mention spike | 63 | 58.86 | 51 | 0 | wallstreetbets 63 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcfy6/) |
| INFQ | 2026-10-06 16:43 | mention spike | 4 | 4.57 | 1 | 0 | wallstreetbets 4 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pee6buo/) |
| QCOM | 2026-10-05 21:14 | mention spike | 3 | 2.86 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzz2zn/) |
| MRNA | 2026-10-06 14:02 | mention spike | 1 | 9.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
