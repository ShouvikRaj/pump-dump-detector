# Stage 1 candidates

Updated 2026-11-21T01:53:08Z by run `44852545600`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 30 | 6.29 | 26 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 19 | 4.0 | 18 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fiv4/) |
| ROPE | 2026-11-20 03:06 | mention spike | 19 | 4.71 | 19 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 10 | 3.29 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| SNDK | 2026-11-21 00:46 | mention spike | 96 | 37.29 | 74 | 0 | wallstreetbets 96 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VWAV | 2026-11-21 00:46 | mention spike | 13 | 1.43 | 9 | 0 | pennystocks 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y14nen/) |
| VOO | 2026-11-21 00:55 | mention spike | 45 | 21.0 | 40 | 0 | wallstreetbets 44, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y184pu/) |
| TLT | 2026-11-20 18:35 | mention spike | 9 | 6.14 | 6 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhtghue96o/) |
| OPEX | 2026-11-20 00:51 | mention spike | 11 | 3.57 | 9 | 0 | wallstreetbets 11 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |
| GME | 2026-11-20 00:51 | mention spike | 28 | 22.29 | 26 | 1 | wallstreetbets 28 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 5 | 3.0 | 2 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y10m65/comment/19sxhagxg7nr4/) |
| AMD | 2026-11-20 14:10 | mention spike | 132 | 177.86 | 96 | 0 | wallstreetbets 129, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1hvk2/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 486 | 397.57 | 334 | 1 | wallstreetbets 479, smallstreetbets 7 | Nasdaq | #24 | [link](https://www.reddit.com/r/smallstreetbets/comments/1y1jd2v/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
