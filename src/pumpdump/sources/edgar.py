"""SEC EDGAR: an issuer's filings (with acceptance times) and its reported share count.

Needs a User-Agent naming a reachable contact (the SEC_USER_AGENT secret, see
symbols.sec_contact); sec.gov answers anything else with 403. Only issuers with
a CIK (in SEC's ticker list) can be looked up, so non-reporting OTC pinks have
no EDGAR data at all.
"""

from __future__ import annotations

import json

from .web import Web, short_text

SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{:010d}.json"
SHARES_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK{:010d}/dei/EntityCommonStockSharesOutstanding.json"


class EdgarError(Exception):
    pass


def _get(web: Web, url: str, contact: str) -> tuple[int, str]:
    return web.fetch(url, headers={"User-Agent": contact, "Accept-Encoding": "gzip, deflate"})


def submissions(web: Web, cik: int, contact: str, since: str) -> dict:
    """Issuer facts and the filings made on or after `since` (YYYY-MM-DD), newest first."""
    status, text = _get(web, SUBMISSIONS_URL.format(int(cik)), contact)
    if status != 200:
        raise EdgarError(f"submissions HTTP {status}: {short_text(text)}")
    j = json.loads(text)
    rec = j.get("filings", {}).get("recent", {})
    forms = rec.get("form", [])
    items = rec.get("items") or [""] * len(forms)
    accession = rec.get("accessionNumber") or [""] * len(forms)
    filings = [
        {"form": forms[i], "filed": rec["filingDate"][i], "accepted": rec["acceptanceDateTime"][i], "items": items[i] or "",
         "accession": accession[i] or ""}
        for i in range(len(forms))
        if rec["filingDate"][i] >= since
    ]
    return {
        "name": j.get("name"),
        "sic": j.get("sic"),
        "category": (j.get("category") or "").replace("<br>", "; "),
        "state_of_incorporation": j.get("stateOfIncorporation"),
        "former_names": [
            {"name": f.get("name"), "from": (f.get("from") or "")[:10], "to": (f.get("to") or "")[:10]}
            for f in j.get("formerNames") or []
        ],
        "filings": filings,
    }


def shares_facts(web: Web, cik: int, contact: str) -> list[dict]:
    """Shares outstanding as reported on each filing's cover page (empty if the issuer never tagged it)."""
    status, text = _get(web, SHARES_URL.format(int(cik)), contact)
    if status == 404:
        return []
    if status != 200:
        raise EdgarError(f"shares HTTP {status}: {short_text(text)}")
    units = json.loads(text).get("units", {})
    return [{"end": f["end"], "val": f["val"], "filed": f["filed"], "form": f.get("form")} for f in units.get("shares", [])]
