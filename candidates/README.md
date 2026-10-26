# Stage 1 candidates

Updated 2026-10-26T13:08:08Z by run `40327140188`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 43 | 0.86 | 38 | 0 | wallstreetbets 37, smallstreetbets 6 | NYSE Arca | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 25 | 0.14 | 19 | 1 | wallstreetbets 25 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfpzai/comment/19rolcf27yawy/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 0.0 | 5 | 0 | wallstreetbets 10 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rohpzl2h0jl/) |
| PBR | 2026-10-26 09:22 | mention spike | 22 | 1.43 | 16 | 0 | wallstreetbets 19, smallstreetbets 3 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
