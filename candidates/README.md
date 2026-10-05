# Stage 1 candidates

Updated 2026-10-05T18:59:55Z by run `37360078901`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 31 | 11.14 | 20 | 0 | wallstreetbets 30, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxycup/) |
| DELL | 2026-10-05 16:38 | mention spike | 14 | 5.43 | 7 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| DRTS | 2026-10-04 23:23 | mention spike | 19 | 1.86 | 17 | 1 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxl6cr/comment/pe28r62/) |
| GME | 2026-10-05 16:24 | mention spike | 24 | 4.71 | 21 | 0 | wallstreetbets 23, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyb83x/) |
| PMI | 2026-10-05 13:55 | mention spike | 15 | 1.43 | 10 | 0 | wallstreetbets 13, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1hx05/) |
| SDEV | 2026-10-05 14:09 | mention spike | 19 | 5.29 | 14 | 0 | wallstreetbets 11, pennystocks 8 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2fqec/) |
| SPCX | 2026-10-05 14:51 | mention spike | 116 | 29.14 | 70 | 1 | wallstreetbets 116 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wybz2w/) |
| TSM | 2026-10-05 15:18 | mention spike | 13 | 4.29 | 11 | 0 | wallstreetbets 13 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2ihoq/) |
| VEEA | 2026-10-05 15:33 | mention spike | 21 | 3.43 | 12 | 0 | pennystocks 20, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 6.0 | 24 | 0 | wallstreetbets 47 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe0sxll/) |
| IREN | 2026-10-05 17:49 | mention spike | 10 | 4.43 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe21hda/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
