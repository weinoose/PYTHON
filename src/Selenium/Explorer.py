from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

def imdb():
    # Full-Screen Mode.
    browser.maximize_window()
    browser.get("https://www.imdb.com/chart/top/")
    sleep(1)
    browser.find_element_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr[47]/td[2]/a").click()
    sleep(1)
    # Saves a screenshot.
    browser.save_screenshot("movie(47).png")
    sleep(1)
    # Returns to the previous page.
    browser.back()
    sleep(1)
    browser.find_element_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a").click()
    sleep(1)
    browser.save_screenshot("movie(1).png")
    sleep(1)
    # Closes the current tab.
    browser.close()

imdb()