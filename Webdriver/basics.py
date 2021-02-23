from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\\selenium-java\\chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)

driver.find_element(By.NAME,'q').send_keys("naveen automationlabs")


listofoptions=driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(listofoptions))

for ele in listofoptions:
    print(ele.text)
    if ele.text=="naveen automationlabs youtube":
        ele.click()
        break


time.sleep(5)
driver.quit()