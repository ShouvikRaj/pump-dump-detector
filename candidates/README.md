# Stage 1 candidates

Updated 2026-11-24T13:01:10Z by run `45398852510`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DJT | 2026-11-24 00:45 | mention spike | 30 | 9.43 | 28 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3lcgm/) |
| HPE | 2026-11-24 00:45 | mention spike | 28 | 1.29 | 21 | 0 | wallstreetbets 28 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t3cgiyb5z2b/) |
| MSS | 2026-11-24 00:45 | mention spike | 12 | 0.71 | 7 | 0 | pennystocks 11, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t41rnkd6tq9/) |
| SOAR | 2026-11-24 00:45 | mention spike | 8 | 0.29 | 7 | 0 | pennystocks 8 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t2xtlugwjvm/) |
| IVVD | 2026-11-24 00:45 | mention spike | 6 | 1.0 | 5 | 0 | pennystocks 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y3ix9x/) |
| NYT | 2026-11-24 00:45 | mention spike | 22 | 16.0 | 22 | 0 | wallstreetbets 22 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
