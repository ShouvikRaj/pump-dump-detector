# Stage 1 candidates

Updated 2026-10-06T14:42:40Z by run `37481098439`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 11 | 0.29 | 6 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe807w3/) |
| APLD | 2026-10-05 14:23 | mention spike | 44 | 14.29 | 27 | 1 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| CEG | 2026-10-06 13:36 | mention spike | 14 | 2.14 | 10 | 0 | wallstreetbets 14 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe83kpg/) |
| CRWV | 2026-10-06 13:49 | mention spike | 10 | 4.0 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7y557/) |
| GME | 2026-10-05 16:24 | mention spike | 25 | 6.14 | 19 | 0 | wallstreetbets 24, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 6.86 | 10 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe87iam/) |
| MRNA | 2026-10-06 14:02 | mention spike | 29 | 7.57 | 28 | 0 | wallstreetbets 29 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe86oyc/) |
| MRVL | 2026-10-06 13:36 | mention spike | 45 | 6.86 | 37 | 0 | wallstreetbets 45 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz1ma5/) |
| MSTR | 2026-10-06 08:17 | mention spike | 17 | 6.14 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| NVAX | 2026-10-06 13:49 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyosue/) |
| NVDA | 2026-10-06 14:02 | mention spike | 143 | 65.14 | 113 | 0 | wallstreetbets 143 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz2ms8/) |
| QCOM | 2026-10-05 21:14 | mention spike | 12 | 1.57 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 176 | 82.29 | 92 | 0 | wallstreetbets 175, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 210 | 33.29 | 125 | 0 | wallstreetbets 210 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| VEEA | 2026-10-05 15:33 | mention spike | 18 | 5.14 | 10 | 0 | pennystocks 18 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe7tpj3/) |
| MSFT | 2026-10-05 21:14 | mention spike | 33 | 21.29 | 26 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wym7bz/comment/pe86qyb/) |
| TSM | 2026-10-05 15:18 | mention spike | 9 | 5.29 | 8 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| DRTS | 2026-10-04 23:23 | mention spike | 4 | 3.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| IREN | 2026-10-05 17:49 | mention spike | 8 | 5.0 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7xx7u/) |
| PMI | 2026-10-05 13:55 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| VST | 2026-10-05 04:15 | mention spike | 32 | 12.71 | 17 | 0 | wallstreetbets 32 | NYSE | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe85upa/) |
| DELL | 2026-10-05 16:38 | mention spike | 5 | 7.0 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe80w4o/) |
| SDEV | 2026-10-05 14:09 | mention spike | 6 | 7.43 | 4 | 0 | wallstreetbets 5, pennystocks 1 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe72uup/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
