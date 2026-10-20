# Stage 1 candidates

Updated 2026-10-20T01:43:26Z by run `39354838606`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 62 | 20.57 | 38 | 0 | wallstreetbets 62 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| GLD | 2026-10-19 16:13 | mention spike | 18 | 4.57 | 12 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phszhop/) |
| GOOG | 2026-10-19 22:36 | mention spike | 29 | 17.0 | 19 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| NFLX | 2026-10-19 19:31 | mention spike | 26 | 9.71 | 22 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.57 | 13 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phseny4/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 13 | 7.71 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ss3y/comment/phrq7ws/) |
| WDC | 2026-10-19 06:00 | mention spike | 11 | 12.14 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2deu/) |
| VTI | 2026-10-18 05:58 | mention spike | 4 | 4.14 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa0bbn/comment/phr7yfr/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
