# Stage 2 market snapshots

Updated 2026-11-12T05:14:57Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

429 candidates and 851 controls so far. Archetypes: other 411, low_float_runner 14, unknown 3, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | other | listed | 576.8 | +4.3% | +13.1% | 1.4x | 1.63B | 2.4% | 1 |  |
| NXXT | 2026-11-12 03:27 | low float runner | listed | 2.05 | +20.6% | -33.1% | 191.7x | 0.8M | 5.9% | 2 |  |
| GME | 2026-11-12 01:54 | other | listed | 25 | -1.7% | +4.8% | 0.5x | 460.4M | 9.2% | 0 |  |
| OUST | 2026-11-12 01:02 | other | listed | 37.51 | -1.9% | +31.9% | 0.8x | 70.8M | 9.7% | 0 |  |
| NYT | 2026-11-12 01:02 | other | listed | 70.94 | -2.3% | +8.1% | 0.6x | 132.3M | 14.1% | 0 |  |
| MSFT | 2026-11-11 15:26 | other | listed | 520.7 | -2.3% | +2.3% | 1.0x | 7.42B | 0.8% | 2 |  |
| NBIS | 2026-11-11 12:32 | other | listed | 154 | +15.0% | -11.6% | 0.8x | 228.7M | 22.3% | 0 |  |
| NVDL | 2026-11-11 07:39 | other | listed | 19.62 | +1.8% | -34.5% | 5.8x |  |  |  |  |
| RGTI | 2026-11-10 21:21 | other | listed | 11.48 | -5.5% | +9.6% | 1.1x | 328.0M | 21.7% | 0 |  |
| CRWV | 2026-11-10 20:00 | other | listed | 47.3 | -3.4% | -2.3% | 0.7x | 328.3M | 21.3% | 1 |  |
| MSTR | 2026-11-10 19:20 | other | listed | 120.4 | -4.1% | -4.0% | 0.8x | 401.8M | 7.2% | 5 |  |
| GLD | 2026-11-10 17:08 | other | listed | 368.6 | -2.9% | +4.9% | 0.8x |  |  | 0 |  |
| TTWO | 2026-11-10 16:24 | other | listed | 220.4 | +6.3% | +8.0% | 2.2x | 186.4M | 5.2% | 0 |  |
| GEV | 2026-11-10 15:44 | other | listed | 774.4 | -6.6% | -3.8% | 1.1x | 264.1M | 2.8% | 0 |  |
| ANT | 2026-11-10 14:52 | unknown | unknown |  |  |  |  |  |  | 3 | yahoo: No data found, symbol may be delisted |
| MSS | 2026-11-09 23:23 | other | listed | 0.996 | +0.0% | -1.4% | 0.9x | 0.4M | 14.0% | 0 |  |
| ASTS | 2026-11-09 22:33 | other | listed | 37.23 | +0.9% | +1.5% | 1.5x | 272.7M | 24.2% | 0 |  |
| IVF | 2026-11-09 22:18 | low float runner | listed | 2.299 | -2.2% | +28.4% | 0.6x | 0.6M | 4.2% | 0 |  |
| ASML | 2026-11-09 22:18 | other | listed | 1,523 | +0.7% | -0.8% | 1.3x | 21.28B | 0.0% | 0 |  |
| RKLB | 2026-11-09 21:25 | other | listed | 55.01 | -6.5% | +13.0% | 1.4x | 556.8M | 8.1% | 2 |  |
| HIMS | 2026-11-09 21:25 | other | listed | 22.46 | -2.1% | -9.1% | 4.4x | 213.8M | 25.0% | 0 |  |
| TTD | 2026-11-09 21:11 | other | listed | 18.86 | +26.3% | +19.0% | 4.3x | 416.6M | 20.0% | 1 |  |
| ONDS | 2026-11-09 20:48 | other | listed | 6.025 | +12.9% | -15.6% | 0.9x | 533.4M | 47.6% | 3 |  |
| OMH | 2026-11-09 20:48 | other | listed | 35.19 | +378.1% | +157.3% | 2.0x | 0.5M | 12.1% | 1 |  |
| AVGO | 2026-11-09 15:56 | other | listed | 318.9 | +8.6% | -9.9% | 1.4x | 4.72B | 1.1% | 1 |  |
| NNN | 2026-11-09 15:04 | other | listed | 41.3 | +0.4% | +0.3% | 1.1x | 181.6M | 3.9% | 0 |  |
| CVS | 2026-11-09 13:52 | other | listed | 84.75 | +1.1% | -7.1% | 1.5x | 1.28B | 1.3% | 0 |  |
| NYT | 2026-11-09 11:01 | other | listed | 68.5 | +0.2% | -2.6% | 1.3x | 132.3M | 14.1% | 0 |  |
| NVDA | 2026-11-09 00:16 | other | listed | 188.7 | +1.1% | -8.8% | 1.6x | 23.13B | 1.3% | 0 |  |
| GME | 2026-11-07 11:05 | other | listed | 24.99 | -0.5% | +3.7% | 0.6x | 460.4M | 10.4% | 0 |  |
