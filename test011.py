from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.find_element_by_id('fromStationText').click()
driver.find_element_by_id('fromStationText').send_keys('苏州\n')
driver.find_element_by_id('toStationText').click()
driver.find_element_by_id('toStationText').send_keys('南京\n')
driver.find_element_by_id('train_date').click()
datas = driver.find_elements_by_css_selector('div.cal>div.cal-cm>div.cell')
for data in datas:
    if data.text == '24':
        data.click()
        break
trains = driver.find_elements_by_css_selector('ul#_ul_station_train_code>li>input')
for train in trains:
    if train.is_selected():
        train.click()
    if train.get_attribute('value') == 'G':
        train.click()
Select(driver.find_element_by_id('cc_start_time')).select_by_value('12001800')
driver.find_element_by_id('query_ticket').click()
if driver.find_element_by_id('show_more').get_attribute('class') == 'down':
    driver.find_element_by_id('show_more').send_keys(Keys.ENTER)
from_cities = driver.find_elements_by_css_selector('ul#from_station_ul input')
to_cities = driver.find_elements_by_css_selector('ul#to_station_ul input')
for city in from_cities:
    if city.is_selected():
        city.click()
    if city.get_attribute('value') == '苏州':
        city.click()
for city in to_cities:
    if city.is_selected():
        city.click()
    if city.get_attribute('value') == '南京':
        city.click()
ress = driver.find_elements_by_css_selector('#sear-result p')
for res in ress:
    print(res.text)
ress = driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]//tr[starts-with(@id,"ticket_")]//div[@class="ticket-info clearfix"]')
for res in ress:
    title = res.find_element_by_tag_name('a').text
    cdz = res.find_element_by_class_name('cdz').text.replace('\n', '-->')
    cds = res.find_element_by_class_name('cds').text.replace('\n', '--')
    ls = res.find_element_by_class_name('ls').text.replace('\n', '/')
    print(f'{title}|{cdz}|{cds}|{ls}|')
driver.save_screenshot('12306.png')
driver.quit()
