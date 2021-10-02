from selenium import webdriver
from time import sleep

class LyricToSong():
    def __init__(self, title):
        self.browser = webdriver.Chrome()
        self.title = title

    def Proceed(self):
        self.browser.maximize_window()
        self.browser.get("https://findmusicbylyrics.com")
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="main_search_box"]').send_keys(self.title)
        self.browser.find_element_by_xpath('//*[@id="main_search_button"]').click()
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a/b/text()').get()
        sleep(2)

    def Quit(self):
        self.browser.close()

file = open("main.txt","r",encoding="UTF-8")
titlex = file.read()

lyrictosong = LyricToSong(titlex)

lyrictosong.Proceed()
lyrictosong.Quit()

file.close()