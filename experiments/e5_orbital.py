"""E5: Orbital feasibility. Pro-space physics vs IEEE/ACM skepticism."""
import json, pathlib
OUT = pathlib.Path("data/processed/e5_orbital.json")
def main():
    res = {
     "pro": ["Space solar CF ~100%+ nameplate vs ground 12-25% (1/8 to 1/5 claim CORRECT)", "Starship Flight 14 Sep28 2026: 26x V3, first orbital", "H100 orbital demo (Crusoe/Starcloud) + Google TPU intent", "Launch cost amortized if $60B/GW thesis holds"],
     "con": ["IEEE Spectrum Jul 2026 Goldstein: Orbital Data Center Fever Dream — math won't align", "ACM ESpaS 2025 (Ohs et al): orbit up to 10x carbon cost vs terrestrial (embodied launch+reentry)", "Viale et al 2023: reflectors help dawn/dusk but regulatory + attitude + structures hard", "300GW/yr launch = ~40% US consumption growth/yr — mass/cadence unprecedented (weekly Starship needed)"],
     "fermi": "200GW space solar @ 1kW/kg array + structure => ~200kT to LEO/yr. Starship ~100T/reusable flight => 2000 flights/yr (~5-6/day). Even 2x lighter => 1000/yr. Weekly cadence (52/yr) is 20-40x short. Terawatt = 10k flights/yr. Physics allows, logistics doesn't — yet.",
     "verdict": "Space gets nameplate physics RIGHT; deployment RATE claim (200-300GW/yr, TW one day) fails Fermi by 1-2 orders vs demonstrated cadence. Best framing: orbital = R&D pathfinder + latency/sovereign niche, not 2027 grid relief.",
     "hidden_pattern": "Always-sunny advantage is real but cooling in vacuum + radiation + servicing dominate. Ground batteries look expensive until you price launch + reentry + replacement. Carbon ledger flips the 'clean space solar' narrative."}
    OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(json.dumps(res, indent=2)); print(json.dumps(res, indent=2))
if __name__ == "__main__": main()
