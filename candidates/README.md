# Stage 1 candidates

Updated 2026-11-21T06:05:09Z by run `44873655818`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 28 | 6.29 | 24 | 0 | wallstreetbets 28 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 19 | 4.14 | 18 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| SNDK | 2026-11-21 00:46 | mention spike | 89 | 37.86 | 68 | 0 | wallstreetbets 89 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VOO | 2026-11-21 00:55 | mention spike | 45 | 21.14 | 40 | 0 | wallstreetbets 44, smallstreetbets 1 | NYSE Arca | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y184pu/) |
| VWAV | 2026-11-21 00:46 | mention spike | 13 | 1.43 | 9 | 0 | pennystocks 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y14nen/) |
| ASML | 2026-11-21 03:02 | mention spike | 7 | 7.57 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y15m24/) |
| ROPE | 2026-11-20 03:06 | mention spike | 15 | 5.43 | 15 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 8 | 3.57 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| TLT | 2026-11-20 18:35 | mention spike | 9 | 5.86 | 6 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| OPEX | 2026-11-20 00:51 | mention spike | 10 | 3.71 | 8 | 0 | wallstreetbets 10 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |
| GME | 2026-11-20 00:51 | mention spike | 24 | 22.29 | 22 | 1 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| AMD | 2026-11-20 14:10 | mention spike | 109 | 175.0 | 77 | 0 | wallstreetbets 106, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1hvk2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 448 | 401.0 | 310 | 1 | wallstreetbets 443, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nxno/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
