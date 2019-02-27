from selenium import webdriver
import time

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.get('http://music.taihe.com/top/new')
time.sleep(1)
div = driver.find_element_by_id("songListWrapper")
liList = div.find_elements_by_tag_name('li')
for li in liList:
    status = li.find_elements_by_class_name('up')
    if status:
        title = li.find_element_by_class_name('song-title')
        songname =title.find_element_by_tag_name('a').text
        if '电影' in songname:
            continue
        if '电视剧' in songname:
            continue
        singer = li.find_element_by_class_name('author_list')
        singername = singer.find_element_by_tag_name('a').text
        print('{:<10}:{}'.format(songname, singername))

driver.quit()

