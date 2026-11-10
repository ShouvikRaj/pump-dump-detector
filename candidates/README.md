# Stage 1 candidates

Updated 2026-11-10T18:21:09Z by run `42873759186`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 80 | 23.71 | 55 | 0 | wallstreetbets 80 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnad5/) |
| ASTS | 2026-11-09 22:33 | mention spike | 85 | 41.86 | 57 | 0 | wallstreetbets 85 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfpywcms5j8/) |
| AVGO | 2026-11-09 15:56 | mention spike | 29 | 13.71 | 24 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfq1x52twqs/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 3.0 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfjsbn95lhe/) |
| HIMS | 2026-11-09 21:25 | mention spike | 22 | 2.43 | 20 | 0 | wallstreetbets 22 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsotex/) |
| IVF | 2026-11-09 22:18 | mention spike | 13 | 1.14 | 13 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| OMH | 2026-11-09 20:48 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 11, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfpns8tsdms/) |
| RKLB | 2026-11-09 21:25 | mention spike | 142 | 22.14 | 82 | 2 | wallstreetbets 142 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprrz/) |
| TTD | 2026-11-09 21:11 | mention spike | 44 | 3.0 | 33 | 0 | wallstreetbets 44 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfhb2nwpr0i/) |
| TTWO | 2026-11-10 16:24 | mention spike | 28 | 9.57 | 20 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfq2qen9535/) |
| GLD | 2026-11-10 17:08 | mention spike | 12 | 6.29 | 7 | 0 | wallstreetbets 12 | NYSE Arca | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfn0isndedf/) |
| CVS | 2026-11-09 13:52 | mention spike | 6 | 3.0 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1065 | 338.57 | 611 | 0 | wallstreetbets 1057, smallstreetbets 8 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xstvcd/) |
| NYT | 2026-11-09 11:01 | mention spike | 6 | 3.14 | 6 | 0 | wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 10 | 6.14 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 3 | 3.43 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfnymt8khdt/) |
| ONDS | 2026-11-09 20:48 | mention spike | 4 | 4.43 | 4 | 0 | wallstreetbets 3, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfk1wtvrqbp/) |
| MSS | 2026-11-09 23:23 | mention spike | 5 | 1.0 | 3 | 0 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xssm2r/comment/19sfoxgwa4j34/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
