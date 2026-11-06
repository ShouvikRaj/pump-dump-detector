# Stage 2 market snapshots

Updated 2026-11-06T02:44:34Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

385 candidates and 765 controls so far. Archetypes: other 370, low_float_runner 12, unknown 2, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| GEV | 2026-11-05 00:45 | other | listed | 828 | -0.6% | -5.1% | 2.0x | 264.1M | 2.8% | 0 |  |
| BROS | 2026-11-04 22:27 | other | listed | 35.97 | -18.2% | +2.5% | 2.2x | 130.3M | 15.5% | 1 |  |
| COHR | 2026-11-04 21:19 | other | listed | 197.9 | +1.4% | -18.6% | 1.4x | 195.0M | 4.6% | 0 |  |
| APP | 2026-11-04 21:19 | other | listed | 315.1 | +16.0% | +4.5% | 2.7x | 265.4M | 4.2% | 0 |  |
| UUUU | 2026-11-04 21:07 | other | listed | 7.27 | +0.8% | -14.1% | 1.0x | 248.2M | 23.4% | 1 |  |
| ARM | 2026-11-04 20:01 | other | listed | 191.2 | -5.6% | -10.6% | 0.7x | 142.6M | 12.4% | 0 |  |
| MU | 2026-11-04 19:48 | other | listed | 801.9 | -6.2% | -7.9% | 0.8x | 1.13B | 2.0% | 0 |  |
