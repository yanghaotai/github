#encoding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://10.0.129.172:28080/yingu-mrs/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='/yingu-mrs/monthRepaymentController/showStrategy']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='datetimepicker']").send_keys("2017-03-30")
driver.find_element_by_xpath(".//*[@id='txtErrorType']").send_keys("1")
for i in range(1000):
    driver.find_element_by_xpath(".//*[@id='search']").click()