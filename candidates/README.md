# Stage 1 candidates

Updated 2026-11-25T00:13:09Z by run `45515259633`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 2026-11-24 21:15 | mention spike | 33 | 2.57 | 29 | 0 | wallstreetbets 33 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4q1wd/) |
| HPE | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| DJT | 2026-11-24 00:45 | mention spike | 2 | 11.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4644ydnp34/) |
| MSS | 2026-11-24 00:45 | mention spike | 1 | 2.29 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t41rnkd6tq9/) |
| SOAR | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| IVVD | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NYT | 2026-11-24 00:45 | mention spike | 4 | 18.43 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
