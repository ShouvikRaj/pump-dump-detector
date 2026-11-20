# Stage 1 candidates

Updated 2026-11-20T16:51:09Z by run `44776689609`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GME | 2026-11-20 00:51 | mention spike | 30 | 16.43 | 26 | 0 | wallstreetbets 27, smallstreetbets 2, pennystocks 1 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| OPEX | 2026-11-20 00:51 | mention spike | 10 | 1.71 | 7 | 0 | wallstreetbets 10 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9gf39djb7/) |
| SGOV | 2026-11-20 14:10 | mention spike | 12 | 2.14 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9na9jnz0h/) |
| INTU | 2026-11-20 03:06 | mention spike | 9 | 1.43 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swej7841xeo/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 3.71 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9c8dpx5ok/) |
| AMD | 2026-11-20 14:10 | mention spike | 99 | 181.43 | 84 | 2 | wallstreetbets 90, smallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y15ase/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 564 | 310.86 | 394 | 3 | wallstreetbets 559, smallstreetbets 4, pennystocks 1 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y174bn/) |
| PANW | 2026-11-18 21:40 | mention spike | 1 | 12.14 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
