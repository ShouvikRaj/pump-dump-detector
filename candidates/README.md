# Stage 1 candidates

Updated 2026-10-28T15:17:10Z by run `40713178185`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 10 | 0.86 | 9 | 0 | wallstreetbets 5, pennystocks 4, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 1.0 | 7 | 0 | pennystocks 7, wallstreetbets 3, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| GLD | 2026-10-28 00:47 | mention spike | 16 | 6.14 | 8 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs8zspc74dh/) |
| HOOD | 2026-10-27 03:54 | mention spike | 233 | 11.29 | 143 | 0 | wallstreetbets 233 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsblg5u85wk/) |
| INOD | 2026-10-27 14:48 | mention spike | 14 | 1.71 | 7 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| SKHY | 2026-10-27 19:51 | mention spike | 106 | 9.57 | 61 | 0 | wallstreetbets 106 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsb9o95kbtt/) |
| SLS | 2026-10-28 13:05 | mention spike | 52 | 4.29 | 32 | 0 | wallstreetbets 48, pennystocks 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhpxe6/) |
| SOFI | 2026-10-27 00:43 | mention spike | 39 | 8.71 | 25 | 0 | wallstreetbets 37, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| STX | 2026-10-27 19:12 | mention spike | 84 | 4.0 | 58 | 0 | wallstreetbets 84 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsbh453alep/) |
| USAR | 2026-10-27 17:13 | mention spike | 15 | 3.57 | 8 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs9hycfx78g/) |
| VRT | 2026-10-28 11:39 | mention spike | 17 | 1.0 | 16 | 1 | wallstreetbets 17 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| MSFT | 2026-10-27 00:09 | mention spike | 53 | 30.43 | 46 | 0 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| CLS | 2026-10-26 19:24 | mention spike | 2 | 8.14 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 7 | 5.86 | 6 | 0 | wallstreetbets 7 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsa551rxn1h/) |
| ASML | 2026-10-27 17:38 | mention spike | 4 | 3.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 68 | 55.71 | 42 | 0 | wallstreetbets 68 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdxs0/) |
| RDDT | 2026-10-26 14:04 | mention spike | 41 | 27.57 | 30 | 0 | wallstreetbets 41 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rs8l3gyoa91/) |
| GOOG | 2026-10-27 00:43 | mention spike | 104 | 66.29 | 62 | 0 | wallstreetbets 104 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsblupnomap/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
