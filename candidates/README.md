# Stage 1 candidates

Updated 2026-11-11T18:59:09Z by run `43081601010`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 111 | 34.0 | 87 | 0 | wallstreetbets 110, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtooay/) |
| AVGO | 2026-11-09 15:56 | mention spike | 37 | 16.14 | 26 | 0 | wallstreetbets 36, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shj8e1303j5/) |
| CRWV | 2026-11-10 20:00 | mention spike | 504 | 36.14 | 240 | 3 | wallstreetbets 502, smallstreetbets 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| GEV | 2026-11-10 15:44 | mention spike | 14 | 4.57 | 9 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| NBIS | 2026-11-11 12:32 | mention spike | 183 | 48.14 | 109 | 1 | wallstreetbets 182, smallstreetbets 1 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 957 | 484.0 | 514 | 5 | wallstreetbets 946, smallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtq4fi/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.86 | 11 | 0 | wallstreetbets 17 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSFT | 2026-11-11 15:26 | mention spike | 79 | 56.14 | 63 | 0 | wallstreetbets 78, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 8 | 5.57 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shk81gjcxr5/) |
| NVDL | 2026-11-11 07:39 | mention spike | 9 | 2.29 | 8 | 0 | wallstreetbets 9 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfroitlpes/) |
| TTD | 2026-11-09 21:11 | mention spike | 1 | 9.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sfzc1tc362o/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 42 | 40.29 | 31 | 0 | wallstreetbets 39, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 48 | 48.71 | 30 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shjs7e1u40w/) |
| OMH | 2026-11-09 20:48 | mention spike | 10 | 5.0 | 9 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 26 | 13.14 | 22 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnc9r/) |
| HIMS | 2026-11-09 21:25 | mention spike | 4 | 5.71 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shjuniemr4y/) |
| GLD | 2026-11-10 17:08 | mention spike | 8 | 7.57 | 5 | 0 | wallstreetbets 8 | NYSE Arca | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shj8phkhh40/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
