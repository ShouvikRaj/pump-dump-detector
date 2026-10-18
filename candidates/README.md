# Stage 1 candidates

Updated 2026-10-18T13:01:47Z by run `39129717021`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 3.86 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phf4kut/) |
| VTI | 2026-10-18 05:58 | mention spike | 12 | 1.86 | 10 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phh3nvr/) |
| NFLX | 2026-10-17 17:37 | mention spike | 13 | 7.43 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x90lu4/comment/phh6nlr/) |
| VOO | 2026-10-16 19:07 | mention spike | 31 | 16.57 | 29 | 0 | wallstreetbets 31 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8s3ma/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg0wwv/) |
| QQQ | 2026-10-16 18:27 | mention spike | 37 | 83.0 | 33 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| OPEX | 2026-10-16 19:07 | mention spike | 1 | 2.57 | 1 | 0 | smallstreetbets 1 | Cboe BZX |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7yj41/comment/phb22us/) |
| USO | 2026-10-16 11:23 | mention spike | 1 | 9.14 | 1 | 0 | wallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nbc1/comment/phe5ejf/) |
| AVGO | 2026-10-16 20:14 | mention spike | 18 | 13.29 | 17 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phhj5ds/) |
| SGRX | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TSLA | 2026-10-16 07:11 | mention spike | 14 | 48.43 | 12 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8aojz/) |
| XLAB | 2026-10-16 21:20 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXS | 2026-10-16 19:34 | mention spike | 3 | 7.57 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phh0ysa/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
