# Stage 1 candidates

Updated 2026-10-06T18:41:25Z by run `37513120219`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 109 | 30.86 | 94 | 0 | wallstreetbets 109 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz83mm/) |
| APLD | 2026-10-05 14:23 | mention spike | 46 | 15.14 | 28 | 1 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 3, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 11 | 3.86 | 10 | 0 | wallstreetbets 11 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/pe9s9pk/) |
| HTZ | 2026-10-06 16:43 | mention spike | 77 | 3.0 | 42 | 0 | wallstreetbets 73, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz9isw/) |
| INFQ | 2026-10-06 16:43 | mention spike | 18 | 2.14 | 6 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| INTC | 2026-10-06 18:28 | mention spike | 31 | 16.29 | 25 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyk0r6/) |
| MRNA | 2026-10-06 14:02 | mention spike | 23 | 8.57 | 23 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe91scd/) |
| MRVL | 2026-10-06 13:36 | mention spike | 53 | 6.86 | 42 | 0 | wallstreetbets 53 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NVDA | 2026-10-06 14:02 | mention spike | 138 | 63.86 | 109 | 0 | wallstreetbets 138 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz9x82/) |
| OKLO | 2026-10-06 18:14 | mention spike | 14 | 3.57 | 10 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 16 | 0.43 | 8 | 0 | wallstreetbets 16 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ur0d/) |
| QCOM | 2026-10-05 21:14 | mention spike | 10 | 1.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| SPCX | 2026-10-05 14:51 | mention spike | 173 | 41.57 | 106 | 0 | wallstreetbets 173 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| VOO | 2026-10-06 16:15 | mention spike | 18 | 10.29 | 16 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz0kg4/comment/pe9igek/) |
| VST | 2026-10-05 04:15 | mention spike | 48 | 12.71 | 26 | 0 | wallstreetbets 48 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9r4oc/) |
| SPY | 2026-10-06 17:08 | mention spike | 398 | 193.71 | 205 | 1 | wallstreetbets 394, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 7 | 0.43 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| QQQ | 2026-10-06 11:49 | mention spike | 166 | 86.86 | 93 | 0 | wallstreetbets 165, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 7.14 | 12 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9n8lj/) |
| NOK | 2026-10-06 15:49 | mention spike | 9 | 1.86 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ahb0/) |
| VEEA | 2026-10-05 15:33 | mention spike | 17 | 6.29 | 9 | 0 | pennystocks 17 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9qlen/) |
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.71 | 3 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9m126/) |
| GME | 2026-10-05 16:24 | mention spike | 13 | 8.14 | 11 | 0 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 31 | 21.43 | 24 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9bvid/) |
| TSM | 2026-10-05 15:18 | mention spike | 7 | 5.57 | 5 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 4.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 5 | 5.57 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| DELL | 2026-10-05 16:38 | mention spike | 5 | 6.57 | 3 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe92l5t/) |
| SDEV | 2026-10-05 14:09 | mention spike | 4 | 7.86 | 4 | 0 | pennystocks 2, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
