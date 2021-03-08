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
    browser.back() # Returns the previous page.
    time.sleep(2)
    browser.refresh() # Refreshes the page.
    browser.set_window_size(1000,500)
    time.sleep(2)
    browser.maximize_window() # Full-Screen Mode.
    browser.save_screenshot("tutorial.png") # Takes screenshot.
    browser.close() # Closes the current page.

basics()