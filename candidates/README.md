# Stage 1 candidates

Updated 2026-10-21T20:00:37Z by run `39665377422`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 93 | 19.86 | 60 | 0 | wallstreetbets 92, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 65 | 22.14 | 39 | 0 | wallstreetbets 65 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg6lzzls20y/) |
| IBM | 2026-10-21 18:15 | mention spike | 23 | 2.71 | 17 | 1 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg6ialk89j9/) |
| LRCX | 2026-10-20 16:42 | mention spike | 31 | 3.43 | 17 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7lpd9/comment/19rg6errd3pvm/) |
| META | 2026-10-21 11:34 | mention spike | 154 | 30.43 | 104 | 0 | wallstreetbets 153, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 8.86 | 21 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.0 | 10 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg5tn2f0w8x/) |
| NFLX | 2026-10-19 19:31 | mention spike | 219 | 21.86 | 162 | 0 | wallstreetbets 214, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 6.0 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.43 | 10 | 1 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| SMCI | 2026-10-20 21:06 | mention spike | 108 | 6.29 | 69 | 1 | wallstreetbets 107, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 451 | 54.71 | 264 | 2 | wallstreetbets 449, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| PAC | 2026-10-21 02:19 | mention spike | 5 | 1.0 | 5 | 0 | smallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 8.86 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0szjg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
