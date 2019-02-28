from selenium import webdriver

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://music.163.com/#/discover/toplist?id=3778678')
driver.switch_to.frame('g_iframe')
songs = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('b')
singers = songs = driver.find_element_by_tag_name('tbody').find_elements_by_class_name('text')

for i in singers:
    str1 = i.get_attribute('title')
    print(str1)



driver.quit()