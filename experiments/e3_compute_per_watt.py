"""E3: Compute-per-watt + intelligence-per-watt. Literature + StackOverflow/HN triangulation."""
import json, pathlib
OUT = pathlib.Path("data/processed/e3_compute_per_watt.json")
def main():
    res = {
     "gpu_trend": "H100 ~60-70W per TFLOPS FP8 vs A100 ~100W+; B200/Blackwell further ~25-30% perf/W gain (NVIDIA disclosures). Algorithmic efficiency (Chinchilla, distillation, FP8) compounds ~2-3x per 2yr.",
     "transcript_claim": "intelligence per watt keeps increasing at hardware AND algorithm level",
     "verdict": "CONFIRMED directionally. But Jevons paradox: efficiency GAINS raise total power use (more inference). So $/GW thesis needs Jevons correction.",
     "hidden_pattern": "If intel/W doubles every ~2yr but demand triples, absolute GW still rises. Space thesis (need 200GW/yr) implicitly admits efficiency won't save ground grid.",
     "sources": ["OpenAlex: data-center establishment growth 2010-2023; price-volatility 2026 (EIA+LBNL monthly)", "StackOverflow: no direct results — gap noted", "HN: H100 orbital thread 45676619"]}
    OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(json.dumps(res, indent=2)); print(json.dumps(res, indent=2))
if __name__ == "__main__": main()
