import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
url="http://erp.kpriet.ac.in:8181/erpoperations/portal/StudentLoginV2.aspx"
driver.get(url)
driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID,'txt_rollno').send_keys("22EE016")
time.sleep(3)
driver.find_element(By.ID,'txt_password').send_keys("PA17112004")
time.sleep(3)

login=driver.find_element(By.ID,"btn_submit")
login.click()
time.sleep(5)

print("Success")
driver.quit()
