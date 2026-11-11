# Stage 1 candidates

Updated 2026-11-11T17:28:10Z by run `43066752258`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 111 | 32.43 | 84 | 0 | wallstreetbets 111 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtkxyp/) |
| AVGO | 2026-11-09 15:56 | mention spike | 36 | 15.71 | 27 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shglplg30f7/) |
| CRWV | 2026-11-10 20:00 | mention spike | 497 | 33.57 | 231 | 3 | wallstreetbets 496, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| MSFT | 2026-11-11 15:26 | mention spike | 109 | 50.86 | 86 | 0 | wallstreetbets 109 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtgne3/) |
| NBIS | 2026-11-11 12:32 | mention spike | 165 | 47.43 | 95 | 0 | wallstreetbets 165 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1061 | 464.43 | 566 | 5 | wallstreetbets 1049, smallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtmw3c/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.86 | 11 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSTR | 2026-11-10 19:20 | mention spike | 8 | 5.43 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfla470vz7/) |
| NVDL | 2026-11-11 07:39 | mention spike | 9 | 2.29 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfroitlpes/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 4.57 | 8 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shby819v55v/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 51 | 39.0 | 36 | 0 | wallstreetbets 48, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 56 | 47.14 | 38 | 1 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shflumj0fdu/) |
| OMH | 2026-11-09 20:48 | mention spike | 11 | 4.71 | 9 | 0 | wallstreetbets 6, pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 26 | 12.86 | 22 | 0 | wallstreetbets 26 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnc9r/) |
| HIMS | 2026-11-09 21:25 | mention spike | 5 | 5.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 10 | 6.86 | 2 | 0 | wallstreetbets 10 | NYSE Arca | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shezgnsfzdx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
