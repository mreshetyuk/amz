from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login.variables import user_name
from login.variables import password
from login.web_driver import  driver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time as t


def login():
    drv=driver()
    drv.get("https://www.amazon.com")
    #t.sleep(2)
    ActionChains(drv).move_to_element(drv.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]"))
    drv.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]").click()
    drv.find_element_by_xpath("//*[@id='ap_email']").send_keys(user_name())
    try:
        drv.find_element_by_xpath("//*[@id='ap_password']")
    except NoSuchElementException:
        drv.find_element_by_xpath("//*[@id='continue']").click()
    drv.find_element_by_xpath("//*[@id='ap_password']").send_keys(password())
    t.sleep(1)
    drv.find_element_by_xpath("//*[@id='signInSubmit']").click()
    drv.get("https://www.amazon.com")
    t.sleep(20)

    #drv.quit()

login()
