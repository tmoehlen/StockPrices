from splinter import Browser
import time
import netrc


with Browser('chrome') as browser:
    # Visit URL
    url = "https://finance.yahoo.com/quote/TWLO?p=TWLO"
    browser.visit(url)

    # Interact with elements

    Filter = browser.find_by_id('quote-header-info')
    find_h = browser.find_by_css('div[class="Trsdu"]')
    find_h.click()
    print(find_h)
    Filter.click()
    time.sleep(2)
