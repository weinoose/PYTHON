from selenium import webdriver
from database import gmail, gmail_password
import smtplib
from selenium.common.exceptions import NoSuchElementException

def sendMail(msg):
    sender = gmail
    reciever = "emiryarkinyaman@gmail.com"
    password = gmail_password
    # Creating the Server.
    server = smtplib.SMTP("smtp.gmail.com:587")
    # Starting the Server.
    server.starttls()
    # Login Process.
    server.login(sender, password)
    # Sending Process.
    server.sendmail(sender, reciever, msg)
    # Quitting the Server.
    server.quit()

try:
    webdriver.Chrome().get("https://instagram.com")
    webdriver.Chrome().find_element_by_xpath("xpath").click()
    webdriver.Chrome().refresh()
    print("Found!")
except (NoSuchElementException):
    print("Error!")
    sendMail("Access Denied...\nSent from Automation")