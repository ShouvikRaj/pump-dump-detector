# Stage 1 candidates

Updated 2026-11-15T03:25:09Z by run `43671949734`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DXYZ | 2026-11-14 23:53 | mention spike | 22 | 1.57 | 18 | 1 | wallstreetbets 22 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/) |
| MSTR | 2026-11-13 06:20 | mention spike | 24 | 7.86 | 21 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfswx/) |
| LHX | 2026-11-14 03:08 | mention spike | 9 | 1.86 | 7 | 0 | wallstreetbets 9 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| ATC | 2026-11-13 22:10 | mention spike | 14 | 9.86 | 12 | 0 | wallstreetbets 13, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| NWS | 2026-11-13 23:41 | mention spike | 6 | 3.0 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| DHS | 2026-11-14 00:36 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| HSBC | 2026-11-14 01:03 | mention spike | 5 | 1.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/comment/19snc99b1t5s3/) |
| ARM | 2026-11-13 13:15 | mention spike | 6 | 5.14 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwjtnf/comment/19snika8hyn6o/) |
| NFLX | 2026-11-13 00:27 | mention spike | 5 | 9.71 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvevzf/comment/19snackxw2jhg/) |
| CRWD | 2026-11-13 10:58 | mention spike | 1 | 3.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvqdrh/comment/19slsxliwi90k/) |
| MSFT | 2026-11-12 20:54 | mention spike | 12 | 101.29 | 12 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xwcx4w/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
