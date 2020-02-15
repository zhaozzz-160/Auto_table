from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("$YOUR_URL")

myClass = driver.find_element_by_id("webform_SYS_string1")
name = driver.find_element_by_id("webform_SYS_string2")
num = driver.find_element_by_id("webform_SYS_string3")

myClass.send_keys("2班")
name.send_keys("苏照")
num.send_keys("1234")
driver.find_element_by_id("savebtn").click()



