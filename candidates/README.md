# Stage 1 candidates

Updated 2026-11-15T00:25:12Z by run `43657264788`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-13 22:10 | mention spike | 35 | 4.29 | 32 | 0 | wallstreetbets 34, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 16 | 1.57 | 14 | 1 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/) |
| LHX | 2026-11-14 03:08 | mention spike | 15 | 1.0 | 10 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| NWS | 2026-11-13 23:41 | mention spike | 11 | 2.29 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| DHS | 2026-11-14 00:36 | mention spike | 4 | 1.57 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqg7i/comment/19slqfnxjkwqr/) |
| HSBC | 2026-11-14 01:03 | mention spike | 4 | 1.43 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/comment/19sm9325svoua/) |
| ARM | 2026-11-13 13:15 | mention spike | 5 | 5.14 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfbgr/comment/19sn7qh015yf4/) |
| NFLX | 2026-11-13 00:27 | mention spike | 6 | 9.86 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvevzf/comment/19snackxw2jhg/) |
| CRWD | 2026-11-13 10:58 | mention spike | 1 | 3.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqdrh/comment/19slsxliwi90k/) |
| MSFT | 2026-11-12 20:54 | mention spike | 16 | 101.29 | 14 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xwcx4w/) |
| MSTR | 2026-11-13 06:20 | mention spike | 18 | 7.86 | 15 | 0 | wallstreetbets 18 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfswx/) |
| SMU | 2026-11-13 14:07 | mention spike | 2 | 2.14 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuejhq/comment/19smnvh5ft4dh/) |
| WMT | 2026-11-14 02:06 | mention spike | 1 | 3.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smchb7e8mdd/) |
| GME | 2026-11-12 01:54 | mention spike | 11 | 13.14 | 11 | 0 | wallstreetbets 10, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xw06p8/) |
| SLS | 2026-11-13 01:09 | mention spike | 3 | 5.86 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwdwu8/comment/19sn7kt9x0xwg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
