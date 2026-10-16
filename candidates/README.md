# Stage 1 candidates

Updated 2026-10-16T20:53:43Z by run `38965387078`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-10-16 20:40 | mention spike | 56 | 21.86 | 39 | 0 | wallstreetbets 55, smallstreetbets 1 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6klgl/) |
| AVGO | 2026-10-16 20:14 | mention spike | 28 | 10.86 | 21 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6j2sr/) |
| MSTR | 2026-10-16 19:07 | mention spike | 10 | 3.29 | 10 | 0 | wallstreetbets 10 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zccw/) |
| OPEX | 2026-10-16 19:07 | mention spike | 13 | 0.71 | 12 | 0 | wallstreetbets 13 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| QQQ | 2026-10-16 18:27 | mention spike | 209 | 65.0 | 118 | 0 | wallstreetbets 209 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6jxv6/) |
| RCS | 2026-10-16 12:29 | mention spike | 14 | 0.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7n0ov/comment/ph6bpbn/) |
| SOXS | 2026-10-16 19:34 | mention spike | 16 | 6.0 | 10 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 12 | 2.57 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| TSLA | 2026-10-16 07:11 | mention spike | 235 | 19.14 | 159 | 0 | wallstreetbets 233, smallstreetbets 2 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 30 | 5.0 | 18 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6a23m/) |
| VOO | 2026-10-16 19:07 | mention spike | 26 | 12.71 | 20 | 0 | wallstreetbets 26 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qjdh/comment/ph6kfwy/) |
| BETR | 2026-10-15 23:28 | mention spike | 2 | 1.43 | 2 | 1 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| IBKR | 2026-10-16 13:35 | mention spike | 4 | 4.0 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| DRMA | 2026-10-15 23:28 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 18 | 17.71 | 15 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6btu4/) |
| RKLB | 2026-10-14 19:24 | mention spike | 31 | 20.29 | 25 | 1 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
