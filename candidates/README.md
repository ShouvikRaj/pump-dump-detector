# Stage 1 candidates

Updated 2026-10-06T19:34:24Z by run `37519866940`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 120 | 30.57 | 103 | 0 | wallstreetbets 120 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz83mm/) |
| APLD | 2026-10-05 14:23 | mention spike | 42 | 15.57 | 26 | 1 | wallstreetbets 42 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CIRC | 2026-10-06 17:21 | mention spike | 11 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 4, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 11 | 3.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/pe9s9pk/) |
| HTZ | 2026-10-06 16:43 | mention spike | 85 | 2.86 | 45 | 0 | wallstreetbets 81, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzasrs/) |
| INFQ | 2026-10-06 16:43 | mention spike | 18 | 2.29 | 5 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| INTC | 2026-10-06 18:28 | mention spike | 32 | 15.86 | 25 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyk0r6/) |
| MRVL | 2026-10-06 13:36 | mention spike | 52 | 7.0 | 41 | 0 | wallstreetbets 52 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 3.43 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 23 | 0.43 | 12 | 1 | wallstreetbets 23 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea638h/) |
| SPCX | 2026-10-05 14:51 | mention spike | 168 | 42.71 | 103 | 0 | wallstreetbets 168 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| VOO | 2026-10-06 16:15 | mention spike | 20 | 10.14 | 18 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea8yj1/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 12.86 | 26 | 0 | wallstreetbets 47 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9r4oc/) |
| AVGO | 2026-10-06 19:34 | mention spike | 41 | 18.0 | 34 | 0 | wallstreetbets 41 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea6pv1/) |
| QCOM | 2026-10-05 21:14 | mention spike | 9 | 1.86 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| SKHY | 2026-10-06 18:54 | mention spike | 11 | 4.86 | 8 | 0 | wallstreetbets 11 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyrwmk/) |
| MRNA | 2026-10-06 14:02 | mention spike | 21 | 8.86 | 21 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe91scd/) |
| NVDA | 2026-10-06 14:02 | mention spike | 120 | 66.43 | 100 | 0 | wallstreetbets 120 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz9x82/) |
| SPY | 2026-10-06 17:08 | mention spike | 381 | 195.57 | 199 | 1 | wallstreetbets 377, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 5 | 0.71 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| QQQ | 2026-10-06 11:49 | mention spike | 161 | 87.57 | 90 | 0 | wallstreetbets 160, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 7.29 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE Arca | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea97nh/) |
| NOK | 2026-10-06 15:49 | mention spike | 9 | 2.0 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea6hf2/) |
| VEEA | 2026-10-05 15:33 | mention spike | 16 | 6.43 | 9 | 0 | pennystocks 16 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9qlen/) |
| ALEC | 2026-10-05 23:41 | mention spike | 9 | 0.86 | 3 | 0 | pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9m126/) |
| GME | 2026-10-05 16:24 | mention spike | 14 | 8.14 | 12 | 0 | wallstreetbets 13, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 32 | 21.57 | 26 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea4sgg/) |
| TSM | 2026-10-05 15:18 | mention spike | 4 | 5.86 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 4.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 4 | 5.71 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| DELL | 2026-10-05 16:38 | mention spike | 5 | 6.57 | 3 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe92l5t/) |
| SDEV | 2026-10-05 14:09 | mention spike | 4 | 8.0 | 4 | 0 | pennystocks 2, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
