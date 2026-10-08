# Stage 2 market snapshots

Updated 2026-10-08T03:01:53Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

48 candidates and 96 controls so far. Archetypes: other 45, low_float_runner 3.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| KEEL | 2026-10-08 03:01 | other | listed | 3.34 | +0.3% | -5.7% | 1.0x | 589.8M | 18.6% | 0 |  |
| UUUU | 2026-10-07 20:50 | other | listed | 10.26 | +0.0% | -7.0% | 1.8x | 248.2M | 22.4% | 0 |  |
| SMCI | 2026-10-07 20:50 | other | listed | 45 | +0.1% | +9.4% | 1.1x | 557.6M | 17.1% | 0 |  |
| LEVI | 2026-10-07 20:37 | other | listed | 19.16 | -1.8% | -1.0% | 5.8x | 93.0M | 8.7% | 0 |  |
| IREN | 2026-10-07 19:18 | other | listed | 38.77 | -6.1% | -0.2% | 1.0x | 346.2M | 24.0% | 1 |  |
| LLY | 2026-10-07 17:44 | other | listed | 1,196 | +3.4% | -2.3% | 0.9x | 889.0M | 0.8% | 0 |  |
| BIYA | 2026-10-07 16:38 | low float runner | listed | 2.11 | +54.6% | -33.4% | 12.7x | 3.0M | 2.1% | 2 |  |
| GLD | 2026-10-07 13:01 | other | listed | 374.7 | -2.0% | -0.2% | 0.9x |  |  | 0 |  |
| SOXL | 2026-10-07 12:34 | other | listed | 153.9 | -6.3% | +11.7% | 0.7x |  |  |  |  |
| SOXS | 2026-10-07 12:08 | other | listed | 31.12 | +5.0% | -10.9% | 0.8x |  |  |  |  |
| BULL | 2026-10-07 12:08 | other | listed | 5.45 | -25.1% | +1.5% | 0.5x | 322.2M | 11.2% | 1 |  |
| SNDK | 2026-10-07 10:09 | other | listed | 1,625 | -2.1% | -4.0% | 0.7x | 144.5M | 3.9% | 0 |  |
| CRWD | 2026-10-06 23:59 | other | listed | 278.6 | +2.2% | +5.2% | 0.5x | 1.01B | 2.8% | 1 |  |
| AVGO | 2026-10-06 19:34 | other | listed | 378.1 | +4.3% | +3.7% | 0.9x | 4.72B | 1.1% | 1 |  |
| SKHY | 2026-10-06 18:54 | other | listed | 184.1 | -5.6% | +7.2% | 0.6x | 5.67B | 0.5% | 1 |  |
| INTC | 2026-10-06 18:28 | other | listed | 114.7 | -1.3% | +0.1% | 0.7x | 4.62B | 3.4% | 3 |  |
| OKLO | 2026-10-06 18:14 | other | listed | 39.07 | +8.6% | -3.1% | 0.8x | 149.6M | 22.5% | 1 |  |
| PENG | 2026-10-06 18:01 | other | listed | 57.2 | -5.8% | +10.4% | 1.8x | 49.7M | 14.3% | 0 |  |
| CIRC | 2026-10-06 17:21 | other | listed | 0.4392 | -18.4% | +36.2% | 1.6x | 55.8M | 1.6% | 1 |  |
| SPY | 2026-10-06 17:08 | other | listed | 779.9 | +0.7% | +1.2% | 1.0x |  |  | 0 |  |
| INFQ | 2026-10-06 16:43 | other | listed | 12.74 | +0.6% | -10.4% | 1.0x | 195.6M | 10.7% | 3 |  |
| HTZ | 2026-10-06 16:43 | other | listed | 2.02 | +12.8% | +5.9% | 1.3x | 170.6M | 67.9% | 0 |  |
| VOO | 2026-10-06 16:15 | other | listed | 717.9 | +0.8% | +1.2% | 0.6x |  |  |  |  |
| NOK | 2026-10-06 15:49 | other | listed | 10.78 | +5.6% | +0.8% | 0.5x | 4.45B | 1.2% | 0 |  |
| AMD | 2026-10-06 14:55 | other | listed | 651.8 | +3.2% | +3.9% | 0.6x | 1.62B | 2.5% | 3 |  |
| NVDA | 2026-10-06 14:02 | other | listed | 242.3 | +1.4% | +4.4% | 1.2x | 23.13B | 1.3% | 0 |  |
| MRNA | 2026-10-06 14:02 | other | listed | 198 | -2.6% | +3.0% | 1.3x | 372.2M | 8.8% | 0 |  |
| NVAX | 2026-10-06 13:49 | other | listed | 13.19 | +5.0% | +16.3% | 5.5x | 142.6M | 35.0% | 0 |  |
| CRWV | 2026-10-06 13:49 | other | listed | 89.86 | +2.8% | +2.7% | 0.6x | 328.3M | 16.7% | 1 |  |
| MRVL | 2026-10-06 13:36 | other | listed | 286.3 | +5.5% | +7.7% | 0.7x | 873.9M | 3.6% | 1 |  |
