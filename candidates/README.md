# Stage 1 candidates

Updated 2026-10-16T21:46:16Z by run `38971509081`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-10-16 20:40 | mention spike | 55 | 21.86 | 38 | 0 | wallstreetbets 54, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6klgl/) |
| AMD | 2026-10-16 21:33 | mention spike | 56 | 28.43 | 44 | 0 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7nfws/) |
| AVGO | 2026-10-16 20:14 | mention spike | 28 | 10.57 | 21 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6j2sr/) |
| OPEX | 2026-10-16 19:07 | mention spike | 13 | 0.71 | 12 | 0 | wallstreetbets 13 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| QQQ | 2026-10-16 18:27 | mention spike | 212 | 65.0 | 122 | 0 | wallstreetbets 212 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7sg39/) |
| RCS | 2026-10-16 12:29 | mention spike | 14 | 0.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7n0ov/comment/ph6bpbn/) |
| SGRX | 2026-10-16 21:20 | mention spike | 11 | 0.0 | 5 | 0 | pennystocks 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7h6m1/) |
| SOXS | 2026-10-16 19:34 | mention spike | 16 | 6.0 | 10 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 14 | 2.57 | 12 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6v5sz/) |
| TSLA | 2026-10-16 07:11 | mention spike | 234 | 19.14 | 160 | 0 | wallstreetbets 231, smallstreetbets 2, pennystocks 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 27 | 5.57 | 18 | 0 | wallstreetbets 27 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6pjch/) |
| VOO | 2026-10-16 19:07 | mention spike | 26 | 12.71 | 20 | 0 | wallstreetbets 26 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qjdh/comment/ph6kfwy/) |
| XLAB | 2026-10-16 21:20 | mention spike | 14 | 0.0 | 9 | 0 | pennystocks 12, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x7hxai/) |
| MSTR | 2026-10-16 19:07 | mention spike | 9 | 3.43 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5zccw/) |
| BETR | 2026-10-15 23:28 | mention spike | 2 | 1.57 | 2 | 1 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |
| IBKR | 2026-10-16 13:35 | mention spike | 5 | 4.0 | 4 | 0 | wallstreetbets 4, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 2 | 3.14 | 1 | 2 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |
| DRMA | 2026-10-15 23:28 | mention spike | 5 | 1.43 | 4 | 2 | pennystocks 4, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |
| TSM | 2026-10-14 19:51 | mention spike | 17 | 17.86 | 15 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph6btu4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
