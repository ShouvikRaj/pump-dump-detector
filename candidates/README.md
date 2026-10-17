# Stage 1 candidates

Updated 2026-10-17T17:03:06Z by run `39051623486`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| TQQQ | 2026-10-16 18:54 | mention spike | 10 | 3.43 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phbow2b/) |
| VOO | 2026-10-16 19:07 | mention spike | 37 | 14.0 | 33 | 0 | wallstreetbets 36, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| QQQ | 2026-10-16 18:27 | mention spike | 144 | 68.29 | 93 | 0 | wallstreetbets 143, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 8 | 1.57 | 8 | 0 | wallstreetbets 7, smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| SCHD | 2026-10-17 04:49 | mention spike | 9 | 3.0 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyz2ss/comment/phbbc9z/) |
| USO | 2026-10-16 11:23 | mention spike | 20 | 6.57 | 14 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| AVGO | 2026-10-16 20:14 | mention spike | 14 | 12.0 | 13 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb5lvj/) |
| SGRX | 2026-10-16 21:20 | mention spike | 4 | 1.0 | 4 | 0 | pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph6f9hu/) |
| TSLA | 2026-10-16 07:11 | mention spike | 61 | 40.86 | 50 | 0 | wallstreetbets 60, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 1 | 2.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph5qg3w/) |
| SOXS | 2026-10-16 19:34 | mention spike | 6 | 7.0 | 4 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 23 | 22.43 | 18 | 0 | wallstreetbets 22, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb2t3e/) |
| AMD | 2026-10-16 21:33 | mention spike | 24 | 29.71 | 23 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7nfws/) |
| MSTR | 2026-10-16 19:07 | mention spike | 4 | 3.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| RCS | 2026-10-16 12:29 | mention spike | 3 | 1.86 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 13 | 8.29 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cbn8/comment/phbh8qi/) |
| BETR | 2026-10-15 23:28 | mention spike | 1 | 1.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph66ib5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
