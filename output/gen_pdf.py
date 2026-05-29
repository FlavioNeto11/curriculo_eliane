# -*- coding: utf-8 -*-
import os, sys, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent.resolve()
HTML = (HERE / "portfolio.html").as_uri()
PDF_OUT = HERE / "portfolio_eliane_sindica_profissional.pdf"
SHOT_DIR = HERE / "_shots"
SHOT_DIR.mkdir(exist_ok=True)
make_shots = "--shots" in sys.argv

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width":794,"height":1123}, device_scale_factor=2)
    page.goto(HTML, wait_until="networkidle")
    page.emulate_media(media="print")
    try:
        page.evaluate("document.fonts.ready")
    except Exception:
        pass
    page.wait_for_timeout(900)

    # PDF
    page.pdf(path=str(PDF_OUT), width="210mm", height="297mm",
             print_background=True, prefer_css_page_size=True,
             margin={"top":"0","right":"0","bottom":"0","left":"0"})
    print("PDF:", PDF_OUT, os.path.getsize(PDF_OUT)//1024, "KB")

    # Also publish a copy to the repository root (final deliverable location)
    import shutil
    root_copy = HERE.parent / PDF_OUT.name
    shutil.copy(str(PDF_OUT), str(root_copy))
    print("Copied to repo root:", root_copy)

    if make_shots:
        n = page.locator("section.page").count()
        print("pages:", n)
        for i in range(n):
            el = page.locator("section.page").nth(i)
            el.screenshot(path=str(SHOT_DIR / f"page_{i+1:02d}.png"))
        print("shots written to", SHOT_DIR)
    browser.close()
