# Stage 1 candidates

Updated 2026-10-07T19:18:01Z by run `37673271088`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 70 | 20.0 | 40 | 1 | wallstreetbets 70 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x04nzd/) |
| BIYA | 2026-10-07 16:38 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x00v08/) |
| BULL | 2026-10-07 12:08 | mention spike | 65 | 1.14 | 26 | 0 | wallstreetbets 65 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 2.0 | 5 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| CRWD | 2026-10-06 23:59 | mention spike | 13 | 3.86 | 11 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 15 | 3.57 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peguo09/) |
| HTZ | 2026-10-06 16:43 | mention spike | 106 | 15.0 | 61 | 3 | wallstreetbets 87, pennystocks 18, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 8.57 | 11 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehdomd/) |
| LLY | 2026-10-07 17:44 | mention spike | 11 | 1.0 | 5 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh0hxo/) |
| PENG | 2026-10-06 18:01 | mention spike | 29 | 3.43 | 16 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SOXL | 2026-10-07 12:34 | mention spike | 37 | 13.14 | 14 | 0 | wallstreetbets 37 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegym1x/) |
| IREN | 2026-10-07 19:18 | mention spike | 11 | 4.86 | 11 | 0 | wallstreetbets 11 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehor48/) |
| AMD | 2026-10-06 14:55 | mention spike | 111 | 39.43 | 92 | 0 | wallstreetbets 109, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| SKHY | 2026-10-06 18:54 | mention spike | 13 | 5.71 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh6kle/) |
| OKLO | 2026-10-06 18:14 | mention spike | 3 | 5.86 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 6 | 2.71 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcvj2/) |
| VOO | 2026-10-06 16:15 | mention spike | 14 | 10.86 | 14 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pegoezm/) |
| SOXS | 2026-10-07 12:08 | mention spike | 11 | 4.0 | 4 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehm2e3/) |
| AVGO | 2026-10-06 19:34 | mention spike | 26 | 20.86 | 19 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehdtqb/) |
| CEG | 2026-10-06 13:36 | mention spike | 4 | 5.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehoxio/) |
| INTC | 2026-10-06 18:28 | mention spike | 23 | 18.43 | 20 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzvgqg/) |
| MRVL | 2026-10-06 13:36 | mention spike | 14 | 13.71 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SNDK | 2026-10-07 10:09 | mention spike | 89 | 43.14 | 52 | 0 | wallstreetbets 89 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VST | 2026-10-05 04:15 | mention spike | 15 | 18.71 | 13 | 0 | wallstreetbets 15 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x04bzq/comment/pehgpkj/) |
| NVDA | 2026-10-06 14:02 | mention spike | 138 | 71.86 | 110 | 1 | wallstreetbets 137, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| MSTR | 2026-10-06 08:17 | mention spike | 7 | 7.57 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh3684/) |
| CRWV | 2026-10-06 13:49 | mention spike | 6 | 4.43 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| SPCX | 2026-10-05 14:51 | mention spike | 59 | 59.43 | 48 | 0 | wallstreetbets 59 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcfy6/) |
| INFQ | 2026-10-06 16:43 | mention spike | 3 | 4.71 | 1 | 0 | wallstreetbets 3 | NYSE | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pee6buo/) |
| QCOM | 2026-10-05 21:14 | mention spike | 3 | 2.86 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzz2zn/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
