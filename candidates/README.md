# Stage 1 candidates

Updated 2026-10-16T19:07:34Z by run `38952446302`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | 2026-10-16 18:27 | mention spike | 168 | 66.29 | 101 | 0 | wallstreetbets 168 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5z0my/) |
| RCS | 2026-10-16 12:29 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph4kk07/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 11 | 2.57 | 8 | 0 | wallstreetbets 11 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5vtmo/) |
| TSLA | 2026-10-16 07:11 | mention spike | 223 | 19.71 | 153 | 0 | wallstreetbets 221, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 28 | 5.0 | 14 | 0 | wallstreetbets 28 | NYSE Arca | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5ykbn/) |
| MSTR | 2026-10-16 19:07 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zccw/) |
| OPEX | 2026-10-16 19:07 | mention spike | 10 | 0.71 | 9 | 0 | wallstreetbets 10 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zbml/) |
| VOO | 2026-10-16 19:07 | mention spike | 23 | 12.86 | 18 | 0 | wallstreetbets 23 | NYSE Arca | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph5yn93/) |
| BETR | 2026-10-15 23:28 | mention spike | 9 | 0.43 | 5 | 1 | pennystocks 7, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| IBKR | 2026-10-16 13:35 | mention spike | 8 | 3.57 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 6 | 2.29 | 4 | 0 | pennystocks 5, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 3 | 1.29 | 2 | 0 | pennystocks 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 18 | 17.57 | 15 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5xe8q/) |
| RKLB | 2026-10-14 19:24 | mention spike | 33 | 19.57 | 24 | 1 | wallstreetbets 33 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |
| WMT | 2026-10-14 19:24 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4lhx7/) |
| TLT | 2026-10-14 18:31 | mention spike | 13 | 11.86 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5rgi9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
