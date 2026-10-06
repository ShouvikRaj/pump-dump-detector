# Stage 1 candidates

Updated 2026-10-06T12:42:54Z by run `37465165072`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.14 | 7 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe704m8/) |
| APLD | 2026-10-05 14:23 | mention spike | 45 | 13.43 | 26 | 1 | wallstreetbets 45 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| GME | 2026-10-05 16:24 | mention spike | 28 | 5.43 | 22 | 0 | wallstreetbets 27, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 6.71 | 9 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE Arca | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe6g51p/) |
| MSFT | 2026-10-05 21:14 | mention spike | 50 | 19.0 | 36 | 0 | wallstreetbets 50 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy8qku/) |
| MSTR | 2026-10-06 08:17 | mention spike | 19 | 5.71 | 17 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| QQQ | 2026-10-06 11:49 | mention spike | 167 | 80.43 | 88 | 0 | wallstreetbets 166, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyl1kk/) |
| SPCX | 2026-10-05 14:51 | mention spike | 216 | 30.29 | 133 | 0 | wallstreetbets 216 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyuw3k/) |
| TSM | 2026-10-05 15:18 | mention spike | 11 | 5.0 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| VEEA | 2026-10-05 15:33 | mention spike | 21 | 4.43 | 11 | 0 | pennystocks 20, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| QCOM | 2026-10-05 21:14 | mention spike | 9 | 2.14 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/pe3eo6g/) |
| DRTS | 2026-10-04 23:23 | mention spike | 7 | 3.86 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| IREN | 2026-10-05 17:49 | mention spike | 8 | 5.0 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe31di3/) |
| PMI | 2026-10-05 13:55 | mention spike | 2 | 0.29 | 1 | 0 | pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wxyz2p/comment/pe0qett/) |
| VST | 2026-10-05 04:15 | mention spike | 22 | 12.0 | 14 | 0 | wallstreetbets 22 | NYSE | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7joky/) |
| DELL | 2026-10-05 16:38 | mention spike | 6 | 6.57 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| SDEV | 2026-10-05 14:09 | mention spike | 13 | 6.43 | 8 | 0 | wallstreetbets 9, pennystocks 4 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/pe72uup/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
