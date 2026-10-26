# Stage 1 candidates

Updated 2026-10-26T19:41:08Z by run `40388708631`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 21 | 0.0 | 19 | 0 | wallstreetbets 21 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| CLS | 2026-10-26 19:24 | mention spike | 10 | 1.0 | 7 | 0 | wallstreetbets 10 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rp167jixh50/) |
| EWZ | 2026-10-26 00:21 | mention spike | 55 | 0.57 | 46 | 0 | wallstreetbets 49, smallstreetbets 6 | NYSE Arca | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 36 | 0.14 | 29 | 1 | wallstreetbets 36 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19roz4o7lz7r8/) |
| NU | 2026-10-26 11:48 | mention spike | 18 | 0.0 | 5 | 0 | wallstreetbets 18 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ros9vyni0ow/) |
| PBR | 2026-10-26 09:22 | mention spike | 29 | 1.43 | 23 | 0 | wallstreetbets 26, smallstreetbets 3 | NYSE | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| RDDT | 2026-10-26 14:04 | mention spike | 76 | 11.71 | 57 | 0 | wallstreetbets 76 | NYSE | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rp2m2acx9ms/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
