# Stage 1 candidates

Updated 2026-10-26T11:48:06Z by run `40317043004`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | 2026-10-26 00:21 | mention spike | 37 | 0.86 | 32 | 0 | wallstreetbets 31, smallstreetbets 6 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 20 | 0.14 | 16 | 1 | wallstreetbets 20 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfpzai/comment/19rohz2h4ukea/) |
| PBR | 2026-10-26 09:22 | mention spike | 19 | 1.57 | 14 | 0 | wallstreetbets 16, smallstreetbets 3 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| NU | 2026-10-26 11:48 | mention spike | 10 | 0.0 | 5 | 0 | wallstreetbets 10 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19rohpzl2h0jl/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
