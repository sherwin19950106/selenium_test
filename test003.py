from selenium import webdriver
import pprint
import collections


def weather():
    driver = webdriver.Chrome(r'E:\chromedriver.exe')
    driver.get('http://www.weather.com.cn/weather/101190101.shtml')
    ret = driver.find_element_by_id('7d')
    list_weather = ret.text.split('分时段预报')[0].split('\n')
    dict_weather = collections.OrderedDict()
    for i in range(len(list_weather)):
        if i % 4 == 0:
            try:
                dict_weather[list_weather[i]] = list_weather[i+1] + ' ' + list_weather[i+2] + ' ' + list_weather[i+3]
            except IndexError:
                pass
    driver.close()
    return dict_weather


if __name__ == '__main__':
    pprint.pprint(weather())


