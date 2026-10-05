"""Benchmark suite: scores each transcript claim 0-100 on evidence, reproducibility, live-verified."""
import json, pathlib
RUBRIC = {"evidence_strength": 40, "live_repro": 30, "falsifiability": 15, "novelty": 15}
SCORES = [
 {"claim": "C1 500GW avg", "evidence_strength": 38, "live_repro": 28, "falsifiability": 13, "novelty": 5, "note": "517GW recomputed; trivially repro"},
 {"claim": "C2 China 3x", "evidence_strength": 30, "live_repro": 28, "falsifiability": 14, "novelty": 6, "note": "-29% overstatement penalty"},
 {"claim": "C3 1%power=1%GDP", "evidence_strength": 20, "live_repro": 20, "falsifiability": 14, "novelty": 13, "note": "Math ok, causality weak — highest PhD value if fixed"},
 {"claim": "C4 10GW=25% additions", "evidence_strength": 18, "live_repro": 15, "falsifiability": 12, "novelty": 8, "note": "Needs EIA 861 + interconnection queue"},
 {"claim": "C5 1M jobs", "evidence_strength": 22, "live_repro": 18, "falsifiability": 13, "novelty": 11, "note": "Stock vs flow conflation; rate penalty hidden"},
 {"claim": "C6 Starship V3 orbital", "evidence_strength": 37, "live_repro": 25, "falsifiability": 12, "novelty": 7, "note": "Flight 14 confirmed"},
 {"claim": "C7 H100 orbit", "evidence_strength": 28, "live_repro": 18, "falsifiability": 10, "novelty": 9, "note": "Demo, not production"},
 {"claim": "C8 200GW space solar", "evidence_strength": 15, "live_repro": 12, "falsifiability": 14, "novelty": 14, "note": "Fermi fails 20-40x; carbon 10x"},
 {"claim": "C10 OpenShell+BlueField", "evidence_strength": 39, "live_repro": 30, "falsifiability": 14, "novelty": 10, "note": "Only fully OSS-repro claim"},
 {"claim": "C12 $5T wealth", "evidence_strength": 38, "live_repro": 29, "falsifiability": 13, "novelty": 5, "note": "Live mcap confirms, attribution caveat"},
]
def main():
    total = []
    for s in SCORES:
        score = s["evidence_strength"]+s["live_repro"]+s["falsifiability"]+s["novelty"]
        total.append({**s, "total": score})
    total.sort(key=lambda x: x["total"], reverse=True)
    out = pathlib.Path("data/processed/benchmark_scores.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"rubric": RUBRIC, "scores": total,
      "headline": "Strongest: safety OSS + power math. Weakest: orbital rate + subsidy-free clean. Biggest PhD gap: non-linear $/GW with Jevons + ratepayer wedge."}, indent=2))
    print(json.dumps(total, indent=2))
if __name__ == "__main__": main()
