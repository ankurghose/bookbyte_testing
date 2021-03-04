from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

driver = webdriver.Chrome("/Users/ankur/PycharmProjects/bookbyte_testing/Drivers/chromedriver88")
#driver.set_pageload_timeout(10)
driver.get("https://www.amazon.com/sp?seller=A2N51X1QYGFUPK")

# string var address

address = driver.find_elements_by_xpath("//span[contains(text(),'2800 Pringle Rd SE Suite 100')]")[0].text
print(address)
address1 = '2800 Pringle RD SE Suite 100'
address2 = 'Wrong Address'

assert address != '2800 Pringle RD SE Suite 100'
assert address == address2




driver.quit()