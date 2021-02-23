from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver=None
@pytest.fixture(scope='module')
def init__driver():
    global driver
    print("********************SETUP*****************")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    print("********************TEAR DOWN*****************")
    driver.quit()

def test_google_title(init__driver):
    assert driver.title=="Google"

def test_google_url(init__driver):
    assert driver.current_url=="https://www.google.com/"

