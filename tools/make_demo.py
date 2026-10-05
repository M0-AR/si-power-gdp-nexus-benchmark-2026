"""Generate assets/demo.gif (terminal-style walkthrough) without screen recorder."""
import pathlib
from PIL import Image, ImageDraw, ImageFont
A = pathlib.Path("assets"); A.mkdir(exist_ok=True)
W,H = 900,420
frames=[]
texts=[
 "SI Power-GDP Nexus  |  live-verified 2026",
 "$ python experiments/run_all.py\n> E1 $56.6B/GW  E2 2.33x  E7 $7.11T",
 "$ pytest -q  &&  python benchmarks/benchmark_suite.py\n> 3 passed  |  Safety 93  Wealth 85",
 "Open docs/preview.html  ->  charts + scorecard\nCEO summary in 30 seconds. Done.",
]
try: font = ImageFont.load_default(size=22)
except: font = ImageFont.load_default()
for t in texts:
    img = Image.new("RGB",(W,H),(11,16,32))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([14,14,W-14,H-14], radius=18, outline=(36,48,86), width=2)
    d.text((40,60), t, fill=(110,231,255), font=font, spacing=10)
    d.text((40,H-70), "si-power-gdp-nexus-benchmark-2026  •  MIT", fill=(159,176,216), font=font)
    frames.append(img)
out = A/"demo.gif"
frames[0].save(out, save_all=True, append_images=frames[1:], duration=1400, loop=0)
print(f"wrote {out} ({out.stat().st_size} bytes)")
