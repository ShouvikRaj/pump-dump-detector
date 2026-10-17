# Stage 1 candidates

Updated 2026-10-17T15:25:00Z by run `39044906868`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| OPEX | 2026-10-16 19:07 | mention spike | 12 | 0.86 | 11 | 0 | wallstreetbets 12 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| QQQ | 2026-10-16 18:27 | mention spike | 187 | 64.43 | 114 | 0 | wallstreetbets 186, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 2.71 | 10 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyz2ss/comment/phbbc9z/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 12 | 3.0 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/phba13i/) |
| USO | 2026-10-16 11:23 | mention spike | 27 | 5.71 | 21 | 0 | wallstreetbets 27 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| VOO | 2026-10-16 19:07 | mention spike | 38 | 13.71 | 33 | 0 | wallstreetbets 37, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| AVGO | 2026-10-16 20:14 | mention spike | 20 | 11.86 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb5lvj/) |
| SGRX | 2026-10-16 21:20 | mention spike | 7 | 0.57 | 4 | 0 | pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph6f9hu/) |
| TSLA | 2026-10-16 07:11 | mention spike | 86 | 38.0 | 67 | 0 | wallstreetbets 85, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 2 | 2.71 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5qg3w/) |
| SOXS | 2026-10-16 19:34 | mention spike | 8 | 6.86 | 5 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 31 | 21.71 | 22 | 0 | wallstreetbets 30, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb2t3e/) |
| AMD | 2026-10-16 21:33 | mention spike | 32 | 29.86 | 31 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7nfws/) |
| MSTR | 2026-10-16 19:07 | mention spike | 6 | 3.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| RCS | 2026-10-16 12:29 | mention spike | 4 | 1.71 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 14 | 8.0 | 13 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7xa5g/comment/ph8vfmc/) |
| BETR | 2026-10-15 23:28 | mention spike | 1 | 1.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
