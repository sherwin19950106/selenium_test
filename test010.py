from selenium import webdriver


driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://www.51job.com')
driver.find_element_by_css_selector('a.more').click()
driver.find_element_by_css_selector('p.ipt>input').send_keys('测试工程师')
driver.find_element_by_css_selector('p#work_position_click').click()
cities = driver.find_elements_by_css_selector('div#work_position_click_center_right_list_000000 tr td')
for city in cities:
    if city.get_attribute('class') == 'on':
        city.click()
    if city.text == '南京':
        city.click()
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()
driver.find_element_by_css_selector('span#funtype_click').click()
driver.find_element_by_css_selector('li#funtype_click_center_left_each_0100').click()
driver.find_element_by_css_selector('em#funtype_click_center_right_list_category_0100_2700').click()
driver.find_element_by_css_selector('em#funtype_click_center_right_list_sub_category_each_0100_2707').click()
driver.find_element_by_css_selector('span#funtype_click_bottom_save').click()
driver.find_element_by_css_selector('#providesalary_list').click()
driver.find_element_by_css_selector('#providesalary_list .ul span[data-value="06"]').click()
driver.find_element_by_css_selector('div[class="btnbox p_sou"]>span').click()
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

