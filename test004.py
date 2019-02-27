from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.get('http://192.168.1.251/deci/login')
sleep(2)
driver.find_element_by_name('number').send_keys('13000000000')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_xpath('//input[@value="登录"]').click()
sleep(3)
ele = driver.find_element_by_xpath('//div[@class="user-name fs-18"]')
print(ele.text)