# Stage 2 market snapshots

Updated 2026-10-13T08:00:56Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

93 candidates and 186 controls so far. Archetypes: other 90, low_float_runner 3.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| SMCI | 2026-10-12 17:00 | other | listed | 39.24 | -6.3% | -4.2% | 0.7x | 557.7M | 15.7% | 0 |  |
| TSM | 2026-10-12 15:13 | other | listed | 447.5 | -1.3% | -4.1% | 0.9x | 37.84B | 0.1% | 0 |  |
| ONDS | 2026-10-12 14:47 | other | listed | 6.76 | +0.4% | -7.0% | 0.6x | 533.4M | 42.8% | 5 |  |
| SOXX | 2026-10-12 14:20 | other | listed | 546.6 | -2.3% | -5.0% | 0.8x |  |  |  |  |
| MU | 2026-10-12 14:20 | other | listed | 984.9 | -4.3% | -4.3% | 0.8x | 1.13B | 2.3% | 0 |  |
| CBRS | 2026-10-12 14:20 | other | listed | 150.7 | -8.2% | -1.4% | 0.9x | 109.9M | 12.8% | 0 |  |
| MGM | 2026-10-12 06:49 | other | listed | 29.36 | +0.3% | -4.0% | 1.0x | 181.0M | 10.5% | 0 |  |
| IREN | 2026-10-12 03:44 | other | listed | 35.21 | +0.0% | -15.7% | 1.0x | 346.2M | 23.6% | 1 |  |
| UNH | 2026-10-09 13:59 | other | listed | 381.6 | +2.9% | +1.6% | 1.5x | 895.0M | 1.5% | 0 |  |
| SLS | 2026-10-09 13:19 | other | listed | 11.4 | +1.2% | -0.6% | 0.7x | 201.1M | 29.4% | 0 |  |
| DAL | 2026-10-09 12:52 | other | listed | 80.14 | -2.4% | -2.4% | 1.2x | 649.7M | 4.0% | 0 |  |
| TSM | 2026-10-09 12:39 | other | listed | 465.4 | +1.6% | -0.3% | 1.4x | 37.84B | 0.1% | 0 |  |
| HUM | 2026-10-09 12:39 | other | listed | 449 | +16.0% | +2.0% | 2.2x | 119.8M | 2.4% | 0 |  |
| ONDS | 2026-10-09 01:49 | other | listed | 6.874 | +0.4% | -3.8% | 1.0x | 533.4M | 44.5% | 5 |  |
| IBM | 2026-10-09 01:09 | other | listed | 225.5 | +2.3% | +0.3% | 0.6x | 940.2M | 2.4% | 2 |  |
| SOXL | 2026-10-09 00:30 | other | listed | 142.2 | -10.5% | +7.5% | 0.9x |  |  |  |  |
| MCD | 2026-10-09 00:16 | other | listed | 236.9 | +2.6% | -0.0% | 0.7x | 706.6M | 1.7% | 0 |  |
