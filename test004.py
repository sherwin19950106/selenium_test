from selenium import webdriver


driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://192.168.1.251/deci/login')
driver.maximize_window()
driver.find_element_by_name('number').send_keys('13000000000')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_css_selector('div.form-submit').find_element_by_xpath('//input[@value="登录"]').click()
def outdata():
    eles = driver.find_elements_by_css_selector('tr.el-table__row')
    for i in range(len(eles)):
        t1 = eles[i].find_element_by_css_selector('td.el-table_1_column_1  ').text
        t2 = eles[i].find_element_by_css_selector('td.el-table_1_column_2  ').text
        t3 = eles[i].find_element_by_css_selector('td.el-table_1_column_3  ').text
        t4 = eles[i].find_element_by_css_selector('td.el-table_1_column_4  ').text
        t5 = eles[i].find_element_by_css_selector('td.el-table_1_column_5  ').text
        t6 = eles[i].find_element_by_css_selector('td.el-table_1_column_6  ').text
        t7 = eles[i].find_element_by_css_selector('td.el-table_1_column_7  ').text
        t8 = eles[i].find_element_by_css_selector('td.el-table_1_column_8  ').text
        t9 = eles[i].find_element_by_css_selector('td.el-table_1_column_9  ').text
        if i == len(eles)/2:
            break
        print(f'{t1}|{t2}|{t3}|{t4}|{t5}|{t6}|{t7}|{t8}|{t9}|')
outdata()
eles = driver.find_element_by_css_selector('ul.el-pager').find_elements_by_css_selector('li')
for i in range(len(eles)):
    if i == 0:
        continue
    eles[i].click()
    try:
        outdata()
    except Exception:
        pass

driver.quit()

