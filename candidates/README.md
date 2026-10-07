# Stage 1 candidates

Updated 2026-10-07T11:28:50Z by run `37614251075`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 173 | 29.0 | 134 | 0 | wallstreetbets 172, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wznjo8/) |
| AVGO | 2026-10-06 19:34 | mention spike | 44 | 18.43 | 35 | 1 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peem3ah/) |
| CEG | 2026-10-06 13:36 | mention spike | 23 | 2.71 | 16 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| CRWD | 2026-10-06 23:59 | mention spike | 11 | 3.57 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peep4ki/) |
| HTZ | 2026-10-06 16:43 | mention spike | 114 | 3.14 | 64 | 3 | wallstreetbets 100, pennystocks 13, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzn9uv/) |
| INTC | 2026-10-06 18:28 | mention spike | 39 | 16.57 | 30 | 0 | wallstreetbets 39 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| MRVL | 2026-10-06 13:36 | mention spike | 56 | 7.43 | 42 | 0 | wallstreetbets 56 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| NOK | 2026-10-06 15:49 | mention spike | 11 | 1.71 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| OKLO | 2026-10-06 18:14 | mention spike | 17 | 3.57 | 11 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 41 | 0.71 | 17 | 1 | wallstreetbets 41 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 15 | 5.14 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| SNDK | 2026-10-07 10:09 | mention spike | 91 | 39.0 | 52 | 0 | wallstreetbets 91 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze66b/) |
| VOO | 2026-10-06 16:15 | mention spike | 19 | 10.57 | 17 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/pedvwh5/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 13.57 | 30 | 0 | wallstreetbets 47 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peeei7r/) |
| NVDA | 2026-10-06 14:02 | mention spike | 137 | 69.71 | 113 | 1 | wallstreetbets 136, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/) |
| APLD | 2026-10-05 14:23 | mention spike | 38 | 18.14 | 28 | 1 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wztcrn/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.86 | 4 | 1 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peb9jxf/) |
| MSTR | 2026-10-06 08:17 | mention spike | 6 | 7.86 | 6 | 0 | wallstreetbets 6 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peblv2o/) |
| CRWV | 2026-10-06 13:49 | mention spike | 5 | 4.71 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/peag1fo/) |
| SPCX | 2026-10-05 14:51 | mention spike | 104 | 53.86 | 64 | 0 | wallstreetbets 104 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 18 | 2.57 | 4 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 4 | 2.43 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| MRNA | 2026-10-06 14:02 | mention spike | 13 | 8.43 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| SPY | 2026-10-06 17:08 | mention spike | 391 | 196.57 | 207 | 2 | wallstreetbets 389, smallstreetbets 2 | NYSE Arca | #7 | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7w6nl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 124 | 92.29 | 74 | 0 | wallstreetbets 124 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peenjdj/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 7.86 | 11 | 0 | wallstreetbets 15 | NYSE Arca | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/peefm86/) |
| VEEA | 2026-10-05 15:33 | mention spike | 13 | 7.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peehvkb/) |
| ALEC | 2026-10-05 23:41 | mention spike | 6 | 1.57 | 2 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzmvzx/comment/peeexod/) |
| GME | 2026-10-05 16:24 | mention spike | 8 | 9.29 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecyki8/) |
| MSFT | 2026-10-05 21:14 | mention spike | 31 | 22.86 | 25 | 0 | wallstreetbets 29, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzdzq5/) |
| TSM | 2026-10-05 15:18 | mention spike | 5 | 5.71 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pedul7m/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
