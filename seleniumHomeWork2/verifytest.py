from re import T
from turtle import back
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#帶入預期的效果
answer_denny = "denny|ETMall東森購物網"
answer_link = "https://www.etmall.com.tw/Search?keyword=denny"
answer_gary = "Running Man前成員Gary復出太太美貌不輸智孝更被萌爆兒子 ..."
answer_links = "https://www.hk01.com/%E7%9F%A5%E6%80%A7%E5%A5%B3%E7%94%9F/433727/running-man%E5%89%8D%E6%88%90%E5%93%A1gary%E5%BE%A9%E5%87%BA-%E5%A4%AA%E5%A4%AA%E7%BE%8E%E8%B2%8C%E4%B8%8D%E8%BC%B8%E6%99%BA%E5%AD%9D-%E6%9B%B4%E8%A2%AB%E8%90%8C%E7%88%86%E5%85%92%E5%AD%90%E6%90%B6%E9%8F%A1"

name = ["Denny","Gary"]
driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
for names in name:
    driver.get('https://www.google.com/')
    search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.send_keys(names)
    search.send_keys(Keys.RETURN)
    title = driver.find_element(By.XPATH,'//*[@id="rso"]/div[4]/div/div[1]/div/a/h3')
    link = driver.find_element(By.XPATH,'//*[@id="rso"]/div[4]/div/div[1]/div/a').get_attribute('href')
    titles = title.text
    # print(titles,link)
    if answer_denny == titles and answer_link == link:
        print(titles,link)
    elif answer_gary == titles and answer_links == link:
        print(titles,link)
        driver.quit()
        print("成功")
    else:
        print("失敗")
