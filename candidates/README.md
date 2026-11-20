# Stage 1 candidates

Updated 2026-11-20T03:20:08Z by run `44666702018`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 1108 | 204.14 | 688 | 3 | wallstreetbets 1103, pennystocks 3, smallstreetbets 2 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0sab3/) |
| GME | 2026-11-20 00:51 | mention spike | 37 | 16.0 | 34 | 0 | wallstreetbets 33, pennystocks 2, smallstreetbets 2 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| INTU | 2026-11-20 03:06 | mention spike | 10 | 1.29 | 6 | 0 | wallstreetbets 10 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swej7841xeo/) |
| OPEX | 2026-11-20 00:51 | mention spike | 10 | 1.43 | 8 | 0 | wallstreetbets 10 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swe60mm2hk5/) |
| ROPE | 2026-11-20 03:06 | mention spike | 11 | 3.71 | 11 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swg9m537pet/) |
| PANW | 2026-11-18 21:40 | mention spike | 2 | 12.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |
| UNH | 2026-11-18 17:15 | mention spike | 19 | 9.29 | 16 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 32 | 23.0 | 26 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kyvz/comment/19sw3102ah6e8/) |
| TTWO | 2026-11-19 00:42 | mention spike | 20 | 17.0 | 20 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eqrp/) |
| LULU | 2026-11-19 00:49 | mention spike | 3 | 3.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpta7/comment/19svv61ikre0y/) |
| CRWD | 2026-11-19 03:02 | mention spike | 2 | 6.86 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19swfyfkzb5gi/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
