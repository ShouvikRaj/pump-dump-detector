# Stage 1 candidates

Updated 2026-11-20T14:36:06Z by run `44754606362`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-20 14:10 | mention spike | 384 | 151.14 | 260 | 2 | wallstreetbets 374, smallstreetbets 10 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0ynu2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 1014 | 246.57 | 619 | 4 | wallstreetbets 1006, smallstreetbets 5, pennystocks 3 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y12hpi/) |
| GME | 2026-11-20 00:51 | mention spike | 37 | 15.57 | 33 | 0 | wallstreetbets 34, smallstreetbets 2, pennystocks 1 | NYSE | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 10 | 1.29 | 6 | 0 | wallstreetbets 10 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swej7841xeo/) |
| OPEX | 2026-11-20 00:51 | mention spike | 11 | 1.57 | 8 | 0 | wallstreetbets 11 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9gf39djb7/) |
| ROPE | 2026-11-20 03:06 | mention spike | 13 | 3.71 | 13 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9c8dpx5ok/) |
| SGOV | 2026-11-20 14:10 | mention spike | 12 | 2.14 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx9na9jnz0h/) |
| PANW | 2026-11-18 21:40 | mention spike | 2 | 12.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |
| UNH | 2026-11-18 17:15 | mention spike | 18 | 9.57 | 16 | 0 | wallstreetbets 18 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 20 | 24.71 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sx80g7971fo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
