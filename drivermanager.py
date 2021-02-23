from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

Browsername="chrome1"
if Browsername=="chrome":
    driver= webdriver.Chrome(ChromeDriverManager().install())
elif Browsername=="FF":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif Browsername == "IE":
    driver = webdriver.Ie(IEDriverManager().install())
else:
    print("Enter correct browser \t " + Browsername)
    raise Exception("Incorrect entry")

driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)