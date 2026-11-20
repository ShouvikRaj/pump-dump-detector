# Stage 1 candidates

Updated 2026-11-20T22:48:11Z by run `44831465952`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ORCL | 2026-11-20 17:56 | mention spike | 12 | 4.29 | 11 | 0 | wallstreetbets 12 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fiv4/) |
| SGOV | 2026-11-20 14:10 | mention spike | 9 | 2.71 | 7 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1990c/comment/19sxqrcborktg/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 4.14 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| OPEX | 2026-11-20 00:51 | mention spike | 7 | 2.43 | 6 | 0 | wallstreetbets 7 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sxu0ui8nsjo/) |
| GME | 2026-11-20 00:51 | mention spike | 20 | 18.86 | 20 | 0 | wallstreetbets 18, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fipl/) |
| INTU | 2026-11-20 03:06 | mention spike | 4 | 2.29 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| TLT | 2026-11-20 18:35 | mention spike | 7 | 4.57 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| AMD | 2026-11-20 14:10 | mention spike | 69 | 170.43 | 51 | 0 | wallstreetbets 68, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fb7l/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 347 | 352.0 | 242 | 2 | wallstreetbets 344, smallstreetbets 3 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fipl/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
