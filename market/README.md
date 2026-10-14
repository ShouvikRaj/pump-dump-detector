# Stage 2 market snapshots

Updated 2026-10-14T12:46:31Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

110 candidates and 220 controls so far. Archetypes: other 105, low_float_runner 5.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UPST | 2026-10-14 12:46 | other | listed | 23.28 | -2.3% | -0.1% | 0.7x | 83.7M | 34.1% | 0 |  |
| GLND | 2026-10-14 12:29 | other | listed | 4.09 | +85.1% | -26.3% | 0.1x |  |  | 0 |  |
| CLF | 2026-10-14 11:39 | other | listed | 12.94 | +0.6% | +5.0% | 0.9x | 564.4M | 13.9% | 0 |  |
| BBAI | 2026-10-14 05:42 | other | listed | 2.44 | +2.1% | -7.4% | 2.3x | 475.4M | 29.6% | 1 |  |
| RSP | 2026-10-14 00:41 | other | listed | 213.4 | +0.1% | +1.0% | 0.6x |  |  |  |  |
| SOXL | 2026-10-13 22:51 | other | listed | 129.4 | +1.4% | -22.3% | 1.3x |  |  |  |  |
| BAC | 2026-10-13 20:37 | other | listed | 53 | -1.8% | -0.2% | 1.1x | 6.97B | 1.2% | 2673 |  |
| AAOI | 2026-10-13 20:10 | other | listed | 99 | +1.2% | -24.9% | 1.1x | 80.9M | 17.2% | 1 |  |
| JBDI | 2026-10-13 18:51 | low float runner | listed | 3.677 | +267.7% | +0.0% | 0.0x | 5.0M | 0.7% | 0 |  |
| TTWO | 2026-10-13 18:32 | other | listed | 199.2 | -4.6% | +2.6% | 0.8x | 186.1M | 5.0% | 0 |  |
| CLGN | 2026-10-13 16:38 | low float runner | listed | 4.05 | +0.7% | +17.9% | 2.4x | 0.9M | 4.9% | 1 |  |
| GME | 2026-10-13 14:38 | other | listed | 26.95 | -1.0% | +7.9% | 0.9x | 461.2M | 9.3% | 0 |  |
| MSFT | 2026-10-13 13:59 | other | listed | 550.2 | +1.7% | +3.0% | 0.8x | 7.41B | 0.8% | 0 |  |
| AMC | 2026-10-13 13:59 | other | listed | 3.135 | +4.5% | +7.5% | 0.5x | 835.3M | 5.9% | 0 |  |
| USAR | 2026-10-13 13:32 | other | listed | 11.6 | -1.9% | -13.4% | 1.0x | 148.9M | 30.3% | 3 |  |
| OKLO | 2026-10-13 13:32 | other | listed | 31.49 | -2.2% | -10.5% | 1.0x | 157.9M | 20.8% | 1 |  |
| JPM | 2026-10-13 10:39 | other | listed | 324.9 | -2.8% | +0.6% | 0.7x | 2.64B | 0.9% | 5893 |  |
| SXTC | 2026-10-13 08:00 | other | listed | 0.0917 | -10.1% | -95.1% | 4.6x | 0.4M | 16.3% | 3 |  |
| CRWV | 2026-10-13 03:58 | other | listed | 79.19 | -1.3% | -8.2% | 0.6x | 328.3M | 18.3% | 1 |  |
| NBIS | 2026-10-13 03:35 | other | listed | 207.3 | -1.3% | -9.7% | 0.9x | 228.7M | 19.5% | 0 |  |
| SKHY | 2026-10-13 02:56 | other | listed | 160.3 | -1.2% | -16.8% | 0.8x | 5.67B | 0.7% | 0 |  |
| SNDK | 2026-10-13 01:10 | other | listed | 1,454 | -8.1% | -8.0% | 0.6x | 144.5M | 3.3% | 0 |  |
| NIO | 2026-10-12 22:44 | other | listed | 3.47 | +0.0% | +1.5% | 0.9x | 1.90B | 6.9% | 0 |  |
| SOFI | 2026-10-12 21:51 | other | listed | 15.25 | +0.1% | -4.3% | 0.9x | 1.27B | 16.9% | 0 |  |
| META | 2026-10-12 20:58 | other | listed | 742.4 | -0.1% | +0.1% | 1.1x | 2.20B | 1.5% | 0 |  |
| BMBL | 2026-10-12 20:58 | other | listed | 3.82 | +0.5% | +49.0% | 18.5x | 109.3M | 13.4% | 0 |  |
| UNH | 2026-10-12 20:32 | other | listed | 379.5 | +0.3% | -0.0% | 1.2x | 895.0M | 1.8% | 0 |  |
| RDDT | 2026-10-12 20:18 | other | listed | 156 | -2.5% | +6.3% | 1.0x | 140.7M | 15.7% | 0 |  |
| WFF | 2026-10-12 18:19 | other | listed | 27.94 | +127.3% | +411.0% | 372.0x | 38.5M | 0.2% | 1 |  |
| ASML | 2026-10-12 17:40 | other | listed | 1,761 | -1.1% | -4.7% | 0.8x | 21.33B | 0.0% | 0 |  |
