# Stage 1 candidates

Updated 2026-10-07T22:49:35Z by run `37698530210`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 184 | 20.14 | 98 | 1 | wallstreetbets 184 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| BIYA | 2026-10-07 16:38 | mention spike | 11 | 0.0 | 8 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| BULL | 2026-10-07 12:08 | mention spike | 68 | 1.14 | 27 | 0 | wallstreetbets 68 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzv8ti/) |
| CRWD | 2026-10-06 23:59 | mention spike | 17 | 3.86 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| GLD | 2026-10-07 13:01 | mention spike | 17 | 3.43 | 11 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pehzt6j/) |
| HTZ | 2026-10-06 16:43 | mention spike | 107 | 17.86 | 60 | 2 | wallstreetbets 93, pennystocks 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzxm5j/) |
| IREN | 2026-10-07 19:18 | mention spike | 13 | 5.0 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peiol2j/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 8.71 | 10 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peiom23/) |
| LEVI | 2026-10-07 20:37 | mention spike | 13 | 0.86 | 9 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ycv/) |
| LLY | 2026-10-07 17:44 | mention spike | 11 | 1.0 | 5 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh0hxo/) |
| SMCI | 2026-10-07 20:50 | mention spike | 14 | 4.29 | 11 | 0 | wallstreetbets 14 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peira1d/) |
| UUUU | 2026-10-07 20:50 | mention spike | 11 | 2.14 | 7 | 0 | wallstreetbets 11 | NYSE American | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ltz/) |
| SOXL | 2026-10-07 12:34 | mention spike | 29 | 14.43 | 13 | 0 | wallstreetbets 29 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehx4ik/) |
| PENG | 2026-10-06 18:01 | mention spike | 10 | 6.14 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehmo5f/) |
| CIRC | 2026-10-06 17:21 | mention spike | 8 | 2.29 | 5 | 0 | pennystocks 5, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| AMD | 2026-10-06 14:55 | mention spike | 95 | 41.86 | 80 | 0 | wallstreetbets 93, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzwyoe/) |
| SKHY | 2026-10-06 18:54 | mention spike | 7 | 5.71 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh6kle/) |
| OKLO | 2026-10-06 18:14 | mention spike | 2 | 6.0 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 4 | 3.0 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehcvj2/) |
| VOO | 2026-10-06 16:15 | mention spike | 11 | 10.86 | 11 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peirtdj/) |
| SOXS | 2026-10-07 12:08 | mention spike | 10 | 4.29 | 4 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei7y2v/) |
| AVGO | 2026-10-06 19:34 | mention spike | 21 | 21.29 | 16 | 1 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei0efr/) |
| CEG | 2026-10-06 13:36 | mention spike | 6 | 5.86 | 4 | 0 | wallstreetbets 6 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/peirllx/) |
| INTC | 2026-10-06 18:28 | mention spike | 19 | 18.86 | 17 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x05wz7/) |
| MRVL | 2026-10-06 13:36 | mention spike | 13 | 13.86 | 9 | 0 | wallstreetbets 13 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pehudwc/) |
| SNDK | 2026-10-07 10:09 | mention spike | 78 | 44.29 | 48 | 0 | wallstreetbets 78 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06txo/) |
| VST | 2026-10-05 04:15 | mention spike | 16 | 18.71 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei5bvu/) |
| NVDA | 2026-10-06 14:02 | mention spike | 132 | 72.14 | 106 | 1 | wallstreetbets 131, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06lz6/) |
| MSTR | 2026-10-06 08:17 | mention spike | 5 | 7.71 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peh3684/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
