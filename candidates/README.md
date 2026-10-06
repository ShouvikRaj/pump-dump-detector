# Stage 1 candidates

Updated 2026-10-06T14:02:51Z by run `37475545758`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 11 | 0.29 | 6 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe807w3/) |
| APLD | 2026-10-05 14:23 | mention spike | 44 | 13.86 | 25 | 1 | wallstreetbets 44 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 13 | 2.14 | 9 | 0 | wallstreetbets 13 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe800bq/) |
| CRWV | 2026-10-06 13:49 | mention spike | 10 | 4.0 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7y557/) |
| GME | 2026-10-05 16:24 | mention spike | 28 | 5.71 | 21 | 0 | wallstreetbets 27, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MRVL | 2026-10-06 13:36 | mention spike | 38 | 6.71 | 31 | 0 | wallstreetbets 38 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 18 | 6.0 | 16 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NVAX | 2026-10-06 13:49 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| QCOM | 2026-10-05 21:14 | mention spike | 13 | 1.43 | 11 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 177 | 81.14 | 94 | 0 | wallstreetbets 176, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 225 | 30.14 | 134 | 0 | wallstreetbets 225 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| VEEA | 2026-10-05 15:33 | mention spike | 20 | 4.86 | 10 | 0 | pennystocks 20 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe7tpj3/) |
| MRNA | 2026-10-06 14:02 | mention spike | 24 | 7.71 | 23 | 0 | wallstreetbets 24 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe80tby/) |
| NVDA | 2026-10-06 14:02 | mention spike | 141 | 67.71 | 109 | 0 | wallstreetbets 140, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz2ms8/) |
| IWM | 2026-10-06 00:59 | mention spike | 13 | 7.0 | 9 | 0 | wallstreetbets 12, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe6g51p/) |
| MSFT | 2026-10-05 21:14 | mention spike | 38 | 20.0 | 29 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7zswl/) |
| TSM | 2026-10-05 15:18 | mention spike | 10 | 5.14 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| DRTS | 2026-10-04 23:23 | mention spike | 5 | 3.71 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| IREN | 2026-10-05 17:49 | mention spike | 9 | 4.86 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7xx7u/) |
| PMI | 2026-10-05 13:55 | mention spike | 1 | 0.43 | 1 | 0 | pennystocks 1 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wxyz2p/comment/pe0qett/) |
| VST | 2026-10-05 04:15 | mention spike | 32 | 12.43 | 17 | 0 | wallstreetbets 32 | NYSE | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe80gsd/) |
| DELL | 2026-10-05 16:38 | mention spike | 6 | 6.86 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe80w4o/) |
| SDEV | 2026-10-05 14:09 | mention spike | 8 | 7.14 | 6 | 0 | wallstreetbets 6, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe72uup/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
