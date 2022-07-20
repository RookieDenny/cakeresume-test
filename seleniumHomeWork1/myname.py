from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get('https://www.google.com/')

search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.send_keys("戴棕鳴")
search.send_keys(Keys.RETURN)

title = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3')
name = title.text
name1 = "戴棕鳴"
start = name.find(name1)
if start > -1:
    if name1 == name[start:start+3]:
        print("有名子")
    else:
        print("沒名子")
else:
    print("沒名子")


driver.quit()
