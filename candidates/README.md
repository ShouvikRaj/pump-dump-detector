# Stage 1 candidates

Updated 2026-10-28T16:36:06Z by run `40726499121`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BRAI | 2026-10-27 17:53 | mention spike | 12 | 1.0 | 7 | 0 | pennystocks 7, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| ENPH | 2026-10-28 16:10 | mention spike | 10 | 0.29 | 9 | 0 | wallstreetbets 10 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rse288cx9t0/) |
| HOOD | 2026-10-27 03:54 | mention spike | 234 | 11.57 | 141 | 0 | wallstreetbets 234 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsep8ilkkip/) |
| INOD | 2026-10-27 14:48 | mention spike | 15 | 2.29 | 8 | 0 | wallstreetbets 15 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| MSFT | 2026-10-27 00:09 | mention spike | 56 | 30.71 | 50 | 0 | wallstreetbets 56 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| SKHY | 2026-10-27 19:51 | mention spike | 110 | 9.57 | 63 | 0 | wallstreetbets 110 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rseu25f88v5/) |
| SLS | 2026-10-28 13:05 | mention spike | 54 | 4.14 | 34 | 0 | wallstreetbets 50, pennystocks 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhpxe6/) |
| STX | 2026-10-27 19:12 | mention spike | 86 | 4.14 | 57 | 0 | wallstreetbets 86 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsewxbu8nab/) |
| VRT | 2026-10-28 11:39 | mention spike | 17 | 1.0 | 16 | 1 | wallstreetbets 17 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| BBAI | 2026-10-27 20:57 | mention spike | 9 | 1.0 | 9 | 0 | wallstreetbets 5, pennystocks 3, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| USAR | 2026-10-27 17:13 | mention spike | 11 | 4.14 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs9hycfx78g/) |
| GLD | 2026-10-28 00:47 | mention spike | 11 | 6.71 | 7 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs8zspc74dh/) |
| SOFI | 2026-10-27 00:43 | mention spike | 32 | 9.29 | 19 | 0 | wallstreetbets 30, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| CLS | 2026-10-26 19:24 | mention spike | 1 | 8.29 | 1 | 0 | wallstreetbets 1 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 7 | 5.86 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsa551rxn1h/) |
| ASML | 2026-10-27 17:38 | mention spike | 4 | 3.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 73 | 55.71 | 45 | 0 | wallstreetbets 73 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhrwje/) |
| RDDT | 2026-10-26 14:04 | mention spike | 40 | 27.86 | 32 | 0 | wallstreetbets 40 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsc7pztlale/) |
| GOOG | 2026-10-27 00:43 | mention spike | 105 | 67.0 | 64 | 0 | wallstreetbets 105 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsf8l36h145/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
