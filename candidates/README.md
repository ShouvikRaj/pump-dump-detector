# Stage 1 candidates

Updated 2026-10-06T18:54:59Z by run `37514814513`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 112 | 30.57 | 96 | 0 | wallstreetbets 112 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz83mm/) |
| APLD | 2026-10-05 14:23 | mention spike | 46 | 15.14 | 28 | 1 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 3, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 11 | 3.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/pe9s9pk/) |
| HTZ | 2026-10-06 16:43 | mention spike | 82 | 3.0 | 45 | 0 | wallstreetbets 78, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzasrs/) |
| INFQ | 2026-10-06 16:43 | mention spike | 19 | 2.14 | 6 | 0 | wallstreetbets 18, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| INTC | 2026-10-06 18:28 | mention spike | 31 | 16.29 | 25 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyk0r6/) |
| MRVL | 2026-10-06 13:36 | mention spike | 52 | 7.0 | 41 | 0 | wallstreetbets 52 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| OKLO | 2026-10-06 18:14 | mention spike | 17 | 3.57 | 11 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 18 | 0.43 | 9 | 0 | wallstreetbets 18 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9xkh0/) |
| QCOM | 2026-10-05 21:14 | mention spike | 10 | 1.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| SPCX | 2026-10-05 14:51 | mention spike | 169 | 42.0 | 105 | 0 | wallstreetbets 169 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| VOO | 2026-10-06 16:15 | mention spike | 18 | 10.14 | 16 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz0kg4/comment/pe9igek/) |
| VST | 2026-10-05 04:15 | mention spike | 48 | 12.71 | 26 | 0 | wallstreetbets 48 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9r4oc/) |
| SKHY | 2026-10-06 18:54 | mention spike | 11 | 4.86 | 8 | 0 | wallstreetbets 11 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyrwmk/) |
| MRNA | 2026-10-06 14:02 | mention spike | 22 | 8.71 | 22 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe91scd/) |
| NVDA | 2026-10-06 14:02 | mention spike | 136 | 64.29 | 108 | 0 | wallstreetbets 136 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz9x82/) |
| SPY | 2026-10-06 17:08 | mention spike | 390 | 194.57 | 203 | 1 | wallstreetbets 386, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 7 | 0.43 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| QQQ | 2026-10-06 11:49 | mention spike | 165 | 87.29 | 92 | 0 | wallstreetbets 164, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 7.14 | 12 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9n8lj/) |
| NOK | 2026-10-06 15:49 | mention spike | 9 | 1.86 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ahb0/) |
| VEEA | 2026-10-05 15:33 | mention spike | 17 | 6.29 | 9 | 0 | pennystocks 17 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9qlen/) |
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.71 | 3 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9m126/) |
| GME | 2026-10-05 16:24 | mention spike | 13 | 8.14 | 11 | 0 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 31 | 21.43 | 24 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9bvid/) |
| TSM | 2026-10-05 15:18 | mention spike | 5 | 5.86 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 4.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 5 | 5.57 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| DELL | 2026-10-05 16:38 | mention spike | 5 | 6.57 | 3 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe92l5t/) |
| SDEV | 2026-10-05 14:09 | mention spike | 4 | 7.86 | 4 | 0 | pennystocks 2, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
