from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(5)

driver.get("https://www.spicejet.com")
time.sleep(3)
driver.maximize_window()
login=driver.find_element(By.ID,'ctl00_HyperLinkLogin')
act_chains=ActionChains(driver)
act_chains.move_to_element(login).perform()

spice_Club=driver.find_element(By.ID,'SpiceClub Members')
act_chains.move_to_element(spice_Club).perform()

member_login=driver.find_element(By.ID,'Member Login')
act_chains.move_to_element(member_login).perform()

time.sleep(5)
driver.quit()