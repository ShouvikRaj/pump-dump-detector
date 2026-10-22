# Stage 1 candidates

Updated 2026-10-22T12:26:10Z by run `39778210053`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 26 | 0.57 | 10 | 0 | pennystocks 26 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| AVEX | 2026-10-22 11:25 | mention spike | 10 | 0.86 | 8 | 0 | wallstreetbets 6, pennystocks 4 | NYSE | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbyywi/) |
| BABA | 2026-10-22 02:50 | mention spike | 12 | 1.29 | 9 | 0 | wallstreetbets 12 | NYSE | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh54s6o6fc4/) |
| GOOG | 2026-10-19 22:36 | mention spike | 105 | 23.0 | 68 | 0 | wallstreetbets 105 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rheo4gp5jnl/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 89 | 24.14 | 43 | 1 | wallstreetbets 89 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhdz80szjy8/) |
| IBM | 2026-10-21 18:15 | mention spike | 104 | 2.43 | 72 | 1 | wallstreetbets 103, smallstreetbets 1 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 74 | 4.43 | 48 | 1 | wallstreetbets 74 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rheg478zoox/) |
| META | 2026-10-21 11:34 | mention spike | 371 | 34.14 | 201 | 1 | wallstreetbets 370, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 10.29 | 18 | 0 | wallstreetbets 27, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhbfa71rnb5/) |
| MSTR | 2026-10-21 19:47 | mention spike | 16 | 8.29 | 11 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| NOK | 2026-10-22 05:55 | mention spike | 13 | 3.86 | 9 | 0 | wallstreetbets 13 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhed379zxz8/) |
| RDDT | 2026-10-21 22:45 | mention spike | 26 | 10.43 | 19 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhbmkcv4jpd/) |
| SDEV | 2026-10-22 07:27 | mention spike | 13 | 0.29 | 7 | 0 | pennystocks 11, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1xc7pzo/) |
| TSLA | 2026-10-22 07:27 | mention spike | 227 | 86.0 | 141 | 1 | wallstreetbets 225, smallstreetbets 2 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxty0/) |
| OKLO | 2026-10-20 21:21 | mention spike | 6 | 7.57 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgue5p772g5/) |
| SPCX | 2026-10-20 10:18 | mention spike | 200 | 97.14 | 117 | 0 | wallstreetbets 197, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xccjwa/) |
| SMCI | 2026-10-20 21:06 | mention spike | 20 | 19.29 | 14 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhdwfhvcfd0/) |
| NFLX | 2026-10-19 19:31 | mention spike | 77 | 44.71 | 58 | 0 | wallstreetbets 75, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcbbl9/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.14 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhed6wfc3i8/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
