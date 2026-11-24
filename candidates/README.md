# Stage 1 candidates

Updated 2026-11-24T06:10:08Z by run `45338106586`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DJT | 2026-11-24 00:45 | mention spike | 29 | 9.43 | 27 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3lcgm/) |
| HPE | 2026-11-24 00:45 | mention spike | 28 | 1.29 | 21 | 0 | wallstreetbets 28 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t3cgiyb5z2b/) |
| IVVD | 2026-11-24 00:45 | mention spike | 13 | 0.0 | 6 | 0 | pennystocks 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y3ix9x/) |
| MSS | 2026-11-24 00:45 | mention spike | 12 | 0.57 | 7 | 0 | pennystocks 10, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t30jxa8m5cz/) |
| SOAR | 2026-11-24 00:45 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 10 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t2xtlugwjvm/) |
| NYT | 2026-11-24 00:45 | mention spike | 37 | 13.71 | 33 | 0 | wallstreetbets 37 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
