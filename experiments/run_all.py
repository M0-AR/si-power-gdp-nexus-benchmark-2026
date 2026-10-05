"""Run all experiments sequentially (avoid 429-style parallel fetch)."""
import subprocess, sys
ORDER = ["e1_power_gdp.py","e2_china_gap.py","e3_compute_per_watt.py","e4_jobs.py","e5_orbital.py","e6_safety.py","e7_market.py"]
import pathlib
for f in ORDER:
    print(f"\n===== {f} =====")
    r = subprocess.run([sys.executable, f"experiments/{f}"], capture_output=False)
    if r.returncode != 0: print(f"WARN {f} exit {r.returncode}")
print("\nAll done. See data/processed/*.json")
