# Stage 2 market snapshots

Updated 2026-10-20T21:06:32Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

161 candidates and 322 controls so far. Archetypes: other 153, low_float_runner 8.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SMCI | 2026-10-20 21:06 | other | listed | 36.6 | +12.7% | -16.9% | 1.1x | 557.7M | 15.7% | 0 |  |
| GOOGL | 2026-10-20 18:16 | other | listed | 340.8 | -1.0% | -2.4% | 0.8x | 10.88B | 0.7% | 3 |  |
| LRCX | 2026-10-20 16:42 | other | listed | 264.7 | -2.8% | -12.1% | 1.2x | 1.25B | 2.1% | 0 |  |
| IWM | 2026-10-20 16:03 | other | listed | 275.8 | +1.7% | -2.4% | 0.7x |  |  |  |  |
| CRWV | 2026-10-20 14:57 | other | listed | 63.86 | +4.5% | -23.8% | 2.5x | 328.3M | 18.3% | 1 |  |
| HTZ | 2026-10-20 13:24 | other | listed | 2.108 | +14.6% | -0.5% | 0.8x | 170.6M | 72.3% | 0 |  |
| SPCX | 2026-10-20 10:18 | other | listed | 146.8 | -0.8% | -9.5% | 0.9x | 4.97B | 3.6% | 0 |  |
| APLD | 2026-10-20 04:07 | other | listed | 19.34 | +0.5% | -17.2% | 1.5x | 261.4M | 21.7% | 0 |  |
| GOOG | 2026-10-19 22:36 | other | listed | 340.1 | -0.0% | -2.5% | 0.7x | 10.88B | 0.5% | 3 |  |
| NFLX | 2026-10-19 19:31 | other | listed | 69.83 | -1.0% | +0.3% | 1.1x | 4.13B | 2.0% | 1 |  |
| RIVN | 2026-10-19 18:51 | other | listed | 12.29 | -1.1% | -11.0% | 1.0x | 945.4M | 17.9% | 0 |  |
| TQQQ | 2026-10-19 16:13 | other | listed | 71.72 | +5.1% | -16.1% | 1.7x |  |  |  |  |
| GLD | 2026-10-19 16:13 | other | listed | 379.6 | -0.6% | -0.7% | 1.2x |  |  | 0 |  |
| AMZN | 2026-10-19 16:13 | other | listed | 262.8 | +5.1% | -4.7% | 1.1x | 9.81B | 0.9% | 3 |  |
| TCRT | 2026-10-19 14:18 | low float runner | listed | 3.185 | +21.1% | +232.9% | 1.7x | 1.2M | 0.8% | 1 |  |
| WDC | 2026-10-19 06:00 | other | listed | 327.3 | -1.4% | -16.4% | 0.9x |  |  | 0 | yahoo summary: crumb HTTP 429: Too Many Requests |
| VTI | 2026-10-18 05:58 | other | listed | 373.5 | -0.2% | -2.1% | 1.1x |  |  |  |  |
| NFLX | 2026-10-17 17:37 | other | listed | 70.33 | -0.3% | +0.3% | 1.1x | 4.13B | 2.0% | 2 |  |
| SCHD | 2026-10-17 04:49 | other | listed | 34.37 | +0.1% | +4.0% | 1.1x |  |  |  |  |
| SOXX | 2026-10-17 01:44 | other | listed | 493.7 | +0.1% | -11.8% | 2.1x |  |  |  |  |
| AMD | 2026-10-16 21:33 | other | listed | 530.1 | +0.2% | -13.0% | 1.0x | 1.62B | 2.4% | 3 |  |
| XLAB | 2026-10-16 21:20 | other | listed | 2.41 | +2.5% | +141.3% | 189.9x |  |  | 0 |  |
| SGRX | 2026-10-16 21:20 | other | listed | 0.7814 | -10.0% | +17.4% | 115.8x | 0.7M | 2.1% | 0 |  |
| AAPL | 2026-10-16 20:40 | other | listed | 343.4 | -0.0% | +2.0% | 1.5x | 14.57B | 0.8% | 0 |  |
| AVGO | 2026-10-16 20:14 | other | listed | 329.6 | +0.3% | -9.1% | 1.3x | 4.72B | 1.1% | 1 |  |
| SOXS | 2026-10-16 19:34 | other | listed | 48.04 | +10.1% | +29.2% | 1.5x |  |  |  |  |
| VOO | 2026-10-16 19:07 | other | listed | 699.9 | -1.3% | -0.3% | 0.8x |  |  |  |  |
| OPEX | 2026-10-16 19:07 | other | listed | 2.812 | -18.0% | -1.2% | 5.6x |  |  |  |  |
| MSTR | 2026-10-16 19:07 | other | listed | 134.4 | -11.1% | -0.1% | 1.0x | 363.6M | 8.1% | 0 |  |
| TQQQ | 2026-10-16 18:54 | other | listed | 68.22 | -7.6% | -8.0% | 1.5x |  |  |  |  |
