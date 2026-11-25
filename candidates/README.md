# Stage 1 candidates

Updated 2026-11-25T12:51:09Z by run `45616931959`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BENF | 2026-11-25 00:43 | mention spike | 12 | 0.14 | 7 | 0 | pennystocks 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y4edv2/) |
| DELL | 2026-11-24 21:15 | mention spike | 36 | 3.71 | 32 | 0 | wallstreetbets 36 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| HPE | 2026-11-24 00:45 | mention spike | 1 | 7.57 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4uwxevhmmd/) |
| DJT | 2026-11-24 00:45 | mention spike | 6 | 12.43 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4rrfk/comment/19t58n1cxqhj8/) |
| MSS | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
