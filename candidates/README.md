# Stage 1 candidates

Updated 2026-11-11T17:53:10Z by run `43071044422`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 112 | 32.71 | 87 | 0 | wallstreetbets 112 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtkxyp/) |
| AVGO | 2026-11-09 15:56 | mention spike | 38 | 15.86 | 27 | 0 | wallstreetbets 37, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shha2sm5q03/) |
| CRWV | 2026-11-10 20:00 | mention spike | 503 | 33.71 | 235 | 3 | wallstreetbets 501, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| NBIS | 2026-11-11 12:32 | mention spike | 172 | 47.43 | 100 | 0 | wallstreetbets 171, smallstreetbets 1 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1022 | 470.86 | 541 | 5 | wallstreetbets 1011, smallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xto0pz/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.86 | 11 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSFT | 2026-11-11 15:26 | mention spike | 82 | 55.0 | 64 | 0 | wallstreetbets 82 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtgne3/) |
| MSTR | 2026-11-10 19:20 | mention spike | 8 | 5.43 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfla470vz7/) |
| NVDL | 2026-11-11 07:39 | mention spike | 9 | 2.29 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfroitlpes/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 4.57 | 8 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shby819v55v/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 48 | 39.43 | 33 | 0 | wallstreetbets 45, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 53 | 47.57 | 37 | 1 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shflumj0fdu/) |
| OMH | 2026-11-09 20:48 | mention spike | 9 | 5.0 | 8 | 0 | wallstreetbets 5, pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 26 | 12.86 | 22 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnc9r/) |
| HIMS | 2026-11-09 21:25 | mention spike | 5 | 5.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.86 | 3 | 0 | wallstreetbets 11 | NYSE Arca | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shgrrm6sbtt/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
