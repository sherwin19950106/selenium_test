from selenium import webdriver
import time
driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.get('https://movie.douban.com/')
time.sleep(5)
ele = driver.find_element_by_id('billboard')
print(ele.text)
driver.close()