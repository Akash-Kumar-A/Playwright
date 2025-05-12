#attribute method
from playwright_basic import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Main_Page")    
    #XPath LOCATOR
    #xpath->'//tagname[@attribute="value"]')
    login_but = page.wait_for_selector('#pt-login-2')
    login_but.click()
    username_input = page.wait_for_selector('//input[@name="wpName"]')
    username_input.type('Akdemo123')
    password_input = page.wait_for_selector('//input[@name="wpPassword"]')
    password_input.type('Akdemo@123')
    login_button = page.wait_for_selector('//button[@name="wploginattempt"]')
    login_button.click()
    page.wait_for_timeout(5000)