# Stage 1 candidates

Updated 2026-11-14T18:51:11Z by run `43628216711`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-13 22:10 | mention spike | 61 | 0.0 | 58 | 0 | wallstreetbets 60, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| DHS | 2026-11-14 00:36 | mention spike | 15 | 0.14 | 13 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqg7i/comment/19slqfnxjkwqr/) |
| HSBC | 2026-11-14 01:03 | mention spike | 13 | 0.14 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/) |
| LHX | 2026-11-14 03:08 | mention spike | 17 | 0.43 | 11 | 0 | wallstreetbets 17 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smrltsmq0xu/) |
| NWS | 2026-11-13 23:41 | mention spike | 27 | 0.0 | 24 | 0 | wallstreetbets 26, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| ARM | 2026-11-13 13:15 | mention spike | 6 | 5.14 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smsv75bic75/) |
| NFLX | 2026-11-13 00:27 | mention spike | 7 | 9.29 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvs85t/comment/19smrhy2m6qv4/) |
| CRWD | 2026-11-13 10:58 | mention spike | 8 | 2.29 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqdrh/comment/19slsxliwi90k/) |
| MSFT | 2026-11-12 20:54 | mention spike | 58 | 96.29 | 37 | 0 | wallstreetbets 58 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvmysb/) |
| MSTR | 2026-11-13 06:20 | mention spike | 7 | 7.86 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sms5zrllnwk/) |
| SMU | 2026-11-13 14:07 | mention spike | 4 | 1.86 | 4 | 0 | wallstreetbets 3, smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuejhq/comment/19smnvh5ft4dh/) |
| WMT | 2026-11-14 02:06 | mention spike | 2 | 3.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smchb7e8mdd/) |
| GME | 2026-11-12 01:54 | mention spike | 13 | 12.71 | 13 | 0 | wallstreetbets 11, pennystocks 1, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xw06p8/) |
| SLS | 2026-11-13 01:09 | mention spike | 5 | 5.43 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sm4quxrjhad/) |
| CBRS | 2026-11-12 16:56 | mention spike | 2 | 12.86 | 1 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xv4xx4/comment/19sl7ykb5o7gi/) |
| CSCO | 2026-11-12 21:20 | mention spike | 4 | 5.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19slriey0wlkz/) |
| AMAT | 2026-11-12 18:42 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| IWM | 2026-11-13 19:02 | mention spike | 4 | 5.29 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smvcmtd5y6c/) |
| ASML | 2026-11-12 20:43 | mention spike | 1 | 6.0 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19slpq4b53eiq/) |
| TSLA | 2026-11-13 15:04 | mention spike | 16 | 36.29 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smoo8sw9jyd/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
