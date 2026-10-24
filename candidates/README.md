# Stage 1 candidates

Updated 2026-10-24T20:46:10Z by run `40130870105`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| USO | 2026-10-23 16:35 | mention spike | 7 | 18.43 | 7 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rldexwyjpr5/) |
| CRDO | 2026-10-23 12:23 | mention spike | 2 | 5.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rkv8jmr8qhv/) |
| MSFT | 2026-10-23 06:51 | mention spike | 16 | 24.0 | 13 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe985s/) |
| CRWD | 2026-10-23 20:37 | mention spike | 2 | 4.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rjwkjkz934y/) |
| LUNR | 2026-10-23 18:21 | mention spike | 2 | 3.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rkcp2vo5u05/) |
| NVDA | 2026-10-23 02:14 | mention spike | 21 | 64.14 | 19 | 0 | wallstreetbets 18, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xeexq8/comment/19rlkl6tanmjl/) |
| RDDT | 2026-10-23 20:37 | mention spike | 9 | 12.57 | 7 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe985s/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
