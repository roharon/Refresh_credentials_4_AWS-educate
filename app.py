from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
import lxml


AWS_VOCAREUM_LOGIN_PAGE = "https://www.awseducate.com/signin/SiteLogin"
VOCAREUM_WELCOME_SITE = "https://labs.vocareum.com/main/"
AWS_ACCOUNT_SITE = "https://www.awseducate.com/student/s/awssite"

AWS_ID = ""
AWS_PW = ""
with open("./account.json") as f:
    JSON_OBJECT = json.load(f)
    AWS_ID = JSON_OBJECT['user_email']
    AWS_PW = JSON_OBJECT['user_password']

def auto_login():
    browser = webdriver.Chrome("./chromedriver")
    browser.get(AWS_VOCAREUM_LOGIN_PAGE)

    browser.implicitly_wait(8)
    time.sleep(4)

    user_email = browser.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:username')
    user_pasword = browser.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:password')
    browser.implicitly_wait(10)

    user_email.send_keys(AWS_ID)
    user_pasword.send_keys(AWS_PW)

    #browser.find_element_by_class_name("btn btn-primary btn-block").submit()
    browser.implicitly_wait(10)
    browser.execute_script("trylogin(event)")
    browser.execute_script("trylogin(event)")
    browser.implicitly_wait(10)

    browser.get(AWS_ACCOUNT_SITE)

    time.sleep(10)
    #educate_startert_button = browser.find_element_by_class_name("btn")


"""
    html = browser.page_source

    soup = BeautifulSoup(html, lxml)

    key_span = soup.select('#clickeybox > pre > span')
    print(key_span)
"""

if __name__ == "__main__":
    #print(AWS_PW, AWS_ID)
    auto_login()


