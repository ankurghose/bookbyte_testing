from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/ankur/PycharmProjects/bookbyte_testing/Drivers/chromedriver88")
#driver.set_pageload_timeout(10)
driver.get("https://www.bookbyte.com/advancedsearch.aspx")

driver.find_element_by_id("ctl00_mBody").click()
#time.sleep(4)
driver.find_element_by_name("ctl00$ContentPlaceHolder1$tbKeywords").send_keys("college")
#time.sleep(4)
#driver.find_elements_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_tbKeywords']").send_keys("college")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ibSearch").click()
#time.sleep(4)

searchresults = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbSearchedFor").text
print(searchresults)
driver.quit()
#closes the driver