# Stage 1 candidates

Updated 2026-10-21T22:32:11Z by run `39687093670`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 104 | 20.14 | 64 | 0 | wallstreetbets 103, smallstreetbets 1 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbz1vw/comment/19rgdnwv4h0cg/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 23.0 | 42 | 1 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgc2q1vjnz6/) |
| IBM | 2026-10-21 18:15 | mention spike | 80 | 2.86 | 51 | 1 | wallstreetbets 80 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgdp4wga42q/) |
| LRCX | 2026-10-20 16:42 | mention spike | 64 | 3.71 | 43 | 1 | wallstreetbets 64 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgbx4tk0un9/) |
| META | 2026-10-21 11:34 | mention spike | 312 | 32.14 | 176 | 1 | wallstreetbets 311, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 9.57 | 18 | 0 | wallstreetbets 28 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 10 | 0 | wallstreetbets 15 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SPCX | 2026-10-20 10:18 | mention spike | 312 | 76.71 | 192 | 1 | wallstreetbets 310, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 52 | 14.0 | 37 | 1 | wallstreetbets 51, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 142 | 33.57 | 105 | 0 | wallstreetbets 137, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 10 | 5.71 | 7 | 1 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 4 | 1.14 | 4 | 0 | smallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 15 | 8.57 | 11 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
