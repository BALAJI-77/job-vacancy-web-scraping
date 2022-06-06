from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from openpyxl import Workbook
import pandas as pd

all_links=[]
driver= webdriver.Chrome()
driver.get("https://www.ibisworld.com/au/list-of-enterprise-profiles/")
time.sleep(15)
element = driver.find_element_by_class_name("core-profiles")
all_options = element.find_elements_by_tag_name("span")
for element2 in all_options:
    if element2.text != "*New*":
        all_links.append(element2.text)
        print(element2.text)

for links3 in all_links:
    print(links3)
    file = pd.ExcelFile('list_of_jobs_2.xlsx')
    df = pd.read_excel(file)
    df1 = pd.DataFrame(df)
    row_to_add = pd.DataFrame({'List of Job roles':[links3]})
    df_final = df1.append(row_to_add, ignore_index=True)
    datatoexcel= pd.ExcelWriter('list_of_jobs_2.xlsx',engine='xlsxwriter')
    df_final.to_excel(datatoexcel,sheet_name='sheet1',index = False)
    datatoexcel.save()