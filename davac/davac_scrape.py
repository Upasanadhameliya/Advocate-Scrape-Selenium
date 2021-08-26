from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\\upa\\downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("http://vyhledavac.cak.cz")
driver.find_element_by_link_text("English").click()
time.sleep(1)
element = driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Search')]")
ActionChains(driver).move_to_element(element).click(element).perform()
time.sleep(10)
driver.get("http://vyhledavac.cak.cz/Home/SearchResult?page=1&pageSize=40000")
# http://vyhledavac.cak.cz/Home/SearchResult?page=1&pageSize=40000
