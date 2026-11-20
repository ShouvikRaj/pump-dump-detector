# Stage 1 candidates

Updated 2026-11-20T21:30:07Z by run `44820182016`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ORCL | 2026-11-20 17:56 | mention spike | 11 | 4.14 | 11 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxiq9388miq/) |
| SGOV | 2026-11-20 14:10 | mention spike | 12 | 2.29 | 10 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1990c/comment/19sxqrcborktg/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| OPEX | 2026-11-20 00:51 | mention spike | 9 | 2.0 | 7 | 0 | wallstreetbets 9 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtritrbia/) |
| GME | 2026-11-20 00:51 | mention spike | 26 | 17.57 | 24 | 0 | wallstreetbets 24, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 4 | 2.29 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| TLT | 2026-11-20 18:35 | mention spike | 9 | 4.29 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| AMD | 2026-11-20 14:10 | mention spike | 85 | 172.29 | 71 | 1 | wallstreetbets 82, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y19ev3/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 407 | 343.0 | 281 | 2 | wallstreetbets 404, smallstreetbets 3 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1etd1/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
