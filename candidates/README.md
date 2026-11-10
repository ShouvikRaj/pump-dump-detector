# Stage 1 candidates

Updated 2026-11-10T16:37:10Z by run `42855348342`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 66 | 24.14 | 48 | 0 | wallstreetbets 66 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnad5/) |
| ASTS | 2026-11-09 22:33 | mention spike | 83 | 41.14 | 52 | 0 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfm5ue3s7pc/) |
| HIMS | 2026-11-09 21:25 | mention spike | 24 | 2.0 | 21 | 0 | wallstreetbets 24 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsotex/) |
| IVF | 2026-11-09 22:18 | mention spike | 15 | 0.86 | 15 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| OMH | 2026-11-09 20:48 | mention spike | 21 | 1.57 | 15 | 0 | wallstreetbets 12, pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xse80g/comment/19sfm3yshyppd/) |
| RKLB | 2026-11-09 21:25 | mention spike | 142 | 21.86 | 79 | 2 | wallstreetbets 142 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprrz/) |
| TTD | 2026-11-09 21:11 | mention spike | 47 | 2.57 | 34 | 0 | wallstreetbets 47 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfhb2nwpr0i/) |
| TTWO | 2026-11-10 16:24 | mention spike | 27 | 9.43 | 20 | 0 | wallstreetbets 27 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrwh6s/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 3.0 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfjsbn95lhe/) |
| AVGO | 2026-11-09 15:56 | mention spike | 25 | 13.57 | 20 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsjfsh/comment/19sfm2ed91iyr/) |
| CVS | 2026-11-09 13:52 | mention spike | 6 | 3.0 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 922 | 322.14 | 550 | 0 | wallstreetbets 912, smallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsoxsr/) |
| NYT | 2026-11-09 11:01 | mention spike | 7 | 3.0 | 7 | 0 | wallstreetbets 6, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 8 | 6.29 | 6 | 0 | wallstreetbets 7, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 2 | 3.43 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfkj3n9ghdv/) |
| ONDS | 2026-11-09 20:48 | mention spike | 4 | 4.43 | 4 | 0 | wallstreetbets 3, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfk1wtvrqbp/) |
| MSS | 2026-11-09 23:23 | mention spike | 5 | 0.86 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19selz71ip5r4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
