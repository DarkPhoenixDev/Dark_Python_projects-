from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.python.org/")
date_time = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
date_time1 = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events = {}

for n  in range(len(date_time)):
     events[n] = {
        "time" : date_time[n].text,
       "event":date_time1[n].text
    }
print(events)

driver.quit()
