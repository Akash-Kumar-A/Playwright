#XPATH -> CONTAINS method
from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    #XPath contains method 
    #ATTRIBUTE -> '//TAGNAME[contains(@attribute,"value")]'
    #TEXT -> '//TAGNAME[contains(text(),"value")]'
    login_but = page.wait_for_selector('//span[contains(text(),"Log in")]').click() #->text method
    page.wait_for_timeout(3000)


#FAMILY CONCEPTS
#FATHER -> '//TAGNAME[@ATTRIBUTE="VALUE"]/PARENT::TAGNAME[]'
#CHILDREN -> '//TAGNAME[@ATTRIBUTE="VALUE"]/CHILD::TAGNAME[]'
#ANCESTOR -> '//TAGNAME[@ATTRIBUTE="VALUE"]/ANCESTOR::TAGNAME[]'
#SIBLINGS -> '//TAGNAME[@ATTRIBUTE="VALUE"]/FOLLOWING-SIBLING::TAGNAME[N]' N->index
