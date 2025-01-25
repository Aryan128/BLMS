import time

from Pages.home_page import Testhomepage
import pytest
from selenium import webdriver
from Pages.LOgin_page import Login
from Pages.sub_link import TestSublink

@pytest.fixture(scope="class")
def driver():
    driver=webdriver.Firefox()
    driver.get("https://online.btes.co.in/login/index.php")
    yield driver
    driver.quit()
@pytest.mark.parametrize("uname,passwd",[("aryan@123","Aryan@123")])
def test_hp(driver,uname,passwd):
    t = Testhomepage(driver)
    l = Login(driver)
    s = TestSublink(driver)
    t.valid_login_page(uname,passwd)
    time.sleep(15)
    l.click_on_course()
    s.sub_link()
    expected = driver.title
    assert driver.title == expected, "Failed to fetch."


