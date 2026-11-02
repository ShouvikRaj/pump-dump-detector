# Stage 1 candidates

Updated 2026-11-02T15:08:09Z by run `41467580753`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-02 07:17 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| MSOS | 2026-10-31 21:03 | mention spike | 15 | 2.14 | 11 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s17vnwgu06a/) |
| NNN | 2026-11-01 19:38 | mention spike | 10 | 1.57 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xl8bb4/) |
| PLTR | 2026-11-02 13:09 | mention spike | 38 | 13.57 | 34 | 0 | wallstreetbets 37, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s18d8lk7vs5/) |
| RKLB | 2026-11-02 15:08 | mention spike | 18 | 9.71 | 9 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s17t9kio40w/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
