# Stage 1 candidates

Updated 2026-10-28T12:11:08Z by run `40684881409`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 14 | 0.29 | 10 | 0 | pennystocks 8, wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 0.43 | 5 | 0 | pennystocks 8, wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xgyubd/) |
| GLD | 2026-10-28 00:47 | mention spike | 17 | 5.86 | 6 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rru96sh15lw/) |
| HOOD | 2026-10-27 03:54 | mention spike | 218 | 9.43 | 137 | 0 | wallstreetbets 218 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs2sc3ki3fl/) |
| INOD | 2026-10-27 14:48 | mention spike | 25 | 0.14 | 10 | 0 | wallstreetbets 25 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| SKHY | 2026-10-27 19:51 | mention spike | 96 | 9.14 | 56 | 0 | wallstreetbets 96 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs3bsid1asi/) |
| SOFI | 2026-10-27 00:43 | mention spike | 50 | 6.14 | 33 | 0 | wallstreetbets 48, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| STX | 2026-10-27 19:12 | mention spike | 80 | 3.86 | 57 | 0 | wallstreetbets 80 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs1ahxs9kv7/) |
| USAR | 2026-10-27 17:13 | mention spike | 13 | 3.43 | 6 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs383g09ejl/) |
| VRT | 2026-10-28 11:39 | mention spike | 12 | 1.0 | 12 | 1 | wallstreetbets 12 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| MSFT | 2026-10-27 00:09 | mention spike | 51 | 29.43 | 48 | 0 | wallstreetbets 51 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| CLS | 2026-10-26 19:24 | mention spike | 6 | 7.57 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 5 | 6.0 | 4 | 0 | wallstreetbets 5 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrhp24dgsyr/) |
| ASML | 2026-10-27 17:38 | mention spike | 6 | 2.86 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 4 | 3.0 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 79 | 54.29 | 47 | 0 | wallstreetbets 79 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdxs0/) |
| RDDT | 2026-10-26 14:04 | mention spike | 46 | 25.57 | 31 | 0 | wallstreetbets 46 | NYSE | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| GOOG | 2026-10-27 00:43 | mention spike | 117 | 61.86 | 64 | 0 | wallstreetbets 117 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs1p0tzbnc1/) |
| ANT | 2026-10-26 13:24 | mention spike | 10 | 4.43 | 10 | 0 | wallstreetbets 10 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 3 | 1.86 | 2 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrgvsj5imjo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
