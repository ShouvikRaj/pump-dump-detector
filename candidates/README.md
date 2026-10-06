# Stage 1 candidates

Updated 2026-10-06T15:22:33Z by run `37486831983`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 11 | 0.29 | 6 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe807w3/) |
| AMD | 2026-10-06 14:55 | mention spike | 80 | 31.43 | 69 | 0 | wallstreetbets 80 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz4re0/) |
| APLD | 2026-10-05 14:23 | mention spike | 43 | 14.57 | 26 | 1 | wallstreetbets 43 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 16 | 2.14 | 12 | 0 | wallstreetbets 16 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8hio9/) |
| CRWV | 2026-10-06 13:49 | mention spike | 10 | 4.0 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7y557/) |
| GME | 2026-10-05 16:24 | mention spike | 24 | 6.29 | 18 | 0 | wallstreetbets 23, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| IWM | 2026-10-06 00:59 | mention spike | 16 | 6.71 | 11 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8hdo6/) |
| MRNA | 2026-10-06 14:02 | mention spike | 29 | 7.57 | 28 | 0 | wallstreetbets 29 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe86oyc/) |
| MRVL | 2026-10-06 13:36 | mention spike | 48 | 6.86 | 40 | 0 | wallstreetbets 48 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 17 | 6.14 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NVAX | 2026-10-06 13:49 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| NVDA | 2026-10-06 14:02 | mention spike | 143 | 64.29 | 114 | 0 | wallstreetbets 143 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz2ms8/) |
| QCOM | 2026-10-05 21:14 | mention spike | 12 | 1.57 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 182 | 82.29 | 96 | 0 | wallstreetbets 181, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 203 | 35.0 | 122 | 0 | wallstreetbets 203 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| VEEA | 2026-10-05 15:33 | mention spike | 16 | 5.43 | 10 | 0 | pennystocks 16 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe7tpj3/) |
| MSFT | 2026-10-05 21:14 | mention spike | 34 | 21.14 | 27 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8eed0/) |
| TSM | 2026-10-05 15:18 | mention spike | 8 | 5.43 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 3.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| IREN | 2026-10-05 17:49 | mention spike | 7 | 5.29 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8i5zp/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| VST | 2026-10-05 04:15 | mention spike | 33 | 12.71 | 18 | 0 | wallstreetbets 33 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8hio9/) |
| DELL | 2026-10-05 16:38 | mention spike | 5 | 7.29 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe8dpza/) |
| SDEV | 2026-10-05 14:09 | mention spike | 7 | 7.43 | 5 | 0 | wallstreetbets 5, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wz4rhh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
