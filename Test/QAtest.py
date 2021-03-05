import os
import requests
import json
import jsonpath

import threading
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class QA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
     chrome_options = Options()
     chrome_options.add_argument("--headless")

     cls.driver = webdriver.Chrome("/Users/ankur/PycharmProjects/bookbyte_testing/Drivers/chromedriver88")
    # (options=chrome_options)


    @classmethod
    def tearDownClass(cls):
     cls.driver.quit()

    def test_request_search(self):
      wait = WebDriverWait(self.driver, 10)
      self.driver.get("https://www.bookbyte.com/advancedsearch.aspx")
      self.driver.find_element_by_name("ctl00$ContentPlaceHolder1$tbKeywords").send_keys("college")
      self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ibSearch").click()
      searchresults = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbSearchedFor").text
      print(searchresults)
      self.assertEqual(searchresults,"collegei","college book was not found")
      self.driver.quit()


    def test_request_address(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.amazon.com/sp?seller=A2N51X1QYGFUPK")
        address = self.driver.find_elements_by_xpath("//span[contains(text(),'2800 Pringle Rd SE Suite 100')]")[0].text
        print(address)
        address1 = ('2800 Pringle RD SE Suite 100')
        address2 = 'Wrong Address'
        self.assertEqual(address,address1,"address is correct")
        self.assertEqual(address,address2,"not the correct address")

    def test_request_googleapi(self):

        # storing the variable in the url
        url = "https://www.googleapis.com/books/v1/volumes?q=isbn:0131103628&key=AIzaSyBY8LEYyV5982mLwBmFkJq5dbWtdwiO3X8"
        requests.get(url)

        # Send Get request
        response = requests.get(url)
        # will print out the response
        print(response)

        # print response body
        print(response.content)
