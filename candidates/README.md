# Stage 1 candidates

Updated 2026-10-06T19:21:08Z by run `37518202067`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 120 | 30.43 | 102 | 0 | wallstreetbets 120 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz83mm/) |
| APLD | 2026-10-05 14:23 | mention spike | 42 | 15.71 | 25 | 1 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CIRC | 2026-10-06 17:21 | mention spike | 11 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 4, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 11 | 3.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/pe9s9pk/) |
| HTZ | 2026-10-06 16:43 | mention spike | 85 | 3.0 | 45 | 0 | wallstreetbets 81, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzasrs/) |
| INFQ | 2026-10-06 16:43 | mention spike | 18 | 2.29 | 5 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| INTC | 2026-10-06 18:28 | mention spike | 32 | 16.14 | 25 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyk0r6/) |
| MRVL | 2026-10-06 13:36 | mention spike | 52 | 7.0 | 41 | 0 | wallstreetbets 52 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 3.57 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 23 | 0.43 | 12 | 1 | wallstreetbets 23 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea638h/) |
| QCOM | 2026-10-05 21:14 | mention spike | 10 | 1.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| SPCX | 2026-10-05 14:51 | mention spike | 170 | 42.43 | 104 | 0 | wallstreetbets 170 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| VST | 2026-10-05 04:15 | mention spike | 48 | 12.71 | 26 | 0 | wallstreetbets 48 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9r4oc/) |
| SKHY | 2026-10-06 18:54 | mention spike | 11 | 4.86 | 8 | 0 | wallstreetbets 11 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyrwmk/) |
| VOO | 2026-10-06 16:15 | mention spike | 18 | 10.29 | 16 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea5o7k/) |
| MRNA | 2026-10-06 14:02 | mention spike | 21 | 8.86 | 21 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe91scd/) |
| NVDA | 2026-10-06 14:02 | mention spike | 121 | 66.0 | 101 | 0 | wallstreetbets 121 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz9x82/) |
| SPY | 2026-10-06 17:08 | mention spike | 377 | 195.57 | 198 | 1 | wallstreetbets 373, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 5 | 0.71 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| QQQ | 2026-10-06 11:49 | mention spike | 163 | 87.14 | 90 | 0 | wallstreetbets 162, smallstreetbets 1 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| IWM | 2026-10-06 00:59 | mention spike | 13 | 7.29 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | NYSE Arca | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9n8lj/) |
| NOK | 2026-10-06 15:49 | mention spike | 8 | 2.0 | 5 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ahb0/) |
| VEEA | 2026-10-05 15:33 | mention spike | 16 | 6.43 | 9 | 0 | pennystocks 16 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9qlen/) |
| ALEC | 2026-10-05 23:41 | mention spike | 9 | 0.86 | 3 | 0 | pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9m126/) |
| GME | 2026-10-05 16:24 | mention spike | 14 | 8.14 | 12 | 0 | wallstreetbets 13, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 32 | 21.57 | 26 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea4sgg/) |
| TSM | 2026-10-05 15:18 | mention spike | 4 | 5.86 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 4.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 4 | 5.71 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| DELL | 2026-10-05 16:38 | mention spike | 5 | 6.57 | 3 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe92l5t/) |
| SDEV | 2026-10-05 14:09 | mention spike | 5 | 7.86 | 5 | 0 | wallstreetbets 3, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
