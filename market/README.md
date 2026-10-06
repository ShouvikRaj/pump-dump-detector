# Stage 2 market snapshots

Updated 2026-10-06T15:49:26Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

25 candidates and 50 controls so far. Archetypes: other 23, low_float_runner 2.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NOK | 2026-10-06 15:49 | other | listed | 10.78 | +5.6% | +0.8% | 0.5x | 4.45B | 1.2% | 0 |  |
| AMD | 2026-10-06 14:55 | other | listed | 651.8 | +3.2% | +3.9% | 0.6x | 1.62B | 2.5% | 3 |  |
| NVDA | 2026-10-06 14:02 | other | listed | 242.3 | +1.4% | +4.4% | 1.2x | 23.13B | 1.3% | 0 |  |
| MRNA | 2026-10-06 14:02 | other | listed | 198 | -2.6% | +3.0% | 1.3x | 372.2M | 8.8% | 0 |  |
| NVAX | 2026-10-06 13:49 | other | listed | 13.19 | +5.0% | +16.3% | 5.5x | 142.6M | 35.0% | 0 |  |
| CRWV | 2026-10-06 13:49 | other | listed | 89.86 | +2.8% | +2.7% | 0.6x | 328.3M | 16.7% | 1 |  |
| MRVL | 2026-10-06 13:36 | other | listed | 286.3 | +5.5% | +7.7% | 0.7x | 873.9M | 3.6% | 1 |  |
| CEG | 2026-10-06 13:36 | other | listed | 302.2 | +12.9% | +2.8% | 1.2x | 353.1M | 3.3% | 0 |  |
| QQQ | 2026-10-06 11:49 | other | listed | 760.4 | +0.6% | +2.7% | 0.8x |  |  |  |  |
| MSTR | 2026-10-06 08:17 | other | listed | 164.6 | +0.1% | +4.6% | 0.8x | 363.6M | 8.5% | 0 |  |
| IWM | 2026-10-06 00:59 | other | listed | 283.1 | +0.6% | -0.2% | 1.3x |  |  |  |  |
| ALEC | 2026-10-05 23:41 | other | listed | 1.96 | -1.5% | +3.6% | 64.9x | 84.9M | 7.2% | 0 |  |
| QCOM | 2026-10-05 21:14 | other | listed | 181.4 | +0.4% | -3.6% | 0.8x | 1.05B | 3.7% | 2 |  |
| MSFT | 2026-10-05 21:14 | other | listed | 525 | -0.0% | +3.1% | 1.2x | 7.41B | 0.9% | 0 |  |
| IREN | 2026-10-05 17:49 | other | listed | 40.24 | -3.6% | -5.4% | 1.2x | 346.2M | 24.0% | 1 |  |
| DELL | 2026-10-05 16:38 | other | listed | 554.8 | -1.4% | -0.1% | 0.6x | 292.2M | 4.7% | 2 |  |
| GME | 2026-10-05 16:24 | other | listed | 25.55 | +3.4% | +5.6% | 1.3x | 461.2M | 8.5% | 0 |  |
| VEEA | 2026-10-05 15:33 | low float runner | listed | 5.06 | +52.0% | +8.1% | 0.1x | 1.5M | 80.0% | 1 |  |
| TSM | 2026-10-05 15:18 | other | listed | 483.2 | +2.2% | +4.9% | 1.0x | 37.84B | 0.1% | 0 |  |
| SPCX | 2026-10-05 14:51 | other | listed | 166.9 | +5.0% | +6.9% | 1.3x | 4.34B | 3.7% | 0 |  |
| APLD | 2026-10-05 14:23 | other | listed | 24.68 | -2.8% | -3.3% | 1.7x | 250.7M | 23.1% | 0 |  |
| SDEV | 2026-10-05 14:09 | other | listed | 6.85 | -8.4% | +402.0% | 8.0x | 22.6M | 5.4% | 2 |  |
| PMI | 2026-10-05 13:55 | low float runner | listed | 6.16 | +6.6% | +25.1% | 4.2x | 1.3M | 18.1% | 0 |  |
| VST | 2026-10-05 04:15 | other | listed | 144 | +2.8% | +1.1% | 2.6x | 312.9M | 3.1% | 3 |  |
| DRTS | 2026-10-04 23:23 | other | listed | 14.51 | -1.7% | +1.6% | 0.6x | 64.1M | 5.4% | 0 |  |
