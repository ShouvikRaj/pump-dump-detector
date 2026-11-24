# Stage 1 candidates

Updated 2026-11-24T15:15:05Z by run `45422804091`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| HPE | 2026-11-24 00:45 | mention spike | 28 | 1.29 | 21 | 0 | wallstreetbets 28 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t3cgiyb5z2b/) |
| DJT | 2026-11-24 00:45 | mention spike | 21 | 10.71 | 21 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3lcgm/) |
| MSS | 2026-11-24 00:45 | mention spike | 6 | 1.57 | 4 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t41rnkd6tq9/) |
| SOAR | 2026-11-24 00:45 | mention spike | 6 | 0.57 | 6 | 0 | pennystocks 6 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t2xtlugwjvm/) |
| IVVD | 2026-11-24 00:45 | mention spike | 2 | 1.57 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t38ha6mpxno/) |
| NYT | 2026-11-24 00:45 | mention spike | 15 | 17.14 | 15 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
