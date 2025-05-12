from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://github.com/")
    print("page successfully opened")
    print(page.title())
    page.screenshot(path="A:\CBOTS INTERNSHIP\GITHUB\Playwright\screenshots\github.png")
    page.wait_for_timeout(5000)
