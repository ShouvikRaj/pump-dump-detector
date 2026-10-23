# Stage 2 market snapshots

Updated 2026-10-23T01:00:16Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

205 candidates and 409 controls so far. Archetypes: other 194, low_float_runner 10, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| FPS | 2026-10-22 16:39 | other | listed | 24.64 | -22.4% | -2.9% | 0.9x | 170.6M | 8.3% | 0 |  |
| SOXL | 2026-10-22 15:59 | other | listed | 85.17 | -17.5% | -6.6% | 1.0x |  |  |  |  |
| PLTR | 2026-10-22 15:59 | other | listed | 198.2 | -1.7% | +0.4% | 0.9x | 2.11B | 2.6% | 0 |  |
| GEV | 2026-10-22 15:59 | other | listed | 822.1 | -11.2% | -1.7% | 1.4x | 265.8M | 2.8% | 0 |  |
| WDC | 2026-10-22 14:55 | other | listed | 352.8 | -6.8% | +4.0% | 1.0x | 358.2M | 5.1% | 0 |  |
| SHFS | 2026-10-22 14:55 | other | listed | 0.2479 | +61.0% | -33.6% | 34.6x | 0.9M | 4.1% | 3 |  |
| BKYI | 2026-10-22 14:55 | low float runner | listed | 2.937 | +39.9% | -27.8% | 0.0x | 1.3M | 74.5% | 1 |  |
| IWM | 2026-10-22 14:12 | other | listed | 276.2 | -0.1% | +1.9% | 0.6x |  |  |  |  |
| HTZ | 2026-10-22 14:12 | other | listed | 2.375 | +14.7% | +11.9% | 1.1x | 170.6M | 72.3% | 0 |  |
| AVGO | 2026-10-22 14:12 | other | listed | 329.2 | -2.5% | -2.4% | 0.8x | 4.72B | 1.1% | 1 |  |
