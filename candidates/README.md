# Stage 1 candidates

Updated 2026-10-26T13:51:07Z by run `40332813271`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 12 | 0.0 | 11 | 0 | wallstreetbets 12 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19romqlvmnj7p/) |
| EWZ | 2026-10-26 00:21 | mention spike | 45 | 0.86 | 39 | 0 | wallstreetbets 39, smallstreetbets 6 | NYSE Arca | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 27 | 0.14 | 21 | 1 | wallstreetbets 27 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ronakok0s8z/) |
| NU | 2026-10-26 11:48 | mention spike | 15 | 0.0 | 5 | 0 | wallstreetbets 15 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ronb4c20g01/) |
| PBR | 2026-10-26 09:22 | mention spike | 24 | 1.43 | 18 | 0 | wallstreetbets 21, smallstreetbets 3 | NYSE | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
