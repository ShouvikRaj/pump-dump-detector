# Stage 1 candidates

Updated 2026-11-21T20:56:10Z by run `44948426213`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 27 | 6.14 | 23 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 3 | 6.14 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| VWAV | 2026-11-21 00:46 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SNDK | 2026-11-21 00:46 | mention spike | 10 | 46.86 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y259ja/) |
| VOO | 2026-11-21 00:55 | mention spike | 18 | 24.29 | 16 | 0 | wallstreetbets 17, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1i0rl/comment/19sz039z7i55t/) |
| ASML | 2026-11-21 03:02 | mention spike | 2 | 7.14 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y20zkd/comment/19szh15ny1268/) |
| ROPE | 2026-11-20 03:06 | mention spike | 5 | 6.29 | 5 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1gajf/comment/19sy70b3x1agw/) |
| SGOV | 2026-11-20 14:10 | mention spike | 2 | 4.29 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| TLT | 2026-11-20 18:35 | mention spike | 1 | 6.86 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1zkyu/) |
| OPEX | 2026-11-20 00:51 | mention spike | 4 | 4.57 | 3 | 0 | wallstreetbets 4 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
