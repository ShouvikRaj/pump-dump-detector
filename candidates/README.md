# Stage 1 candidates

Updated 2026-10-28T14:25:09Z by run `40704399888`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 11 | 0.71 | 9 | 0 | pennystocks 5, wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 10 | 0.71 | 5 | 0 | pennystocks 7, wallstreetbets 2, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhnxu5/) |
| GLD | 2026-10-28 00:47 | mention spike | 18 | 6.0 | 8 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs8zspc74dh/) |
| HOOD | 2026-10-27 03:54 | mention spike | 242 | 9.43 | 148 | 0 | wallstreetbets 242 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs99txr2qjk/) |
| INOD | 2026-10-27 14:48 | mention spike | 18 | 1.14 | 9 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| SKHY | 2026-10-27 19:51 | mention spike | 105 | 9.43 | 59 | 0 | wallstreetbets 105 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs9aim9gich/) |
| SLS | 2026-10-28 13:05 | mention spike | 44 | 4.29 | 26 | 0 | wallstreetbets 40, pennystocks 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhnpwf/) |
| SOFI | 2026-10-27 00:43 | mention spike | 42 | 8.29 | 28 | 0 | wallstreetbets 40, smallstreetbets 2 | Nasdaq | #14 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| STX | 2026-10-27 19:12 | mention spike | 83 | 3.71 | 58 | 0 | wallstreetbets 83 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs7ye3sa5eq/) |
| USAR | 2026-10-27 17:13 | mention spike | 14 | 3.57 | 7 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs828oxz4df/) |
| VRT | 2026-10-28 11:39 | mention spike | 16 | 1.0 | 15 | 1 | wallstreetbets 16 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| MSFT | 2026-10-27 00:09 | mention spike | 52 | 30.14 | 47 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| CLS | 2026-10-26 19:24 | mention spike | 2 | 8.14 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 6 | 5.86 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs7o3fkyrxd/) |
| ASML | 2026-10-27 17:38 | mention spike | 4 | 3.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 3 | 3.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 72 | 56.0 | 44 | 0 | wallstreetbets 72 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdxs0/) |
| RDDT | 2026-10-26 14:04 | mention spike | 46 | 26.86 | 33 | 0 | wallstreetbets 46 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| GOOG | 2026-10-27 00:43 | mention spike | 106 | 65.29 | 62 | 0 | wallstreetbets 106 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs8xcn9t4o3/) |
| ANT | 2026-10-26 13:24 | mention spike | 7 | 4.86 | 7 | 0 | wallstreetbets 7 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs2tqeomqxs/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
