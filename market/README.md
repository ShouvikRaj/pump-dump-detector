# Stage 2 market snapshots

Updated 2026-10-30T13:54:31Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

290 candidates and 577 controls so far. Archetypes: other 277, low_float_runner 11, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TSM | 2026-10-30 13:54 | other | listed | 415.6 | -3.8% | +4.7% | 0.7x | 37.84B | 0.1% | 0 |  |
| SMCI | 2026-10-30 13:42 | other | listed | 32.76 | -4.9% | +2.1% | 0.7x | 557.7M | 14.4% | 0 |  |
| AMD | 2026-10-30 13:25 | other | listed | 512 | -9.6% | +11.5% | 0.8x | 1.62B | 2.3% | 3 |  |
| NVDA | 2026-10-30 11:53 | other | listed | 206.8 | -3.2% | +0.7% | 0.8x | 23.13B | 1.3% | 0 |  |
| ARM | 2026-10-30 11:00 | other | listed | 208.5 | -8.9% | +8.9% | 1.0x | 142.6M | 12.4% | 0 |  |
| BURU | 2026-10-30 10:30 | other | listed | 0.5403 | +45.2% | -9.3% | 192.8x | 8.4M | 18.2% | 2 |  |
| NKE | 2026-10-30 09:12 | other | listed | 38.91 | +1.3% | +0.3% | 0.5x | 1.18B | 8.8% | 0 |  |
| PLTR | 2026-10-30 08:33 | other | listed | 193.7 | -1.4% | +0.1% | 0.9x | 2.11B | 2.7% | 0 |  |
| SCHD | 2026-10-30 05:02 | other | listed | 35.83 | +0.6% | +0.6% | 1.1x |  |  |  |  |
| VOO | 2026-10-30 04:49 | other | listed | 703 | -0.6% | +0.7% | 0.9x |  |  |  |  |
| DJT | 2026-10-30 01:20 | other | listed | 5.67 | -5.0% | -10.4% | 1.8x | 160.9M | 10.9% | 0 |  |
| DELL | 2026-10-30 00:42 | other | listed | 443.2 | -10.3% | +1.6% | 0.6x | 292.1M | 4.2% | 2 |  |
| MSTR | 2026-10-30 00:00 | other | listed | 133.6 | -8.0% | -5.4% | 0.6x | 363.6M | 8.0% | 0 |  |
| AAPL | 2026-10-29 22:53 | other | listed | 350.5 | +0.5% | +0.2% | 1.1x | 14.57B | 0.9% | 0 |  |
| ROPE | 2026-10-29 22:12 | other | listed | 30.96 | +0.0% | +1.2% | 0.5x |  |  |  |  |
| PINS | 2026-10-29 22:12 | other | listed | 18.02 | -9.5% | -13.1% | 3.9x | 484.6M | 9.7% | 0 |  |
| GME | 2026-10-29 21:47 | other | listed | 23.9 | -0.4% | -5.5% | 0.5x | 460.4M | 10.4% | 0 |  |
| CROX | 2026-10-29 21:35 | other | listed | 150.5 | +0.2% | +24.2% | 4.7x | 46.1M | 9.9% | 0 |  |
| NRXP | 2026-10-29 20:56 | other | listed | 2.77 | +4.1% | +10.8% | 1.2x | 37.4M | 26.6% | 0 |  |
| SNDK | 2026-10-29 20:27 | other | listed | 1,355 | +1.9% | +5.5% | 0.8x | 144.5M | 3.3% | 0 |  |
| IWM | 2026-10-29 19:09 | other | listed | 283.3 | +0.7% | +1.7% | 0.8x |  |  |  |  |
| SAP | 2026-10-29 17:49 | other | listed | 233.3 | -1.5% | +1.8% | 0.7x | 14.45B | 0.0% | 0 |  |
| LLY | 2026-10-29 14:09 | other | listed | 1,385 | +7.5% | +1.4% | 0.9x | 889.0M | 0.8% | 0 |  |
| RDDT | 2026-10-29 14:06 | other | listed | 130.3 | -3.3% | -12.1% | 1.3x | 140.7M | 15.4% | 0 |  |
| AMZN | 2026-10-29 14:06 | other | listed | 245.7 | -3.5% | -3.0% | 1.0x | 9.81B | 1.0% | 3 |  |
| DXYZ | 2026-10-29 13:37 | other | listed | 27.21 | -1.6% | -4.7% | 0.8x |  |  | 2 |  |
| INTC | 2026-10-29 11:49 | other | listed | 92.52 | -3.2% | +2.8% | 0.8x | 4.62B | 3.2% | 3 |  |
| ELPW | 2026-10-29 10:54 | low float runner | listed | 2.8 | -6.7% | +30.4% | 956.9x | 0.1M | 39.6% | 4 |  |
| TTWO | 2026-10-29 04:39 | other | listed | 196.3 | +0.5% | -5.3% | 0.9x | 186.1M | 5.2% | 0 |  |
| WEN | 2026-10-29 04:31 | other | listed | 7.05 | -0.3% | +12.6% | 6.6x | 157.1M | 33.3% | 0 |  |
