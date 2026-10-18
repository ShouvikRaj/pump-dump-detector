# Stage 1 candidates

Updated 2026-10-18T00:27:40Z by run `39082796646`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VOO | 2026-10-16 19:07 | mention spike | 28 | 15.0 | 28 | 0 | wallstreetbets 28 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nbc1/comment/phef7bi/) |
| NFLX | 2026-10-17 17:37 | mention spike | 11 | 7.57 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phdyk4k/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 7 | 4.29 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nydz/comment/pheb4a6/) |
| QQQ | 2026-10-16 18:27 | mention spike | 48 | 79.71 | 41 | 0 | wallstreetbets 47, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 2 | 2.43 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| SCHD | 2026-10-17 04:49 | mention spike | 7 | 3.14 | 7 | 0 | wallstreetbets 7 | NYSE Arca | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8owp2/comment/pheind0/) |
| USO | 2026-10-16 11:23 | mention spike | 8 | 8.14 | 5 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nbc1/comment/phe5ejf/) |
| AVGO | 2026-10-16 20:14 | mention spike | 12 | 12.71 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7pjx2/comment/phe2ybv/) |
| SGRX | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TSLA | 2026-10-16 07:11 | mention spike | 22 | 46.0 | 21 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 3 | 7.29 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 3 | 24.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phe2lwz/) |
| AMD | 2026-10-16 21:33 | mention spike | 15 | 30.57 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/pheh9a5/) |
| MSTR | 2026-10-16 19:07 | mention spike | 4 | 3.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8k6vw/) |
| RCS | 2026-10-16 12:29 | mention spike | 2 | 2.0 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 8 | 9.14 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8owp2/comment/phej4ws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
