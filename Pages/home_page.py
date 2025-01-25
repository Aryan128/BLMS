import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Testhomepage:
    def __init__(self,driver):
        self.driver=driver
        self.username = '//*[@id="username"]'
        self.password = '//*[@id="password"]'
        self.signin='//*[@id="loginbtn"]'
    def valid_login_page(self,uname, passwd):
        self.driver.find_element(By.XPATH,self.username).send_keys(uname)
        self.driver.find_element(By.XPATH,self.password).send_keys(passwd)
        self.driver.find_element(By.XPATH,self.signin).click()



