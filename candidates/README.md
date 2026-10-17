# Stage 1 candidates

Updated 2026-10-17T14:32:01Z by run `39041123435`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-10-16 20:14 | mention spike | 26 | 11.0 | 19 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phazw41/) |
| OPEX | 2026-10-16 19:07 | mention spike | 13 | 0.71 | 12 | 0 | wallstreetbets 13 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| QQQ | 2026-10-16 18:27 | mention spike | 208 | 63.57 | 122 | 0 | wallstreetbets 207, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| SCHD | 2026-10-17 04:49 | mention spike | 10 | 2.71 | 9 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph8wyi2/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 11 | 3.0 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph99hte/) |
| USO | 2026-10-16 11:23 | mention spike | 27 | 5.71 | 21 | 0 | wallstreetbets 27 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| VOO | 2026-10-16 19:07 | mention spike | 37 | 13.43 | 31 | 0 | wallstreetbets 36, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| SGRX | 2026-10-16 21:20 | mention spike | 9 | 0.29 | 4 | 0 | pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph6f9hu/) |
| TSLA | 2026-10-16 07:11 | mention spike | 117 | 34.43 | 87 | 0 | wallstreetbets 116, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 4 | 2.43 | 3 | 0 | pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x7hxai/) |
| SOXS | 2026-10-16 19:34 | mention spike | 10 | 6.57 | 5 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 34 | 21.86 | 24 | 0 | wallstreetbets 33, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb2t3e/) |
| AMD | 2026-10-16 21:33 | mention spike | 34 | 29.57 | 33 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7nfws/) |
| MSTR | 2026-10-16 19:07 | mention spike | 7 | 3.71 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| RCS | 2026-10-16 12:29 | mention spike | 6 | 1.43 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 15 | 7.86 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7xa5g/comment/ph8vfmc/) |
| BETR | 2026-10-15 23:28 | mention spike | 1 | 1.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |
| IBKR | 2026-10-16 13:35 | mention spike | 2 | 4.29 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 1 | 3.29 | 1 | 1 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5o3u8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
