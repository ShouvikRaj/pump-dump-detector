# Stage 1 candidates

Updated 2026-11-20T12:49:09Z by run `44738717798`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 895 | 233.71 | 584 | 3 | wallstreetbets 887, smallstreetbets 5, pennystocks 3 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y12hpi/) |
| GME | 2026-11-20 00:51 | mention spike | 35 | 15.71 | 32 | 0 | wallstreetbets 32, smallstreetbets 2, pennystocks 1 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 10 | 1.29 | 6 | 0 | wallstreetbets 10 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swej7841xeo/) |
| OPEX | 2026-11-20 00:51 | mention spike | 9 | 1.57 | 7 | 0 | wallstreetbets 9 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swe60mm2hk5/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 3.86 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swg9m537pet/) |
| PANW | 2026-11-18 21:40 | mention spike | 2 | 12.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |
| UNH | 2026-11-18 17:15 | mention spike | 17 | 9.57 | 15 | 0 | wallstreetbets 17 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 23 | 24.0 | 20 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kyvz/comment/19sw3102ah6e8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
