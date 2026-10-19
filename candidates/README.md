# Stage 1 candidates

Updated 2026-10-19T07:19:43Z by run `39215204912`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| WDC | 2026-10-19 06:00 | mention spike | 20 | 10.57 | 19 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| VTI | 2026-10-18 05:58 | mention spike | 5 | 3.71 | 5 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/comment/phlcwg8/) |
| SCHD | 2026-10-17 04:49 | mention spike | 5 | 6.29 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ct1y/comment/phmf0ll/) |
| NFLX | 2026-10-17 17:37 | mention spike | 8 | 9.14 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1typ6n0/comment/phn9fe6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
