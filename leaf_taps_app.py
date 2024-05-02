import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://leaftaps.com/opentaps/control/main")
    page.get_by_label("Username").fill("demosalesmanager")
    page.get_by_label("Password").fill("crmsfa")
    print(page.title())
    page.get_by_role("button", name="Login").click()
    page.click()
    # crmsfa_text = page.get_by_role("link", name="CRM/SFA").text_content()
    page.get_by_role("link", name="CRM/SFA").click()
    page.get_by_role("link", name="Leads").click()

    all_shortcut_links = page.locator("xpath=//*[@class='shortcuts']//li").all()
    for shorcut_link in all_shortcut_links:
        shorcut_link.click()
        break
    leads_text = page.locator("xpath=//div[@id='sectionHeaderTitle_leads']").text_content()
    if 'Leads' in leads_text:
        assert 'Leads' in leads_text

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
