# Stage 1 candidates

Updated 2026-11-21T15:35:11Z by run `44919746570`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 28 | 6.0 | 24 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 10 | 5.29 | 10 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| VWAV | 2026-11-21 00:46 | mention spike | 4 | 2.71 | 4 | 0 | pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y0utx8/comment/19sxfluux66it/) |
| SNDK | 2026-11-21 00:46 | mention spike | 54 | 41.29 | 46 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VOO | 2026-11-21 00:55 | mention spike | 38 | 21.86 | 34 | 0 | wallstreetbets 36, smallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y184pu/) |
| ASML | 2026-11-21 03:02 | mention spike | 2 | 7.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sxsxv3j4nr7/) |
| ROPE | 2026-11-20 03:06 | mention spike | 11 | 5.86 | 11 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 3 | 4.14 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| TLT | 2026-11-20 18:35 | mention spike | 4 | 6.57 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1zkyu/) |
| OPEX | 2026-11-20 00:51 | mention spike | 6 | 4.29 | 5 | 0 | wallstreetbets 6 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |
| GME | 2026-11-20 00:51 | mention spike | 22 | 21.14 | 20 | 1 | wallstreetbets 22 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
