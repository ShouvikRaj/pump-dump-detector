# Stage 2 market snapshots

Updated 2026-10-28T21:57:30Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

256 candidates and 509 controls so far. Archetypes: other 244, low_float_runner 10, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NOW | 2026-10-28 21:57 | other | listed | 123.1 | -18.0% | -2.0% | 2.3x | 1.03B | 2.7% | 0 |  |
| GOOGL | 2026-10-28 21:46 | other | listed | 289.9 | -10.8% | -2.9% | 2.2x | 10.88B | 0.7% | 3 |  |
| MRVL | 2026-10-28 21:20 | other | listed | 227.5 | -9.6% | +2.8% | 0.6x | 873.8M | 2.8% | 0 |  |
| LITE | 2026-10-28 21:20 | other | listed | 1,016 | +11.1% | +7.4% | 0.9x | 89.1M | 8.7% | 0 |  |
| FTNT | 2026-10-28 21:20 | other | listed | 131.1 | -24.7% | +0.0% | 2.8x | 618.9M | 2.0% | 0 |  |
| GOOG | 2026-10-28 20:50 | other | listed | 292.9 | -9.0% | -2.7% | 1.6x | 10.88B | 0.4% | 3 |  |
| ORCL | 2026-10-28 18:38 | other | listed | 142.9 | +9.5% | -0.5% | 0.9x | 1.86B | 2.6% | 0 |  |
| DJT | 2026-10-28 17:04 | other | listed | 5.975 | -6.1% | -1.7% | 1.0x | 160.9M | 10.9% | 0 |  |
| ENPH | 2026-10-28 16:10 | other | listed | 25.04 | -15.9% | -7.7% | 3.4x | 128.1M | 23.0% | 0 |  |
| SLS | 2026-10-28 13:05 | other | listed | 12.92 | +6.1% | +1.6% | 1.1x | 201.1M | 26.7% | 0 |  |
| VRT | 2026-10-28 11:39 | other | listed | 242.3 | +16.2% | +2.5% | 1.5x | 383.8M | 3.6% | 0 |  |
| GLD | 2026-10-28 00:47 | other | listed | 372.3 | +1.2% | -3.1% | 0.8x |  |  | 0 |  |
| BBAI | 2026-10-27 20:57 | other | listed | 2.28 | -3.0% | +8.3% | 2.1x | 475.3M | 28.7% | 1 |  |
| SKHY | 2026-10-27 19:51 | other | listed | 146.5 | +2.7% | -0.2% | 0.9x | 5.67B | 0.6% | 0 |  |
| STX | 2026-10-27 19:12 | other | listed | 676.6 | +5.0% | -2.5% | 0.8x | 225.9M | 3.5% | 0 |  |
| BRAI | 2026-10-27 17:53 | other | listed | 3.9 | +84.0% | -52.6% | 86.0x | 40.0M | 0.2% | 0 |  |
| ASML | 2026-10-27 17:38 | other | listed | 1,638 | +2.9% | -3.4% | 1.3x | 21.28B | 0.0% | 0 |  |
| USAR | 2026-10-27 17:13 | other | listed | 10.12 | +13.6% | -11.7% | 1.1x | 182.2M | 28.3% | 3 |  |
| INOD | 2026-10-27 14:48 | other | listed | 45.03 | -24.8% | +10.9% | 0.6x | 33.1M | 13.7% | 2 |  |
| GOOGL | 2026-10-27 13:39 | other | listed | 318.9 | +0.7% | -8.0% | 1.0x | 10.88B | 0.7% | 3 |  |
| HOOD | 2026-10-27 03:54 | other | listed | 93.64 | +0.9% | -3.8% | 0.8x | 784.4M | 4.7% | 0 |  |
| VOO | 2026-10-27 02:38 | other | listed | 704.4 | +0.1% | -0.2% | 0.8x |  |  |  |  |
| SOFI | 2026-10-27 00:43 | other | listed | 14.48 | -0.9% | +0.4% | 0.9x | 1.27B | 17.3% | 0 |  |
| RIVN | 2026-10-27 00:43 | other | listed | 11.5 | -2.8% | -4.8% | 0.9x | 945.4M | 17.4% | 0 |  |
| GOOG | 2026-10-27 00:43 | other | listed | 315.1 | -0.7% | -5.8% | 0.7x | 10.88B | 0.4% | 3 |  |
| DXYZ | 2026-10-27 00:43 | other | listed | 28.49 | +3.6% | -1.5% | 0.8x |  |  | 2 |  |
| COIN | 2026-10-27 00:43 | other | listed | 160.1 | -2.6% | -5.0% | 0.8x | 219.8M | 10.8% | 0 |  |
| AMKR | 2026-10-27 00:43 | other | listed | 38.32 | -2.5% | -6.0% | 1.3x | 108.7M | 9.2% | 0 |  |
| MSFT | 2026-10-27 00:09 | other | listed | 532.4 | +1.5% | -0.9% | 0.6x | 7.41B | 0.9% | 0 |  |
| CLS | 2026-10-26 19:24 | other | listed | 258 | -0.8% | -14.4% | 1.4x | 114.1M | 3.9% | 2 |  |
