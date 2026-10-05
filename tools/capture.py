"""Headless capture of docs/preview.html -> assets/preview.png using Playwright if available, else report skip."""
import pathlib, sys
OUT = pathlib.Path("assets/preview.png")
HTML = pathlib.Path("docs/preview.html").resolve()
def main():
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"SKIP playwright not installed: {e}")
        return 0
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception as e:
            print(f"SKIP browser launch failed (run: python -m playwright install chromium): {e}")
            return 0
        pg = b.new_page(viewport={"width":1280,"height":900})
        pg.goto(f"file://{HTML}", wait_until="networkidle")
        pg.wait_for_timeout(2500)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        pg.screenshot(path=str(OUT), full_page=True)
        b.close()
        print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0
if __name__ == "__main__": sys.exit(main())
