# Stage 1 candidates

Updated 2026-10-08T13:51:58Z by run `37787618182`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ADBE | 2026-10-08 04:07 | mention spike | 14 | 2.71 | 14 | 1 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0b2e8/) |
| APLD | 2026-10-05 14:23 | mention spike | 225 | 21.86 | 113 | 0 | wallstreetbets 225 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x08cxw/) |
| IREN | 2026-10-07 19:18 | mention spike | 16 | 4.86 | 16 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemnpno/) |
| KEEL | 2026-10-08 03:01 | mention spike | 11 | 1.86 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemtz7e/) |
| LEVI | 2026-10-07 20:37 | mention spike | 15 | 0.86 | 11 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemjuxb/) |
| META | 2026-10-08 13:39 | mention spike | 48 | 19.57 | 34 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemzdmf/) |
| PLTR | 2026-10-08 13:12 | mention spike | 31 | 9.86 | 28 | 0 | wallstreetbets 31 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0chhl/) |
| SMCI | 2026-10-07 20:50 | mention spike | 11 | 3.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pek0slz/) |
| TTWO | 2026-10-08 13:27 | mention spike | 13 | 3.57 | 6 | 1 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzzgqj/) |
| HTZ | 2026-10-06 16:43 | mention spike | 100 | 21.0 | 63 | 0 | wallstreetbets 90, pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0ijc4/) |
| UUUU | 2026-10-07 20:50 | mention spike | 9 | 2.29 | 5 | 0 | wallstreetbets 9 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pei8ltz/) |
| BULL | 2026-10-07 12:08 | mention spike | 13 | 9.57 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemda3h/) |
| GLD | 2026-10-07 13:01 | mention spike | 7 | 4.86 | 7 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pem5tfj/) |
| BIYA | 2026-10-07 16:38 | mention spike | 4 | 1.0 | 4 | 0 | wallstreetbets 2, pennystocks 1, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0a0in/) |
| CRWD | 2026-10-06 23:59 | mention spike | 8 | 5.14 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x01lii/) |
| LLY | 2026-10-07 17:44 | mention spike | 10 | 1.71 | 4 | 0 | wallstreetbets 10 | NYSE | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pem2x4w/) |
| IWM | 2026-10-06 00:59 | mention spike | 18 | 9.14 | 10 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemz5jw/) |
| SOXL | 2026-10-07 12:34 | mention spike | 15 | 16.71 | 11 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemszxo/) |
| PENG | 2026-10-06 18:01 | mention spike | 7 | 6.71 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x06jh0/comment/pekbr5a/) |
| CIRC | 2026-10-06 17:21 | mention spike | 5 | 2.71 | 3 | 0 | wallstreetbets 3, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzskww/comment/pefyj58/) |
| AMD | 2026-10-06 14:55 | mention spike | 52 | 48.71 | 47 | 0 | wallstreetbets 51, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzimpi/comment/pemnqcb/) |
| SKHY | 2026-10-06 18:54 | mention spike | 12 | 5.86 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemzcws/) |
| OKLO | 2026-10-06 18:14 | mention spike | 7 | 5.86 | 4 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wzyokb/) |
| NOK | 2026-10-06 15:49 | mention spike | 2 | 3.43 | 1 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemus3f/) |
| VOO | 2026-10-06 16:15 | mention spike | 11 | 11.71 | 11 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0de7b/comment/pelkm2s/) |
| SOXS | 2026-10-07 12:08 | mention spike | 12 | 5.29 | 5 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x0myiq/comment/pemxzhx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
