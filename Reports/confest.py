import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get("https://online.btes.co.in/login/index.php")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("aryan@123")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Aryan@123")
driver.find_element(By.XPATH,'//*[@id="loginbtn"]').click()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/a/span[3]').click()
print(driver.title)
driver.maximize_window()
driver.find_element(By.XPATH,
                         "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[4]/div[3]/ul/li[6]/div/div/div[2]/div[1]/a/span").click()
time.sleep(6)
a=driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/section/div[1]/div[2]/div[2]/div[1]/form/button')
driver.execute_script("arguments[0].click();",a)
print("1 ",driver.title)
time.sleep(6)
b=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/section/div[1]/div[2]/form/div[2]/div[2]/fieldset/div/div[2]/div[1]/div[1]/div[1]/a/i')
ActionChains(driver).click(b).perform()
print("2 ",driver.title)
# driver.find_element(By.LINK_TEXT,'Wikimedia').click()
# driver.find_element(By.NAME,'wikimedia_keyword').send_keys("test_py")
#
# d=driver.find_element(By.CSS_SELECTOR,'#yui_3_17_2_1_1737041768056_1040"]')
# driver.execute_script("arguments[0].click()",d)



