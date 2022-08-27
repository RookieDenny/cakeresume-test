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
for x in all_advanced_filter:
    if x.text not in answer:
        print("Check advanced search Is there a display fail")
        break
else:
    print("Check advanced search Is there a display pass")
driver.get('https://www.cakeresume.com/jobs')

#Check filter company whether succeed
#檢查篩選公司功能正確
time.sleep(1)
company_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/a')
company_button.click()
time.sleep(2)
button_field = driver.find_elements(By.CLASS_NAME,'CompanySearchItem_actions__SlIDN')
for x in button_field:
    if data['apply_text'] in x.text:
        print('Check filter company whether succeed fail')
        break
else:
    print('Check filter company whether succeed pass')
driver.get('https://www.cakeresume.com/jobs')

#Check filter place taiwan whether succeed
#檢查篩選地點功能正確 - 台灣
place_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[1]/button')
place_element.click()
taiwan_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div')
taiwan_element.click()
time.sleep(2)
place_field = driver.find_elements(By.CLASS_NAME,'JobSearchItem_featureSegmentLink__0qG7L')
for x in place_field:
    if data["taiwan"] or data["taiwanEg"] in x.text:
        pass
    else:
        print('Check filter place taiwan whether succeed fail')
        break
else:
    print('Check filter place taiwan whether succeed pass')
driver.get('https://www.cakeresume.com/jobs')

#Check filter work type intern whether succeed
#檢查篩選工作型態功能正確 - 實習生
#Check filter seniority elementary whether succeed
#檢查篩選資歷功能正確 - 初階
filterField = {
    "intern":{
        "element":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/div[1]/button',
        "check":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/div[2]/div/div/div/div/div[3]/div',
        "comparison":'實習生・實習',
        'name':'Check filter work type intern whether succeed '
    },
    "elementary":{
        "element":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div[1]/button',
        "check":'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/div[2]/div/div/div/div/div[1]/div',
        "comparison":'全職・初階',
        'name':'Check filter seniority elementary whether succeed '
    }
}
for index,add in filterField.items():
    driver.find_element(By.XPATH,filterField[index]["element"]).click()
    driver.find_element(By.XPATH,filterField[index]["check"]).click()
    time.sleep(2)
    count = 1
    while count <= 10:
        label = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+ str(count)+']/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]')
        labelTittle = label.text.replace('\n','')
        count += 1
        if filterField[index]["comparison"] != labelTittle:
            print(filterField[index]["name"] +"fail")
            break
    else:
        print(filterField[index]["name"] +"pass")
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
    print("Check new sort whether succeed pass")
else:
    print("Check new sort whether succeed fail")
driver.get('https://www.cakeresume.com/jobs')

#Check search input value can work successful
#檢查搜尋功能正確
searchElement = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input')
searchElement.send_keys(data["search_verification"]["search_name"])
searchElement.send_keys(Keys.RETURN)
time.sleep(2)
grab_subtitle = driver.find_elements(By.CLASS_NAME,'JobSearchItem_companyName__QKkj5')
for x in grab_subtitle:
    if x.text != data["search_verification"]["company_name"]:
        print("Check search input value can work successful fail")
else:
    print("Check search input value can work successful pass")
driver.get('https://www.cakeresume.com/jobs')

#Check streamline typesetting did succeed
#檢查精簡排版正確
describe_element = driver.find_element(By.CLASS_NAME,'JobSearchItem_description__tNSbN')
gear_button_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]/button')
gear_button_element.click()
typesetting_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/ul/li[2]/div/div[1]/div')
typesetting_button.click()
time.sleep(2)
each_field = driver.find_elements(By.CLASS_NAME,'JobSearchItem_wrapper__0zoCh')
for x in each_field:
    if describe_element in each_field:
        print('Check streamline typesetting did succeed fail')
else:
    print('Check streamline typesetting did succeed pass')
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
    print("Check the second page url correct pass")
else:
    print("Check the second page url correct fail")
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
    print("Check vacancies title and Content page title Same pass")
else:
    print("Check vacancies title and Content page title Same fail")
driver.quit()