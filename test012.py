from selenium import webdriver
import win32com.client


driver = webdriver.Chrome(r'E:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://tinypng.com/')
driver.find_element_by_css_selector('.target .icon').click()
shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys(r"C:\Users\Administrator\Desktop\1.jpg" + '\n')
driver.quit()
