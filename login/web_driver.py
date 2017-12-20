from selenium import webdriver
from login.variables import chrome_driver_path

def driver():
    driver=webdriver.Chrome(chrome_driver_path())
    return driver


