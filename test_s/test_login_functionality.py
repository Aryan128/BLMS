import time
import pytest
from Pages.LOgin_page import Login
from selenium import webdriver
@pytest.fixture(scope="class")
def driver():
    driver=webdriver.Firefox()
    driver.get("https://online.btes.co.in/login/index.php")
    yield driver
    driver.quit()

@pytest.mark.parametrize("uname,passw",[("aryan@123","Aaryan@123"), ("aryan@123","Aryan@123")])
def test_login_button(uname,passw,driver):
    login_b=Login(driver)
    login_b.enter_uname(uname)
    login_b.enter_pass(passw)
    login_b.signin_button()
    time.sleep(5)
    assert driver.title=="Dashboard" , "Failed to login"






