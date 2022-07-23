from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
myname = "戴棕鳴"
driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get('https://www.google.com/')

seachBarElement = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
seachBarElement.send_keys(myname)
seachBarElement.send_keys(Keys.RETURN)

titleElement = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3')
searchTitle = titleElement.text
myNameIndex = searchTitle.find(myname)
if myNameIndex > -1 and myname == searchTitle[myNameIndex:myNameIndex+3]:
        print("有名子")
else:
        print("沒名子")

driver.quit()
