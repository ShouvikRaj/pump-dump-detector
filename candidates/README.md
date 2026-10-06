# Stage 1 candidates

Updated 2026-10-06T17:48:12Z by run `37506272055`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 106 | 31.0 | 91 | 0 | wallstreetbets 106 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz83mm/) |
| APLD | 2026-10-05 14:23 | mention spike | 46 | 15.0 | 29 | 1 | wallstreetbets 46 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 22 | 2.14 | 16 | 0 | wallstreetbets 22 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9eme1/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 3, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 10 | 3.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7y557/) |
| HTZ | 2026-10-06 16:43 | mention spike | 58 | 2.86 | 30 | 0 | wallstreetbets 55, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9j1zn/) |
| INFQ | 2026-10-06 16:43 | mention spike | 20 | 1.71 | 6 | 0 | wallstreetbets 19, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 6.86 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE Arca | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9hqny/) |
| MRNA | 2026-10-06 14:02 | mention spike | 27 | 8.0 | 27 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe91scd/) |
| MRVL | 2026-10-06 13:36 | mention spike | 50 | 6.86 | 40 | 0 | wallstreetbets 50 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 15 | 6.29 | 14 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NOK | 2026-10-06 15:49 | mention spike | 10 | 1.71 | 6 | 0 | wallstreetbets 10 | NYSE | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ahb0/) |
| NVAX | 2026-10-06 13:49 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| NVDA | 2026-10-06 14:02 | mention spike | 145 | 62.86 | 114 | 0 | wallstreetbets 145 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6281/) |
| QCOM | 2026-10-05 21:14 | mention spike | 11 | 1.57 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 176 | 85.57 | 99 | 0 | wallstreetbets 175, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 175 | 40.71 | 108 | 0 | wallstreetbets 175 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| SPY | 2026-10-06 17:08 | mention spike | 389 | 194.29 | 203 | 1 | wallstreetbets 385, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| VEEA | 2026-10-05 15:33 | mention spike | 21 | 5.43 | 11 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9ht27/) |
| VOO | 2026-10-06 16:15 | mention spike | 19 | 10.14 | 17 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz0kg4/comment/pe9igek/) |
| ALEC | 2026-10-05 23:41 | mention spike | 9 | 0.71 | 3 | 0 | pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9ittw/) |
| GME | 2026-10-05 16:24 | mention spike | 13 | 8.14 | 11 | 0 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 34 | 21.14 | 27 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9bvid/) |
| TSM | 2026-10-05 15:18 | mention spike | 7 | 5.57 | 5 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 3.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| IREN | 2026-10-05 17:49 | mention spike | 5 | 5.57 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| VST | 2026-10-05 04:15 | mention spike | 44 | 12.71 | 23 | 0 | wallstreetbets 44 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9gnci/) |
| DELL | 2026-10-05 16:38 | mention spike | 6 | 6.57 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe92l5t/) |
| SDEV | 2026-10-05 14:09 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 4, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
