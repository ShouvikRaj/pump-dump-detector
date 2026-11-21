# Stage 1 candidates

Updated 2026-11-21T00:55:13Z by run `44845813814`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ORCL | 2026-11-20 17:56 | mention spike | 20 | 3.86 | 19 | 0 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fiv4/) |
| ROPE | 2026-11-20 03:06 | mention spike | 20 | 4.57 | 20 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SNDK | 2026-11-21 00:46 | mention spike | 99 | 36.71 | 78 | 0 | wallstreetbets 99 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VWAV | 2026-11-21 00:46 | mention spike | 13 | 1.43 | 9 | 0 | pennystocks 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y14nen/) |
| CRWD | 2026-11-21 00:55 | mention spike | 29 | 6.29 | 25 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| VOO | 2026-11-21 00:55 | mention spike | 46 | 20.86 | 41 | 0 | wallstreetbets 45, smallstreetbets 1 | NYSE Arca | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y184pu/) |
| TLT | 2026-11-20 18:35 | mention spike | 11 | 5.71 | 6 | 0 | wallstreetbets 11 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| SGOV | 2026-11-20 14:10 | mention spike | 9 | 3.29 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| OPEX | 2026-11-20 00:51 | mention spike | 8 | 3.43 | 7 | 0 | wallstreetbets 8 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sxu0ui8nsjo/) |
| GME | 2026-11-20 00:51 | mention spike | 32 | 21.43 | 30 | 1 | wallstreetbets 31, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 7 | 2.71 | 2 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| AMD | 2026-11-20 14:10 | mention spike | 145 | 176.71 | 107 | 0 | wallstreetbets 142, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1hvk2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 516 | 391.14 | 352 | 1 | wallstreetbets 509, smallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1jd2v/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
