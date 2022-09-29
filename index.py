from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

with open("config.json",mode="r",encoding="utf-8") as file:
    data = json.load(file)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.cakeresume.com/jobs')
#Check advanced search Is there a display
#檢查進階搜尋功能正確
advanced_search = driver.find_element(By.XPATH,data["advanced_search"]["advanced_search_xpath"])
advanced_search.click()
all_advanced_filter = driver.find_elements(By.CLASS_NAME,data["advanced_search"]["advanced_search_classname"])
for x in all_advanced_filter:
    if x.text not in data["advanced_search"]["advanced_search_result"].split(','):
        print(data["advanced_search"]["advanced_search_testcase"] + " fail")
        break
else:
    print(data["advanced_search"]["advanced_search_testcase"] + " pass")
driver.get('https://www.cakeresume.com/jobs')

#Check filter company whether succeed
#檢查篩選公司功能正確
time.sleep(1)
company_button = driver.find_element(By.XPATH,data["filter_company"]["filter_company_xpath"])
company_button.click()
time.sleep(2)
button_field = driver.find_elements(By.CLASS_NAME,data["filter_company"]["filter_company_classname"])
for x in button_field:
    if data["filter_company"]["apply_now"] in x.text:
        print(data["filter_company"]["filter_company_testcase"] + " fail")
        break
else:
    print(data["filter_company"]["filter_company_testcase"] + " pass")
driver.get('https://www.cakeresume.com/jobs')

#Check filter place taiwan whether succeed
#檢查篩選地點功能正確 - 台灣
place_element = driver.find_element(By.XPATH,data["filter_place"]["filter_place_xpath"])
place_element.click()
taiwan_element = driver.find_element(By.XPATH,data["filter_place"]["filter_place_button_xpath"])
taiwan_element.click()
time.sleep(2)
place_field = driver.find_elements(By.CLASS_NAME,data["filter_place"]["filter_place_classname"])
for x in place_field:
    if data["filter_place"]["taiwan"] not in x.text and data["filter_place"]["taiwanEg"] not in x.text:
        print(data["filter_place"]["filter_place_testcase"] + ' fail')
        break
else:
    print(data["filter_place"]["filter_place_testcase"] + ' pass')
driver.get('https://www.cakeresume.com/jobs')

#Check filter work type intern whether succeed
#檢查篩選工作型態功能正確 - 實習生
#Check filter seniority elementary whether succeed
#檢查篩選資歷功能正確 - 初階
for index,add in data["filterField"].items():
    driver.find_element(By.XPATH,data["filterField"][index]["element"]).click()
    driver.find_element(By.XPATH,data["filterField"][index]["check"]).click()
    time.sleep(2)
    count = 1
    while count <= 10:
        label = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div[6]/div/div/div['+ str(count)+']/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]')
        labelTittle = label.text.replace('\n','')
        count += 1
        if data["filterField"][index]["comparison"] != labelTittle:
            print(data["filterField"][index]["name"] +" fail")
            break
    else:
        print(data["filterField"][index]["name"] +" pass")
    driver.get('https://www.cakeresume.com/jobs')

#Check new sort whether succeed
#檢查最新功能正確
menuElement = driver.find_element(By.XPATH,data["new_sort"]["new_sort_button_xpath"])
menuElement.click()
latestButton = driver.find_element(By.XPATH,data["new_sort"]["new_sort_xpath"])
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
    print(data["new_sort"]["new_sort_testcase"] + " pass")
else:
    print(data["new_sort"]["new_sort_testcase"] + " fail")
driver.get('https://www.cakeresume.com/jobs')

#Check search input value can work successful
#檢查搜尋功能正確
searchElement = driver.find_element(By.XPATH,data["search"]["search_xpath"])
searchElement.send_keys(data["search"]["search_enter"])
searchElement.send_keys(Keys.RETURN)
time.sleep(2)
grab_subtitle = driver.find_elements(By.CLASS_NAME,data["search"]["search_classname"])
for x in grab_subtitle:
    if x.text != data["search"]["search_result"]:
        print(data["search"]["search_testcase"] + " fail")
else:
    print(data["search"]["search_testcase"] + " pass")
driver.get('https://www.cakeresume.com/jobs')

#Check streamline typesetting did succeed
#檢查精簡排版正確
describe_element = driver.find_element(By.CLASS_NAME,data["streamline_typesetting"]["streamline_typesetting_describe_classname"])
gear_button_element = driver.find_element(By.XPATH,data["streamline_typesetting"]["streamline_typesetting_xpath"])
gear_button_element.click()
typesetting_button = driver.find_element(By.XPATH,data["streamline_typesetting"]["streamline_typesetting_button_xpath"])
typesetting_button.click()
time.sleep(2)
each_field = driver.find_elements(By.CLASS_NAME,data["streamline_typesetting"]["streamline_typesetting_classname"])
for x in each_field:
    if describe_element in each_field:
        print(data["streamline_typesetting"]["streamline_typesetting_testcase"] + ' fail')
else:
    print(data["streamline_typesetting"]["streamline_typesetting_testcase"] + ' pass')
driver.get('https://www.cakeresume.com/jobs')

#Check the second page url correct
#檢查頁面網址正確
formFeed_element = driver.find_element(By.XPATH,data["second_page"]["second_page_xpath"])
formFeed_element.click()
time.sleep(2)
pageUrl_element = driver.find_element(By.XPATH,data["second_page"]["second_innerpage_xpath"])
grab_pageUrl = pageUrl_element.get_attribute('href')
if grab_pageUrl == data["second_page"]["second_page_url"]:
    print(data["second_page"]["second_page_testcase"] + " pass")
else:
    print(data["second_page"]["second_page_testcase"] + " fail")
driver.get('https://www.cakeresume.com/jobs')

#Check vacancies title and Content page title Same
#檢查職缺標題跟內容頁標題一致
first_field_element = driver.find_element(By.XPATH,data["title_Same"]["title_Same_xpath"])
first_field_text = first_field_element.text
first_field_element.click()
driver.switch_to.window(driver.window_handles[1])
pagination_title_element = driver.find_element(By.CLASS_NAME,data["title_Same"]["title_Same_classname"])
pagination_title_text = pagination_title_element.text
if first_field_text == pagination_title_text:
    print(data["title_Same"]["title_Same_testcase"] + " pass")
else:
    print(data["title_Same"]["title_Same_testcase"] + " fail")
driver.quit()
