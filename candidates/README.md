# Stage 1 candidates

Updated 2026-11-20T17:18:09Z by run `44781097540`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| OPEX | 2026-11-20 00:51 | mention spike | 10 | 1.71 | 7 | 0 | wallstreetbets 10 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9gf39djb7/) |
| SGOV | 2026-11-20 14:10 | mention spike | 11 | 2.29 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9na9jnz0h/) |
| GME | 2026-11-20 00:51 | mention spike | 28 | 16.71 | 25 | 0 | wallstreetbets 25, smallstreetbets 2, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 9 | 1.43 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swej7841xeo/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 3.71 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9c8dpx5ok/) |
| AMD | 2026-11-20 14:10 | mention spike | 92 | 180.71 | 79 | 2 | wallstreetbets 83, smallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y18cpg/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 413 | 332.14 | 296 | 3 | wallstreetbets 408, smallstreetbets 4, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y174bn/) |
| PANW | 2026-11-18 21:40 | mention spike | 1 | 12.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
