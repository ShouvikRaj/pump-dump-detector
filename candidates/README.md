# Stage 1 candidates

Updated 2026-10-17T21:32:04Z by run `39071304064`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VOO | 2026-10-16 19:07 | mention spike | 26 | 15.14 | 26 | 0 | wallstreetbets 26 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| NFLX | 2026-10-17 17:37 | mention spike | 10 | 7.57 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cn0b/comment/phcon80/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 5 | 4.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phcxpc7/) |
| QQQ | 2026-10-16 18:27 | mention spike | 40 | 80.71 | 34 | 0 | wallstreetbets 39, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 2 | 2.43 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| SCHD | 2026-10-17 04:49 | mention spike | 6 | 3.29 | 6 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyz2ss/comment/phbbc9z/) |
| USO | 2026-10-16 11:23 | mention spike | 7 | 8.14 | 4 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| AVGO | 2026-10-16 20:14 | mention spike | 8 | 12.71 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7xa5g/comment/phd7gdh/) |
| SGRX | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TSLA | 2026-10-16 07:11 | mention spike | 20 | 46.43 | 19 | 0 | wallstreetbets 20 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 2 | 7.29 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 2 | 24.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phd0v5x/) |
| AMD | 2026-10-16 21:33 | mention spike | 10 | 30.57 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phcsnv3/) |
| MSTR | 2026-10-16 19:07 | mention spike | 3 | 4.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8k6vw/) |
| RCS | 2026-10-16 12:29 | mention spike | 2 | 2.0 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 5 | 9.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cbn8/comment/phbh8qi/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
