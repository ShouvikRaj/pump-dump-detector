# Stage 1 candidates

Updated 2026-11-14T20:25:10Z by run `43636629475`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-13 22:10 | mention spike | 62 | 0.0 | 59 | 0 | wallstreetbets 61, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| DHS | 2026-11-14 00:36 | mention spike | 15 | 0.14 | 13 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqg7i/comment/19slqfnxjkwqr/) |
| HSBC | 2026-11-14 01:03 | mention spike | 13 | 0.14 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/) |
| LHX | 2026-11-14 03:08 | mention spike | 19 | 0.43 | 13 | 0 | wallstreetbets 19 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| NWS | 2026-11-13 23:41 | mention spike | 27 | 0.0 | 24 | 0 | wallstreetbets 26, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| ARM | 2026-11-13 13:15 | mention spike | 5 | 5.29 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smsv75bic75/) |
| NFLX | 2026-11-13 00:27 | mention spike | 6 | 9.57 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smxxgdep9ad/) |
| CRWD | 2026-11-13 10:58 | mention spike | 8 | 2.29 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqdrh/comment/19slsxliwi90k/) |
| MSFT | 2026-11-12 20:54 | mention spike | 51 | 97.14 | 35 | 0 | wallstreetbets 51 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvmysb/) |
| MSTR | 2026-11-13 06:20 | mention spike | 7 | 8.0 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwan3u/comment/19smzlg9hyhj5/) |
| SMU | 2026-11-13 14:07 | mention spike | 3 | 2.0 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuejhq/comment/19smnvh5ft4dh/) |
| WMT | 2026-11-14 02:06 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smchb7e8mdd/) |
| GME | 2026-11-12 01:54 | mention spike | 12 | 13.0 | 12 | 0 | wallstreetbets 11, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xw06p8/) |
| SLS | 2026-11-13 01:09 | mention spike | 3 | 5.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sm4quxrjhad/) |
| CBRS | 2026-11-12 16:56 | mention spike | 1 | 13.0 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx9xf5d26a/) |
| CSCO | 2026-11-12 21:20 | mention spike | 2 | 5.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19slriey0wlkz/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
