from selenium import webdriver
import time
AWS_VOCAREUM_LOGIN_PAGE = "https://www.awseducate.com/signin/SiteLogin"



def auto_login():
    browser = webdriver.Chrome("./chromedriver")
    browser.get(AWS_VOCAREUM_LOGIN_PAGE)

    time.sleep(5)

    user_email = browser.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:username')
    user_pasword = browser.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:password')

    user_email.send_keys(AWS_ID)
    user_pasword.send_keys(AWS_PW)

    #browser.find_element_by_class_name("btn btn-primary btn-block").submit()
    user_pasword.send_keys(AWS_PW)
    user_pasword.send_keys(AWS_PW)
    user_pasword.send_keys(AWS_PW)

    login_button = browser.find_element_by_class_name("loginText")
    login_button.submit()

    browser.implicitly_wait(10)

    time.sleep(5)


if __name__ == "__main__":
    auto_login()


