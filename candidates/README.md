# Stage 1 candidates

Updated 2026-10-19T11:44:32Z by run `39246748933`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| WDC | 2026-10-19 06:00 | mention spike | 18 | 11.0 | 17 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| VTI | 2026-10-18 05:58 | mention spike | 4 | 3.86 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/comment/phlcwg8/) |
| SCHD | 2026-10-17 04:49 | mention spike | 6 | 6.29 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/pho8eri/) |
| NFLX | 2026-10-17 17:37 | mention spike | 7 | 9.29 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1typ6n0/comment/phn9fe6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
