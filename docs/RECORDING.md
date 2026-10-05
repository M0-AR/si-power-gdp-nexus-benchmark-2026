# Recording a 2-minute demo — hosted directly in-repo

GitHub plays GIFs inline with no upload needed. We host the demo here:

```markdown
![site preview — hosted in-repo](assets/preview.png)
![2-min demo — hosted here](assets/demo.gif)
```

No video ID, no external link. Both files live in `assets/`.

## Steps

1. `python experiments/run_all.py` — terminal recording part 1 (30 s).
2. Scroll `docs/preview.html` (or the Pages URL) — part 2 (45 s).
3. `python tools/make_charts.py` — part 3 (15 s).
4. Record with any screen recorder (OBS, Loom, macOS Cmd+Shift+5).
5. Export GIF: 900 px wide, 15 fps, < 8 MB. Keep text readable: zoom to 125%.
6. Save as `assets/demo.gif` — done, it plays inline. No upload needed.

Keep the demo under 2 minutes: claim → command → chart → verdict.
