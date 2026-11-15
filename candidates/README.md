# Stage 1 candidates

Updated 2026-11-15T02:22:09Z by run `43666844738`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-13 22:10 | mention spike | 40 | 6.14 | 37 | 0 | wallstreetbets 39, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 22 | 1.57 | 18 | 1 | wallstreetbets 22 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/) |
| LHX | 2026-11-14 03:08 | mention spike | 11 | 1.57 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| MSTR | 2026-11-13 06:20 | mention spike | 23 | 7.86 | 20 | 0 | wallstreetbets 23 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfswx/) |
| NWS | 2026-11-13 23:41 | mention spike | 8 | 2.71 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| DHS | 2026-11-14 00:36 | mention spike | 3 | 2.0 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqg7i/comment/19slqfnxjkwqr/) |
| HSBC | 2026-11-14 01:03 | mention spike | 5 | 1.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/comment/19snc99b1t5s3/) |
| ARM | 2026-11-13 13:15 | mention spike | 5 | 5.14 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfbgr/comment/19sn7qh015yf4/) |
| NFLX | 2026-11-13 00:27 | mention spike | 5 | 9.71 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvevzf/comment/19snackxw2jhg/) |
| CRWD | 2026-11-13 10:58 | mention spike | 1 | 3.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqdrh/comment/19slsxliwi90k/) |
| MSFT | 2026-11-12 20:54 | mention spike | 13 | 101.14 | 12 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xwcx4w/) |
| SMU | 2026-11-13 14:07 | mention spike | 3 | 2.14 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwhukf/comment/19snea0vtd8tg/) |
| WMT | 2026-11-14 02:06 | mention spike | 1 | 3.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smchb7e8mdd/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
