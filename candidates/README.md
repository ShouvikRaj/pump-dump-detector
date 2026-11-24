# Stage 1 candidates

Updated 2026-11-24T22:11:07Z by run `45497571299`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 2026-11-24 21:15 | mention spike | 34 | 2.43 | 30 | 0 | wallstreetbets 34 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4q1wd/) |
| HPE | 2026-11-24 00:45 | mention spike | 7 | 4.29 | 6 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t3cgiyb5z2b/) |
| DJT | 2026-11-24 00:45 | mention spike | 4 | 11.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4644ydnp34/) |
| MSS | 2026-11-24 00:45 | mention spike | 1 | 2.29 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t41rnkd6tq9/) |
| SOAR | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| IVVD | 2026-11-24 00:45 | mention spike | 1 | 1.71 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t38ha6mpxno/) |
| NYT | 2026-11-24 00:45 | mention spike | 7 | 18.14 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
