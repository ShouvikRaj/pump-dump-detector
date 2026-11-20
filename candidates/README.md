# Stage 1 candidates

Updated 2026-11-20T21:41:07Z by run `44822147454`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ORCL | 2026-11-20 17:56 | mention spike | 12 | 4.14 | 12 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fiv4/) |
| SGOV | 2026-11-20 14:10 | mention spike | 11 | 2.43 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1990c/comment/19sxqrcborktg/) |
| ROPE | 2026-11-20 03:06 | mention spike | 9 | 4.14 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| OPEX | 2026-11-20 00:51 | mention spike | 9 | 2.0 | 7 | 0 | wallstreetbets 9 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtritrbia/) |
| GME | 2026-11-20 00:51 | mention spike | 25 | 17.71 | 24 | 0 | wallstreetbets 23, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fipl/) |
| INTU | 2026-11-20 03:06 | mention spike | 4 | 2.29 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| TLT | 2026-11-20 18:35 | mention spike | 9 | 4.29 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| AMD | 2026-11-20 14:10 | mention spike | 81 | 172.57 | 67 | 1 | wallstreetbets 79, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fb7l/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 391 | 345.43 | 271 | 2 | wallstreetbets 388, smallstreetbets 3 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fipl/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
