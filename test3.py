
from playwright.sync_api import sync_playwright


with sync_playwright() as syncPlay:
    browser = syncPlay.chromium.launch(headless=False, slow_mo=2000)
    page =  browser.new_page()
    page.goto("http://playwright.dev")
    page.screenshot(path="./screenshots/snap.png")
    browser.close()