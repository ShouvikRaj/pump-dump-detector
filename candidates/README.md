# Stage 1 candidates

Updated 2026-10-17T18:30:10Z by run `39058321984`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| NFLX | 2026-10-17 17:37 | mention spike | 13 | 7.29 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cn0b/comment/phc9msf/) |
| VOO | 2026-10-16 19:07 | mention spike | 35 | 14.29 | 31 | 0 | wallstreetbets 34, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 10 | 3.43 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phbow2b/) |
| QQQ | 2026-10-16 18:27 | mention spike | 105 | 73.0 | 76 | 0 | wallstreetbets 104, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 7 | 1.71 | 7 | 0 | wallstreetbets 6, smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| SCHD | 2026-10-17 04:49 | mention spike | 9 | 3.0 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyz2ss/comment/phbbc9z/) |
| USO | 2026-10-16 11:23 | mention spike | 16 | 6.86 | 11 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| AVGO | 2026-10-16 20:14 | mention spike | 13 | 12.0 | 11 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phc3hkz/) |
| SGRX | 2026-10-16 21:20 | mention spike | 3 | 1.14 | 3 | 0 | pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph6f9hu/) |
| TSLA | 2026-10-16 07:11 | mention spike | 44 | 43.14 | 38 | 0 | wallstreetbets 43, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 5 | 7.14 | 3 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 16 | 23.29 | 13 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb2t3e/) |
| AMD | 2026-10-16 21:33 | mention spike | 19 | 30.14 | 18 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phcb2ps/) |
| MSTR | 2026-10-16 19:07 | mention spike | 2 | 4.14 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| RCS | 2026-10-16 12:29 | mention spike | 3 | 1.86 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 11 | 8.57 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cbn8/comment/phbh8qi/) |
| BETR | 2026-10-15 23:28 | mention spike | 1 | 1.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
