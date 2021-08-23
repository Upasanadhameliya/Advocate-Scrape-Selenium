from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("D:\\upa\\downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
try:
    eng = driver.find_element_by_name('ctl00$ctl17')
    ActionChains(driver).move_to_element(eng).click(eng).perform()
except:
    pass

entries = 0

for page in range(0,5):
    for ind,_ in enumerate(driver.find_elements_by_class_name('dxb-hb'),0):
        time.sleep(2)

        element = driver.find_elements_by_class_name('dxb-hb')[ind]
        ActionChains(driver).move_to_element(element).click(element).perform()
        entries += 1
        time.sleep(2)
        print(f"Page:{page+1}, Entry:{entries}, Name: {driver.find_element_by_id('ctl00_ContentPlaceHolder1_TxtName_I').get_attribute('value')}")
        driver.back()
        # driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        pg_element = driver.find_elements_by_class_name('dxp-num')[page]
        pg_element.click()
# breakpoint()

# ActionChains(driver).move_to_element(pg_element).click(pg_element).perform()

# try:
#     eng = driver.find_element_by_name('ctl00$ctl17')
#     ActionChains(driver).move_to_element(eng).click(eng).perform()
# except:
#     pass


# element = driver.find_element_by_class_name('dxb-hb')
# ActionChains(driver).move_to_element(element).click(element).perform()
# time.sleep(2)
# driver.back()


# driver.implicitly_wait(10)

# # driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
# driver.implicitly_wait(10)


# driver.execute_script("window.history.go(-1)")
# driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
# driver.navigate().to("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")

# driver.implicitly_wait(10)

# breakpoint()
