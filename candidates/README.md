# Stage 1 candidates

Updated 2026-11-10T14:52:08Z by run `42837212175`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASTS | 2026-11-09 22:33 | mention spike | 88 | 39.57 | 55 | 0 | wallstreetbets 88 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfgswmhbmrn/) |
| HIMS | 2026-11-09 21:25 | mention spike | 22 | 1.71 | 18 | 0 | wallstreetbets 22 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sffzrh2vksh/) |
| IVF | 2026-11-09 22:18 | mention spike | 15 | 0.86 | 15 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| OMH | 2026-11-09 20:48 | mention spike | 16 | 1.57 | 12 | 0 | wallstreetbets 11, pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xse80g/comment/19sfb5rm713mt/) |
| RKLB | 2026-11-09 21:25 | mention spike | 143 | 20.86 | 79 | 2 | wallstreetbets 143 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsdy48/) |
| TTD | 2026-11-09 21:11 | mention spike | 47 | 2.57 | 34 | 0 | wallstreetbets 47 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfhb2nwpr0i/) |
| ANT | 2026-11-10 14:52 | mention spike | 52 | 24.29 | 37 | 0 | wallstreetbets 52 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnad5/) |
| CVS | 2026-11-09 13:52 | mention spike | 9 | 2.57 | 8 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 802 | 298.71 | 499 | 0 | wallstreetbets 791, smallstreetbets 11 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnhxl/) |
| NYT | 2026-11-09 11:01 | mention spike | 9 | 2.57 | 9 | 0 | wallstreetbets 8, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsik05/comment/19sfag03fc5a9/) |
| NNN | 2026-11-09 15:04 | mention spike | 10 | 6.0 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 1 | 3.43 | 1 | 0 | smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ONDS | 2026-11-09 20:48 | mention spike | 6 | 4.14 | 5 | 0 | wallstreetbets 5, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sejep6ua8gy/) |
| MSS | 2026-11-09 23:23 | mention spike | 5 | 0.86 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19selz71ip5r4/) |
| AVGO | 2026-11-09 15:56 | mention spike | 16 | 13.43 | 11 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsjfsh/comment/19sfbtphxs30i/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
