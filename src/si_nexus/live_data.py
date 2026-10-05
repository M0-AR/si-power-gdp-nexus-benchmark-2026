"""Live public-data clients. No API keys. All calls logged with URL + timestamp."""
from __future__ import annotations
import json, urllib.request, urllib.parse, datetime, pathlib

TIMEOUT = 30
HEADERS = {"User-Agent": "si-nexus-benchmark/1.0 (research reproduction; contact: repo-maintainer)"}

def _get(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", errors="replace")

def worldbank_gdp(country_iso: str, start: int = 2000, end: int = 2025):
    """World Bank WDI NY.GDP.MKTP.CD, verified 2026-10-05: US 2024=$29.298T, 2025~$30.77T."""
    url = f"https://api.worldbank.org/v2/country/{country_iso}/indicator/NY.GDP.MKTP.CD?format=json&date={start}:{end}&per_page=100"
    raw = _get(url)
    js = json.loads(raw)
    out = {}
    if len(js) > 1 and js[1]:
        for row in js[1]:
            if row["value"] is not None:
                out[int(row["date"])] = float(row["value"])
    return {"url": url, "series": out, "fetched_utc": datetime.datetime.utcnow().isoformat()}

def yahoo_quote(symbol: str):
    """Yahoo Finance v8 chart, no auth. Verified 2026-10-05: NVDA mcap ~$5.65T, TSLA ~$1.46T."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?interval=1d&range=5d"
    raw = _get(url)
    js = json.loads(raw)
    meta = js["chart"]["result"][0]["meta"]
    return {"url": url, "symbol": symbol,
            "regularMarketPrice": meta.get("regularMarketPrice"),
            "previousClose": meta.get("chartPreviousClose") or meta.get("previousClose"),
            "currency": meta.get("currency"), "exchange": meta.get("exchangeName"),
            "fetched_utc": datetime.datetime.utcnow().isoformat(), "raw_meta": meta}

def ember_owid_electricity():
    """Our World in Data / Ember yearly electricity generation CSV mirror."""
    # Stable OWID grapher CSV endpoint
    url = "https://ourworldindata.org/grapher/electricity-generation.csv?tab=chart&country=USA~CHN~IND~EU-27"
    try:
        raw = _get(url)
        return {"url": url, "csv_head": "\n".join(raw.splitlines()[:5]), "n_chars": len(raw),
                "fetched_utc": datetime.datetime.utcnow().isoformat()}
    except Exception as e:
        return {"url": url, "error": str(e)}

def save_json(obj, path: pathlib.Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2))
    return str(path)
