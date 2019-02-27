from selenium import webdriver

driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
ret = driver.find_element_by_id('forecastID')
list_all = ret.text.split('\n')
dict_city = {}
list_wendu = []
for i in range(len(list_all)):
    if i % 2 == 0:
        dict_city[list_all[i]] = int(list_all[i+1].split('℃')[1].replace('/', ''))
        list_wendu.append(int(list_all[i+1].split('℃')[1].replace('/', '')))
low = min(list_wendu)
print(f'江苏省最低温度为{low}℃的城市有：', end='')
for i in dict_city:
    if dict_city[i] == low:
        print(i, end=' ')
driver.close()