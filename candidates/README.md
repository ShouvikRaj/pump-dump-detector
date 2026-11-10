# Stage 1 candidates

Updated 2026-11-10T17:48:07Z by run `42866950493`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 77 | 24.0 | 53 | 0 | wallstreetbets 77 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnad5/) |
| ASTS | 2026-11-09 22:33 | mention spike | 85 | 41.71 | 56 | 0 | wallstreetbets 85 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfp9dq8bojk/) |
| AVGO | 2026-11-09 15:56 | mention spike | 27 | 13.71 | 22 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprrz/comment/19sfp3nta67kz/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 3.0 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfjsbn95lhe/) |
| HIMS | 2026-11-09 21:25 | mention spike | 22 | 2.29 | 20 | 0 | wallstreetbets 22 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsotex/) |
| IVF | 2026-11-09 22:18 | mention spike | 15 | 0.86 | 15 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| OMH | 2026-11-09 20:48 | mention spike | 20 | 2.0 | 13 | 0 | wallstreetbets 11, pennystocks 9 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xse80g/comment/19sfououxilr7/) |
| RKLB | 2026-11-09 21:25 | mention spike | 142 | 22.29 | 80 | 2 | wallstreetbets 142 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprrz/) |
| TTD | 2026-11-09 21:11 | mention spike | 45 | 2.86 | 33 | 0 | wallstreetbets 45 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfhb2nwpr0i/) |
| TTWO | 2026-11-10 16:24 | mention spike | 27 | 9.57 | 19 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfn48dp4xs0/) |
| GLD | 2026-11-10 17:08 | mention spike | 14 | 6.14 | 9 | 0 | wallstreetbets 14 | NYSE Arca | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfn0isndedf/) |
| CVS | 2026-11-09 13:52 | mention spike | 6 | 3.0 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1034 | 333.14 | 596 | 0 | wallstreetbets 1025, smallstreetbets 9 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xssmwj/) |
| NYT | 2026-11-09 11:01 | mention spike | 6 | 3.14 | 6 | 0 | wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 9 | 6.14 | 7 | 0 | wallstreetbets 8, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 3 | 3.43 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfnymt8khdt/) |
| ONDS | 2026-11-09 20:48 | mention spike | 4 | 4.43 | 4 | 0 | wallstreetbets 3, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfk1wtvrqbp/) |
| MSS | 2026-11-09 23:23 | mention spike | 6 | 0.86 | 4 | 0 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xssm2r/comment/19sfoxgwa4j34/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
