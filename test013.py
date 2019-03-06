from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.vmall.com/')
#点击 "华为官网" 链接
driver.find_element_by_xpath('(//div[@class="s-sub"]//a)[2]').click()
main_handle = driver.current_window_handle
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if '消费' in driver.title:
        break
with open('str.txt', 'r') as f1:
    str1 = f1.read()
for i in driver.find_elements_by_css_selector('.left-box>ul>li'):
    if i.text not in str1:
        print('缺少-->'+i.text)
    else:
        print('存在-->'+i.text)
#最后再回到主窗口
driver.switch_to.window(main_handle)
mouse = driver.find_element_by_xpath('(//div[@class="category-info"])[2]')
ActionChains(driver).move_to_element(mouse).perform()
eles = driver.find_elements_by_xpath('//li[@id="zxnav_1"]//ul[@class="subcate-list clearfix"]//li[@class="subcate-item"]')
for ele in eles:
    if ele.text in '平板电脑  笔记本电脑 笔记本配件':
        print('存在-->'+ele.text)
    else:
        print('缺少-->'+ele.text)


