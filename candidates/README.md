# Stage 1 candidates

Updated 2026-10-20T22:23:06Z by run `39506548845`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 2026-10-20 18:16 | mention spike | 54 | 18.71 | 22 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phy60op/) |
| HTZ | 2026-10-20 13:24 | mention spike | 18 | 7.43 | 14 | 0 | wallstreetbets 17, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 12 | 1.86 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phy4mnu/) |
| NFLX | 2026-10-19 19:31 | mention spike | 160 | 11.71 | 117 | 0 | wallstreetbets 160 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb427h/) |
| OKLO | 2026-10-20 21:21 | mention spike | 14 | 4.71 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xatiax/) |
| SMCI | 2026-10-20 21:06 | mention spike | 57 | 5.57 | 40 | 0 | wallstreetbets 57 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phy91lc/) |
| SPCX | 2026-10-20 10:18 | mention spike | 271 | 40.29 | 180 | 1 | wallstreetbets 271 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb5hu2/) |
| GOOG | 2026-10-19 22:36 | mention spike | 27 | 18.57 | 22 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| AMZN | 2026-10-19 16:13 | mention spike | 52 | 26.14 | 27 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2h1z/comment/phxyvzj/) |
| RIVN | 2026-10-19 18:51 | mention spike | 2 | 4.57 | 1 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| CRWV | 2026-10-20 14:57 | mention spike | 118 | 93.43 | 68 | 1 | wallstreetbets 118 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 6 | 6.43 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 9 | 5.29 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxslms/) |
| APLD | 2026-10-20 04:07 | mention spike | 15 | 19.14 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
