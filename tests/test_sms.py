"""
Test

Note:
For capture the input and output try:
python3 -m pytest --capture=tee-sys test.py
"""

# Pytest
import unittest
from pyunitreport import HTMLTestRunner

# Selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Utilities
import time


class QuickAccount(unittest.TestCase):
    """
    It will execute all the test for the script
    'quickaccount'.
    """
    
    def setUp(self):
        """
        Setup of the driver browser.
        """
        
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get('https://smsreceivefree.com/country/usa')
        self.driver.maximize_window()
        
    def test_choose_phone(self):
        self.driver.find_element_by_xpath(
            '/html/body/main/section/div[1]/div[1]/div/div/div[3]/a'
        ).click()
        
        number = self.driver.find_element_by_xpath(
            '//*[@id="home"]/section/h1/small'
        )
        
        self.assertEqual('+12183000472', number.text)
        
    def tearDown(self):
        """
        Test Fisnished.
        """
        
        self.driver.close()
        self.driver.quit()
        
    
if __name__ == '__main__':
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='quickaccount_reports',
            report_name='quickaccount_report'
        )
    )