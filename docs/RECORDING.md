# Recording a 2-minute demo that actually plays on GitHub

GitHub renders GIFs natively in READMEs but strips `<video>` tags. Use this pattern:

```markdown
[![2-min demo](assets/preview.png)](https://www.youtube.com/watch?v=VIDEO_ID)
![demo](assets/demo.gif)
```

## Steps

1. `python experiments/run_all.py` — terminal recording part 1 (30 s).
2. Scroll `docs/preview.html` (or the Pages URL) — part 2 (45 s).
3. `python tools/make_charts.py` — part 3 (15 s).
4. Record with any screen recorder (OBS, Loom, macOS Cmd+Shift+5).
5. Export GIF: 900 px wide, 15 fps, < 8 MB. Keep text readable: zoom to 125%.
6. Upload MP4 to YouTube (unlisted is fine), replace `VIDEO_ID` in README + preview.
7. Save GIF as `assets/demo.gif` (plays inline, no click needed).

## Why both?

- GIF = instant autoplay proof, no leaving GitHub.
- YouTube thumbnail = full narration + audio for those who click.

Keep the demo under 2 minutes: claim → command → chart → verdict.
