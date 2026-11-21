# Stage 1 candidates

Updated 2026-11-21T14:32:11Z by run `44913936302`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 28 | 6.0 | 24 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 12 | 5.0 | 12 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| VWAV | 2026-11-21 00:46 | mention spike | 6 | 2.43 | 6 | 0 | pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y0utx8/comment/19sxfluux66it/) |
| SNDK | 2026-11-21 00:46 | mention spike | 55 | 41.29 | 47 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VOO | 2026-11-21 00:55 | mention spike | 38 | 22.14 | 34 | 0 | wallstreetbets 36, smallstreetbets 2 | NYSE Arca | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y184pu/) |
| ASML | 2026-11-21 03:02 | mention spike | 3 | 7.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y15m24/) |
| ROPE | 2026-11-20 03:06 | mention spike | 11 | 6.0 | 11 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 3 | 4.14 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| TLT | 2026-11-20 18:35 | mention spike | 3 | 6.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| OPEX | 2026-11-20 00:51 | mention spike | 6 | 4.29 | 5 | 0 | wallstreetbets 6 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |
| GME | 2026-11-20 00:51 | mention spike | 22 | 21.29 | 20 | 1 | wallstreetbets 22 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| AMD | 2026-11-20 14:10 | mention spike | 63 | 174.29 | 50 | 0 | wallstreetbets 62, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1hvk2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 156 | 439.86 | 137 | 0 | wallstreetbets 150, smallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1xc75/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
