# Stage 2 market snapshots

Updated 2026-10-29T21:35:44Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

273 candidates and 543 controls so far. Archetypes: other 260, low_float_runner 11, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CROX | 2026-10-29 21:35 | other | listed | 150.5 | +0.2% | +24.2% | 4.7x | 46.1M | 9.9% | 0 |  |
| NRXP | 2026-10-29 20:56 | other | listed | 2.77 | +4.1% | +10.8% | 1.2x | 37.4M | 26.6% | 0 |  |
| SNDK | 2026-10-29 20:27 | other | listed | 1,355 | +1.9% | +5.5% | 0.8x | 144.5M | 3.3% | 0 |  |
| IWM | 2026-10-29 19:09 | other | listed | 283.3 | +0.7% | +1.7% | 0.8x |  |  |  |  |
| SAP | 2026-10-29 17:49 | other | listed | 233.3 | -1.5% | +1.8% | 0.7x | 14.45B | 0.0% | 0 |  |
| LLY | 2026-10-29 14:09 | other | listed | 1,385 | +7.5% | +1.4% | 0.9x | 889.0M | 0.8% | 0 |  |
| RDDT | 2026-10-29 14:06 | other | listed | 130.3 | -3.3% | -12.1% | 1.3x | 140.7M | 15.4% | 0 |  |
| AMZN | 2026-10-29 14:06 | other | listed | 245.7 | -3.5% | -3.0% | 1.0x | 9.81B | 1.0% | 3 |  |
| DXYZ | 2026-10-29 13:37 | other | listed | 27.21 | -1.6% | -4.7% | 0.8x |  |  | 2 |  |
| INTC | 2026-10-29 11:49 | other | listed | 92.52 | -3.2% | +2.8% | 0.8x | 4.62B | 3.2% | 3 |  |
| ELPW | 2026-10-29 10:54 | low float runner | listed | 2.8 | -6.7% | +30.4% | 956.9x | 0.1M | 39.6% | 4 |  |
| TTWO | 2026-10-29 04:39 | other | listed | 196.3 | +0.5% | -5.3% | 0.9x | 186.1M | 5.2% | 0 |  |
| WEN | 2026-10-29 04:31 | other | listed | 7.05 | -0.3% | +12.6% | 6.6x | 157.1M | 33.3% | 0 |  |
| CVNA | 2026-10-29 04:06 | other | listed | 63.94 | +8.3% | -0.2% | 2.1x | 706.4M | 9.5% | 0 |  |
| CBRS | 2026-10-29 00:52 | other | listed | 109.7 | -8.0% | +0.9% | 1.4x | 109.9M | 18.1% | 0 |  |
| COHR | 2026-10-28 23:40 | other | listed | 243.6 | +1.7% | +0.9% | 1.0x | 195.0M | 4.6% | 0 |  |
| GGLL | 2026-10-28 22:11 | other | listed | 68.93 | -21.7% | -5.8% | 3.1x |  |  |  |  |
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
