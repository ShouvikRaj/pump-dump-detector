# Stage 1 candidates

Updated 2026-10-05T15:46:55Z by run `37335504730`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 28 | 11.0 | 18 | 0 | wallstreetbets 27, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxycup/) |
| DRTS | 2026-10-04 23:23 | mention spike | 24 | 1.0 | 20 | 1 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxl6cr/) |
| PMI | 2026-10-05 13:55 | mention spike | 13 | 1.43 | 9 | 0 | wallstreetbets 11, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe0yksq/) |
| SDEV | 2026-10-05 14:09 | mention spike | 16 | 5.29 | 13 | 0 | pennystocks 8, wallstreetbets 8 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe0mk4i/) |
| SPCX | 2026-10-05 14:51 | mention spike | 68 | 29.14 | 46 | 1 | wallstreetbets 68 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxl6cr/) |
| TSM | 2026-10-05 15:18 | mention spike | 10 | 4.14 | 7 | 0 | wallstreetbets 10 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe12awq/) |
| VEEA | 2026-10-05 15:33 | mention spike | 15 | 3.29 | 9 | 0 | pennystocks 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 6.0 | 24 | 0 | wallstreetbets 47 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe0sxll/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
