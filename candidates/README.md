# Stage 1 candidates

Updated 2026-10-26T15:48:09Z by run `40351693768`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 19 | 0.0 | 17 | 0 | wallstreetbets 19 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rorq5x4t7gg/) |
| EWZ | 2026-10-26 00:21 | mention spike | 50 | 0.57 | 41 | 0 | wallstreetbets 44, smallstreetbets 6 | NYSE Arca | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 34 | 0.14 | 27 | 1 | wallstreetbets 34 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19roskneq0phe/) |
| NU | 2026-10-26 11:48 | mention spike | 18 | 0.0 | 5 | 0 | wallstreetbets 18 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ros9vyni0ow/) |
| PBR | 2026-10-26 09:22 | mention spike | 26 | 1.43 | 20 | 0 | wallstreetbets 23, smallstreetbets 3 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| RDDT | 2026-10-26 14:04 | mention spike | 56 | 11.43 | 45 | 0 | wallstreetbets 56 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rosl0p52lmo/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
