# Stage 1 candidates

Updated 2026-10-07T07:17:17Z by run `37586293720`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 168 | 27.86 | 133 | 0 | wallstreetbets 168 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wznjo8/) |
| AVGO | 2026-10-06 19:34 | mention spike | 44 | 17.86 | 34 | 1 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/ped0gf9/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CRWD | 2026-10-06 23:59 | mention spike | 11 | 3.43 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecl6uc/) |
| HTZ | 2026-10-06 16:43 | mention spike | 111 | 3.14 | 63 | 3 | wallstreetbets 99, pennystocks 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wzn9uv/) |
| MRVL | 2026-10-06 13:36 | mention spike | 56 | 7.14 | 41 | 0 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| NOK | 2026-10-06 15:49 | mention spike | 11 | 1.71 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pebjgfm/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 3.43 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 39 | 0.71 | 17 | 1 | wallstreetbets 39 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 4.71 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecrj0c/) |
| VOO | 2026-10-06 16:15 | mention spike | 19 | 10.43 | 17 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzj0k5/comment/peceo51/) |
| VST | 2026-10-05 04:15 | mention spike | 51 | 12.86 | 30 | 0 | wallstreetbets 51 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/ped2hlz/) |
| APLD | 2026-10-05 14:23 | mention spike | 38 | 17.71 | 28 | 2 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pedkd2c/) |
| INTC | 2026-10-06 18:28 | mention spike | 35 | 16.14 | 28 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pechnec/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.86 | 4 | 1 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peb9jxf/) |
| MSTR | 2026-10-06 08:17 | mention spike | 9 | 7.43 | 8 | 0 | wallstreetbets 9 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peblv2o/) |
| CRWV | 2026-10-06 13:49 | mention spike | 7 | 4.43 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/peag1fo/) |
| SPCX | 2026-10-05 14:51 | mention spike | 99 | 53.71 | 62 | 0 | wallstreetbets 99 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 16 | 2.57 | 4 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 4 | 2.43 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| MRNA | 2026-10-06 14:02 | mention spike | 14 | 8.43 | 14 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| NVDA | 2026-10-06 14:02 | mention spike | 144 | 68.43 | 117 | 1 | wallstreetbets 143, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/) |
| SPY | 2026-10-06 17:08 | mention spike | 385 | 195.14 | 199 | 2 | wallstreetbets 383, smallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 1 | 1.29 | 1 | 0 | wallstreetbets 1 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7w6nl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 135 | 90.43 | 79 | 0 | wallstreetbets 135 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pedffq4/) |
| IWM | 2026-10-06 00:59 | mention spike | 15 | 7.71 | 11 | 0 | wallstreetbets 15 | NYSE Arca | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peddxox/) |
| VEEA | 2026-10-05 15:33 | mention spike | 13 | 7.0 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/peb6ry8/) |
| ALEC | 2026-10-05 23:41 | mention spike | 6 | 1.43 | 2 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/peb9e27/) |
| GME | 2026-10-05 16:24 | mention spike | 11 | 8.86 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 32 | 22.14 | 26 | 0 | wallstreetbets 30, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzdzq5/) |
| TSM | 2026-10-05 15:18 | mention spike | 4 | 5.71 | 4 | 0 | wallstreetbets 4 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wvz349/comment/pedrgzz/) |
| DRTS | 2026-10-04 23:23 | mention spike | 1 | 4.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
