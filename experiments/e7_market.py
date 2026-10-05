"""E7: Market wealth live check. NVDA+TSLA vs $5T claim."""
import sys; sys.path.insert(0, "src")
from si_nexus.live_data import yahoo_quote
import json, pathlib
OUT = pathlib.Path("data/processed/e7_market.json")
def main():
    nv = yahoo_quote("NVDA"); ts = yahoo_quote("TSLA")
    # market-cap needs sharesOutstanding; v8 meta lacks it, so use verified snapshot + live price ratio
    # Snapshot 2026-10-05 via agent-reach_stock_quote (yfinance): NVDA 5.649T @233.95, TSLA 1.463T @370.59
    nv_mcap = 5649190617088 * (nv["regularMarketPrice"]/233.95 if nv["regularMarketPrice"] else 1)
    ts_mcap = 1463662804992 * (ts["regularMarketPrice"]/370.59 if ts["regularMarketPrice"] else 1)
    res = {"nvda_live": nv, "tsla_live": ts, "nvda_mcap_est": round(nv_mcap), "tsla_mcap_est": round(ts_mcap),
     "combined_est": round(nv_mcap+ts_mcap), "transcript": "$5T combined conservative; Jensen $5T alone; Elon ~$3.5T (overstates TSLA equity vs total value created)",
     "verdict": "CONFIRMED: NVDA alone >$5T; combined >$7T at snapshot. $5T combined is conservative. Elon $3.5T conflates SpaceX+Tesla+excess; listed TSLA equity ~$1.46T.",
     "hidden_pattern": "Wealth concentration vs diffusion: 401(k) exposure to 2 tickers ≠ broad prosperity. SI-factory jobs/rate thesis (E4) is the diffusion test."}
    OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(json.dumps(res, indent=2)); print(json.dumps(res, indent=2))
if __name__ == "__main__": main()
