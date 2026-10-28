# Stage 1 candidates

Updated 2026-10-28T13:25:09Z by run `40696074352`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 12 | 0.57 | 9 | 0 | pennystocks 6, wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 0.57 | 5 | 0 | pennystocks 7, smallstreetbets 2, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhnxu5/) |
| GLD | 2026-10-28 00:47 | mention spike | 19 | 5.86 | 8 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs5ua46x90h/) |
| HOOD | 2026-10-27 03:54 | mention spike | 228 | 9.57 | 141 | 0 | wallstreetbets 228 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs65wqs29r5/) |
| INOD | 2026-10-27 14:48 | mention spike | 18 | 1.14 | 9 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| SKHY | 2026-10-27 19:51 | mention spike | 96 | 9.43 | 56 | 0 | wallstreetbets 96 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs3padq0t7p/) |
| SLS | 2026-10-28 13:05 | mention spike | 18 | 4.43 | 14 | 0 | wallstreetbets 15, pennystocks 3 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhnpwf/) |
| SOFI | 2026-10-27 00:43 | mention spike | 39 | 7.86 | 26 | 0 | wallstreetbets 37, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| STX | 2026-10-27 19:12 | mention spike | 81 | 3.86 | 58 | 0 | wallstreetbets 81 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs68mc9zox0/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 3.57 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs383g09ejl/) |
| VRT | 2026-10-28 11:39 | mention spike | 13 | 1.0 | 13 | 1 | wallstreetbets 13 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| MSFT | 2026-10-27 00:09 | mention spike | 49 | 30.0 | 45 | 0 | wallstreetbets 49 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| CLS | 2026-10-26 19:24 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 5 | 5.86 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrhp24dgsyr/) |
| ASML | 2026-10-27 17:38 | mention spike | 6 | 2.86 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 4 | 3.0 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 76 | 55.14 | 44 | 0 | wallstreetbets 76 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdxs0/) |
| RDDT | 2026-10-26 14:04 | mention spike | 43 | 26.29 | 30 | 0 | wallstreetbets 43 | NYSE | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| GOOG | 2026-10-27 00:43 | mention spike | 114 | 62.86 | 65 | 0 | wallstreetbets 114 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs6dq648a8x/) |
| ANT | 2026-10-26 13:24 | mention spike | 8 | 4.71 | 8 | 0 | wallstreetbets 8 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
