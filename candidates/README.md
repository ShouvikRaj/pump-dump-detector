# Stage 1 candidates

Updated 2026-11-25T03:29:08Z by run `45539694359`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BENF | 2026-11-25 00:43 | mention spike | 11 | 0.0 | 6 | 0 | pennystocks 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y4edv2/) |
| DELL | 2026-11-24 21:15 | mention spike | 39 | 3.14 | 33 | 0 | wallstreetbets 39 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| HPE | 2026-11-24 00:45 | mention spike | 5 | 7.0 | 5 | 0 | wallstreetbets 5 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4uwxevhmmd/) |
| DJT | 2026-11-24 00:45 | mention spike | 11 | 11.86 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4rrfk/comment/19t58n1cxqhj8/) |
| MSS | 2026-11-24 00:45 | mention spike | 2 | 2.43 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t41rnkd6tq9/) |
| SOAR | 2026-11-24 00:45 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t4lim86r20x/) |
| IVVD | 2026-11-24 00:45 | mention spike | 2 | 1.86 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t4jxdoc4a9s/) |
| NYT | 2026-11-24 00:45 | mention spike | 6 | 21.43 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4hlc3/comment/19t4pwr1k0cir/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
