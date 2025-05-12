#XPATH -> CONTAINS method
from playwright_basic import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    #XPath contains method 
    #ATTRIBUTE -> '//TAGNAME[contains(@attribute,"value")]'
    #TEXT -> '//TAGNAME[contains(text(),"value")]'
    login_but = page.wait_for_selector('//span[contains(text(),"Log in")]').click()
    page.wait_for_timeout(3000)
