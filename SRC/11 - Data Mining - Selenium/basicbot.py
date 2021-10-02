from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

def imdb():
    browser.maximize_window() # Full-Screen Mode.
    browser.get("https://www.imdb.com/chart/top/")
    sleep(1)
    browser.find_element_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr[47]/td[2]/a").click()
    sleep(1)
    browser.save_screenshot("movie(47).png") # Saving the screenshot.
    sleep(1)
    browser.back() # Returns the previous page.
    sleep(1)
    browser.find_element_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a").click()
    sleep(1)
    browser.save_screenshot("movie(1).png") # Saving the screenshot.
    sleep(1)
    browser.close() # Closes the current page.

imdb()