# Stage 1 candidates

Updated 2026-11-11T20:20:09Z by run `43093986155`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 107 | 34.86 | 86 | 0 | wallstreetbets 106, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtqzun/) |
| CRWV | 2026-11-10 20:00 | mention spike | 490 | 40.86 | 235 | 3 | wallstreetbets 488, smallstreetbets 2 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| NBIS | 2026-11-11 12:32 | mention spike | 203 | 48.57 | 122 | 1 | wallstreetbets 201, smallstreetbets 2 | Nasdaq | #15 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtqx9q/) |
| RGTI | 2026-11-10 21:21 | mention spike | 16 | 3.0 | 10 | 0 | wallstreetbets 16 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 850 | 505.57 | 478 | 3 | wallstreetbets 840, smallstreetbets 10 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtq4fi/) |
| AVGO | 2026-11-09 15:56 | mention spike | 35 | 16.57 | 24 | 0 | wallstreetbets 34, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shmhua4pvq8/) |
| NVDL | 2026-11-11 07:39 | mention spike | 9 | 2.43 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shlgzz8unz8/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 4.71 | 8 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 75 | 57.0 | 60 | 0 | wallstreetbets 74, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 7 | 5.71 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shk81gjcxr5/) |
| TTD | 2026-11-09 21:11 | mention spike | 1 | 9.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sfzc1tc362o/) |
| IVF | 2026-11-09 22:18 | mention spike | 1 | 3.0 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shl5u61uq5e/) |
| RKLB | 2026-11-09 21:25 | mention spike | 37 | 40.71 | 29 | 0 | wallstreetbets 34, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 41 | 49.14 | 26 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shjs7e1u40w/) |
| OMH | 2026-11-09 20:48 | mention spike | 10 | 5.0 | 9 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 24 | 13.43 | 20 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnc9r/) |
| HIMS | 2026-11-09 21:25 | mention spike | 5 | 5.86 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shnm2gz7ug4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
