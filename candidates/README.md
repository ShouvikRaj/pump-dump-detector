# Stage 1 candidates

Updated 2026-10-06T13:36:04Z by run `37471984639`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.29 | 6 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe7rs91/) |
| APLD | 2026-10-05 14:23 | mention spike | 44 | 13.71 | 25 | 1 | wallstreetbets 44 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| GME | 2026-10-05 16:24 | mention spike | 28 | 5.57 | 21 | 0 | wallstreetbets 27, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 6.71 | 9 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe6g51p/) |
| MSFT | 2026-10-05 21:14 | mention spike | 44 | 18.86 | 33 | 0 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7uhoz/) |
| MSTR | 2026-10-06 08:17 | mention spike | 19 | 5.86 | 17 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| QCOM | 2026-10-05 21:14 | mention spike | 11 | 2.14 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7sulz/) |
| QQQ | 2026-10-06 11:49 | mention spike | 172 | 80.86 | 91 | 0 | wallstreetbets 171, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 221 | 29.14 | 136 | 0 | wallstreetbets 221 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| TSM | 2026-10-05 15:18 | mention spike | 10 | 5.14 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| VEEA | 2026-10-05 15:33 | mention spike | 21 | 4.71 | 10 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe7tpj3/) |
| CEG | 2026-10-06 13:36 | mention spike | 10 | 2.14 | 8 | 0 | wallstreetbets 10 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7v5z9/) |
| MRVL | 2026-10-06 13:36 | mention spike | 17 | 6.71 | 15 | 0 | wallstreetbets 17 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| DRTS | 2026-10-04 23:23 | mention spike | 5 | 3.71 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| IREN | 2026-10-05 17:49 | mention spike | 8 | 4.86 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe31di3/) |
| PMI | 2026-10-05 13:55 | mention spike | 2 | 0.29 | 1 | 0 | pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wxyz2p/comment/pe0qett/) |
| VST | 2026-10-05 04:15 | mention spike | 24 | 12.43 | 14 | 0 | wallstreetbets 24 | NYSE | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7v7kl/) |
| DELL | 2026-10-05 16:38 | mention spike | 6 | 6.57 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| SDEV | 2026-10-05 14:09 | mention spike | 12 | 6.57 | 8 | 0 | wallstreetbets 9, pennystocks 3 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe72uup/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
