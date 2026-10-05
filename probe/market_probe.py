"""Temporary probe (Stage 2 design), round 2: request shapes for the chosen sources.

Prints status codes and small samples only. Removed once Stage 2's sources are chosen.
"""
import json
import time

import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/128.0.0.0 Safari/537.36")
H = {"User-Agent": UA, "Accept": "application/json"}


def section(name):
    print("\n" + "=" * 20 + " " + name + " " + "=" * 20, flush=True)


def finra(label, body):
    try:
        r = requests.post("https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest", json=body, headers=H, timeout=60)
        print(f"\n### {label}: status={r.status_code} len={len(r.text)}\n{r.text[:1500]}")
    except Exception as exc:
        print(f"\n### {label}: ERROR {exc}")


section("FINRA short interest")
finra("symbol + date range", {"limit": 20, "compareFilters": [{"compareType": "equal", "fieldName": "symbolCode", "fieldValue": "DRTS"}],
                              "dateRangeFilters": [{"fieldName": "settlementDate", "startDate": "2026-07-01", "endDate": "2026-10-05"}]})
finra("settlement equal + domain", {"limit": 20, "compareFilters": [{"compareType": "equal", "fieldName": "settlementDate", "fieldValue": "2026-09-15"}],
                                    "domainFilters": [{"fieldName": "symbolCode", "values": ["DRTS", "BLGO", "FNMA", "AABB"]}]})
finra("symbol only", {"limit": 5, "compareFilters": [{"compareType": "equal", "fieldName": "symbolCode", "fieldValue": "BLGO"}]})
r = requests.get("https://api.finra.org/metadata/group/otcMarket/name/consolidatedShortInterest", headers=H, timeout=60)
try:
    print("fields:", [(f["name"], f["type"]) for f in r.json()["fields"]])
except Exception as exc:
    print("metadata", r.status_code, exc, r.text[:300])

section("Nasdaq screener")
nh = {"User-Agent": UA, "Accept": "application/json, text/plain, */*", "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}
r = requests.get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&download=true", headers=nh, timeout=60)
j = r.json()
rows = j["data"]["rows"]
print("status", r.status_code, "rows", len(rows), "asOf", j["data"].get("asOf"), "keys", list(j["data"].keys()))
print([x for x in rows if x["symbol"] in ("DRTS", "VST", "GME")])
print("sample", rows[:2])
r = requests.get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=3&offset=0", headers=nh, timeout=60)
print("limit3 asof:", r.json()["data"].get("asof"))

section("Yahoo chart shapes")
now = int(time.time())
for sym, params in [
    ("DRTS", {"period1": now - 30 * 86400, "period2": now - 25 * 86400, "interval": "5m", "includePrePost": "true"}),
    ("UURAF", {"range": "10y", "interval": "1d", "events": "div,splits"}),
    ("ZZZZZQ", {"range": "1mo", "interval": "1d"}),
    ("BRK-B", {"range": "5d", "interval": "1d"}),
    ("AABB", {"range": "5d", "interval": "1d"}),
]:
    r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}", params=params, headers=H, timeout=30)
    print(f"\n### chart {sym} {params}: status={r.status_code} len={len(r.text)}")
    try:
        res = r.json()["chart"]
        if res.get("error"):
            print("error:", res["error"])
        else:
            x = res["result"][0]
            ts = x.get("timestamp") or []
            print("meta keys:", sorted(x["meta"].keys()))
            print("n bars:", len(ts), "first:", ts[:2], "last:", ts[-2:], "events:", json.dumps(x.get("events"))[:600])
            q = x["indicators"]["quote"][0]
            print("quote keys:", list(q.keys()), "adjclose:", "adjclose" in x["indicators"])
            print("tradingPeriods:", json.dumps(x["meta"].get("tradingPeriods"))[:300])
    except Exception as exc:
        print("parse error", exc, r.text[:300])
    time.sleep(0.5)

section("Yahoo quoteSummary modules")
s = requests.Session()
s.headers["User-Agent"] = UA
s.get("https://fc.yahoo.com", timeout=30)
crumb = s.get("https://query2.finance.yahoo.com/v1/test/getcrumb", timeout=30).text.strip()
for sym in ["DRTS", "AABB", "ZZZZZQ"]:
    r = s.get(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{sym}",
              params={"modules": "price,summaryDetail,defaultKeyStatistics,summaryProfile", "crumb": crumb}, timeout=30)
    print(f"\n### quoteSummary {sym}: status={r.status_code} len={len(r.text)}")
    try:
        j = r.json()["quoteSummary"]
        if j.get("error"):
            print("error:", j["error"])
        else:
            res = j["result"][0]
            for mod, val in res.items():
                print(mod, json.dumps(val)[:1200])
    except Exception as exc:
        print("parse error", exc, r.text[:300])
print("\nPROBE DONE")
