import time
from selenium.webdriver.common.by import By
class TestSublink:
    def __init__(self,driver):
        self.driver=driver
    def sub_link(self):
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[4]/div[3]/ul/li[6]/div/div/div[2]/div[1]/a/span").click()
        time.sleep(6)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/section/div[1]/div[2]/div[2]/div[1]/form/button'))