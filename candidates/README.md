# Stage 1 candidates

Updated 2026-10-19T23:16:50Z by run `39340479126`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 62 | 20.14 | 37 | 0 | wallstreetbets 62 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| GLD | 2026-10-19 16:13 | mention spike | 18 | 4.43 | 12 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phroesq/) |
| GOOG | 2026-10-19 22:36 | mention spike | 28 | 16.57 | 18 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| NFLX | 2026-10-19 19:31 | mention spike | 26 | 9.43 | 22 | 0 | wallstreetbets 26 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.57 | 13 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phseny4/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 14 | 7.57 | 14 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ss3y/comment/phrq7ws/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| WDC | 2026-10-19 06:00 | mention spike | 11 | 12.14 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2deu/) |
| VTI | 2026-10-18 05:58 | mention spike | 4 | 4.14 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa0bbn/comment/phr7yfr/) |
| SCHD | 2026-10-17 04:49 | mention spike | 8 | 6.29 | 7 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phqshfm/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
