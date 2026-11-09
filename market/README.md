# Stage 2 market snapshots

Updated 2026-11-09T13:52:28Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

403 candidates and 801 controls so far. Archetypes: other 388, low_float_runner 12, unknown 2, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CVS | 2026-11-09 13:52 | other | listed | 84.75 | +1.1% | -7.1% | 1.5x | 1.28B | 1.3% | 0 |  |
| NYT | 2026-11-09 11:01 | other | listed | 68.5 | +0.2% | -2.6% | 1.3x | 132.3M | 14.1% | 0 |  |
| NVDA | 2026-11-09 00:16 | other | listed | 188.7 | +1.1% | -8.8% | 1.6x | 23.13B | 1.3% | 0 |  |
| GME | 2026-11-07 11:05 | other | listed | 24.99 | -0.5% | +3.7% | 0.6x | 460.4M | 10.4% | 0 |  |
| RKLB | 2026-11-07 03:40 | other | listed | 53.57 | +0.9% | -3.0% | 1.1x | 556.8M | 8.1% | 2 |  |
| SPCE | 2026-11-07 02:18 | other | listed | 2.75 | +15.6% | -12.8% | 1.3x | 150.9M | 25.9% | 0 |  |
| LUNR | 2026-11-06 20:47 | other | listed | 10.43 | +20.9% | -26.2% | 1.8x | 131.6M | 28.9% | 0 |  |
| VIVK | 2026-11-06 18:22 | other | listed | 0.5063 | +36.8% | -75.3% | 0.4x | 0.5M | 21.8% | 0 |  |
| ORCL | 2026-11-06 18:13 | other | listed | 113.8 | -1.1% | -17.5% | 1.4x | 1.86B | 2.6% | 5 |  |
| GRND | 2026-11-06 18:01 | other | listed | 13.5 | -1.0% | +5.7% | 1.8x | 45.0M | 18.5% | 0 |  |
| WDC | 2026-11-06 16:54 | other | listed | 262.2 | -2.0% | -32.3% | 2.1x | 371.9M | 5.2% | 0 |  |
| INOD | 2026-11-06 15:46 | other | listed | 35.75 | -7.4% | -16.4% | 2.1x | 33.1M | 13.7% | 0 |  |
| DKNG | 2026-11-06 14:52 | other | listed | 17.13 | -27.2% | +13.5% | 2.0x | 425.5M | 9.3% | 0 |  |
| KORU | 2026-11-06 09:05 | other | listed | 7.181 | +10.0% | -48.7% | 3.5x |  |  |  |  |
| TQQQ | 2026-11-06 07:56 | other | listed | 51.1 | +1.3% | -27.1% | 3.5x |  |  |  |  |
| ASTS | 2026-11-06 07:56 | other | listed | 30.84 | +2.1% | -29.9% | 1.8x | 272.7M | 24.2% | 0 |  |
| LABT | 2026-11-06 04:28 | other | listed | 0.5099 | -5.6% | +125.0% | 185.7x | 0.8M | 10.6% | 2 |  |
| UVXY | 2026-11-06 03:36 | other | listed | 23.06 | -2.3% | +41.0% | 3.5x |  |  | 0 |  |
| QQQ | 2026-11-06 02:44 | other | listed | 651.2 | +0.6% | -9.5% | 3.0x |  |  |  |  |
| SPY | 2026-11-06 00:59 | other | listed | 734.4 | +0.2% | -4.7% | 3.0x |  |  | 0 |  |
| EWY | 2026-11-06 00:59 | other | listed | 133 | +1.0% | -18.6% | 2.6x |  |  |  |  |
| SGOV | 2026-11-05 23:26 | other | listed | 100.5 | +0.0% | -0.3% | 1.8x |  |  |  |  |
| VTI | 2026-11-05 23:10 | other | listed | 359 | -0.4% | -4.7% | 3.3x |  |  |  |  |
| IONQ | 2026-11-05 22:33 | other | listed | 27.23 | +3.0% | -16.7% | 1.6x | 378.4M | 12.7% | 2 |  |
| ABNB | 2026-11-05 22:33 | other | listed | 186.5 | +9.6% | +2.2% | 2.6x | 405.8M | 3.6% | 0 |  |
| VOO | 2026-11-05 22:19 | other | listed | 671.9 | -0.3% | -4.7% | 3.2x |  |  |  |  |
| ANT | 2026-11-05 22:06 | unknown | unknown |  |  |  |  |  |  | 2 | yahoo: No data found, symbol may be delisted |
| SNDK | 2026-11-05 21:12 | other | listed | 810.7 | +0.5% | -39.4% | 3.2x | 140.4M | 3.4% | 0 |  |
| ROPE | 2026-11-05 20:49 | other | listed | 31 | -2.0% | +3.8% | 0.7x |  |  |  |  |
| SQQQ | 2026-11-05 19:19 | other | listed | 48.29 | +16.2% | +14.6% | 1.5x |  |  |  |  |
