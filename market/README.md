# Stage 2 market snapshots

Updated 2026-10-17T17:37:35Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

144 candidates and 288 controls so far. Archetypes: other 137, low_float_runner 7.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| QQQ | 2026-10-16 18:27 | other | listed | 710.8 | -2.4% | -2.6% | 1.4x |  |  |  |  |
| IBKR | 2026-10-16 13:35 | other | listed | 84.83 | -1.4% | -0.5% | 1.5x | 439.2M | 3.1% | 3 |  |
| RCS | 2026-10-16 12:29 | other | listed | 5 | +1.0% | -1.8% | 0.9x |  |  | 0 |  |
| USO | 2026-10-16 11:23 | other | listed | 156.9 | -0.3% | +6.6% | 0.8x |  |  | 0 |  |
| TSLA | 2026-10-16 07:11 | other | listed | 362.3 | -0.0% | -3.3% | 0.8x | 2.82B | 2.5% | 0 |  |
| DRMA | 2026-10-15 23:28 | other | listed | 0.9 | -1.1% | -15.0% | 4315.7x | 2.9M | 2.9% | 1 |  |
| BETR | 2026-10-15 23:28 | other | listed | 10.8 | +0.4% | +6.0% | 4.3x | 8.5M | 44.1% | 0 |  |
| WETO | 2026-10-15 21:16 | low float runner | listed | 1.23 | +0.8% | +13.0% | 16.8x | 0.2M | 1159.2% | 2 |  |
| SOXS | 2026-10-15 15:04 | other | listed | 45.26 | +6.4% | +38.7% | 1.2x |  |  |  |  |
| PFE | 2026-10-14 20:17 | other | listed | 29.17 | -0.1% | +4.3% | 1.2x | 5.69B | 2.6% | 0 |  |
| HOOD | 2026-10-14 20:04 | other | listed | 101.1 | +0.0% | -7.7% | 1.1x | 784.4M | 5.1% | 0 |  |
| TSM | 2026-10-14 19:51 | other | listed | 430.8 | -3.2% | -7.7% | 0.9x | 37.84B | 0.1% | 0 |  |
| WMT | 2026-10-14 19:24 | other | listed | 115.7 | +3.1% | +4.7% | 0.8x | 4.85B | 1.7% | 0 |  |
| RKLB | 2026-10-14 19:24 | other | listed | 59.41 | -7.5% | -14.4% | 0.7x | 556.9M | 8.0% | 2 |  |
| LQDA | 2026-10-14 19:11 | other | listed | 33.93 | +26.6% | +3.5% | 0.8x | 65.3M | 19.3% | 0 |  |
| TLT | 2026-10-14 18:31 | other | listed | 78.93 | +0.7% | +1.4% | 0.6x |  |  |  |  |
| SOFI | 2026-10-14 18:18 | other | listed | 14.01 | -8.1% | -3.3% | 0.6x | 1.27B | 16.9% | 0 |  |
