# Stage 1 candidates

Updated 2026-10-06T18:14:53Z by run `37509711796`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 107 | 30.86 | 92 | 0 | wallstreetbets 107 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz83mm/) |
| APLD | 2026-10-05 14:23 | mention spike | 45 | 15.14 | 28 | 1 | wallstreetbets 45 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 25 | 2.14 | 17 | 0 | wallstreetbets 25 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9nwzg/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.57 | 5 | 1 | pennystocks 5, wallstreetbets 3, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wyrpw0/) |
| CRWV | 2026-10-06 13:49 | mention spike | 10 | 3.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7y557/) |
| HTZ | 2026-10-06 16:43 | mention spike | 72 | 2.86 | 37 | 0 | wallstreetbets 68, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz9isw/) |
| INFQ | 2026-10-06 16:43 | mention spike | 17 | 2.14 | 6 | 0 | wallstreetbets 16, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| MRNA | 2026-10-06 14:02 | mention spike | 26 | 8.14 | 26 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe91scd/) |
| MRVL | 2026-10-06 13:36 | mention spike | 51 | 6.86 | 41 | 0 | wallstreetbets 51 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NVAX | 2026-10-06 13:49 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| NVDA | 2026-10-06 14:02 | mention spike | 144 | 63.0 | 112 | 0 | wallstreetbets 144 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6281/) |
| PENG | 2026-10-06 18:01 | mention spike | 13 | 0.43 | 8 | 0 | wallstreetbets 13 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9kmlj/) |
| QCOM | 2026-10-05 21:14 | mention spike | 10 | 1.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 172 | 86.29 | 94 | 0 | wallstreetbets 171, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 172 | 41.29 | 107 | 0 | wallstreetbets 172 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| SPY | 2026-10-06 17:08 | mention spike | 395 | 193.0 | 205 | 1 | wallstreetbets 391, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| VOO | 2026-10-06 16:15 | mention spike | 19 | 10.14 | 17 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz0kg4/comment/pe9igek/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 12.71 | 26 | 0 | wallstreetbets 47 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9pkkm/) |
| OKLO | 2026-10-06 18:14 | mention spike | 12 | 3.57 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ot78/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 7.0 | 13 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9n8lj/) |
| NOK | 2026-10-06 15:49 | mention spike | 9 | 1.86 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9ahb0/) |
| VEEA | 2026-10-05 15:33 | mention spike | 17 | 6.0 | 9 | 0 | pennystocks 17 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9ht27/) |
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.71 | 3 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe9m126/) |
| GME | 2026-10-05 16:24 | mention spike | 13 | 8.14 | 11 | 0 | wallstreetbets 12, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 31 | 21.43 | 24 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9bvid/) |
| TSM | 2026-10-05 15:18 | mention spike | 7 | 5.57 | 5 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe98cw5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 4.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 5 | 5.57 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| DELL | 2026-10-05 16:38 | mention spike | 6 | 6.43 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe92l5t/) |
| SDEV | 2026-10-05 14:09 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 4, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
