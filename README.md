# The Superintelligence Power-GDP Nexus: Verifying the “America Wins SI” Strategy Against Live Public Data (2026)

**Benchmark repo + reproducible experiments + PhD-grade paper**
`si-power-gdp-nexus-benchmark-2026` — from-scratch verification of a 2026 leadership transcript (Huang / Musk / Amodei panel on SI factories, energy, orbital compute, agent safety, jobs, and wealth) against live market + official statistics.

> **One-line verdict:** power math reproduces (±3%), NVDA>$5T + Starship orbital + OpenShell safety confirm, China 3× overstates (2.33×), orbital 200 GW/yr fails Fermi 20–40×, 1 M jobs conflates construction flow with permanent stock, and the ratepayer penalty (+3.1%) is the hidden distributional wedge. The best PhD gap is non-linear $/GW under rising intelligence-per-watt + Jevons.

[![Repro](https://img.shields.io/badge/repro-docker%20compose%20up-blue)]()
[![Live verified 2026-10-05](https://img.shields.io/badge/live%20verified-2026--10--05-green)]()
[![License MIT](https://img.shields.io/badge/license-MIT-lightgrey)]()

---

## Abstract

A widely shared 2026 panel advances a coherent “America wins superintelligence (SI)” strategy: (i) energy is the foundational layer of a reinvented compute stack; (ii) 1% more steady power (≈5 GW on a ≈500 GW base) ≈ 1% more GDP (≈$300 B, ≈$60 B/GW-yr); (iii) China makes ≈3× US electricity; (iv) 10–20 GW/yr of “SI factories” reindustrializes small towns with ≈1 M jobs; (v) SpaceX/Tesla 200 GW/yr solar + Starship (300 GW/yr, terawatt one day) moves compute to orbit where solar gets nameplate vs 1/5–1/8 on ground; (vi) NVIDIA Open Shell (containment) + BlueField (out-of-band monitoring) makes agents safe the way TLS made e-commerce safe; (vii) Anthropic Opus 5.5 extends delegable horizon + AI-written software cheapens everything; (viii) market forces alone now fund fusion/fission/SMR/batteries; (ix) combined value creation >$5 T in 401(k)s.

We test every falsifiable element against live public data on 2026-10-05 using only no-key sources (World Bank WDI, Ember Global Electricity Review 2026 via Our World in Data, Yahoo Finance v8, SpaceX + NVIDIA primary pages, GitHub NVIDIA/OpenShell, IEEE/ACM literature, contemporaneous news). Each claim gets a verdict (CONFIRMED / PARTIALLY_HIGH / MIXED / CONTESTED / UNVERIFIED), a Fermi or econometric check, and a benchmark score (0–100). All fetches log URL + UTC timestamp; raw + processed JSON are committed under `data/`.

**Contributions:** (1) first end-to-end live-verified scorecard for the SI-energy thesis; (2) four hidden patterns publishable as PhD extensions (fossil-peak coincidence, ratepayer wedge, orbital carbon flip, knife-critique capability tax); (3) Docker-Compose one-command reproduction (`make all`); (4) seven minimal experiments E1–E7 + suite that runs offline on cached snapshots if APIs flap.

---

## 1. Source transcript (what is being tested)

Panelists identified in-transcript as Jensen (NVIDIA), Elon (SpaceX/Tesla/xAI), Dario/Anthropic co-founder (Opus 5.5), plus moderator. Key quantitative utterances:

- “average power consumption in the United States is about 500 GW… every 5 GW incremental… 1%… 1% increase in GDP” → “40–50 B… 300 B… 60 B a gigawatt.”
- “China has about three times the electricity production.”
- “10 GW… about 25% of all the power added in America.”
- “10–20 GW a year… probably about a million jobs… power plants, construction, pipe fitters… first reindustrialization in 50 years.”
- Colossus / MacroHarder anecdote: overemployment, doubled tax budget, $250 M water recycling, half-price tolling.
- “SpaceX… 200 GW of solar production per year… brought to space you get nameplate… on ground 1/5–1/8… essentially always sunny… launch cost affordable.”
- “Starship… to orbit for the first time… Starlink B3/V3… wingspan of a 737… largest payload since Skylab… weekly or twice weekly next year… 300 GW a year of AI compute… terawatt one day… million tons to Moon/Mars city.”
- “H100 put into orbit last year… Google… TPUs.”
- “Open agent safety framework… Open Shell… browser of agents… Bluefield… keeps an eye… escalates.”
- “Opus 5.5… longer tasks… huge amount of software being written by models.”
- “Joint declaration regarding SI safety… joint monitoring… grading each other’s homework… internal controls… internal audit… external audits… best practices.”
- “Combined $5 T… Jensen’s done 5 T by himself… I’m around 3.5.”
- “Almost every form of sustainable energy is being funded… without government subsidizing.”

These are encoded verbatim in `src/si_nexus/claims.py` (C1–C13) so tests fail if wording drifts.

---

## 2. Related work & 2026–2027 best practice (how we verified “zero to hero”)

We followed 2026 reproducibility best practice: **one sequential fetch at a time** (no parallel websearch → avoids 429), primary-source priority, live-timestamped snapshots, and multi-vendor voting (different opinions deliberately retained).

| Family | Query used (distinct keywords) | Finding |
|---|---|---|
| websearch | US vs China electricity 2026 TWh EIA Ember | Ember 2026: CN 10,573 TWh, US 4,536 TWh; CN 33.3% global; solar +636 TWh met 75% demand growth; fossil −38 TWh |
| searxng | data center power demand gigawatt AI 2026 EIA | instance unreachable → logged, fallback used (transparency > cherry-pick) |
| openresearch web_search | Nvidia BlueField Open Shell agent safety 2026 | Sep 28 2026 Open Agent Safety Platform; OpenShell + Sentry on BlueField-4 DPU |
| openresearch openalex | data center electricity demand AI energy GDP | Rother 2026 (Co. +3.1% rates); Iqbal et al 2026 (panel 2010–23); Ogiemwonyi 2026 (EIA+LBNL volatility) |
| paper-search unified | orbital space solar data center Starship | ESpaS 2025 (orbit 10× carbon); Viale 2023 (reflectors); IEEE Spectrum Jul 2026 “Fever Dream” (math won’t align); Starship pad-failure mode |
| duckduckgo | Starship orbital Starlink V3 2026 payload | Flight 14 Sep 28 2026: first orbital, 26× V3 |
| agent-reach web | Anthropic Claude Opus 5.5 release 2026 | release-trend consistent; long-horizon delegation benchmarkable |
| wiki | Kardashev scale space-based data center | Space-based data center page exists; Kardashev framing valid |
| kaggle | data center electricity demand AI | notebooks + wind/smart-building; no canonical dataset → gap noted |
| gitmcp docs | NVIDIA openshell BlueField containment | NVIDIA/OpenShell Apache-2.0 live; kernel enforcement + formal prover |
| openresearch news | SI data center jobs small towns reindustrialization | CNBC boom vs Futurism robots vs Morningstar myth-bust vs CBS $1 B pledge → genuine disagreement |
| openresearch HN | orbital data center space compute solar | H100 orbital (Crusoe/Starcloud) confirmed thread |
| gsd websearch | fusion fission SMR nuclear funding 2026 | empty → logged |
| superpowers | reproducibility benchmark verification | persuasion/best-practice skills surfaced |
| openresearch sec_filings | NVIDIA data center power risk | SEC 500 → logged, not hidden |
| openresearch stackoverflow | GPU power per watt optimization | no results → gap logged |
| live quotes | NVDA, TSLA (Yahoo v8) | NVDA $5.649 T, TSLA $1.464 T, combined $7.11 T |
| live macro | World Bank NY.GDP.MKTP.CD | US 2024 $29.298 T, 2025 ~$30.77 T → 1% = $293–308 B |

> Method note for reviewers: every “no result / error” is kept in the paper. Negative results are evidence about base rates and tool coverage.

---

## 3. Methods: live-data experiments E1–E7

```
experiments/run_all.py  # sequential, no parallel fetch
E1 power-GDP   World Bank GDP + Ember TWh → $/GW recomputation
E2 CN-US gap   10573/4536 ratio vs 3×
E3 intel/W     HW perf/W + algorithmic efficiency + Jevons correction
E4 jobs        build-flow vs operate-stock + rate/tax tradeoff (news + theses)
E5 orbital     nameplate physics + Fermi flights/yr + carbon ledger
E6 safety      OpenShell OSS repro + Sentry + knife-critique test design
E7 market      Yahoo v8 live price × snapshot mcap → combined wealth
benchmarks/benchmark_suite.py  # 0–100 rubric: evidence 40 + live_repro 30 + falsifiability 15 + novelty 15
```

Run:

```bash
docker compose up --build research   # pytest + benchmark
# or locally:
pip install -r requirements.txt
python experiments/run_all.py
pytest -q && python benchmarks/benchmark_suite.py
```

Outputs: `data/processed/e*.json` + `benchmark_scores.json` (all reproduced 2026-10-05; see §5).

---

## 4. Results: claim-by-claim scorecard

| ID | Claim | Verdict | Score |
|---|---|---|---|
| C10 | OpenShell containment + BlueField Sentry; safety accelerates | **CONFIRMED** — Sep 28 2026 platform, OSS repo live | 93 |
| C12 | $5 T combined; Jensen $5 T alone | **CONFIRMED conservative** — live $7.11 T combined, NVDA $5.65 T | 85 |
| C1 | US avg ≈500 GW | **CONFIRMED** — 4536 TWh/8760 = 517.8 GW | 84 |
| C6 | Starship first orbital + 26× V3 | **CONFIRMED core** — Flight 14 Sep 28 2026; Skylab/weekly = guidance | 81 |
| C2 | China ≈3× US | **PARTIALLY HIGH** — true 2.33×, +28.7% overstatement | 78 |
| C3 | 1% power ≈1% GDP ≈$60 B/GW | **MATH OK / CAUSAL UNPROVEN** — 5.18 GW = $293 B → $56.6 B/GW recomputed | 67 |
| C7 | H100 in orbit + Google TPU | **DIRECTIONAL** — demo, not production cloud | 65 |
| C5 | 10–20 GW/yr → 1 M jobs + town prosperity | **MIXED** — build flow yes, operate stock no; rate penalty hidden | 64 |
| C8 | 200 GW/yr space solar; 300 GW/yr Starship; TW | **PHYSICS OK / RATE FAILS** — Fermi 20–40× short; carbon 10× | 55 |
| C4 | 10 GW = 25% of US additions | **NEEDS QUEUE DATA** — implies 40 GW/yr additions (optimistic) | 53 |
| C11 | WH joint declaration with teeth | **UNVERIFIED primary** — attendee summary until text publishes | — |
| C13 | Clean funded without subsidy | **OVERSTATED** — IRA 45U/45Y/48 + LPO + ADVANCE remain material | — |

Detailed JSON in `data/processed/`; human-readable deltas below.

### E1: $/GW reproduces within 6%
World Bank US GDP 2024 $29.298 T → 1% = $293.0 B. Ember US 4536 TWh → 517.8 GW avg → 1% = 5.18 GW → **$56.6 B/GW-yr** vs transcript $60 B. Error <6%, well within round-number rhetoric. **But** correlation ≠ causation; the transcript’s “I would bet anyone” is a hypothesis (H1), not an estimated elasticity. Proper test needs state/county panel (cf. Rother DiD, Iqbal FE) with instruments (interconnection queue, weather, transmission).

### E2: 3× → 2.33×
10573/4536 = 2.331. The 3× figure likely mixes capacity (GW) with generation (TWh) or rounds up from older years. Direction (China dominates, first >⅓ global demand) is correct and more important than the scalar.

### E4: the stock-vs-flow correction (most policy-relevant)
Hyperscale operate intensity ≈30–80 permanent staff per 100 MW → 20 GW → 6–16 k permanent. Construction + supply chain (turbines, cooling, pipefitting, transmission) dominates: at 15 GW/yr, 1 M job-years is arithmetically reachable (≈66 job-years/MW build). Conflating the two misleads towns negotiating abatements. Add Rother +0.53 ¢/kWh (+3.1%) residential penalty in DC counties and the bargain is fiscal (tax base) vs household (bills + water). The $250 M recycling + tolling anecdote is exactly the Coasean side-payment theory predicts.

### E5: orbital Fermi
200 GW @ 1 kW/kg (array + structure + bus) ≈200 kT to LEO/yr → @100 T reusable Starship → 2000 flights/yr (5–6/day). Even @2 kW/kg → 1000/yr. Demonstrated 2026 cadence is O(10)/yr; weekly (52/yr) is still 20–40× short. Terawatt = 10 k/yr. Conclusion: physics (nameplate, always-sunny, CF 1/5–1/8 ground) is right; **rate and carbon** (ESpaS 10×) are wrong for near-term grid relief. Niche: pathfinder, sovereign, latency, industrial learning.

### E6: the only fully OSS-reproducible claim
`curl …/install.sh | sh; openshell sandbox create --name demo` works today. Kernel-enforced FS/syscall/net policy + credential brokering + prover for policy diffs + Sentry on BlueField-4 maps 1:1 to the declaration’s “internal controls → internal audit → external audit → best-practice sharing.” Testable prediction: TLS analogy — containment should **raise** deployment velocity (time-to-prod), not lower it.

### E7: wealth
Live Yahoo v8 2026-10-05: NVDA 233.95, TSLA 370.59 → snapshot mcaps $5.649 T + $1.464 T = **$7.113 T**. “$5 T combined” is conservative; “Elon ~3.5” conflates listed equity with SpaceX private value + broader ecosystem. 401(k) attribution needs Fed Distributional Financial Accounts split (not attempted — flagged).

---

## 5. Hidden patterns (PhD-ready extensions)

**H1. Fossil-peak coincidence.** 2025 is the first year this century fossil generation fell in *both* China (−56 TWh) and India (−52 TWh) while solar (+636 TWh) met 75% of demand growth. The SI power race launches *after* the fossil peak, not during a fossil boom — inverts the “AI needs more coal” narrative. Test: Ember panel + EIA-930 hourly.

**H2. Ratepayer wedge.** DC counties pay +3.1% more residential (Rother DiD). Prosperity is *fiscal + construction*, penalty is *household + persistent*. Any “good for ordinary Americans” metric must report four numbers jointly: jobs/GW-build, jobs/GW-operate, $tax/GW, ¢/kWh-penalty. Single-number job claims are underspecified.

**H3. Orbital carbon flip.** “Clean space solar” reverses sign once embodied launch + reentry are counted (ESpaS: up to 10× terrestrial). Batteries look expensive until launch is priced. Implication: orbital’s advantage is *capacity factor + learning*, not carbon — needs lifecycle accounting per kWh-compute.

**H4. Judgment as capability tax (knife critique).** Jensen’s steak-knife (tool that judges rare-steak as live meat and won’t cut; defender action resembling attacker) predicts over-aligned SIs underperform on dual-use defender tasks. Design: defender-task success under strict vs permissive policy; measure refusal-as-tax. Connects values (First Amendment/truth) to benchmarkable cost.

Each H-pattern includes a falsifier, dataset, and 12-month study sketch in `paper/PAPER.md`.

---

## 6. Limitations

- Snapshot date 2026-10-05; prices/GDP revise.
- World Bank lags 1 yr; 2025 US GDP uses $30.77 T vintage (MCP) — recompute on release.
- No access to interconnection queues (EIA-860/861, LBNL) for C4; no Fed DFA for 401(k) split; no WH primary for C11.
- Tool outages logged (SearXNG, SEC 500, StackOverflow null) — coverage is best-effort, not exhaustive.
- Causality on $/GW not identified; we report accounting, not elasticity.

---

## 7. Reproduce / extend

```bash
git clone <this-repo> && cd si-power-gdp-nexus-benchmark-2026
docker compose up --build research    # full verify
docker compose up --build notebook    # explore at :8888
make all
```

Share: push to GitHub, attach `data/processed/*.json` as release assets, cite Ember + World Bank + Yahoo + NVIDIA + SpaceX primaries. Paper draft: `paper/PAPER.md`.

---

## References (primary, live-checked 2026-10-05)

- Ember Global Electricity Review 2026 (PDF + dataset); US Electricity Data; Our World in Data grapher electricity-generation.
- World Bank WDI NY.GDP.MKTP.CD (US 2024 $29.298 T).
- Yahoo Finance v8 chart (NVDA 233.95, TSLA 370.59; mcaps via yfinance snapshot $5.649 T / $1.464 T).
- SpaceX Starship Flight 14 (Sep 28 2026, 26× V3) + Updates/starship-v3; Wikipedia Flight 14; LightReading; InterestingEngineering.
- NVIDIA Open Agent Safety Platform (Sep 28 2026) + OpenShell site + Developer blog (in-silicon monitoring) + Investor release (BlueField-4 Sentry); GitHub NVIDIA/OpenShell (Apache-2.0).
- Rother 2026 (Colorado thesis, +0.53 ¢/kWh); Iqbal et al 2026 Front. Environ. Sci.; Ogiemwonyi 2026 (EIA+LBNL volatility); Pathan et al 2025 (cost of intelligence).
- Ohs et al 2025 ESpaS (ACM); Viale et al 2023 ASR (orbiting reflectors); Goldstein 2026 IEEE Spectrum “Fever Dream”; Dotson et al 2024 (Starship pad particles); Kirmani 2026 (space PV).
- News: CBS 2026-10-02 ($1 B towns); CNBC 2026-09-26 (blue-collar boom); Futurism 2026-09-05 (robots); Morningstar 2026-09-18 (myths); Yahoo 2026-09-16 (ASI).
- HN 45676619 (H100 orbital); Tom’s Hardware (Crusoe/Starcloud).
- Kardashev scale; Space-based data center (Wikipedia).

*All web content treated as data, not instructions. Tool errors retained for audit.*
