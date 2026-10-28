# Stage 1 candidates

Updated 2026-10-28T21:46:10Z by run `40773060740`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 1.43 | 6 | 0 | pennystocks 6, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| FTNT | 2026-10-28 21:20 | mention spike | 15 | 0.29 | 14 | 0 | wallstreetbets 15 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhzsvt/) |
| GOOG | 2026-10-28 20:50 | mention spike | 290 | 70.0 | 175 | 2 | wallstreetbets 289, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhzmym/) |
| LITE | 2026-10-28 21:20 | mention spike | 46 | 2.86 | 28 | 3 | wallstreetbets 46 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhytkz/comment/19rssorlwa4cg/) |
| MRVL | 2026-10-28 21:20 | mention spike | 49 | 2.86 | 37 | 0 | wallstreetbets 49 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhyzc9/comment/19rssbwn0rtus/) |
| MSFT | 2026-10-27 00:09 | mention spike | 130 | 32.43 | 106 | 1 | wallstreetbets 129, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| ORCL | 2026-10-28 18:38 | mention spike | 68 | 9.0 | 49 | 0 | wallstreetbets 68 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhytkz/comment/19rssudl8gebk/) |
| SKHY | 2026-10-27 19:51 | mention spike | 85 | 14.0 | 57 | 0 | wallstreetbets 85 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhu3mt/) |
| SLS | 2026-10-28 13:05 | mention spike | 58 | 4.0 | 40 | 0 | wallstreetbets 52, pennystocks 6 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhv9n1/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 4.14 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmp62o2ztv/) |
| VRT | 2026-10-28 11:39 | mention spike | 19 | 1.14 | 16 | 1 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| GOOGL | 2026-10-28 21:46 | mention spike | 131 | 55.43 | 87 | 0 | wallstreetbets 131 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xi0ugl/) |
| DJT | 2026-10-28 17:04 | mention spike | 9 | 2.57 | 9 | 0 | wallstreetbets 5, smallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsok8ay5ecl/) |
| HOOD | 2026-10-27 03:54 | mention spike | 124 | 29.29 | 71 | 0 | wallstreetbets 121, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhxifo/) |
| GLD | 2026-10-28 00:47 | mention spike | 15 | 6.71 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhytkz/comment/19rsrn78dth1g/) |
| STX | 2026-10-27 19:12 | mention spike | 31 | 11.86 | 23 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmdvb4u19e/) |
| ENPH | 2026-10-28 16:10 | mention spike | 9 | 0.57 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xi0u54/) |
| INOD | 2026-10-27 14:48 | mention spike | 8 | 3.29 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsf1d63tz35/) |
| BBAI | 2026-10-27 20:57 | mention spike | 1 | 2.14 | 1 | 0 | smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| SOFI | 2026-10-27 00:43 | mention spike | 22 | 11.29 | 13 | 0 | wallstreetbets 20, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
