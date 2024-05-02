import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.get_by_label("Top languages").click()
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("dogs")
    page.get_by_label("Search Wikipedia").press("Enter")
    page.screenshot(path="snap.png")
    context.tracing.stop(path="./videos & Screenshots/trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
