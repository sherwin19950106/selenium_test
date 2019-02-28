from selenium import webdriver
import time

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.get('https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=0')
time.sleep(1)
chooses = driver.find_element_by_class_name('sort')
labels = chooses.find_elements_by_tag_name('label')
one = input('输入序号查询：1.按热度排序，2.按时间排序，3.按评价排序')
assert one.isdigit()
for label in labels:
    if one == '1':
        print('---豆瓣高分电影（按热度排序）--- ')
        break
    elif one == '2':
        choose = label.find_element_by_xpath('//input[@value="time"]')
        choose.click()
        print('---豆瓣高分电影（按时间排序）--- ')
        break
    elif one == '3':
        choose = label.find_element_by_xpath('//input[@value="rank"]')
        choose.click()
        print('---豆瓣高分电影（按评价排序）--- ')
        break
    else:
        print('输入指令不对，按按热度排序')
        print('---豆瓣高分电影（按热度排序）--- ')
        break
time.sleep(3)
eles = driver.find_elements_by_class_name('item')
for ele in eles:
    print(ele.text)
driver.quit()
