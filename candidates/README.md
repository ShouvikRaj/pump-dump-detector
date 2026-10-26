# Stage 1 candidates

Updated 2026-10-26T17:54:08Z by run `40372850245`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 20 | 0.0 | 18 | 0 | wallstreetbets 20 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| EWZ | 2026-10-26 00:21 | mention spike | 54 | 0.57 | 45 | 0 | wallstreetbets 48, smallstreetbets 6 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 34 | 0.14 | 27 | 1 | wallstreetbets 34 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19roskneq0phe/) |
| NU | 2026-10-26 11:48 | mention spike | 18 | 0.0 | 5 | 0 | wallstreetbets 18 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ros9vyni0ow/) |
| PBR | 2026-10-26 09:22 | mention spike | 26 | 1.43 | 20 | 0 | wallstreetbets 23, smallstreetbets 3 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| RDDT | 2026-10-26 14:04 | mention spike | 63 | 11.43 | 51 | 0 | wallstreetbets 63 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19roxrt9khcsi/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
