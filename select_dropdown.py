from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    
    # Select an option from a dropdown
    dropdown_select = page.query_selector('//input[@id="vector-main-menu-dropdown-checkbox"]')
    page.wait_for_timeout(3000)
    #dropdown_select.select_option(label="Random article")
    page.wait_for_timeout(5000)
    #dropdown_select.select_option('//input[@id="vector-main-menu-dropdown-checkbox"]',value="Special:Random")
    