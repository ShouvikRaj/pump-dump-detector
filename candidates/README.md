# Stage 1 candidates

Updated 2026-10-07T03:31:32Z by run `37567079039`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-10-06 14:55 | mention spike | 160 | 28.43 | 128 | 0 | wallstreetbets 160 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzjnmm/) |
| APLD | 2026-10-05 14:23 | mention spike | 40 | 16.86 | 26 | 2 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecpeq7/) |
| AVGO | 2026-10-06 19:34 | mention spike | 44 | 17.71 | 34 | 1 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecs6bh/) |
| CEG | 2026-10-06 13:36 | mention spike | 26 | 2.14 | 17 | 0 | wallstreetbets 26 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9tgj0/) |
| CRWD | 2026-10-06 23:59 | mention spike | 11 | 3.57 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecl6uc/) |
| HTZ | 2026-10-06 16:43 | mention spike | 108 | 3.14 | 60 | 2 | wallstreetbets 98, pennystocks 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzl5tz/) |
| INTC | 2026-10-06 18:28 | mention spike | 36 | 16.14 | 29 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pechnec/) |
| MRVL | 2026-10-06 13:36 | mention spike | 56 | 7.14 | 41 | 0 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| NOK | 2026-10-06 15:49 | mention spike | 11 | 1.71 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pebjgfm/) |
| OKLO | 2026-10-06 18:14 | mention spike | 18 | 3.43 | 12 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzagtq/) |
| PENG | 2026-10-06 18:01 | mention spike | 39 | 0.71 | 17 | 1 | wallstreetbets 39 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzdu4h/) |
| SKHY | 2026-10-06 18:54 | mention spike | 17 | 4.86 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecrj0c/) |
| VOO | 2026-10-06 16:15 | mention spike | 20 | 10.57 | 18 | 0 | wallstreetbets 20 | NYSE Arca | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzj0k5/comment/peceo51/) |
| VST | 2026-10-05 04:15 | mention spike | 52 | 12.71 | 30 | 0 | wallstreetbets 52 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pecs6bh/) |
| CIRC | 2026-10-06 17:21 | mention spike | 10 | 0.86 | 4 | 1 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peb9jxf/) |
| MSTR | 2026-10-06 08:17 | mention spike | 10 | 7.29 | 9 | 0 | wallstreetbets 10 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peblv2o/) |
| CRWV | 2026-10-06 13:49 | mention spike | 7 | 4.43 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/peag1fo/) |
| SPCX | 2026-10-05 14:51 | mention spike | 108 | 52.29 | 66 | 0 | wallstreetbets 108 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wza1qu/) |
| INFQ | 2026-10-06 16:43 | mention spike | 16 | 2.57 | 4 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wz6p9j/) |
| QCOM | 2026-10-05 21:14 | mention spike | 4 | 2.43 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe814jl/) |
| MRNA | 2026-10-06 14:02 | mention spike | 16 | 9.14 | 16 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/peawjm8/) |
| NVDA | 2026-10-06 14:02 | mention spike | 137 | 68.0 | 113 | 0 | wallstreetbets 137 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/) |
| SPY | 2026-10-06 17:08 | mention spike | 378 | 196.71 | 194 | 2 | wallstreetbets 376, smallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wz5c6o/) |
| NVAX | 2026-10-06 13:49 | mention spike | 4 | 0.86 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe7w6nl/) |
| QQQ | 2026-10-06 11:49 | mention spike | 142 | 90.29 | 84 | 0 | wallstreetbets 142 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pect983/) |
| IWM | 2026-10-06 00:59 | mention spike | 12 | 7.71 | 9 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pea97nh/) |
| VEEA | 2026-10-05 15:33 | mention spike | 13 | 7.0 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/peb6ry8/) |
| ALEC | 2026-10-05 23:41 | mention spike | 6 | 1.43 | 2 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wyszlu/comment/peb9e27/) |
| GME | 2026-10-05 16:24 | mention spike | 11 | 8.71 | 10 | 0 | wallstreetbets 10, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyy6hz/) |
| MSFT | 2026-10-05 21:14 | mention spike | 32 | 22.14 | 27 | 0 | wallstreetbets 30, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wzdzq5/) |
| TSM | 2026-10-05 15:18 | mention spike | 2 | 5.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzcn2q/comment/pebw5nw/) |
| DRTS | 2026-10-04 23:23 | mention spike | 1 | 4.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyyns2/comment/pe9o0nz/) |
| IREN | 2026-10-05 17:49 | mention spike | 3 | 5.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj28g/comment/peag1fo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
