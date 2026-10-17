# Stage 1 candidates

Updated 2026-10-17T03:03:49Z by run `38997294388`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-10-16 20:40 | mention spike | 55 | 21.29 | 38 | 0 | wallstreetbets 54, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6klgl/) |
| AMD | 2026-10-16 21:33 | mention spike | 58 | 28.14 | 45 | 0 | wallstreetbets 58 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7nfws/) |
| MSTR | 2026-10-16 19:07 | mention spike | 10 | 3.43 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| OPEX | 2026-10-16 19:07 | mention spike | 13 | 0.57 | 12 | 0 | wallstreetbets 13 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph69x61/) |
| QQQ | 2026-10-16 18:27 | mention spike | 217 | 64.71 | 124 | 0 | wallstreetbets 217 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7sg39/) |
| RCS | 2026-10-16 12:29 | mention spike | 16 | 0.0 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SGRX | 2026-10-16 21:20 | mention spike | 11 | 0.0 | 5 | 0 | pennystocks 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7h6m1/) |
| SOXS | 2026-10-16 19:34 | mention spike | 16 | 6.14 | 11 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| SOXX | 2026-10-17 01:44 | mention spike | 17 | 7.43 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7rzx9/comment/ph80vxx/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 14 | 2.57 | 12 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6v5sz/) |
| TSLA | 2026-10-16 07:11 | mention spike | 219 | 21.0 | 151 | 0 | wallstreetbets 216, smallstreetbets 2, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 27 | 5.29 | 18 | 0 | wallstreetbets 27 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph6pjch/) |
| VOO | 2026-10-16 19:07 | mention spike | 32 | 12.43 | 26 | 0 | wallstreetbets 31, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| XLAB | 2026-10-16 21:20 | mention spike | 21 | 0.0 | 9 | 0 | pennystocks 19, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x7hxai/) |
| AVGO | 2026-10-16 20:14 | mention spike | 28 | 10.71 | 20 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph7zu4v/) |
| BETR | 2026-10-15 23:28 | mention spike | 2 | 1.71 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |
| IBKR | 2026-10-16 13:35 | mention spike | 5 | 4.0 | 4 | 0 | wallstreetbets 4, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 2 | 3.14 | 1 | 2 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |
| DRMA | 2026-10-15 23:28 | mention spike | 4 | 1.57 | 3 | 2 | pennystocks 3, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |
| TSM | 2026-10-14 19:51 | mention spike | 15 | 18.14 | 13 | 0 | wallstreetbets 14, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7qgff/comment/ph7id1x/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
