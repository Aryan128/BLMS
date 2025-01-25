import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver=driver
    def enter_uname(self,uname):
        a=self.driver.find_element(By.XPATH,'//*[@id="username"]')
        a.send_keys(uname)
    def enter_pass(self,passw):
        b=self.driver.find_element(By.XPATH,'//*[@id="password"]')
        b.send_keys(passw)
    def signin_button(self):
        self.driver.find_element(By.XPATH,'//*[@id="loginbtn"]').click()
    def click_on_course(self):
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/a/span[3]').click()
    # def sub_link(self):
    #     self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[4]/div[3]/ul/li[6]/div/div/div[2]/div[1]/a/span").click()
    #     time.sleep(6)
    #     self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/section/div[1]/div[2]/div[2]/div[1]/form/button'))
    # def submission(self):
    #     ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/section/div[1]/div[2]/form/div[2]/div[2]/fieldset/div/div[2]/div[1]/div[1]/div[1]/a/i')).click().perform()
    # def drag_and_drop(self):
    #     self.driver.find_element(By.LINK_TEXT, 'Wikimedia').click()
    #     self.driver.find_element(By.NAME, 'wikimedia_keyword').send_keys("test_py")
    #     self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.CSS_SELECTOR, '#yui_3_17_2_1_1737041768056_1040"]'))
