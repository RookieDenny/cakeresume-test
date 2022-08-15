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
#Check advanced search Is there a display
#檢查進階搜尋功能正確
answer = ['地點','職務類別','工作型態','資歷','年資','薪資','管理責任','遠端工作','公司規模','公司產業','公司使用技術','職缺描述語言']
advanced_search = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[4]/button')
advanced_search.click()
all_advanced_filter = driver.find_elements(By.CLASS_NAME,'JobSearchPage_searchFilter__u5x7s')
result = []
for x in all_advanced_filter:
    result.append(x.text)
if result == answer:
    print("Advanced screening verification succeeded")
else:
    print("Advanced screening validation errors")
driver.get('https://www.cakeresume.com/jobs')

#Check filter company whether succeed
#檢查篩選公司功能正確
company_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/a')
company_button.click()
time.sleep(2)
if driver.find_elements(By.CLASS_NAME,'Button_button__N4TAn Button_buttonSecondary__IeCFQ Button_buttonMedium__G0RRs Button_buttonIconLeft__DAz5D'):
    print("Company screening failed")
else:
    print("Company screened successfully")
driver.get('https://www.cakeresume.com/jobs')

#Check filter place taiwan whether succeed
#檢查篩選地點功能正確 - 台灣
place_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[1]/button')
place_element.click()
taiwan_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div')
taiwan_element.click()
time.sleep(2)
count = 1
while count <= 10:
    label_place = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(count)+']/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/a')
    get_label_text = label_place.text
    if data["taiwan"] in get_label_text or data["taiwanEg"] in get_label_text:
        if count == 10:
            print("Check filter Location Taiwan Success")
    else:
        print(get_label_text + "Does not include Taiwan")
        count +=10
    count += 1
driver.get('https://www.cakeresume.com/jobs')

#Check filter work type intern whether succeed
#檢查篩選工作型態功能正確 - 實習生
#Check filter seniority elementary whether succeed
#檢查篩選資歷功能正確 - 初階
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
    while limit <= 10:
        label = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+ str(limit)+']/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]')
        labelTittle = label.text.replace('\n','')
        if filterField[index]["comparison"] == labelTittle:
            if limit == 10:
                print("filter"+str(index)+"success")
        else:
            print(labelTittle + "失敗")
            limit += 10
        limit += 1
    driver.get('https://www.cakeresume.com/jobs')

#Check new sort whether succeed
#檢查最新功能正確
menuElement = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div[1]/button')
menuElement.click()
latestButton = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/ul/li[2]')
latestButton.click()
time.sleep(2)
count = 1
result = []
while count <= 10:
    if driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(count)+']/div/div[2]/div[2]/div[1]/div/div[2]'):
        list_time = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(count)+']/div/div[2]/div[2]/div[1]/div/div[2]').text
        if "分鐘" in list_time:
            result.append(int(list_time.split()[0])*60)
        elif "小時" in list_time:
            result.append(int(list_time.split()[1])*60*60 )
        else:
            result.append(int(list_time.split()[1])*24*60*60)
    else:
        y = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+str(count)+']/div/div[2]/div[2]/div[1]/div[1]/div[2]').text
        if "分鐘" in list_time:
            result.append(int(list_time.split()[0])*60)
        elif "小時" in list_time:
            result.append(int(list_time.split()[1])*60*60 )
        else:
            result.append(int(list_time.split()[1])*24*60*60)
    count += 1
if sorted(result) == result:
    print("Update time sorting is successful")
else:
    print("Update time sorting failed")
driver.get('https://www.cakeresume.com/jobs')

#Check search input value can work successful
#檢查搜尋功能正確
searchElement = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input')
searchElement.send_keys(data["search_verification"]["search_name"])
searchElement.send_keys(Keys.RETURN)
time.sleep(2)
count = 1
grab_subtitle = driver.find_elements(By.CLASS_NAME,'JobSearchItem_companyName__QKkj5')
for x in grab_subtitle:
    if x.text == data["search_verification"]["company_name"]:
        if count == 10:
            print("The search function is correct")
    else:
        print(x.text + "Search function failed")
        count+=10
    count+=1
driver.get('https://www.cakeresume.com/jobs')

#Check streamline typesetting did succeed
#檢查精簡排版正確
gear_button_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]')
gear_button_element.click()
typesetting_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/ul/li[2]/div/div[1]/div')
typesetting_button.click()
time.sleep(2)
if driver.find_elements(By.CLASS_NAME,'JobSearchItem_description__tNSbN'):
    print("Condensed typography failed")
else:
    print("Condensed typography success")
driver.get('https://www.cakeresume.com/jobs')

#Check the second page url correct
#檢查頁面網址正確
driver.execute_script("scroll(0,100000)")
formFeed_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[7]/div/a[2]')
formFeed_element.click()
time.sleep(2)
pageUrl_element = driver.find_element(By.XPATH,'/html/head/link[2]')
grab_pageUrl = pageUrl_element.get_attribute('href')
if grab_pageUrl == data["page_url"]:
    print("Second page URL is correct")
else:
    print("Second page URL error")
driver.get('https://www.cakeresume.com/jobs')

#Check vacancies title and Content page title Same
#檢查職缺標題跟內容頁標題一致
first_field_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/a')
first_field_text = first_field_element.text
first_field_element.click()
driver.switch_to.window(driver.window_handles[1])
pagination_title_element = driver.find_element(By.CLASS_NAME,'JobDescriptionLeftColumn_title__heKvX')
pagination_title_text = pagination_title_element.text
if first_field_text == pagination_title_text:
    print("Job Title and Content Page Title Success")
else:
    print("Job title and content page title fail")
driver.quit()

