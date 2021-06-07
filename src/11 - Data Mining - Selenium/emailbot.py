from selenium import webdriver
from database import gmail, gmail_password
import smtplib
from selenium.common.exceptions import NoSuchElementException

def sendMail(msg):
    sender = gmail
    reciever = "emiryarkinyaman@gmail.com"
    password = gmail_password

    server = smtplib.SMTP("smtp.gmail.com:587") # Creating the Server.
    server.starttls() # Starting the Server.
    server.login(sender, password) # Login Process.
    server.sendmail(sender, reciever, msg) # Sending Process.
    server.quit() # Quitting the Server.

try:
    webdriver.Chrome().get("https://instagram.com")
    webdriver.Chrome().find_element_by_xpath("xpath").click()
    webdriver.Chrome().refresh()
    print("Found!")
except (NoSuchElementException):
    print("Error!")
    sendMail("Access Denied...\nSent from Automation")