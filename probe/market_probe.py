"""Temporary probe (Stage 2 design): which free market-data endpoints answer from GitHub Actions.

Prints status codes and small samples only. Removed once Stage 2's sources are chosen.
"""
import json
import os
import time
import traceback

import requests

UA_BROWSER = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/128.0.0.0 Safari/537.36")
SEC_UA = os.environ.get("SEC_USER_AGENT", "")


def show(label, resp, n=600):
    body = resp.text if hasattr(resp, "text") else str(resp)
    print(f"\n### {label}\nstatus={resp.status_code} type={resp.headers.get('content-type')} len={len(body)}")
    print(body[:n].replace("\n", "\\n"))


def get(label, url, headers=None, n=600, session=None, **kw):
    try:
        t = time.time()
        r = (session or requests).get(url, headers=headers or {"User-Agent": UA_BROWSER}, timeout=30, **kw)
        show(f"{label} ({time.time() - t:.1f}s) {url}", r, n)
        return r
    except Exception as exc:
        print(f"\n### {label} {url}\nERROR {type(exc).__name__}: {exc}")
        return None


def section(name):
    print("\n" + "=" * 20 + " " + name + " " + "=" * 20)


section("yahoo chart (requests)")
for sym in ["DRTS", "FNMA", "BLGO"]:
    get(f"chart {sym}", f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=1mo&interval=1d&events=div%2Csplits", n=900)
get("chart DRTS 5m", "https://query2.finance.yahoo.com/v8/finance/chart/DRTS?range=5d&interval=5m&includePrePost=true", n=400)

section("yahoo quoteSummary with crumb (requests)")
try:
    s = requests.Session()
    s.headers["User-Agent"] = UA_BROWSER
    r0 = s.get("https://fc.yahoo.com", timeout=30, allow_redirects=True)
    print("fc.yahoo.com", r0.status_code, "cookies:", list(s.cookies.keys()))
    rc = s.get("https://query2.finance.yahoo.com/v1/test/getcrumb", timeout=30)
    print("getcrumb", rc.status_code, rc.text[:80])
    crumb = rc.text.strip()
    mods = "defaultKeyStatistics,summaryDetail,price,assetProfile"
    for sym in ["DRTS", "BLGO"]:
        get(f"quoteSummary {sym}", f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{sym}?modules={mods}&crumb={crumb}",
            session=s, headers={"User-Agent": UA_BROWSER}, n=2500)
except Exception:
    traceback.print_exc()

section("yfinance")
try:
    import yfinance as yf
    print("yfinance", yf.__version__)
    keys = ["exchange", "quoteType", "marketCap", "sharesOutstanding", "impliedSharesOutstanding", "floatShares",
            "sharesShort", "sharesShortPriorMonth", "shortRatio", "shortPercentOfFloat", "dateShortInterest",
            "sharesPercentSharesOut", "heldPercentInsiders", "heldPercentInstitutions", "averageVolume",
            "averageVolume10days", "regularMarketPrice", "previousClose", "fiftyTwoWeekHigh", "fiftyTwoWeekLow",
            "fullExchangeName", "lastSplitDate", "lastSplitFactor", "country", "sector", "industry"]
    for sym in ["DRTS", "VST", "FNMA", "BLGO", "UURAF"]:
        try:
            t = yf.Ticker(sym)
            info = t.info
            print(f"\n### yf info {sym}: {json.dumps({k: info.get(k) for k in keys}, default=str)}")
            h = t.history(period="1y", interval="1d", auto_adjust=False, actions=True)
            print(f"yf history {sym}: rows={len(h)} cols={list(h.columns)} last=\n{h.tail(3)}")
            try:
                sf = t.get_shares_full(start="2025-01-01")
                print(f"yf shares_full {sym}: n={0 if sf is None else len(sf)} tail=\n{None if sf is None else sf.tail(3)}")
            except Exception as exc:
                print(f"yf shares_full {sym}: ERROR {exc}")
            m = t.history(period="5d", interval="5m", prepost=True)
            print(f"yf 5m {sym}: rows={len(m)} first={m.index[:1].tolist()} last={m.index[-1:].tolist()}")
        except Exception as exc:
            print(f"yf {sym} ERROR {type(exc).__name__}: {exc}")
        time.sleep(1)
except Exception:
    traceback.print_exc()

section("SEC")
sec_h = {"User-Agent": SEC_UA, "Accept-Encoding": "gzip, deflate"}
print("SEC UA set:", bool(SEC_UA and "@" in SEC_UA))
for cik in [1871321, 880242]:
    r = get(f"submissions {cik}", f"https://data.sec.gov/submissions/CIK{cik:010d}.json", headers=sec_h, n=200)
    if r is not None and r.status_code == 200:
        j = r.json()
        rec = j["filings"]["recent"]
        print({k: j.get(k) for k in ["name", "tickers", "exchanges", "sic", "sicDescription", "category", "stateOfIncorporation",
                                     "fiscalYearEnd", "formerNames", "entityType", "insiderTransactionForIssuerExists"]})
        print("n recent:", len(rec["form"]), "files:", j["filings"].get("files"))
        for i in range(min(15, len(rec["form"]))):
            print(" ", rec["form"][i], rec["filingDate"][i], rec["acceptanceDateTime"][i], rec["accessionNumber"][i],
                  rec.get("items", [""] * 99)[i], rec["primaryDocument"][i])
    time.sleep(0.3)
    for concept in ["dei/EntityCommonStockSharesOutstanding", "dei/EntityPublicFloat"]:
        r = get(f"concept {cik} {concept}", f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/{concept}.json", headers=sec_h, n=150)
        if r is not None and r.status_code == 200:
            j = r.json()
            for unit, vals in j["units"].items():
                print(unit, len(vals), vals[-3:])
        time.sleep(0.3)

section("FINRA")
for f in ["CNMSshvol20261002.txt", "FORFshvol20261002.txt", "FNSQshvol20261002.txt"]:
    r = get(f"regsho {f}", f"https://cdn.finra.org/equity/regsho/daily/{f}", n=300)
    if r is not None and r.status_code == 200:
        lines = r.text.splitlines()
        print("lines:", len(lines), [ln for ln in lines if ln.split("|")[1:2] in (["DRTS"], ["FNMA"], ["BLGO"])][:4])
for url in [
    "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest?limit=3",
    "https://api.finra.org/data/group/otcMarket/name/EquityShortInterest?limit=3",
    "https://api.finra.org/metadata/group/otcMarket/name/consolidatedShortInterest",
]:
    get("finra api GET", url, headers={"User-Agent": UA_BROWSER, "Accept": "application/json"}, n=800)
try:
    body = {"limit": 5, "compareFilters": [{"compareType": "equal", "fieldName": "symbolCode", "fieldValue": "DRTS"}],
            "sortFields": ["-settlementDate"]}
    r = requests.post("https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest", json=body,
                      headers={"User-Agent": UA_BROWSER, "Accept": "application/json"}, timeout=30)
    show("finra api POST consolidatedShortInterest DRTS", r, 1500)
except Exception as exc:
    print("finra POST ERROR", exc)
for d in ["20260915", "20260930"]:
    get(f"finra biweekly file {d}", f"https://cdn.finra.org/equity/otcmarket/biweekly/shrt{d}.csv", n=300)

section("Nasdaq API")
nh = {"User-Agent": UA_BROWSER, "Accept": "application/json, text/plain, */*", "Origin": "https://www.nasdaq.com",
      "Referer": "https://www.nasdaq.com/"}
get("nasdaq info", "https://api.nasdaq.com/api/quote/DRTS/info?assetclass=stocks", headers=nh, n=900)
get("nasdaq summary", "https://api.nasdaq.com/api/quote/DRTS/summary?assetclass=stocks", headers=nh, n=1500)
get("nasdaq historical", "https://api.nasdaq.com/api/quote/DRTS/historical?assetclass=stocks&fromdate=2026-09-01&todate=2026-10-04&limit=40", headers=nh, n=700)
get("nasdaq short-interest", "https://api.nasdaq.com/api/quote/DRTS/short-interest?assetClass=stocks", headers=nh, n=900)
get("nasdaq screener", "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=3&offset=0", headers=nh, n=900)
get("nasdaq screener full", "https://api.nasdaq.com/api/screener/stocks?tableonly=true&download=true", headers=nh, n=300)

section("OTC Markets")
oh = {"User-Agent": UA_BROWSER, "Accept": "application/json", "Origin": "https://www.otcmarkets.com", "Referer": "https://www.otcmarkets.com/"}
for url in [
    "https://backend.otcmarkets.com/otcapi/company/profile/full/BLGO?symbol=BLGO",
    "https://backend.otcmarkets.com/otcapi/stock/trade/inside/BLGO?symbol=BLGO",
    "https://backend.otcmarkets.com/otcapi/company/profile/BLGO/badges?symbol=BLGO",
    "https://backend.otcmarkets.com/otcapi/historical/BLGO/daily?symbol=BLGO&page=1&pageSize=5&sortOn=closingDate&sortDir=DESC",
    "https://backend.otcmarkets.com/otcapi/company/BLGO/promotions?symbol=BLGO",
    "https://backend.otcmarkets.com/otcapi/security/BLGO/short-interest?symbol=BLGO",
]:
    get("otc", url, headers=oh, n=1500)

section("Stooq")
get("stooq", "https://stooq.com/q/d/l/?s=drts.us&i=d", n=300)
print("\nPROBE DONE")
