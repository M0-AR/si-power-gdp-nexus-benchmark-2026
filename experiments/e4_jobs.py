"""E4: Jobs + community. Blue-collar boom vs weak-permanent-jobs + backlash."""
import json, pathlib
OUT = pathlib.Path("data/processed/e4_jobs.json")
def main():
    res = {
     "transcript": "10-20 GW/yr => ~1M jobs incl construction/power/cooling/pipefitters; overemployment near Colossus/MacroHarder; doubled tax budget; $250M water recycling; half-price tolling",
     "for_claim": ["CNBC 2026-09-26: blue-collar AI job market booming", "CBS 2026-10-02: Amazon $1B for data-center towns", "xAI Memphis anecdote: shortage not unemployment"],
     "against_claim": ["Futurism 2026-09-05: Meta deploying robots for DC maintenance", "Morningstar/MarketWatch 2026-09-18: most of what you know about DCs is wrong (weak ops jobs)", "Colorado thesis 2026: +0.53c/kWh (+3.1%) in DC counties — ratepayer cost", "Frontiers 2026: establishment growth vs emissions panel 2010-2023"],
     "verdict": "Two-phase labor model: Phase A (build, 18-36 mo) = 1M job-years plausible at 15GW/yr; Phase B (operate) = ~30-80 permanent jobs per 100MW hyperscale => only ~6-16k permanent for 20GW. Transcript conflates stock vs flow. Tax/rate tradeoff is the hidden distributional fight.",
     "hidden_pattern": "Counties WITH DCs pay +3.1% MORE for residential power (Rother 2026). Prosperity is fiscal (tax base) + construction wages, but household energy penalty. Community reciprocity (tolling, water plant) is Coasean bargain to offset rate + water externality.",
     "benchmark": "Jobs/GW_build vs jobs/GW_operate vs $tax/GW vs c/kWh_penalty — report all four, never one."}
    OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(json.dumps(res, indent=2)); print(json.dumps(res, indent=2))
if __name__ == "__main__": main()
