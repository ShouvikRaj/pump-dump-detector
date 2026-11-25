# Stage 1 candidates

Updated 2026-11-25T09:19:06Z by run `45583404148`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BENF | 2026-11-25 00:43 | mention spike | 11 | 0.0 | 6 | 0 | pennystocks 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y4edv2/) |
| DELL | 2026-11-24 21:15 | mention spike | 35 | 3.71 | 31 | 0 | wallstreetbets 35 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| HPE | 2026-11-24 00:45 | mention spike | 3 | 7.29 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4uwxevhmmd/) |
| DJT | 2026-11-24 00:45 | mention spike | 8 | 12.29 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4rrfk/comment/19t58n1cxqhj8/) |
| MSS | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOAR | 2026-11-24 00:45 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t4lim86r20x/) |
| IVVD | 2026-11-24 00:45 | mention spike | 2 | 1.86 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t4jxdoc4a9s/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
