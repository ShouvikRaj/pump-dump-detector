# Stage 1 candidates

Updated 2026-11-25T01:33:42Z by run `45525555720`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BENF | 2026-11-25 00:43 | mention spike | 11 | 0.0 | 6 | 0 | pennystocks 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1y4edv2/) |
| DELL | 2026-11-24 21:15 | mention spike | 39 | 3.14 | 33 | 0 | wallstreetbets 39 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| HPE | 2026-11-24 00:45 | mention spike | 6 | 6.86 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4uwxevhmmd/) |
| DJT | 2026-11-24 00:45 | mention spike | 11 | 11.71 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4bir8/comment/19t4nbrz9jkn7/) |
| MSS | 2026-11-24 00:45 | mention spike | 3 | 2.29 | 3 | 0 | wallstreetbets 2, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t41rnkd6tq9/) |
| SOAR | 2026-11-24 00:45 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t4lim86r20x/) |
| IVVD | 2026-11-24 00:45 | mention spike | 2 | 1.86 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y44hxg/comment/19t4jxdoc4a9s/) |
| NYT | 2026-11-24 00:45 | mention spike | 7 | 21.29 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y41nrx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
