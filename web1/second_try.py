from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

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

out = driver.execute_script("WebForm_DoCallback('ctl00$MasterFirstLogInPopUpControl',arg,ASPx.Callback,'ctl00_MasterFirstLogInPopUpControl',ASPx.CallbackError,true);")
