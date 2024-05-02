import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# with sync_playwright() as syncPlay:
#         browser = syncPlay.firefox.launch(headless=False, slow_mo=500)
#         page = browser.new_page()
#         page.goto("http://playwright.dev")
#         print(page.title())
#         browser.close()

async def main():
        async with async_playwright() as asyncPlay:
                browser = await asyncPlay.chromium.launch(headless=False, slow_mo=2000)
                page = await  browser.new_page()
                await page.goto("http://playwright.dev")
                print(await page.title())
                await browser.close()

asyncio.run(main())