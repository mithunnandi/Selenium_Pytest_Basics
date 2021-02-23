from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def test_google():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")
    assert driver.title=="Google"
    driver.quit()

def test_amazon():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.com/")
    assert driver.title=="Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
    driver.quit()

def test_yahoo():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://in.yahoo.com/?p=us")
    assert driver.title=="Yahoo India | News, Finance, Cricket, Lifestyle and Entertainment"
    driver.quit()

def test_rediff():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.rediff.com/")
    assert driver.title=="Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()

