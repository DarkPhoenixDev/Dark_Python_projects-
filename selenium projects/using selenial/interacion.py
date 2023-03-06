from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


driver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
timeout = time.time() + 60
five_min = time.time() + 60*5 # 5minutes

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# text_1 = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# print(text_1.text)
# driver.get("https://www.appbrewery.co/p/newsletter")
# email = driver.find_element(By.NAME,"email")
# email.send_keys("hello")
# email.send_keys(Keys.ENTER)
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_elements(By.CSS_SELECTOR,".inset button" )

wait = WebDriverWait(driver, 100)
element = wait.until(EC.element_to_be_clickable((By.ID, '#bigCookie')))
print('n got clicked')



# cookie_run = True

# while cookie_run:
# #   for cook in cookie:
#     cookie.click()m
# #    cookie.click()
#     if time.time() > timeout:
#        cookie_run = False
#        cookie_sec = driver.find_element(By.ID,"#backgroundLeftCanvas")
# print(f"cokkie/sec : {cookie_sec.text}")


