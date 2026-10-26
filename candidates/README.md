# Stage 1 candidates

Updated 2026-10-26T14:04:08Z by run `40334783297`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ronwxmvkirk/) |
| EWZ | 2026-10-26 00:21 | mention spike | 46 | 0.71 | 40 | 0 | wallstreetbets 40, smallstreetbets 6 | NYSE Arca | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 28 | 0.14 | 22 | 1 | wallstreetbets 28 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ronqlmygtfl/) |
| NU | 2026-10-26 11:48 | mention spike | 15 | 0.0 | 5 | 0 | wallstreetbets 15 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ronb4c20g01/) |
| PBR | 2026-10-26 09:22 | mention spike | 25 | 1.43 | 19 | 0 | wallstreetbets 22, smallstreetbets 3 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |
| RDDT | 2026-10-26 14:04 | mention spike | 30 | 11.57 | 25 | 0 | wallstreetbets 30 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ronv52isxkx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
