# Stage 1 candidates

Updated 2026-11-22T01:18:28Z by run `44970279568`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| MSTR | 2026-11-22 00:48 | mention spike | 33 | 19.71 | 30 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nj84/) |
| NYT | 2026-11-22 00:48 | mention spike | 26 | 9.43 | 25 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y273h3/comment/19szo09q6zq4g/) |
| CRWD | 2026-11-21 00:55 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| ORCL | 2026-11-20 17:56 | mention spike | 13 | 6.86 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| VWAV | 2026-11-21 00:46 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SNDK | 2026-11-21 00:46 | mention spike | 41 | 53.86 | 27 | 0 | wallstreetbets 39, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y259ja/) |
| VOO | 2026-11-21 00:55 | mention spike | 31 | 28.86 | 31 | 0 | wallstreetbets 27, smallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y2a5v2/) |
| ASML | 2026-11-21 03:02 | mention spike | 16 | 7.43 | 14 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y20zkd/comment/19szjropocqwy/) |
| ROPE | 2026-11-20 03:06 | mention spike | 2 | 7.86 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1gajf/comment/19sy70b3x1agw/) |
| SGOV | 2026-11-20 14:10 | mention spike | 4 | 5.57 | 4 | 0 | wallstreetbets 3, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19szjf1z9srpc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
