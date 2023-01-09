import selenium
from selenium import webdriver
import time

print(dir(selenium))

browser = webdriver.Chrome()

def basics():
    browser.get("https://metacritic.com")
    time.sleep(2)
    browser.get("https://www.metacritic.com/browse/games/score/metascore/all/all/filtered")
    time.sleep(2)
    # Returns the previous page.
    browser.back()
    time.sleep(2)
    # Refreshes the page.
    browser.refresh()
    browser.set_window_size(1000,500)
    time.sleep(2)
    browser.maximize_window()
    browser.save_screenshot("tutorial.png")
    browser.close()

basics()