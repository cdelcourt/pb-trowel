# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from urlparse import urlparse
import os

class LoopCsv(unittest.TestCase):
    def setUp(self):
        fp = webdriver.FirefoxProfile('~/Library/Application Support/Firefox/Profiles/xxxxxxxx.default')
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_loop_csv(self):
        driver = self.driver
        with open("url-list.txt") as in_file: # use list of newline-separated URLs using PB-shovel's --links-only option
            for url in in_file:
                print url
                driver.get(url)
                driver.find_element_by_css_selector("#download > span").click()
                time.sleep(3)

                p_url = urlparse(url)
                cwd = os.getcwd()
                path, fn = os.path.split(p_url.path)
                filename, file_extension = os.path.splitext(fn) # split the HTML extension off the end
                fullname = os.path.join(cwd, path, fn)
                relpath = "." + path # make a relative path to move it to
                dl_path = "~/Downloads/Firefox/" + filename
                local_file = relpath + "/" + filename

                print 'Local file is ', local_file

                if not os.path.exists(relpath):
                    os.makedirs(relpath)

                os.rename(dl_path, local_file) # move from downloads to local directory with structure intact
                print "Moved", dl_path, "to", local_file



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
