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
        "The form of practicing the legal profession",
        "Origin of a lawyer",
        "Court Appointment",
        "Legal specialisation",
        "Language",
        "www",
        "E-mail",
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
        "www",
        "E-mail",
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

lf_col_name_map = {
    "LF Name": "Name",
    "LF ID": "Identification Number",
    "LF Address": "Address",
    "LF contacts": "Contacts",
    "LF www": "www",
    "LF email": "E-mail",
    "LF other emails": "Other E-mails",
    "LF Phone": "Phone",
    "LF Other Phone": "Other Phones",
    "LF Mobile": "Mobile",
    "LF Fax": "Fax",
}

tr_col_list = [
    "Name",
    "Registration Number",
    "Status",
    "Language",
    "Contacts",
    "www",
    "E-mail",
]

la_col_list = [
    "Name",
    "Registration Number",
    "Identification Number",
    "ID Databox",
    "Status",
    "The form of practicing the legal profession",
    "Origin of a lawyer",
    "Court Appointment",
    "Legal specialisation",
    "Language",
    "Contacts",
    "www",
    "E-mail",
    "Phone",
]


def store_data(driver, row, row_count, row_type, *args):
    if args:
        row.find_element_by_tag_name("a").send_keys(Keys.CONTROL + Keys.RETURN)
        row_type.append(("LW" if bool(args[0]) else "LT"))
        return (row_count + 1), row_type
    return row_count, row_type


def get_lf_dict(table):
    lf_text = [
        td_tag.text
        for tr_tag in table.find_elements_by_tag_name("tr")
        for td_tag in tr_tag.find_elements_by_tag_name("td")
    ]
    lf_dict = {
        col_lbl: (
            "".join(
                lf_text[(lf_text.index(current_ind) + 1) : (lf_text.index(next_ind))]
            )
        )
        if (next_ind is not None)
        else ("".join(lf_text[(lf_text.index(current_ind) + 1) : (len(lf_text))]))
        for col_lbl, current_ind, next_ind in zip(
            list(lf_col_name_map.keys()),
            list(lf_col_name_map.values()),
            (list(lf_col_name_map.values())[1:] + [None]),
        )
    }
    del lf_dict["LF contacts"]
    return lf_dict


def get_trainee_dict(table):
    tr_text = [
        td_tag.text
        for tr_tag in table.find_elements_by_tag_name("tr")
        for td_tag in tr_tag.find_elements_by_tag_name("td")
    ]

    tr_dict = {
        current_ind: (
            "".join(
                tr_text[(tr_text.index(current_ind) + 1) : (tr_text.index(next_ind))]
            )
        )
        if (next_ind is not None)
        else ("".join(tr_text[(tr_text.index(current_ind) + 1) : (len(tr_text))]))
        for current_ind, next_ind in zip(tr_col_list, (tr_col_list[1:] + [None]))
    }
    del tr_dict["Contacts"]
    return tr_dict


def get_lawyer_dict(table):
    la_text = [
        td_tag.text
        for tr_tag in table.find_elements_by_tag_name("tr")
        for td_tag in tr_tag.find_elements_by_tag_name("td")
    ]
    la_dict = {
        current_ind: (
            "".join(
                la_text[(la_text.index(current_ind) + 1) : (la_text.index(next_ind))]
            )
        )
        if (next_ind is not None)
        else ("".join(la_text[(la_text.index(current_ind) + 1) : (len(la_text))]))
        for current_ind, next_ind in zip(la_col_list, (la_col_list[1:] + [None]))
    }
    del la_dict["Contacts"]
    return la_dict


def add_legal_trainee(driver):
    print("Legal Trainee")
    global legal_trainee_df
    tables = driver.find_elements_by_tag_name("table")
    tr_dict = get_trainee_dict(tables[1])
    legal_trainee_df = legal_trainee_df.append(
        dict(tr_dict, **get_lf_dict(tables[2])), ignore_index=True
    )


def add_lawyer(driver):
    print("Lawyer")
    global lawyer_df
    tables = driver.find_elements_by_tag_name("table")
    la_dict = get_lawyer_dict(tables[1])
    lawyer_df = lawyer_df.append(
        dict(la_dict, **get_lf_dict(tables[-1])), ignore_index=True
    )


row_count, row_type = 0, []

func_dict = {"LT": add_legal_trainee, "LW": add_lawyer}

try:
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
            for i in range(0, row_count):
                driver.switch_to.window(driver.window_handles[-1])
                func_dict[row_type[i]](driver)
                driver.close()
            row_count, row_type = 0, []
            driver.switch_to.window(driver.window_handles[-1])
finally:
    legal_trainee_df.to_excel("trainee_abrupt.xlsx")
    lawyer_df.to_excel("lawyers_abrupt.xlsx")
legal_trainee_df.to_excel("trainee.xlsx")
lawyer_df.to_excel("lawyers.xlsx")
# breakpoint()
