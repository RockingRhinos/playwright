import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  # slow_mo=500
    context = browser.new_context()
    page = context.new_page()
    # page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()  # click(timeout=3000)
    page.click("text=Log In")


    page.get_by_role("button", name="Sign up with email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    # page.fill('input:below(:text("Email"))', "test")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_label("Password").press("Enter")

    # page.get_by_role("link", name="Shop Women").first
    # locator("xpath=//wow-image").nth(1)

    # page.pause()
    # expect(page.get_by_role("button", name="Sign Up")).to_be_disabled()

    # product = page.get_by_text('$85').first.locator('xpath=../../../../..//h3').text_content()
    # page.pause()
    # assert product == "Shoes"
    # print(product)

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            assert 'shoe' in link.text_content()


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
