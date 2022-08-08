from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

with open("config.json",mode="r",encoding="utf-8") as file:
    data = json.load(file)
driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get('https://www.cakeresume.com/jobs')
#檢查篩選欄台灣
back_frontPage = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/header/div/ul/li[1]/a')
place_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[1]/button')
place_element.click()
taiwan_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div')
taiwan_element.click()
time.sleep(2)
count = 1
a = []
while count <= 10:
    label_place = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(count)+']/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/a')
    get_label_text = label_place.text
    if data["taiwan"] in get_label_text or data["taiwanEg"] in get_label_text:
        a.append("成功")
        count += 1 
    else:
        a.append("失敗")
        count += 1
if "失敗" in a:
    print("篩選台灣失敗")
else:
    print("篩選台灣成功")
back_frontPage.click()
time.sleep(2)

#驗證進階選項
answer = ['地點','職務類別','工作型態','資歷','年資','薪資','管理責任','遠端工作','公司規模','公司產業','公司使用技術','職缺描述語言']
advanced_search = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[4]/button')
advanced_search.click()
fieldFilter = driver.find_elements(By.CLASS_NAME,'JobSearchPage_searchFilter__u5x7s')
a = []
for x in fieldFilter:
    a.append(x.text)
if a == answer:
    print("進階篩選驗證成功")
else:
    print("進階篩選驗證錯誤")

#驗證精簡排版
gear_button_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]')
gear_button_element.click()
typesetting_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/ul/li[2]/div/div[1]/div')
typesetting_button.click()
time.sleep(2)
if driver.find_elements(By.CLASS_NAME,'JobSearchItem_description__tNSbN'):
    print("精簡排版失敗")
else:
    print("精簡排版成功")

# 驗證頁面網址正確
driver.execute_script("scroll(0,100000)")
formFeed_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[7]/div/a[2]')
formFeed_element.click()
time.sleep(2)
pageUrl_element = driver.find_element(By.XPATH,'/html/head/link[2]')
grab_pageUrl = pageUrl_element.get_attribute('href')
if grab_pageUrl == data["PageUrl"]:
    print("頁面網址成功")
else:
    print("頁面網址不對")

#驗證最新時間
menuElement = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div[1]/button')
menuElement.click()
latestButton = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/ul/li[2]')
latestButton.click()
time.sleep(2)
x = 1
a = []
while x <= 10:
    if driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(x)+']/div/div[2]/div[2]/div[1]/div/div[2]'):
        y = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(x)+']/div/div[2]/div[2]/div[1]/div/div[2]').text
        if "分鐘" in y:
            a.append(int(y.split()[0])*60)
        elif "小時" in y:
            a.append(int(y.split()[1])*60*60 )
        else:
            a.append(int(y.split()[1])*24*60*60)
        x = x+1
    else:
        y = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(x)+']/div/div[2]/div[2]/div[1]/div[1]/div[2]').text
        if "分鐘" in y:
            a.append(int(y.split()[0])*60)
        elif "小時" in y:
            a.append(int(y.split()[1])*60*60 )
        else:
            a.append(int(y.split()[1])*24*60*60)
        x = x+1
if sorted(a) == a:
    print("最新時間成功")
else:
    print("時最新時間失敗")

#驗證公司篩選
company_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/a')
company_button.click()
time.sleep(2)
if driver.find_elements(By.CLASS_NAME,'Button_button__N4TAn Button_buttonSecondary__IeCFQ Button_buttonMedium__G0RRs Button_buttonIconLeft__DAz5D'):
    print("公司篩選失敗")
else:
    print("公司篩選成功")
back_frontPage = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/header/div/ul/li[1]/a')
back_frontPage.click()
time.sleep(2)
reset = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[3]/div[2]/button[1]')
reset.click()
time.sleep(2)

# 驗證篩選欄實習生・實習，全職・初階
filterField = {
    "intern":{
        "element":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/div[1]/button',
        "check":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/div[2]/div/div/div/div/div[3]/div',
        "comparison":'實習生・實習'
    },
    "elementary":{
        "element":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div[1]/button',
        "check":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div[2]/div/div/div/div/div[1]/div',
        "comparison":'全職・初階'
    }
}
for index,add in filterField.items():
    driver.find_element(By.XPATH,filterField[index]["element"]).click()
    driver.find_element(By.XPATH,filterField[index]["check"]).click()
    time.sleep(2)
    limit = 1
    a = []
    while limit <= 10:
        label = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+ str(limit)+']/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]')
        labelTittle = label.text.replace('\n','')
        if filterField[index]["comparison"] == labelTittle:
            a.append("成功")
            limit += 1 
        else:
            a.append("失敗")
            limit += 1
    back_frontPage = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/header/div/ul/li[1]/a')
    back_frontPage.click()
    time.sleep(2)
    if "失敗" in a:
        print("篩選"+add["comparison"]+"失敗")
    else:
        print("篩選"+add["comparison"]+"成功")

# 驗證搜尋功能正確
searchElement = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input')
searchElement.send_keys(data["searchVerification"]["searchName"])
searchElement.send_keys(Keys.RETURN)
time.sleep(2)
count = 1
a = []
grab_subtitle = driver.find_elements(By.CLASS_NAME,'JobSearchItem_companyName__QKkj5')
for x in grab_subtitle:
    if x.text == data["searchVerification"]["companyName"]:
        a.append("成功")
        count+=1
    else:
        a.append("失敗")
        count+=1
if "失敗" in a:
    print("搜尋功能失敗")
else:
    print("搜尋功能成功")
#驗證職缺標題跟內容頁標題一致
first_field_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/a')
first_field_text = first_field_element.text
first_field_element.click()
driver.switch_to.window(driver.window_handles[1])
pagination_title_element = driver.find_element(By.CLASS_NAME,'JobDescriptionLeftColumn_title__heKvX')
pagination_title_text = pagination_title_element.text
if first_field_text == pagination_title_text:
    print("職缺標題跟內容頁標題成功")
else:
    print("職缺標題跟內容頁標題失敗")
driver.quit()

