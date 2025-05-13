from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   
    page.goto("https://example.com/")

#Script for Radio Button:
radio_button = page.query_selector('//input[@value="FeMale"]')
radio_button.click()
radio_button.check()
#Script for Checkbox:
checkbox = page.query_selector('//input[@value="Cricket"]')
checkbox.check()