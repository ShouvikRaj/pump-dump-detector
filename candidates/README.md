# Stage 1 candidates

Updated 2026-10-05T17:49:34Z by run `37351140284`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 30 | 11.0 | 19 | 0 | wallstreetbets 29, smallstreetbets 1 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxycup/) |
| DELL | 2026-10-05 16:38 | mention spike | 13 | 5.43 | 6 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe133ei/) |
| DRTS | 2026-10-04 23:23 | mention spike | 21 | 1.43 | 19 | 1 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxl6cr/comment/pe0tjgc/) |
| GME | 2026-10-05 16:24 | mention spike | 24 | 4.71 | 21 | 0 | wallstreetbets 23, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyb83x/) |
| PMI | 2026-10-05 13:55 | mention spike | 15 | 1.43 | 10 | 0 | wallstreetbets 13, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1hx05/) |
| SDEV | 2026-10-05 14:09 | mention spike | 17 | 5.29 | 13 | 0 | wallstreetbets 9, pennystocks 8 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1f3he/) |
| SPCX | 2026-10-05 14:51 | mention spike | 105 | 29.29 | 65 | 1 | wallstreetbets 105 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wybz2w/) |
| TSM | 2026-10-05 15:18 | mention spike | 11 | 4.29 | 9 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1t8je/) |
| VEEA | 2026-10-05 15:33 | mention spike | 14 | 3.43 | 9 | 0 | pennystocks 13, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 6.0 | 24 | 0 | wallstreetbets 47 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe0sxll/) |
| IREN | 2026-10-05 17:49 | mention spike | 10 | 4.43 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe21hda/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
