# Stage 1 candidates

Updated 2026-10-06T21:47:14Z by run `37536181614`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 135 | 29.43 | 112 | 0 | wallstreetbets 135 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wze9hx/) |
| AVGO | 2026-10-06 19:34 | mention spike | 41 | 17.71 | 33 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/peae4vx/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CIRC | 2026-10-06 17:21 | mention spike | 11 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 4, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 10 | 4.0 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/peag1fo/) |
| HTZ | 2026-10-06 16:43 | mention spike | 95 | 2.86 | 51 | 1 | wallstreetbets 87, pennystocks 7, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzd3xx/) |
| MRVL | 2026-10-06 13:36 | mention spike | 54 | 7.14 | 40 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| MSTR | 2026-10-06 08:17 | mention spike | 17 | 6.29 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NOK | 2026-10-06 15:49 | mention spike | 10 | 2.0 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peafz14/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 3.57 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 39 | 0.57 | 17 | 1 | wallstreetbets 39 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 16 | 4.86 | 12 | 0 | wallstreetbets 16 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyrwmk/) |
| VOO | 2026-10-06 16:15 | mention spike | 21 | 9.86 | 18 | 0 | wallstreetbets 21 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzep7s/comment/peb2lt9/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 12.86 | 26 | 0 | wallstreetbets 47 | NYSE | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9r4oc/) |
| APLD | 2026-10-05 14:23 | mention spike | 39 | 16.0 | 24 | 1 | wallstreetbets 39 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peatiok/) |
| INTC | 2026-10-06 18:28 | mention spike | 33 | 15.86 | 26 | 0 | wallstreetbets 33 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peagfra/) |
| SPCX | 2026-10-05 14:51 | mention spike | 118 | 49.86 | 74 | 0 | wallstreetbets 118 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 17 | 2.29 | 4 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 4 | 2.43 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| MRNA | 2026-10-06 14:02 | mention spike | 19 | 9.29 | 19 | 0 | wallstreetbets 19 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| NVDA | 2026-10-06 14:02 | mention spike | 108 | 68.29 | 88 | 0 | wallstreetbets 108 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcyv9/) |
| SPY | 2026-10-06 17:08 | mention spike | 376 | 196.71 | 202 | 1 | wallstreetbets 374, smallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 5 | 0.71 | 3 | 0 | wallstreetbets 5 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| QQQ | 2026-10-06 11:49 | mention spike | 141 | 89.57 | 80 | 0 | wallstreetbets 141 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peao66m/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 7.43 | 11 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea97nh/) |
| VEEA | 2026-10-05 15:33 | mention spike | 14 | 6.71 | 7 | 0 | pennystocks 14 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9qlen/) |
| ALEC | 2026-10-05 23:41 | mention spike | 7 | 1.14 | 2 | 0 | pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9m126/) |
| GME | 2026-10-05 16:24 | mention spike | 13 | 8.29 | 11 | 0 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 32 | 22.0 | 27 | 0 | wallstreetbets 30, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzdzq5/) |
| TSM | 2026-10-05 15:18 | mention spike | 2 | 6.14 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 1 | 4.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 3 | 6.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/peag1fo/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| DELL | 2026-10-05 16:38 | mention spike | 6 | 6.57 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/peaflc1/) |
| SDEV | 2026-10-05 14:09 | mention spike | 4 | 8.0 | 4 | 0 | pennystocks 2, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
