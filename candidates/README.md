# Stage 1 candidates

Updated 2026-11-24T03:56:05Z by run `45322704793`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DJT | 2026-11-24 00:45 | mention spike | 30 | 9.29 | 28 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3lcgm/) |
| HPE | 2026-11-24 00:45 | mention spike | 28 | 1.29 | 21 | 0 | wallstreetbets 28 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t3cgiyb5z2b/) |
| IVVD | 2026-11-24 00:45 | mention spike | 13 | 0.0 | 6 | 0 | pennystocks 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y3ix9x/) |
| MSS | 2026-11-24 00:45 | mention spike | 13 | 0.43 | 8 | 0 | pennystocks 11, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39tci/) |
| NYT | 2026-11-24 00:45 | mention spike | 54 | 11.29 | 46 | 0 | wallstreetbets 54 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |
| SOAR | 2026-11-24 00:45 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 10 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y39myz/comment/19t2xtlugwjvm/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
