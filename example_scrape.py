from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Remote("http://localhost:4444/wd/hub", options=webdriver.ChromeOptions())
browser2 = webdriver.Remote("http://localhost:4444/wd/hub", options=webdriver.ChromeOptions())


try:
  browser.get("https://tradedatamonitor.com")
  browser2.get('https://medium.com')
  # sleep(3000)
  sleep(120)
finally:
  browser.quit()
  browser2.quit()
