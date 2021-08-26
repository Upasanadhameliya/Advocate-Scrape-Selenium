from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

lawyer_df = pd.DataFrame(
    columns=[
        "Name",
        "Registration Number",
        "Identification Number",
        "ID Databox",
        "Status",
        "Form of profession",
        "Lawyer Origin",
        "Court Appointment",
        "Legal specialisation",
        "Language",
        "Website",
        "Email",
        "Phone",
        "LF Name",
        "LF ID",
        "LF Address",
        "LF www",
        "LF email",
        "LF other emails",
        "LF Phone",
        "LF Other Phone",
        "LF Mobile",
        "LF Fax",
    ]
)

legal_trainee_df = pd.DataFrame(
    columns=[
        "Name",
        "Registration Number",
        "Status",
        "Language",
        "Website",
        "Email",
        "LF Name",
        "LF ID",
        "LF Address",
        "LF www",
        "LF email",
        "LF other emails",
        "LF Phone",
        "LF Other Phone",
        "LF Mobile",
        "LF Fax",
    ]
)

# law_firm_df = pd.DataFrame(
#     columns=[
#         "Name",
#         "Postal Code",
#         "Fax",
#         "Diary District",
#         "Email",
#         "Address",
#         "Phone",
#         "Court Box",
#         "Url",
#     ]
# )


driver = webdriver.Chrome("D:\\upa\\downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("http://vyhledavac.cak.cz")
driver.find_element_by_link_text("English").click()
time.sleep(1)
element = driver.find_element(
    By.XPATH, "//button[@type='submit' and contains(., 'Search')]"
)
ActionChains(driver).move_to_element(element).click(element).perform()

try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, "//table[contains(@class, 'searchGridTab')]")
        )
    )
except:
    print("Could not find table")
    exit(0)
driver.get("http://vyhledavac.cak.cz/Home/SearchResult?page=1&pageSize=40000")

table = driver.find_element_by_class_name("searchGridTab")
print(table)

table_rows = table.find_elements_by_tag_name("tr")
print("table_rows found!")


def store_data(driver, row, row_count, row_type, *args):
    if args:
        row.find_element_by_tag_name("a").send_keys(Keys.CONTROL + Keys.RETURN)
        row_type.append(("LW" if bool(args[0]) else "LT"))
        return (row_count+1),row_type
    return row_count,row_type

row_count, row_type = 0,[]

for r_ind, row in enumerate(table_rows, 1):
    row_count, row_type = store_data(
        driver,
        row,
        row_count,
        row_type,
        *[
            cell.text
            for c_ind, cell in enumerate(row.find_elements_by_tag_name("td"), 1)
            if c_ind != 6
        ]
    )
    if r_ind % 10 == 0:
        for i in range(0,row_count):
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
        row_count, row_type = 0,[]
        driver.switch_to.window(driver.window_handles[-1])
        # if r_ind == 30:
            # break

# breakpoint()
