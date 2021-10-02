from selenium import webdriver
from time import sleep
from database import username, password

class Instagram():
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def Login(self):
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(2)
        self.browser.get("https://instagram.com/nba")
        sleep(2)

    def Quit(self):
        self.browser.close()

instagram = Instagram(username, password)

instagram.Login()
instagram.Quit()