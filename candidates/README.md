# Stage 1 candidates

Updated 2026-11-09T16:22:08Z by run `42652496630`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 22 | 11.43 | 19 | 0 | wallstreetbets 22 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19sds7cubowis/) |
| CVS | 2026-11-09 13:52 | mention spike | 15 | 0.86 | 13 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| NNN | 2026-11-09 15:04 | mention spike | 15 | 5.57 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xraj53/comment/19sdsuvrr2cgy/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1256 | 144.57 | 678 | 0 | wallstreetbets 1243, smallstreetbets 13 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrvueo/) |
| NYT | 2026-11-09 11:01 | mention spike | 12 | 1.0 | 10 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
