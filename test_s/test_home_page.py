import time

from Pages.home_page import Testhomepage
import pytest
from selenium import webdriver
from Pages.LOgin_page import Login
class Testhp:
    @pytest.fixture(scope="class")
    def driver(self):
        driver=webdriver.Firefox()
        driver.get("https://online.btes.co.in/login/index.php")
        yield driver
        driver.quit()
    @pytest.mark.parametrize("uname,passwd",[("aryan@123","Aryan@123")])
    def test_hp(self,driver,uname,passwd):
        t = Testhomepage(driver)
        l = Login(driver)
        t.valid_login_page(uname,passwd)
        time.sleep(5)
        l.click_on_course()
        assert driver.title == "Course: SDET with Python-AI for IT&R"
        time.sleep(5)


