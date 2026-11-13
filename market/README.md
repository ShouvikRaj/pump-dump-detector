# Stage 2 market snapshots

Updated 2026-11-13T00:27:37Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

443 candidates and 879 controls so far. Archetypes: other 424, low_float_runner 15, unknown 3, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
