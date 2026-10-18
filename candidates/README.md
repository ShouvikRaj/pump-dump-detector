# Stage 1 candidates

Updated 2026-10-18T05:18:42Z by run `39100080437`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 3.86 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phf4kut/) |
| VOO | 2026-10-16 19:07 | mention spike | 28 | 16.57 | 26 | 0 | wallstreetbets 28 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8s3ma/) |
| NFLX | 2026-10-17 17:37 | mention spike | 12 | 7.43 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phfquj8/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 6 | 4.57 | 5 | 0 | wallstreetbets 6 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nydz/comment/pheb4a6/) |
| QQQ | 2026-10-16 18:27 | mention spike | 42 | 81.57 | 35 | 0 | wallstreetbets 41, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 2 | 2.43 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| USO | 2026-10-16 11:23 | mention spike | 6 | 8.43 | 4 | 0 | wallstreetbets 6 | NYSE Arca | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nbc1/comment/phe5ejf/) |
| AVGO | 2026-10-16 20:14 | mention spike | 13 | 13.0 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phfs50j/) |
| SGRX | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TSLA | 2026-10-16 07:11 | mention spike | 16 | 47.43 | 16 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 2 | 7.57 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phfar68/) |
| AAPL | 2026-10-16 20:40 | mention spike | 6 | 24.14 | 6 | 0 | wallstreetbets 6 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phfr2k3/) |
| AMD | 2026-10-16 21:33 | mention spike | 21 | 31.14 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phfwmcz/) |
| MSTR | 2026-10-16 19:07 | mention spike | 5 | 3.86 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8k6vw/) |
| RCS | 2026-10-16 12:29 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SOXX | 2026-10-17 01:44 | mention spike | 6 | 9.71 | 6 | 0 | wallstreetbets 6 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cbn8/comment/phfwyio/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
