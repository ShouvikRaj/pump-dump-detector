# Stage 1 candidates

Updated 2026-11-11T19:40:07Z by run `43087839900`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 110 | 34.71 | 88 | 0 | wallstreetbets 109, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtqzun/) |
| AVGO | 2026-11-09 15:56 | mention spike | 36 | 16.43 | 25 | 0 | wallstreetbets 35, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shmhua4pvq8/) |
| CRWV | 2026-11-10 20:00 | mention spike | 498 | 38.43 | 237 | 3 | wallstreetbets 496, smallstreetbets 2 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| NBIS | 2026-11-11 12:32 | mention spike | 189 | 48.43 | 113 | 1 | wallstreetbets 187, smallstreetbets 2 | Nasdaq | #24 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtqx9q/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 925 | 491.29 | 501 | 5 | wallstreetbets 915, smallstreetbets 10 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtq4fi/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.86 | 11 | 0 | wallstreetbets 17 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDL | 2026-11-11 07:39 | mention spike | 9 | 2.43 | 7 | 0 | wallstreetbets 9 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shlgzz8unz8/) |
| GEV | 2026-11-10 15:44 | mention spike | 14 | 4.57 | 9 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 76 | 56.86 | 61 | 0 | wallstreetbets 75, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 7 | 5.71 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shk81gjcxr5/) |
| TTD | 2026-11-09 21:11 | mention spike | 1 | 9.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sfzc1tc362o/) |
| IVF | 2026-11-09 22:18 | mention spike | 1 | 3.0 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shl5u61uq5e/) |
| RKLB | 2026-11-09 21:25 | mention spike | 41 | 40.14 | 31 | 0 | wallstreetbets 38, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 43 | 49.14 | 27 | 0 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shjs7e1u40w/) |
| OMH | 2026-11-09 20:48 | mention spike | 10 | 5.0 | 9 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 25 | 13.29 | 21 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnc9r/) |
| HIMS | 2026-11-09 21:25 | mention spike | 5 | 5.71 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shm33iaovs3/) |
| GLD | 2026-11-10 17:08 | mention spike | 9 | 7.57 | 6 | 0 | wallstreetbets 9 | NYSE Arca | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shlb2cnpwpx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
