# Stage 1 candidates

Updated 2026-11-20T21:04:11Z by run `44816191073`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| OPEX | 2026-11-20 00:51 | mention spike | 10 | 1.86 | 8 | 0 | wallstreetbets 10 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtritrbia/) |
| ORCL | 2026-11-20 17:56 | mention spike | 12 | 4.0 | 11 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxiq9388miq/) |
| ROPE | 2026-11-20 03:06 | mention spike | 11 | 3.86 | 11 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 12 | 2.29 | 10 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1990c/comment/19sxqrcborktg/) |
| GME | 2026-11-20 00:51 | mention spike | 30 | 17.0 | 27 | 0 | wallstreetbets 28, smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 9 | 1.57 | 6 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| TLT | 2026-11-20 18:35 | mention spike | 9 | 4.29 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| AMD | 2026-11-20 14:10 | mention spike | 96 | 171.71 | 79 | 1 | wallstreetbets 93, smallstreetbets 3 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y19ev3/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 451 | 336.57 | 311 | 2 | wallstreetbets 448, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1b30g/) |
| PANW | 2026-11-18 21:40 | mention spike | 1 | 11.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
