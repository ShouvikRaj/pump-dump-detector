# Stage 1 candidates

Updated 2026-10-26T22:07:08Z by run `40409709403`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-10-26 13:24 | mention spike | 23 | 0.0 | 21 | 0 | wallstreetbets 23 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg24l4/) |
| CLS | 2026-10-26 19:24 | mention spike | 24 | 1.0 | 13 | 0 | wallstreetbets 24 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8i1qi8blx/) |
| EWZ | 2026-10-26 00:21 | mention spike | 58 | 0.57 | 46 | 0 | wallstreetbets 52, smallstreetbets 6 | NYSE Arca | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/) |
| MELI | 2026-10-26 08:42 | mention spike | 37 | 0.14 | 29 | 1 | wallstreetbets 37 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp4axo4ux1e/) |
| NU | 2026-10-26 11:48 | mention spike | 18 | 0.0 | 5 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfslp3/comment/19ros9vyni0ow/) |
| PBR | 2026-10-26 09:22 | mention spike | 29 | 1.43 | 23 | 0 | wallstreetbets 26, smallstreetbets 3 | NYSE | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfthvb/) |
| RDDT | 2026-10-26 14:04 | mention spike | 77 | 12.29 | 57 | 0 | wallstreetbets 77 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg7hq7/comment/19rp8msi6kxxd/) |
| STNE | 2026-10-26 13:24 | mention spike | 11 | 0.0 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xfu7p0/comment/19ronas7lreit/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
