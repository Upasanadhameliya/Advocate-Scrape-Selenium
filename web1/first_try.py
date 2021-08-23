from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("D:\\upa\\downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")


# for ind,_ in enumerate(driver.find_elements_by_class_name('dxb-hb'),0):
#     print(ind)
#     breakpoint()
try:
    eng = driver.find_element_by_name('ctl00$ctl17')
    # breakpoint()
    ActionChains(driver).move_to_element(eng).click(eng).perform()
except:
    pass


element = driver.find_element_by_class_name('dxb-hb')
# driver.implicitly_wait(10)
ActionChains(driver).move_to_element(element).click(element).perform()
    # # driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
# driver.implicitly_wait(10)
time.sleep(2)

# driver.execute_script("window.history.go(-1)")
# driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
# driver.navigate().to("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
driver.back()
# driver.implicitly_wait(10)

# breakpoint()
