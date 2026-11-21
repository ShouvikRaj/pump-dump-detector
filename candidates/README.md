# Stage 1 candidates

Updated 2026-11-21T17:08:08Z by run `44928138028`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | 2026-11-21 00:55 | mention spike | 27 | 6.14 | 23 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jmoj/) |
| ORCL | 2026-11-20 17:56 | mention spike | 4 | 6.0 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1nt2e/) |
| VWAV | 2026-11-21 00:46 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SNDK | 2026-11-21 00:46 | mention spike | 15 | 46.14 | 15 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1fmld/) |
| VOO | 2026-11-21 00:55 | mention spike | 33 | 22.29 | 29 | 0 | wallstreetbets 31, smallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1i0rl/comment/19sz039z7i55t/) |
| ASML | 2026-11-21 03:02 | mention spike | 2 | 7.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sxsxv3j4nr7/) |
| ROPE | 2026-11-20 03:06 | mention spike | 8 | 6.29 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1bi72/) |
| SGOV | 2026-11-20 14:10 | mention spike | 3 | 4.14 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1had5/) |
| TLT | 2026-11-20 18:35 | mention spike | 1 | 6.86 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1zkyu/) |
| OPEX | 2026-11-20 00:51 | mention spike | 4 | 4.57 | 3 | 0 | wallstreetbets 4 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19sy41fab40uc/) |
| GME | 2026-11-20 00:51 | mention spike | 14 | 22.0 | 14 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1jlmk/) |
| INTU | 2026-11-20 03:06 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
