# Stage 1 candidates

Updated 2026-11-14T22:10:13Z by run `43645983195`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-13 22:10 | mention spike | 46 | 2.57 | 42 | 0 | wallstreetbets 45, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| DHS | 2026-11-14 00:36 | mention spike | 13 | 0.43 | 11 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqg7i/comment/19slqfnxjkwqr/) |
| LHX | 2026-11-14 03:08 | mention spike | 19 | 0.43 | 13 | 0 | wallstreetbets 19 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| NWS | 2026-11-13 23:41 | mention spike | 26 | 0.14 | 23 | 0 | wallstreetbets 25, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| HSBC | 2026-11-14 01:03 | mention spike | 4 | 1.43 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/comment/19sm9325svoua/) |
| ARM | 2026-11-13 13:15 | mention spike | 5 | 5.0 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smsv75bic75/) |
| NFLX | 2026-11-13 00:27 | mention spike | 5 | 9.71 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smxxgdep9ad/) |
| CRWD | 2026-11-13 10:58 | mention spike | 5 | 2.71 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqdrh/comment/19slsxliwi90k/) |
| MSFT | 2026-11-12 20:54 | mention spike | 36 | 99.0 | 25 | 0 | wallstreetbets 35, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xwcx4w/) |
| MSTR | 2026-11-13 06:20 | mention spike | 10 | 7.86 | 10 | 0 | wallstreetbets 10 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sn5vxl920qr/) |
| SMU | 2026-11-13 14:07 | mention spike | 2 | 2.14 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuejhq/comment/19smnvh5ft4dh/) |
| WMT | 2026-11-14 02:06 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smchb7e8mdd/) |
| GME | 2026-11-12 01:54 | mention spike | 12 | 13.14 | 12 | 0 | wallstreetbets 11, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xw06p8/) |
| SLS | 2026-11-13 01:09 | mention spike | 3 | 5.57 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sm4quxrjhad/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
