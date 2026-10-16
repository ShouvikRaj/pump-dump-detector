# Stage 2 market snapshots

Updated 2026-10-16T18:28:18Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

131 candidates and 262 controls so far. Archetypes: other 124, low_float_runner 7.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QQQ | 2026-10-16 18:27 | other | listed | 710.8 | -2.4% | -2.6% | 1.4x |  |  |  |  |
| IBKR | 2026-10-16 13:35 | other | listed | 84.83 | -1.4% | -0.5% | 1.5x | 439.2M | 3.1% | 3 |  |
| RCS | 2026-10-16 12:29 | other | listed | 5 | +1.0% | -1.8% | 0.9x |  |  | 0 |  |
| USO | 2026-10-16 11:23 | other | listed | 156.9 | -0.3% | +6.6% | 0.8x |  |  | 0 |  |
| TSLA | 2026-10-16 07:11 | other | listed | 362.3 | -0.0% | -3.3% | 0.8x | 2.82B | 2.5% | 0 |  |
| DRMA | 2026-10-15 23:28 | other | listed | 0.9 | -1.1% | -15.0% | 4315.7x | 2.9M | 2.9% | 1 |  |
| BETR | 2026-10-15 23:28 | other | listed | 10.8 | +0.4% | +6.0% | 4.3x | 8.5M | 44.1% | 0 |  |
| WETO | 2026-10-15 21:16 | low float runner | listed | 1.23 | +0.8% | +13.0% | 16.8x | 0.2M | 1159.2% | 2 |  |
| SOXS | 2026-10-15 15:04 | other | listed | 45.26 | +6.4% | +38.7% | 1.2x |  |  |  |  |
| PFE | 2026-10-14 20:17 | other | listed | 29.17 | -0.1% | +4.3% | 1.2x | 5.69B | 2.6% | 0 |  |
| HOOD | 2026-10-14 20:04 | other | listed | 101.1 | +0.0% | -7.7% | 1.1x | 784.4M | 5.1% | 0 |  |
| TSM | 2026-10-14 19:51 | other | listed | 430.8 | -3.2% | -7.7% | 0.9x | 37.84B | 0.1% | 0 |  |
| WMT | 2026-10-14 19:24 | other | listed | 115.7 | +3.1% | +4.7% | 0.8x | 4.85B | 1.7% | 0 |  |
| RKLB | 2026-10-14 19:24 | other | listed | 59.41 | -7.5% | -14.4% | 0.7x | 556.9M | 8.0% | 2 |  |
| LQDA | 2026-10-14 19:11 | other | listed | 33.93 | +26.6% | +3.5% | 0.8x | 65.3M | 19.3% | 0 |  |
| TLT | 2026-10-14 18:31 | other | listed | 78.93 | +0.7% | +1.4% | 0.6x |  |  |  |  |
| SOFI | 2026-10-14 18:18 | other | listed | 14.01 | -8.1% | -3.3% | 0.6x | 1.27B | 16.9% | 0 |  |
| VOO | 2026-10-14 17:34 | other | listed | 706.2 | -1.3% | -0.1% | 0.6x |  |  |  |  |
| ORCL | 2026-10-14 16:58 | other | listed | 133.1 | -7.1% | -1.1% | 0.9x | 1.86B | 2.6% | 0 |  |
| ARM | 2026-10-14 15:25 | other | listed | 243.1 | -4.8% | -15.6% | 1.2x | 142.6M | 11.4% | 0 |  |
| TCRT | 2026-10-14 13:12 | low float runner | listed | 3.842 | +26.8% | +309.5% | 93.8x | 1.9M | 0.5% | 1 |  |
| UPST | 2026-10-14 12:46 | other | listed | 23.28 | -2.3% | -0.1% | 0.7x | 83.7M | 34.1% | 0 |  |
| GLND | 2026-10-14 12:29 | other | listed | 4.09 | +85.1% | -26.3% | 0.1x |  |  | 0 |  |
| CLF | 2026-10-14 11:39 | other | listed | 12.94 | +0.6% | +5.0% | 0.9x | 564.4M | 13.9% | 0 |  |
| BBAI | 2026-10-14 05:42 | other | listed | 2.44 | +2.1% | -7.4% | 2.3x | 475.4M | 29.6% | 1 |  |
| RSP | 2026-10-14 00:41 | other | listed | 213.4 | +0.1% | +1.0% | 0.6x |  |  |  |  |
| SOXL | 2026-10-13 22:51 | other | listed | 129.4 | +1.4% | -22.3% | 1.3x |  |  |  |  |
| BAC | 2026-10-13 20:37 | other | listed | 53 | -1.8% | -0.2% | 1.1x | 6.97B | 1.2% | 2673 |  |
| AAOI | 2026-10-13 20:10 | other | listed | 99 | +1.2% | -24.9% | 1.1x | 80.9M | 17.2% | 1 |  |
| JBDI | 2026-10-13 18:51 | low float runner | listed | 3.677 | +267.7% | +0.0% | 0.0x | 5.0M | 0.7% | 0 |  |
