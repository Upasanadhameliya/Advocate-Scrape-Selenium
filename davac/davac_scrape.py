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
try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'searchGridTab')]"))
    )

except:
    print("Could not find table")
    exit(0)
driver.get("http://vyhledavac.cak.cz/Home/SearchResult?page=1&pageSize=40000")

table = driver.find_element_by_class_name("searchGridTab")
print(table)

table_rows = table.find_elements_by_tag_name('tr')
print("table_rows found!")

def store_data(*args):
    print(args)

for r_ind, row in enumerate(table_rows,1):
    store_data(*[cell.text for c_ind, cell in enumerate(row.find_elements_by_tag_name('td'),1) if c_ind !=6])
    if r_ind == 5: break
