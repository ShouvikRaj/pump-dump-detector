# Stage 1 candidates

Updated 2026-11-01T15:25:06Z by run `41320860007`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| MSOS | 2026-10-31 21:03 | mention spike | 12 | 0.43 | 10 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkftz6/) |
| INO | 2026-10-31 02:57 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TQQQ | 2026-10-30 18:26 | mention spike | 1 | 7.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjpq2t/comment/19ryp1kou93s3/) |
| NVDA | 2026-10-30 11:53 | mention spike | 32 | 79.71 | 25 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkqgq7/) |
| AMD | 2026-10-30 13:25 | mention spike | 38 | 50.0 | 31 | 0 | wallstreetbets 34, smallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xl3gjf/) |
| SOXL | 2026-10-30 19:57 | mention spike | 6 | 35.43 | 6 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjpq2t/comment/19rz9dzzvw4f6/) |
| APP | 2026-10-30 17:00 | mention spike | 1 | 4.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjrx34/comment/19ry48f2kiuw1/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
