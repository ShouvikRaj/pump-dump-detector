# Stage 1 candidates

Updated 2026-10-16T20:00:50Z by run `38958963389`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| MSTR | 2026-10-16 19:07 | mention spike | 10 | 3.86 | 10 | 0 | wallstreetbets 10 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zccw/) |
| OPEX | 2026-10-16 19:07 | mention spike | 13 | 0.71 | 12 | 0 | wallstreetbets 13 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| QQQ | 2026-10-16 18:27 | mention spike | 199 | 65.14 | 117 | 0 | wallstreetbets 199 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6bib4/) |
| RCS | 2026-10-16 12:29 | mention spike | 14 | 0.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7n0ov/comment/ph6bpbn/) |
| SOXS | 2026-10-16 19:34 | mention spike | 16 | 6.0 | 10 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 13 | 2.43 | 10 | 0 | wallstreetbets 13 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| TSLA | 2026-10-16 07:11 | mention spike | 230 | 19.29 | 157 | 0 | wallstreetbets 228, smallstreetbets 2 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 33 | 5.0 | 19 | 0 | wallstreetbets 33 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6a23m/) |
| VOO | 2026-10-16 19:07 | mention spike | 24 | 12.86 | 19 | 0 | wallstreetbets 24 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph64e79/) |
| BETR | 2026-10-15 23:28 | mention spike | 4 | 1.14 | 3 | 1 | pennystocks 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| IBKR | 2026-10-16 13:35 | mention spike | 8 | 3.57 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 4 | 2.57 | 3 | 0 | pennystocks 3, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 20 | 17.57 | 17 | 0 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6btu4/) |
| RKLB | 2026-10-14 19:24 | mention spike | 34 | 19.57 | 25 | 1 | wallstreetbets 34 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
