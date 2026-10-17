# Stage 1 candidates

Updated 2026-10-17T18:56:41Z by run `39060262037`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VOO | 2026-10-16 19:07 | mention spike | 32 | 14.71 | 32 | 0 | wallstreetbets 31, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/) |
| NFLX | 2026-10-17 17:37 | mention spike | 12 | 7.57 | 10 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cn0b/comment/phcon80/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 8 | 3.71 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phbow2b/) |
| QQQ | 2026-10-16 18:27 | mention spike | 97 | 73.29 | 68 | 0 | wallstreetbets 96, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 6 | 1.86 | 6 | 0 | wallstreetbets 5, smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x84smu/) |
| SCHD | 2026-10-17 04:49 | mention spike | 7 | 3.29 | 7 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyz2ss/comment/phbbc9z/) |
| USO | 2026-10-16 11:23 | mention spike | 15 | 7.0 | 10 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/ph9mk5s/) |
| AVGO | 2026-10-16 20:14 | mention spike | 11 | 12.29 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phc3hkz/) |
| SGRX | 2026-10-16 21:20 | mention spike | 1 | 1.43 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x76a69/comment/ph6f9hu/) |
| TSLA | 2026-10-16 07:11 | mention spike | 36 | 44.29 | 34 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 4 | 7.29 | 3 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ymiq/) |
| AAPL | 2026-10-16 20:40 | mention spike | 13 | 23.71 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phb2t3e/) |
| AMD | 2026-10-16 21:33 | mention spike | 17 | 30.43 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phcsnv3/) |
| MSTR | 2026-10-16 19:07 | mention spike | 2 | 4.14 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7ukwm/comment/ph87ju2/) |
| RCS | 2026-10-16 12:29 | mention spike | 3 | 1.86 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph88ruf/) |
| SOXX | 2026-10-17 01:44 | mention spike | 11 | 8.57 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8cbn8/comment/phbh8qi/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
