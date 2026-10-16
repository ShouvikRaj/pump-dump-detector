# Stage 1 candidates

Updated 2026-10-16T19:34:07Z by run `38955740737`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| MSTR | 2026-10-16 19:07 | mention spike | 10 | 3.86 | 10 | 0 | wallstreetbets 10 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zccw/) |
| OPEX | 2026-10-16 19:07 | mention spike | 11 | 0.71 | 10 | 0 | wallstreetbets 11 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph619c0/) |
| QQQ | 2026-10-16 18:27 | mention spike | 193 | 65.43 | 113 | 0 | wallstreetbets 193 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph65tte/) |
| RCS | 2026-10-16 12:29 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph4kk07/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 12 | 2.43 | 9 | 0 | wallstreetbets 12 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6602b/) |
| TSLA | 2026-10-16 07:11 | mention spike | 230 | 19.57 | 157 | 0 | wallstreetbets 228, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 29 | 5.0 | 15 | 0 | wallstreetbets 29 | NYSE Arca | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph60r7s/) |
| VOO | 2026-10-16 19:07 | mention spike | 24 | 12.86 | 19 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph64e79/) |
| SOXS | 2026-10-16 19:34 | mention spike | 16 | 6.0 | 10 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca | #28 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |
| BETR | 2026-10-15 23:28 | mention spike | 5 | 1.0 | 4 | 1 | pennystocks 3, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| IBKR | 2026-10-16 13:35 | mention spike | 8 | 3.57 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 5 | 2.43 | 3 | 0 | pennystocks 4, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 3 | 1.29 | 2 | 0 | pennystocks 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 19 | 17.57 | 16 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph62lvb/) |
| RKLB | 2026-10-14 19:24 | mention spike | 34 | 19.57 | 25 | 1 | wallstreetbets 34 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |
| WMT | 2026-10-14 19:24 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4lhx7/) |
| TLT | 2026-10-14 18:31 | mention spike | 13 | 11.71 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5rgi9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
