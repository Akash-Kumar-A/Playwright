from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    #CSS LOCATOR id-># , class->. , attribute->['values']
    login_but = page.wait_for_selector('#pt-login-2')
    login_but.click()
    username_input = page.wait_for_selector('#wpName1')
    username_input.type('Akdemo123')
    password_input = page.wait_for_selector('#wpPassword1')
    password_input.type('Akdemo@123')
    login_button = page.wait_for_selector('#wpLoginAttempt')
    login_button.click()
    page.wait_for_timeout(5000)
    print("page successfully opened")
    
        