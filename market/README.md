# Stage 2 market snapshots

Updated 2026-11-17T12:33:33Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

479 candidates and 949 controls so far. Archetypes: other 459, low_float_runner 15, unknown 4, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SLS | 2026-11-17 12:33 | other | listed | 8 | +7.1% | -12.9% | 1.0x | 203.1M | 28.1% | 0 |  |
| SHAZ | 2026-11-17 10:45 | other | listed | 19.41 | -3.6% | -15.9% | 2.2x | 19.4M | 23.2% | 10 |  |
| SNDK | 2026-11-17 10:05 | other | listed | 795.9 | -1.6% | -8.7% | 1.0x | 140.4M | 3.5% | 0 |  |
| JPM | 2026-11-17 10:05 | other | listed | 336 | -0.7% | -1.1% | 1.1x | 2.64B | 0.9% | 5870 |  |
| ROPE | 2026-11-17 06:59 | other | listed | 31.25 | +0.0% | +0.1% | 1.0x |  |  |  |  |
| RSP | 2026-11-17 03:38 | other | listed | 219.1 | +0.1% | -0.9% | 1.0x |  |  |  |  |
| ASTS | 2026-11-17 03:28 | other | listed | 28.55 | -0.1% | -22.5% | 1.3x | 273.7M | 24.7% | 0 |  |
| TQQQ | 2026-11-17 01:13 | other | listed | 53.16 | -7.8% | +10.4% | 1.0x |  |  |  |  |
| INTC | 2026-11-17 00:48 | other | listed | 53.34 | -3.8% | -6.6% | 0.7x | 4.87B | 3.1% | 0 |  |
| VOO | 2026-11-17 00:31 | other | listed | 680.8 | +0.1% | -1.7% | 0.9x |  |  |  |  |
| PLTR | 2026-11-16 23:04 | other | listed | 160.5 | +0.1% | -5.2% | 0.7x | 2.12B | 2.6% | 0 |  |
| RCAT | 2026-11-16 22:11 | other | listed | 2.71 | -23.2% | -21.6% | 1.4x | 139.9M | 27.8% | 0 |  |
| LXEO | 2026-11-16 20:09 | other | listed | 3.265 | +13.8% | -0.7% | 0.3x | 49.8M | 34.2% | 1 |  |
| IREN | 2026-11-16 18:57 | other | listed | 16.41 | -9.7% | -16.0% | 1.0x | 416.1M | 22.8% | 0 |  |
| ANT | 2026-11-16 16:34 | unknown | listed |  |  |  |  |  |  | 3 |  |
| HOOD | 2026-11-16 15:08 | other | listed | 74.57 | -4.2% | -3.8% | 1.0x | 786.1M | 4.5% | 0 |  |
| WMT | 2026-11-16 07:17 | other | listed | 127.9 | -0.1% | +2.0% | 0.8x | 4.85B | 1.5% | 4 |  |
| ASML | 2026-11-15 23:05 | other | listed | 1,476 | -1.3% | +4.9% | 0.8x | 21.28B | 0.0% | 0 |  |
| COIN | 2026-11-15 21:05 | other | listed | 126 | -1.3% | -5.3% | 0.9x | 220.7M | 10.3% | 0 |  |
| TSM | 2026-11-15 07:52 | other | listed | 394.5 | -1.1% | +6.2% | 0.7x | 37.84B | 0.1% | 0 |  |
| DXYZ | 2026-11-14 23:53 | other | listed | 26.3 | -0.6% | +8.6% | 1.3x |  |  | 2 |  |
| LHX | 2026-11-14 03:08 | other | listed | 261.9 | -3.8% | +4.8% | 0.5x | 185.2M | 2.3% | 2 |  |
| WMT | 2026-11-14 02:06 | other | listed | 127.9 | -0.1% | +2.0% | 0.8x | 4.85B | 1.5% | 4 |  |
| HSBC | 2026-11-14 01:03 | other | listed | 89.1 | +0.0% | +1.2% | 0.4x | 13.55B | 0.0% | 6 |  |
| DHS | 2026-11-14 00:36 | other | listed | 120.1 | +0.0% | +2.2% | 1.0x |  |  |  |  |
| NWS | 2026-11-13 23:41 | other | listed | 29.89 | +0.0% | +3.2% | 0.8x | 473.0M | 0.7% | 0 |  |
| ATC | 2026-11-13 22:10 | other | listed | 18.72 | +0.0% | -7.5% | 2.3x |  |  |  |  |
| IWM | 2026-11-13 19:02 | other | listed | 277 | -0.5% | +2.8% | 0.9x |  |  |  |  |
| XLAB | 2026-11-13 16:24 | other | listed | 2.08 | -8.4% | +38.4% | 3.3x |  |  | 3 |  |
| TSLA | 2026-11-13 15:04 | other | listed | 390.9 | -1.6% | +15.6% | 0.7x | 2.82B | 2.3% | 0 |  |
