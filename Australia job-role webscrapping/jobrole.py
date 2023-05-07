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
driver.get("https://www.seek.com.au/career-advice/explore-careers")
time.sleep(4)
v=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div[3]/div[2]/div/div/div/div[4]/div/div")
v.click()
time.sleep(4)
element = driver.find_element_by_class_name("css-1h7evr6")
all_options = element.find_elements_by_tag_name("a")
for option in all_options:
    all_links.append(option.get_attribute("href"))
    
all_links2=[]
for links in all_links:
    driver= webdriver.Chrome()
    driver.get(links)
    time.sleep(3)
    element1 = driver.find_elements_by_class_name("css-1d11irs")
    for element2 in element1:
        print(element2.text)
        all_links2.append(element2.text)
    driver.close()
for links3 in all_links2:
    file = pd.ExcelFile('List_of_Jobs.xlsx')
    df = pd.read_excel(file)
    df1 = pd.DataFrame(df)
    row_to_add = pd.DataFrame({'List of Job roles':[links3]})
    df_final = df1.append(row_to_add, ignore_index=True)
    datatoexcel= pd.ExcelWriter('List_of_Jobs.xlsx',engine='xlsxwriter')
    df_final.to_excel(datatoexcel,sheet_name='sheet1',index = False)
    datatoexcel.save()
