# Stage 1 candidates

Updated 2026-11-15T05:50:11Z by run `43682543184`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DXYZ | 2026-11-14 23:53 | mention spike | 23 | 1.57 | 19 | 1 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/) |
| MSTR | 2026-11-13 06:20 | mention spike | 23 | 8.14 | 21 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfswx/) |
| LHX | 2026-11-14 03:08 | mention spike | 9 | 1.86 | 7 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| ATC | 2026-11-13 22:10 | mention spike | 13 | 10.0 | 11 | 0 | wallstreetbets 12, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xvzvin/) |
| NWS | 2026-11-13 23:41 | mention spike | 2 | 3.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvm2xs/comment/19sm232qrao75/) |
| DHS | 2026-11-14 00:36 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| HSBC | 2026-11-14 01:03 | mention spike | 3 | 1.71 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/comment/19snc99b1t5s3/) |
| ARM | 2026-11-13 13:15 | mention spike | 6 | 5.14 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwjtnf/comment/19snika8hyn6o/) |
| NFLX | 2026-11-13 00:27 | mention spike | 4 | 9.71 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvevzf/comment/19snackxw2jhg/) |
| CRWD | 2026-11-13 10:58 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MSFT | 2026-11-12 20:54 | mention spike | 10 | 101.57 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xwcx4w/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
