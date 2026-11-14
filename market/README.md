# Stage 2 market snapshots

Updated 2026-11-14T01:03:35Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

456 candidates and 905 controls so far. Archetypes: other 437, low_float_runner 15, unknown 3, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HSBC | 2026-11-14 01:03 | other | listed | 89.1 | +0.0% | +1.2% | 0.4x | 13.55B | 0.0% | 6 |  |
| DHS | 2026-11-14 00:36 | other | listed | 120.1 | +0.0% | +2.2% | 1.0x |  |  |  |  |
| NWS | 2026-11-13 23:41 | other | listed | 29.89 | +0.0% | +3.2% | 0.8x | 473.0M | 0.7% | 0 |  |
| ATC | 2026-11-13 22:10 | other | listed | 18.72 | +0.0% | -7.5% | 2.3x |  |  |  |  |
| IWM | 2026-11-13 19:02 | other | listed | 277 | -0.5% | +2.8% | 0.9x |  |  |  |  |
| XLAB | 2026-11-13 16:24 | other | listed | 2.08 | -8.4% | +38.4% | 3.3x |  |  | 3 |  |
| TSLA | 2026-11-13 15:04 | other | listed | 390.9 | -1.6% | +15.6% | 0.7x | 2.82B | 2.3% | 0 |  |
| SMU | 2026-11-13 14:07 | other | listed | 5.24 | +2.3% | +16.4% | 0.2x |  |  |  |  |
| AIMD | 2026-11-13 13:30 | other | listed | 0.9135 | -13.8% | +68.8% | 1371.7x | 2.4M | 1.6% | 0 |  |
| ARM | 2026-11-13 13:15 | other | listed | 200.3 | +0.2% | +19.8% | 0.7x | 144.5M | 10.9% | 0 |  |
| CRWD | 2026-11-13 10:58 | other | listed | 236 | +2.7% | +5.8% | 0.6x | 1.01B | 2.2% | 1 |  |
| MSTR | 2026-11-13 06:20 | other | listed | 114 | -0.4% | -11.5% | 1.1x | 401.8M | 6.7% | 5 |  |
| SLS | 2026-11-13 01:09 | other | listed | 9.646 | +14.6% | -7.9% | 0.5x | 201.1M | 28.4% | 0 |  |
| NFLX | 2026-11-13 00:27 | other | listed | 62.86 | +0.3% | -4.4% | 0.7x | 4.08B | 2.2% | 0 |  |
| IBM | 2026-11-13 00:27 | other | listed | 245 | +0.2% | -1.0% | 0.5x | 943.2M | 1.9% | 1 |  |
| CSCO | 2026-11-12 21:20 | other | listed | 104.4 | +2.4% | +6.6% | 1.2x | 3.94B | 1.5% | 0 |  |
| MSFT | 2026-11-12 20:54 | other | listed | 522.5 | +0.3% | -6.2% | 1.1x | 7.42B | 0.8% | 2 |  |
| ASML | 2026-11-12 20:43 | other | listed | 1,493 | -2.7% | +2.5% | 0.8x | 21.28B | 0.0% | 0 |  |
| AMAT | 2026-11-12 18:42 | other | listed | 392.4 | -0.7% | +7.0% | 0.9x | 790.5M | 1.8% | 0 |  |
| GLD | 2026-11-12 18:15 | other | listed | 355.5 | -2.6% | -2.0% | 0.6x |  |  | 0 |  |
| SMCI | 2026-11-12 17:47 | other | listed | 26.97 | -11.4% | +2.8% | 1.0x | 560.0M | 13.4% | 0 |  |
| TRT | 2026-11-12 17:34 | low float runner | listed | 5.82 | +10.6% | +6.0% | 0.9x | 7.8M | 9.2% | 0 |  |
| PARA | 2026-11-12 17:04 | other | listed | 0.1135 | +57.6% | -77.4% | 3.2x | 0.3M | 15.4% | 5 |  |
| CBRS | 2026-11-12 16:56 | other | listed | 101.6 | +0.5% | +10.0% | 0.9x | 109.9M | 20.2% | 0 |  |
| PLCE | 2026-11-12 16:04 | other | listed | 0.8535 | +326.8% | -16.7% | 9.4x | 8.1M | 44.3% | 0 |  |
| LUNR | 2026-11-12 14:43 | other | listed | 13.96 | +14.6% | +22.7% | 1.2x | 131.6M | 27.5% | 0 |  |
| SLI | 2026-11-12 05:40 | other | listed | 1.49 | +2.1% | +1.4% | 0.5x | 239.2M | 2.5% | 0 |  |
| AMD | 2026-11-12 05:14 | other | listed | 576.8 | +4.3% | +13.1% | 1.4x | 1.63B | 2.4% | 1 |  |
| NXXT | 2026-11-12 03:27 | low float runner | listed | 2.05 | +20.6% | -33.1% | 191.7x | 0.8M | 5.9% | 2 |  |
| GME | 2026-11-12 01:54 | other | listed | 25 | -1.7% | +4.8% | 0.5x | 460.4M | 9.2% | 0 |  |
