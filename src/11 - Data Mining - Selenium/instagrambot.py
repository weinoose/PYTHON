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

    def GetPage(self):
        self.browser.get("https://www.instagram.com/cristiano/")
        sleep(2)

    def FollowUser(self):
        self.browser.find_element_by_tag_name('button').click()
        sleep(2)

    def UnFollowUser(self):
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
        sleep(2)

    def UnFollowCheck(self):
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
        sleep(2)

    def Quit(self):
        self.browser.close()

instagram = Instagram(username, password)

instagram.Login()
instagram.GetPage()
instagram.FollowUser()
instagram.UnFollowUser()
instagram.UnFollowCheck()
instagram.Quit()