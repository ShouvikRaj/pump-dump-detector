# Stage 1 candidates

Updated 2026-10-28T21:33:07Z by run `40771229546`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 1.43 | 6 | 0 | pennystocks 6, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| DJT | 2026-10-28 17:04 | mention spike | 10 | 2.43 | 10 | 0 | smallstreetbets 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsok8ay5ecl/) |
| FTNT | 2026-10-28 21:20 | mention spike | 11 | 0.29 | 11 | 0 | wallstreetbets 11 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhzsvt/) |
| GOOG | 2026-10-28 20:50 | mention spike | 251 | 69.57 | 159 | 2 | wallstreetbets 250, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhzmym/) |
| HOOD | 2026-10-27 03:54 | mention spike | 133 | 28.0 | 76 | 0 | wallstreetbets 130, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhxifo/) |
| LITE | 2026-10-28 21:20 | mention spike | 43 | 2.86 | 25 | 3 | wallstreetbets 43 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhytkz/comment/19rssa9i8ta4h/) |
| MRVL | 2026-10-28 21:20 | mention spike | 48 | 3.0 | 36 | 0 | wallstreetbets 48 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhytkz/comment/19rss882lixs4/) |
| MSFT | 2026-10-27 00:09 | mention spike | 120 | 32.57 | 98 | 1 | wallstreetbets 119, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| ORCL | 2026-10-28 18:38 | mention spike | 66 | 9.0 | 47 | 0 | wallstreetbets 66 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsojmvmr4kk/) |
| SKHY | 2026-10-27 19:51 | mention spike | 85 | 14.0 | 57 | 0 | wallstreetbets 85 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhu3mt/) |
| SLS | 2026-10-28 13:05 | mention spike | 58 | 4.14 | 40 | 0 | wallstreetbets 52, pennystocks 6 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhv9n1/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 4.14 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmp62o2ztv/) |
| VRT | 2026-10-28 11:39 | mention spike | 20 | 1.0 | 17 | 1 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| GLD | 2026-10-28 00:47 | mention spike | 15 | 6.71 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhytkz/comment/19rsrn78dth1g/) |
| STX | 2026-10-27 19:12 | mention spike | 31 | 11.86 | 23 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmdvb4u19e/) |
| ENPH | 2026-10-28 16:10 | mention spike | 9 | 0.57 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xi0u54/) |
| INOD | 2026-10-27 14:48 | mention spike | 8 | 3.29 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsf1d63tz35/) |
| BBAI | 2026-10-27 20:57 | mention spike | 1 | 2.14 | 1 | 0 | smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| SOFI | 2026-10-27 00:43 | mention spike | 24 | 11.0 | 15 | 0 | wallstreetbets 22, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
