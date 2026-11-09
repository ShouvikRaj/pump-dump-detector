# Stage 1 candidates

Updated 2026-11-09T21:11:10Z by run `42698758057`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 24 | 11.86 | 21 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se5olbyx6lc/) |
| CVS | 2026-11-09 13:52 | mention spike | 17 | 0.86 | 15 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| NNN | 2026-11-09 15:04 | mention spike | 15 | 5.0 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xraj53/comment/19sdtwmumgskg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1397 | 153.0 | 748 | 0 | wallstreetbets 1379, smallstreetbets 18 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs2gbi/) |
| NYT | 2026-11-09 11:01 | mention spike | 14 | 1.14 | 12 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 10 | 1.14 | 10 | 0 | pennystocks 7, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se4tffoojoh/) |
| ONDS | 2026-11-09 20:48 | mention spike | 10 | 3.43 | 6 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se49e8ob9nm/) |
| TTD | 2026-11-09 21:11 | mention spike | 10 | 1.86 | 8 | 0 | wallstreetbets 10 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se652lxpye9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
