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

options = webdriver.ChromeOptions()
options.add_extension('adblocker.crx')
driver= webdriver.Chrome(options=options)
driver.get("https://www.listcompany.org/Australia_Country.html")

time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
all_links=[]
time.sleep(2)

    
while True:
    try:
        # time.sleep(2)
        element = driver.find_element_by_class_name("body")
        all_options = element.find_elements_by_tag_name("a")
        for option in all_options:
            all_links.append(option.get_attribute("title"))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        v=driver.find_element_by_link_text("Next")
        v.click()
        # print(all_links)
    except:
        # pass
        break
        
print(all_links)
for links in all_links:
    print(links)
    file = pd.ExcelFile('List of company.xlsx')
    df = pd.read_excel(file)
    df1 = pd.DataFrame(df)
    row_to_add = pd.DataFrame({'List of company':[links]})
    df_final = df1.append(row_to_add, ignore_index=True)
    datatoexcel= pd.ExcelWriter('List of company.xlsx',engine='xlsxwriter')
    df_final.to_excel(datatoexcel,sheet_name='sheet1',index = False)
    datatoexcel.save()
    


# while True:
#     try:
#         time.sleep(2)
#         element = driver.find_element_by_class_name("body")
#         all_options = element.find_elements_by_tag_name("a")
#         for option in all_options:
#             all_links.append(option.get_attribute("title"))
                
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         v=driver.find_element_by_link_text("Next")
#         v.click()
#     except:
#         pass
    
#     print(all_links)
    