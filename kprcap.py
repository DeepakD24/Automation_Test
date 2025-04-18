import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://cap.kpriet.ac.in/login")


username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='input-0']"))
)
username_input.send_keys("22EE046")

pass_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='input-2']"))
)
pass_input.send_keys("20/12/2004")

sign=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='form']/div[3]/button"))
)
sign.click()
time.sleep(3)
#driver.back()
alerts=driver.switch_to.alert
alerts.accept()
time.sleep(2)
print("Signin success")