# Stage 1 candidates

Updated 2026-11-15T13:50:09Z by run `43720551159`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DXYZ | 2026-11-14 23:53 | mention spike | 30 | 1.57 | 26 | 1 | wallstreetbets 30 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/) |
| MSTR | 2026-11-13 06:20 | mention spike | 27 | 8.14 | 22 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfswx/) |
| TSM | 2026-11-15 07:52 | mention spike | 14 | 6.86 | 12 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xw9tfr/) |
| LHX | 2026-11-14 03:08 | mention spike | 8 | 2.0 | 6 | 0 | wallstreetbets 8 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19smx8l74fiv4/) |
| ATC | 2026-11-13 22:10 | mention spike | 9 | 10.57 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwgsga/comment/19snenbqh4tlw/) |
| NWS | 2026-11-13 23:41 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| DHS | 2026-11-14 00:36 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| HSBC | 2026-11-14 01:03 | mention spike | 1 | 2.0 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjz5i/comment/19snc99b1t5s3/) |
| ARM | 2026-11-13 13:15 | mention spike | 5 | 5.43 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwplru/comment/19snvyfipob9c/) |
| NFLX | 2026-11-13 00:27 | mention spike | 4 | 9.71 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvevzf/comment/19snackxw2jhg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
