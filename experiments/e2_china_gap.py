"""E2: US-CN electricity gap. Transcript says 3x. Ember says 2.33x."""
import json, pathlib
OUT = pathlib.Path("data/processed/e2_gap.json")
def main():
    us, cn = 4536, 10573
    ratio = cn/us
    res = {"us_TWh": us, "cn_TWh": cn, "ratio": round(ratio,3),
      "transcript": "3x", "error_pct": round((3-ratio)/ratio*100,1),
      "verdict": "Transcript overstates by ~29%. Correct figure 2.33x (2025). China = 33.3% of global demand, first time >1/3. US clean met 88% of new demand; China solar +336 TWh (>50% global solar growth).",
      "hidden_pattern": "Fossil generation FELL in both China (-56 TWh) and India (-52 TWh) in 2025 — first joint fall this century. Clean > demand growth. SI power race coincides with fossil peak, not fossil boom.",
      "source": "Ember Global Electricity Review 2026 Ch.4 + Our World in Data grapher"}
    OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(json.dumps(res, indent=2)); print(json.dumps(res, indent=2))
if __name__ == "__main__": main()
