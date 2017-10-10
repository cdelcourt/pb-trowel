#!/usr/bin/python

import selenium.webdriver.support.ui as UI
from selenium import webdriver
import unittest, time, re

print 'starting thing!'
class PythonFromide(unittest.TestCase):
    def setUp(self):
        print 'starting selenium driver'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def loop_through_urls(self):
        with open("main-album.txt","w") as in_file:
            for url in in_file:
                print url
                self.base_url = url
                driver.find_element_by_css_selector("#download > span").click()
                driver.find_element_by_css_selector("span.icon-chevron-right").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
