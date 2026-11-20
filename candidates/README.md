# Stage 1 candidates

Updated 2026-11-20T18:25:09Z by run `44791648428`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GME | 2026-11-20 00:51 | mention spike | 30 | 17.0 | 27 | 0 | wallstreetbets 27, smallstreetbets 2, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 10 | 1.43 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| OPEX | 2026-11-20 00:51 | mention spike | 11 | 1.71 | 8 | 0 | wallstreetbets 11 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtritrbia/) |
| ORCL | 2026-11-20 17:56 | mention spike | 12 | 4.29 | 11 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxiq9388miq/) |
| SGOV | 2026-11-20 14:10 | mention spike | 11 | 2.29 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9na9jnz0h/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxiqnnafq4j/) |
| AMD | 2026-11-20 14:10 | mention spike | 111 | 178.71 | 91 | 1 | wallstreetbets 104, smallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y19ev3/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 475 | 333.29 | 331 | 2 | wallstreetbets 472, smallstreetbets 3 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1990c/) |
| PANW | 2026-11-18 21:40 | mention spike | 1 | 12.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
