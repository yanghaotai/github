# coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://shenfenzheng.293.net")
driver.implicitly_wait(10)
driver.maximize_window()

for i in range(0,10000):
    n = '51052220170228'+str(i).zfill(4)
    driver.find_element_by_id("id").send_keys(n)
    driver.find_element_by_id("id").submit()
    # if driver.find_element_by_css_selector("#show_table>tbody>tr>td>div"):
    m = driver.find_element_by_css_selector("#show_table>tbody>tr>td").text
    if '!' not in m:
        print n
    # else:
    #     s = driver.find_element_by_css_selector("#show_table>tbody>tr>td>font").text
    #     print s

    # driver.find_element_by_css_selector("#show_table>tbody>tr>td>div")

