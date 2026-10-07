# Social chatter (StockTwits, Bluesky, X)

Written by the `social` workflow (docs/social.md on main). One row in `snapshots.csv` per fetch:

- `phase` = `flag`: the first fetch for a candidate or control. Features (`st_*` StockTwits, `bsky_*` Bluesky,
  `x_*` X) count posts created in the 24 hours **before** the flag, so they are safe model inputs; `*_n_72h`
  covers 72 hours before, `*_n_after_flag` the posts between the flag and the fetch.
- `phase` = `d1` ... `d10`: candidates only, about daily for 10 days; features count the posts in
  `[window_start_utc, window_end_utc)`, i.e. since the previous row. Not for flag-time models (lookahead).
- `lag_s`: fetch time minus flag time. Deleted posts are missing, so large lags undercount promoters.
- `*_truncated` = 1: the page limit was hit, so counts are lower bounds (very busy tickers).
- `*_fetched`: posts fetched for the row (for X, what was billed).

Raw posts: `raw/YYYY/MM/DD/<snap_key>.json.gz` by fetch date, with every post's text, author, follower count and
account age where the source gives them.
