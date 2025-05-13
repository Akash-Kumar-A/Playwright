from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://psgtech.edu/")

    elements = page.query_selector_all('a')

    for i in elements:
        print(i.text_content())

    page.wait_for_timeout(5000)