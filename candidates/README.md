# Stage 1 candidates

Updated 2026-10-17T13:52:23Z by run `39038311349`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-10-16 20:14 | mention spike | 26 | 11.0 | 19 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phaw8m9/) |
| OPEX | 2026-10-16 19:07 | mention spike | 14 | 0.57 | 13 | 0 | wallstreetbets 14 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| QQQ | 2026-10-16 18:27 | mention spike | 218 | 63.29 | 124 | 0 | wallstreetbets 217, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| SCHD | 2026-10-17 04:49 | mention spike | 10 | 2.71 | 9 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph8wyi2/) |
| SGRX | 2026-10-16 21:20 | mention spike | 11 | 0.0 | 5 | 0 | pennystocks 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7h6m1/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 11 | 3.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph99hte/) |
| TSLA | 2026-10-16 07:11 | mention spike | 130 | 33.14 | 96 | 0 | wallstreetbets 129, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| USO | 2026-10-16 11:23 | mention spike | 27 | 5.71 | 21 | 0 | wallstreetbets 27 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| VOO | 2026-10-16 19:07 | mention spike | 37 | 13.29 | 31 | 0 | wallstreetbets 36, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| XLAB | 2026-10-16 21:20 | mention spike | 8 | 1.86 | 6 | 0 | pennystocks 6, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x7hxai/) |
| SOXS | 2026-10-16 19:34 | mention spike | 12 | 6.29 | 7 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 34 | 22.29 | 24 | 0 | wallstreetbets 33, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6klgl/) |
| AMD | 2026-10-16 21:33 | mention spike | 37 | 29.86 | 35 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7nfws/) |
| MSTR | 2026-10-16 19:07 | mention spike | 7 | 3.86 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| RCS | 2026-10-16 12:29 | mention spike | 6 | 1.43 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 15 | 7.86 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7xa5g/comment/ph8vfmc/) |
| BETR | 2026-10-15 23:28 | mention spike | 1 | 1.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |
| IBKR | 2026-10-16 13:35 | mention spike | 2 | 4.29 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 2 | 3.14 | 1 | 2 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |
| DRMA | 2026-10-15 23:28 | mention spike | 4 | 1.57 | 3 | 2 | pennystocks 3, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
