# Stage 2 market snapshots

Updated 2026-10-27T00:43:54Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

234 candidates and 465 controls so far. Archetypes: other 222, low_float_runner 10, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOFI | 2026-10-27 00:43 | other | listed | 14.48 | -0.9% | +0.4% | 0.9x | 1.27B | 17.3% | 0 |  |
| RIVN | 2026-10-27 00:43 | other | listed | 11.5 | -2.8% | -4.8% | 0.9x | 945.4M | 17.4% | 0 |  |
| GOOG | 2026-10-27 00:43 | other | listed | 315.1 | -0.7% | -5.8% | 0.7x | 10.88B | 0.4% | 3 |  |
| DXYZ | 2026-10-27 00:43 | other | listed | 28.49 | +3.6% | -1.5% | 0.8x |  |  | 2 |  |
| COIN | 2026-10-27 00:43 | other | listed | 160.1 | -2.6% | -5.0% | 0.8x | 219.8M | 10.8% | 0 |  |
| AMKR | 2026-10-27 00:43 | other | listed | 38.32 | -2.5% | -6.0% | 1.3x | 108.7M | 9.2% | 0 |  |
| MSFT | 2026-10-27 00:09 | other | listed | 532.4 | +1.5% | -0.9% | 0.6x | 7.41B | 0.9% | 0 |  |
| CLS | 2026-10-26 19:24 | other | listed | 258 | -0.8% | -14.4% | 1.4x | 114.1M | 3.9% | 2 |  |
| RDDT | 2026-10-26 14:04 | other | listed | 138.3 | -4.1% | -7.6% | 1.0x | 140.7M | 15.7% | 0 |  |
| STNE | 2026-10-26 13:24 | other | listed | 7 | -39.0% | +1.8% | 0.9x | 204.7M | 5.1% | 0 |  |
| ANT | 2026-10-26 13:24 | unknown | unknown |  |  |  |  |  |  |  | yahoo: No data found, symbol may be delisted |
| NU | 2026-10-26 11:48 | other | listed | 11.2 | -26.1% | +4.1% | 1.0x | 3.71B | 3.6% | 0 |  |
| PBR | 2026-10-26 09:22 | other | listed | 20.33 | -22.3% | +0.6% | 1.1x | 3.94B | 0.9% | 0 |  |
| MELI | 2026-10-26 08:42 | other | listed | 1,614 | -10.8% | -1.3% | 0.8x | 50.6M | 1.8% | 2 |  |
| EWZ | 2026-10-26 00:21 | other | listed | 42.75 | +0.4% | +1.8% | 1.6x |  |  |  |  |
| RDDT | 2026-10-23 20:37 | other | listed | 145 | +0.5% | -7.6% | 1.0x | 140.7M | 15.7% | 0 |  |
| CRWD | 2026-10-23 20:37 | other | listed | 258.2 | +0.2% | +13.3% | 1.6x | 1.01B | 2.6% | 1 |  |
| LUNR | 2026-10-23 18:21 | other | listed | 10.56 | +1.1% | -9.7% | 0.8x | 131.6M | 27.7% | 0 |  |
| USO | 2026-10-23 16:35 | other | listed | 168.3 | +3.6% | +3.3% | 0.8x |  |  | 0 |  |
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
