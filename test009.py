from selenium import webdriver

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://www.51job.com')
driver.find_element_by_id('kwdselectid').send_keys('测试')
driver.find_element_by_id('work_position_input').click()
driver.find_element_by_id('work_position_click_ip_location_000000_070200').click()
citys = driver.find_elements_by_css_selector('td.js_more')
for city in citys:
    if city.text == '南京':
        city.find_element_by_tag_name('em').click()
driver.find_element_by_id('work_position_click_bottom_save').click()
driver.find_element_by_xpath('''//button[@onclick="kwdGoSearch($('#kwdselectid').val());"]''').click()
jobs = driver.find_element_by_id('resultList').find_elements_by_css_selector('div.el')
for job in jobs:
    t1 = job.find_element_by_css_selector('.t1').text
    t2 = job.find_element_by_css_selector('.t2').text
    t3 = job.find_element_by_css_selector('.t3').text
    if '南京' not in t3:
        continue
    t4 = job.find_element_by_css_selector('.t4').text
    print(f'{t1}|{t2}|{t3}|{t4}')
driver.quit()
