# Stage 2 market snapshots

Updated 2026-10-22T20:12:32Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

195 candidates and 389 controls so far. Archetypes: other 184, low_float_runner 10, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| AVEX | 2026-10-22 11:25 | other | listed | 10.6 | +9.5% | -31.7% | 7.3x | 19.9M | 18.1% | 0 |  |
| TSLA | 2026-10-22 07:27 | other | listed | 373.6 | -3.3% | +5.3% | 1.4x | 2.82B | 2.5% | 0 |  |
| SDEV | 2026-10-22 07:27 | other | listed | 1.21 | +10.0% | +11.1% | 3.1x | 49.3M | 7.0% | 3 |  |
| NOK | 2026-10-22 05:55 | other | listed | 9.22 | -0.3% | -1.6% | 1.1x | 4.45B | 1.9% | 0 |  |
| BABA | 2026-10-22 02:50 | other | listed | 104 | -0.4% | -6.1% | 1.5x | 2.22B | 1.7% | 0 |  |
| RDDT | 2026-10-21 22:45 | other | listed | 153.5 | +0.1% | +3.1% | 0.8x | 140.7M | 15.7% | 0 |  |
| MSTR | 2026-10-21 19:47 | other | listed | 153.1 | +7.3% | -6.2% | 1.0x | 363.6M | 8.1% | 0 |  |
| IBM | 2026-10-21 18:15 | other | listed | 245.6 | +1.5% | +4.8% | 1.1x | 940.2M | 2.6% | 2 |  |
| AMOD | 2026-10-21 16:41 | low float runner | listed | 1.91 | +48.1% | -21.3% | 0.0x | 1.1M | 3.6% | 4 |  |
| META | 2026-10-21 11:34 | other | listed | 690.9 | -0.5% | -9.0% | 0.8x | 2.20B | 1.5% | 0 |  |
