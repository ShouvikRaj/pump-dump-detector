# Stage 1 candidates

Updated 2026-11-02T15:38:09Z by run `41471948375`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ATC | 2026-11-02 07:17 | mention spike | 10 | 0.0 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xleb57/comment/19s0na4s25s2o/) |
| MSOS | 2026-10-31 21:03 | mention spike | 16 | 2.14 | 12 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s18x3r7nuch/) |
| NNN | 2026-11-01 19:38 | mention spike | 11 | 1.57 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xl8bb4/) |
| PLTR | 2026-11-02 13:09 | mention spike | 42 | 13.57 | 38 | 0 | wallstreetbets 41, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s193s8hhyzo/) |
| RKLB | 2026-11-02 15:08 | mention spike | 18 | 9.71 | 9 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s17t9kio40w/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
