import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

# 1. Khai báo biến browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)


data=[]
# Read utl
idx=0
while True:
    print()
    url = 'https://f319.com'
    browser.get(url)

    # Set date
    end=browser.find_element("id", "end")
    end.clear()
    end.send_keys("{}-{}-{}".format())

    btn=browser.find_element("xpath", "/html/body/div[3]/main/div/form/div[2]/div/button[9]")
    btn.click()

    result=browser.find_elements(By.CLASS_NAME, "font-weight-bold.text-danger.col-12.d-block.p-1.m-0")
    for row in result:
        print(row.text)
        idx += 1
        data.append(row.text)

    # current_date -= timedelta(days=300)
    if idx>7305:
        break

df = pd.DataFrame(data, columns=['KQ'])
df.to_csv("XS_truyen_thong.csv", index=False)
browser.close()