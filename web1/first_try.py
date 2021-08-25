from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


df = pd.DataFrame(
    columns=[
        "Name",
        "Postal Code",
        "Fax",
        "Diary District",
        "Email",
        "Address",
        "Phone",
        "Court Box",
        "Url",
    ]
)

df.to_excel("output.xlsx")

driver = webdriver.Chrome("D:\\upa\\downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx")
try:
    eng = driver.find_element_by_name("ctl00$ctl17")
    ActionChains(driver).move_to_element(eng).click(eng).perform()
except:
    pass

out = driver.execute_script("ASPx.GVPagerOnClick('ctl00_ContentPlaceHolder1_LawyersGrid','PN7');")

entries = 0


for page in range(0, 51):
    for ind, _ in enumerate(driver.find_elements_by_class_name("dxb-hb"), 0):
        try:
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
                )
            except:
                driver.quit()
                df.to_excel("output.xlsx")
                exit(0)

            driver.execute_script(f"ASPx.GVPagerOnClick('ctl00_ContentPlaceHolder1_LawyersGrid','PN{page}');")
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'input'))
                )
            except:
                driver.quit()
                df.to_excel("output.xlsx")
                exit(0)
                # ctl00_ContentPlaceHolder1_NameLabel
            element = driver.find_elements_by_class_name("dxb-hb")[ind]
            ActionChains(driver).move_to_element(element).click(element).perform()
            entries += 1
            try:
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
                )
            except:
                driver.quit()
                df.to_excel("output.xlsx")
                exit(0)
            print(
                f"Entry:{entries}, Name: {driver.find_element_by_id('ctl00_ContentPlaceHolder1_TxtName_I').get_attribute('value')}"
            )
            df.append(
                {
                    "Name": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtName_I"
                    ).get_attribute("value"),
                    "Postal Code": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtPostalCode_I"
                    ).get_attribute("value"),
                    "Fax": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtFax_I"
                    ).get_attribute("value"),
                    "Diary District": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtDistrict_I"
                    ).get_attribute("value"),
                    "Email": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtEmail_I"
                    ).get_attribute("value"),
                    "Address": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtAddress_I"
                    ).get_attribute("value"),
                    "Phone": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtPhone_I"
                    ).get_attribute("value"),
                    "Court Box": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtCourtBox_I"
                    ).get_attribute("value"),
                    "Url": driver.find_element_by_id(
                        "ctl00_ContentPlaceHolder1_TxtUrl_I"
                    ).get_attribute("value")
                    or None,
                }, ignore_index=True
            )
            driver.back()
        except Exception as e:
            print(e)
            continue

df.to_excel("output.xlsx")


#---------------------------------------------------------------------------------------------


# breakpoint()

# driver.execute_script("window.history.go(-1)")
# for ind,_ in enumerate(driver.find_elements_by_class_name('dxb-hb'),0):
#     element = driver.find_elements_by_class_name('dxb-hb')[ind]
#     print(element.get_attribute('id'))

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
