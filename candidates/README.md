# Stage 1 candidates

Updated 2026-10-10T15:26:10Z by run `38063165898`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-08 20:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| ADBE | 2026-10-08 04:07 | mention spike | 2 | 6.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x21cyd/) |
| ASTS | 2026-10-08 21:11 | mention spike | 50 | 41.43 | 35 | 0 | wallstreetbets 49, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1ve6y/comment/pf24y4s/) |
| IBM | 2026-10-09 01:09 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| SLS | 2026-10-09 13:19 | mention spike | 1 | 5.14 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x00v08/comment/pevva79/) |
| UNH | 2026-10-09 13:59 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| CMG | 2026-10-08 19:38 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HUM | 2026-10-09 12:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| UUUU | 2026-10-07 20:50 | mention spike | 0 |  | 0 | 0 |  | NYSE American |  |  |
| CIFR | 2026-10-08 21:37 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MCD | 2026-10-09 00:16 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| NBIS | 2026-10-08 18:05 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| ORCL | 2026-10-08 17:11 | mention spike | 1 | 8.14 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x241e4/comment/pf22c59/) |
| GME | 2026-10-08 16:17 | mention spike | 6 | 15.57 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1vheo/) |
| IREN | 2026-10-07 19:18 | mention spike | 1 | 9.0 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1p2wf/) |
| SKHY | 2026-10-06 18:54 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TSM | 2026-10-09 12:39 | mention spike | 2 | 6.0 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x1ve6y/comment/pf24ewk/) |
| OKLO | 2026-10-06 18:14 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
