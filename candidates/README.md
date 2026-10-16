# Stage 1 candidates

Updated 2026-10-16T20:27:05Z by run `38962210400`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-10-16 20:14 | mention spike | 27 | 11.0 | 20 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6e1aw/) |
| MSTR | 2026-10-16 19:07 | mention spike | 10 | 3.57 | 10 | 0 | wallstreetbets 10 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zccw/) |
| OPEX | 2026-10-16 19:07 | mention spike | 13 | 0.71 | 12 | 0 | wallstreetbets 13 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| QQQ | 2026-10-16 18:27 | mention spike | 210 | 64.86 | 118 | 0 | wallstreetbets 210 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6i0gz/) |
| RCS | 2026-10-16 12:29 | mention spike | 14 | 0.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7n0ov/comment/ph6bpbn/) |
| SOXS | 2026-10-16 19:34 | mention spike | 16 | 6.0 | 10 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 13 | 2.43 | 10 | 0 | wallstreetbets 13 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| TSLA | 2026-10-16 07:11 | mention spike | 231 | 19.43 | 156 | 0 | wallstreetbets 229, smallstreetbets 2 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 32 | 4.86 | 18 | 0 | wallstreetbets 32 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6a23m/) |
| VOO | 2026-10-16 19:07 | mention spike | 25 | 12.86 | 20 | 0 | wallstreetbets 25 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7p1eu/comment/ph6fokr/) |
| BETR | 2026-10-15 23:28 | mention spike | 2 | 1.43 | 2 | 1 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| IBKR | 2026-10-16 13:35 | mention spike | 7 | 3.57 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 3 | 2.71 | 2 | 0 | pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 20 | 17.43 | 17 | 0 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6btu4/) |
| RKLB | 2026-10-14 19:24 | mention spike | 35 | 19.57 | 26 | 1 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
