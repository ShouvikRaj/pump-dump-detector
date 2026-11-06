# Stage 2 market snapshots

Updated 2026-11-06T15:46:32Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

392 candidates and 779 controls so far. Archetypes: other 377, low_float_runner 12, unknown 2, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| APLD | 2026-11-05 17:29 | other | listed | 14.02 | -15.6% | -18.5% | 1.2x | 261.2M | 25.1% | 0 |  |
| DNUT | 2026-11-05 16:25 | other | listed | 4.635 | +31.7% | +15.4% | 1.5x | 91.6M | 20.5% | 0 |  |
| CRWD | 2026-11-05 16:25 | other | listed | 220.3 | -8.6% | -9.6% | 1.0x | 1.01B | 2.4% | 1 |  |
| NVDA | 2026-11-05 15:05 | other | listed | 189.2 | -5.5% | -7.1% | 1.5x | 23.13B | 1.3% | 0 |  |
| OKLO | 2026-11-05 13:17 | other | listed | 21.5 | -2.8% | -18.4% | 1.4x | 157.4M | 22.8% | 1 |  |
| WMT | 2026-11-05 09:54 | other | listed | 129.7 | +0.4% | +8.8% | 1.4x | 4.85B | 1.6% | 4 |  |
| IBKR | 2026-11-05 08:22 | other | listed | 78.05 | +0.2% | -6.8% | 1.6x | 438.4M | 3.0% | 0 |  |
| TTWO | 2026-11-05 07:30 | other | listed | 209.6 | +0.3% | +7.0% | 1.8x | 186.1M | 5.2% | 0 |  |
| SOXS | 2026-11-05 04:50 | other | listed | 60.9 | +4.4% | +46.7% | 1.4x |  |  |  |  |
| SOXL | 2026-11-05 03:15 | other | listed | 64.01 | -4.0% | -37.9% | 2.3x |  |  |  |  |
| SOXX | 2026-11-05 01:08 | other | listed | 445 | -4.3% | -9.0% | 1.4x |  |  |  |  |
