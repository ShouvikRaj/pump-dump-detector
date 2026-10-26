# Stage 1 candidates

Updated 2026-10-26T16:29:08Z by run `40358208316`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 19 | 0.0 | 17 | 0 | wallstreetbets 19 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rorq5x4t7gg/) |
| EWZ | 2026-10-26 00:21 | mention spike | 53 | 0.57 | 44 | 0 | wallstreetbets 47, smallstreetbets 6 | NYSE Arca | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 34 | 0.14 | 27 | 1 | wallstreetbets 34 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19roskneq0phe/) |
| NU | 2026-10-26 11:48 | mention spike | 18 | 0.0 | 5 | 0 | wallstreetbets 18 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ros9vyni0ow/) |
| PBR | 2026-10-26 09:22 | mention spike | 26 | 1.43 | 20 | 0 | wallstreetbets 23, smallstreetbets 3 | NYSE | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| RDDT | 2026-10-26 14:04 | mention spike | 59 | 11.43 | 47 | 0 | wallstreetbets 59 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rotysoqpon7/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
