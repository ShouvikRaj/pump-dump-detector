# Stage 1 candidates

Updated 2026-10-26T12:14:08Z by run `40320292936`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 38 | 0.86 | 33 | 0 | wallstreetbets 32, smallstreetbets 6 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 22 | 0.14 | 17 | 1 | wallstreetbets 22 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19roivesxi6ma/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 0.0 | 5 | 0 | wallstreetbets 10 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rohpzl2h0jl/) |
| PBR | 2026-10-26 09:22 | mention spike | 20 | 1.43 | 15 | 0 | wallstreetbets 17, smallstreetbets 3 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
