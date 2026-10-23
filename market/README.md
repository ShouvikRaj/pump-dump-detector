# Stage 2 market snapshots

Updated 2026-10-23T15:42:43Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

215 candidates and 429 controls so far. Archetypes: other 204, low_float_runner 10, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BE | 2026-10-23 15:42 | other | listed | 191.3 | -12.1% | -7.8% | 1.7x | 289.2M | 7.3% | 0 |  |
| IREN | 2026-10-23 14:50 | other | listed | 25.74 | +0.9% | -16.1% | 1.3x | 346.2M | 23.6% | 1 |  |
| ASTS | 2026-10-23 13:45 | other | listed | 37.61 | -3.0% | -12.8% | 1.0x | 266.5M | 24.3% | 0 |  |
| SKHY | 2026-10-23 13:03 | other | listed | 137.1 | +4.1% | -9.9% | 1.3x | 5.67B | 0.7% | 0 |  |
| CRDO | 2026-10-23 12:23 | other | listed | 154.3 | -5.2% | -8.8% | 1.1x | 170.9M | 6.6% | 0 |  |
| MU | 2026-10-23 10:49 | other | listed | 868 | +1.3% | -8.0% | 1.2x | 1.13B | 2.3% | 0 |  |
| MSFT | 2026-10-23 06:51 | other | listed | 522 | +0.2% | -3.4% | 1.0x | 7.41B | 0.8% | 0 |  |
| AMD | 2026-10-23 05:06 | other | listed | 505.7 | -0.4% | -9.7% | 1.4x | 1.62B | 2.4% | 3 |  |
| SPY | 2026-10-23 03:07 | other | listed | 764.1 | +0.0% | -1.0% | 1.3x |  |  | 0 |  |
| NVDA | 2026-10-23 02:14 | other | listed | 212.4 | +0.1% | -2.3% | 1.2x | 23.13B | 1.3% | 0 |  |
| TQQQ | 2026-10-23 00:59 | other | listed | 66.02 | -9.1% | -2.0% | 1.0x |  |  |  |  |
| AAPL | 2026-10-23 00:03 | other | listed | 348.6 | +1.3% | +0.3% | 1.0x | 14.57B | 0.8% | 0 |  |
| SOXS | 2026-10-22 23:50 | other | listed | 54.75 | +2.4% | +22.5% | 1.2x |  |  |  |  |
| CBRS | 2026-10-22 22:49 | other | listed | 108.7 | -0.3% | -23.4% | 1.1x | 109.9M | 12.8% | 0 |  |
| WMT | 2026-10-22 22:30 | other | listed | 120.8 | -0.2% | +2.8% | 1.3x | 4.85B | 1.7% | 4 |  |
| SNDK | 2026-10-22 22:30 | other | listed | 1,236 | -2.0% | -9.6% | 1.3x | 144.5M | 3.3% | 0 |  |
| SQQQ | 2026-10-22 22:06 | other | listed | 39.67 | +0.2% | +9.6% | 1.2x |  |  |  |  |
| LMT | 2026-10-22 22:06 | other | listed | 590 | +0.0% | +10.8% | 2.6x | 197.4M | 1.4% | 0 |  |
| INTC | 2026-10-22 21:18 | other | listed | 85.24 | -0.3% | -10.4% | 1.3x | 4.62B | 3.6% | 3 |  |
| SCHD | 2026-10-22 21:05 | other | listed | 35.37 | -0.1% | +3.8% | 1.3x |  |  |  |  |
| LULU | 2026-10-22 20:12 | other | listed | 103.4 | -0.6% | +5.0% | 1.5x | 101.7M | 15.1% | 0 |  |
| VST | 2026-10-22 19:45 | other | listed | 139.4 | -10.7% | +2.9% | 0.7x | 313.0M | 3.3% | 3 |  |
| QQQ | 2026-10-22 19:45 | other | listed | 702.6 | -3.1% | -0.5% | 0.9x |  |  |  |  |
| AMAT | 2026-10-22 19:30 | other | listed | 378.9 | -7.4% | -8.4% | 1.0x | 790.5M | 1.7% | 0 |  |
| SOXX | 2026-10-22 18:52 | other | listed | 476.7 | -6.6% | -1.7% | 1.1x |  |  |  |  |
| RSP | 2026-10-22 18:38 | other | listed | 217.2 | +0.3% | +2.1% | 1.0x |  |  |  |  |
| XXII | 2026-10-22 17:45 | other | listed | 0.2476 | -9.3% | -58.1% | 0.3x | 0.5M | 7.6% | 1 |  |
| TOGI | 2026-10-22 17:45 | otc penny | otc | 0.0129 | -19.4% | -15.8% | 1.2x | 154.0M | 0.0% | 0 |  |
| ORCL | 2026-10-22 17:45 | other | listed | 124.1 | -3.9% | -1.1% | 0.9x | 1.86B | 2.6% | 0 |  |
| AAOI | 2026-10-22 17:45 | other | listed | 67.53 | -12.7% | -10.3% | 0.7x | 80.9M | 17.2% | 1 |  |
