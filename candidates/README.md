# Stage 1 candidates

Updated 2026-10-18T06:24:57Z by run `39103909506`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 3.86 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phf4kut/) |
| VTI | 2026-10-18 05:58 | mention spike | 10 | 1.86 | 9 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg315a/) |
| VOO | 2026-10-16 19:07 | mention spike | 29 | 16.43 | 27 | 0 | wallstreetbets 29 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8s3ma/) |
| NFLX | 2026-10-17 17:37 | mention spike | 12 | 7.43 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1typ6n0/comment/phg6fu3/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg0wwv/) |
| QQQ | 2026-10-16 18:27 | mention spike | 42 | 81.57 | 35 | 0 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 2 | 2.43 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| USO | 2026-10-16 11:23 | mention spike | 2 | 9.0 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nbc1/comment/phe5ejf/) |
| AVGO | 2026-10-16 20:14 | mention spike | 14 | 13.14 | 13 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phg1zel/) |
| SGRX | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TSLA | 2026-10-16 07:11 | mention spike | 16 | 47.71 | 15 | 0 | wallstreetbets 16 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 2 | 7.57 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phfar68/) |
| AAPL | 2026-10-16 20:40 | mention spike | 7 | 24.0 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg5frl/) |
| AMD | 2026-10-16 21:33 | mention spike | 23 | 31.29 | 19 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg6hz2/) |
| MSTR | 2026-10-16 19:07 | mention spike | 5 | 3.86 | 5 | 0 | wallstreetbets 5 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8k6vw/) |
| RCS | 2026-10-16 12:29 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SOXX | 2026-10-17 01:44 | mention spike | 6 | 9.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cbn8/comment/phfwyio/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
