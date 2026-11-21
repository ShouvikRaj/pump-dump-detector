# Stage 1 candidates

Updated 2026-11-21T00:26:11Z by run `44842885532`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ORCL | 2026-11-20 17:56 | mention spike | 11 | 3.86 | 11 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fiv4/) |
| SGOV | 2026-11-20 14:10 | mention spike | 9 | 2.86 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| ROPE | 2026-11-20 03:06 | mention spike | 10 | 4.29 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| OPEX | 2026-11-20 00:51 | mention spike | 5 | 2.71 | 4 | 0 | wallstreetbets 5 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sxu0ui8nsjo/) |
| GME | 2026-11-20 00:51 | mention spike | 16 | 19.29 | 16 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fipl/) |
| INTU | 2026-11-20 03:06 | mention spike | 4 | 2.29 | 2 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| TLT | 2026-11-20 18:35 | mention spike | 5 | 4.86 | 4 | 0 | wallstreetbets 5 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| AMD | 2026-11-20 14:10 | mention spike | 66 | 169.29 | 49 | 0 | wallstreetbets 64, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1hvk2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 331 | 359.71 | 229 | 1 | wallstreetbets 328, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1iwvz/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
