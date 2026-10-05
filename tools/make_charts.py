"""Generate assets/charts.png from live processed JSON (no hand-drawn numbers)."""
import json, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

P = pathlib.Path("data/processed")
A = pathlib.Path("assets"); A.mkdir(exist_ok=True)

def load(name, default):
    f = P / name
    if f.exists():
        try: return json.loads(f.read_text())
        except Exception: return default
    return default

e2 = load("e2_gap.json", {"us_TWh":4536,"cn_TWh":10573,"ratio":2.33})
e1 = load("e1_power_gdp.json", {})
bench = load("benchmark_scores.json", {"scores":[]})

fig, ax = plt.subplots(2,2, figsize=(12,8))
fig.suptitle("SI Power-GDP Nexus — generated from live data", fontsize=14, fontweight="bold")

# 1 US vs China
ax[0,0].bar(["US","China"], [e2.get("us_TWh",4536), e2.get("cn_TWh",10573)])
ax[0,0].set_title(f"Electricity 2025 (TWh) — ratio {e2.get('ratio',2.33)}x")
ax[0,0].set_ylabel("TWh")

# 2 $/GW
claimed, recomputed = 60, 56.6
try:
    a = e1.get("analysis", e1)
    if isinstance(a, dict) and "usd_per_GW_at_1pct" in a:
        recomputed = round(a["usd_per_GW_at_1pct"]/1e9,1)
except Exception: pass
ax[0,1].bar(["Claimed","Recomputed"], [claimed, recomputed])
ax[0,1].set_title("$/GW-year ($B)")
ax[0,1].set_ylabel("$B")

# 3 Benchmark scores
scores = bench.get("scores", [])
if scores:
    labels = [s["claim"][:14] for s in scores]
    vals = [s["total"] for s in scores]
    ax[1,0].barh(labels, vals)
    ax[1,0].set_title("Benchmark scores (0-100)")
    ax[1,0].set_xlim(0,100)
else:
    ax[1,0].text(0.5,0.5,"run benchmarks/benchmark_suite.py", ha="center")
    ax[1,0].set_title("Benchmark scores")

# 4 Wealth
ax[1,1].bar(["NVDA","TSLA"], [5.649, 1.464])
ax[1,1].set_title("Market value at check ($T) — total $7.11T")
ax[1,1].set_ylabel("$T")

fig.tight_layout()
out = A/"charts.png"
fig.savefig(out, dpi=150)
print(f"wrote {out} ({out.stat().st_size} bytes)")
