# Stage 1 candidates

Updated 2026-11-21T12:45:08Z by run `44905068779`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 28 | 6.0 | 24 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 16 | 4.57 | 16 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| VWAV | 2026-11-21 00:46 | mention spike | 10 | 1.86 | 9 | 0 | pennystocks 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y14nen/) |
| SNDK | 2026-11-21 00:46 | mention spike | 78 | 38.14 | 59 | 0 | wallstreetbets 78 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VOO | 2026-11-21 00:55 | mention spike | 40 | 22.0 | 35 | 0 | wallstreetbets 38, smallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y184pu/) |
| ASML | 2026-11-21 03:02 | mention spike | 4 | 7.14 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y15m24/) |
| ROPE | 2026-11-20 03:06 | mention spike | 14 | 5.57 | 14 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 8 | 3.43 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| TLT | 2026-11-20 18:35 | mention spike | 5 | 6.43 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| OPEX | 2026-11-20 00:51 | mention spike | 8 | 4.0 | 6 | 0 | wallstreetbets 8 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |
| GME | 2026-11-20 00:51 | mention spike | 24 | 20.86 | 22 | 1 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| AMD | 2026-11-20 14:10 | mention spike | 83 | 173.29 | 60 | 0 | wallstreetbets 80, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1hvk2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 343 | 413.86 | 258 | 1 | wallstreetbets 338, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1srwr/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
