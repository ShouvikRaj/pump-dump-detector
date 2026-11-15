# Stage 1 candidates

Updated 2026-11-15T21:35:12Z by run `43763841235`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| COIN | 2026-11-15 21:05 | mention spike | 10 | 0.71 | 8 | 1 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwesfj/comment/19souzj7ihpgl/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 32 | 1.57 | 28 | 1 | wallstreetbets 32 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/) |
| MSTR | 2026-11-13 06:20 | mention spike | 24 | 9.14 | 18 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwfswx/) |
| TSM | 2026-11-15 07:52 | mention spike | 2 | 8.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwhukf/comment/19soj7mygicbk/) |
| LHX | 2026-11-14 03:08 | mention spike | 1 | 3.14 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sotl24p2e6c/) |
| ATC | 2026-11-13 22:10 | mention spike | 3 | 11.43 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwgsga/comment/19snenbqh4tlw/) |
| NWS | 2026-11-13 23:41 | mention spike | 1 | 3.86 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/comment/19sov2r3zmerk/) |
| DHS | 2026-11-14 00:36 | mention spike | 1 | 2.43 | 1 | 0 | wallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sorfnyeanup/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
