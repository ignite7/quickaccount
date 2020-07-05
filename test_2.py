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
        self.driver.get(
            'https://accounts.google.com/signup/v2/webcreateaccount?hl'
            '=en&flowName=GlifWebSignIn&flowEntry=SignUp'
        )
        self.driver.maximize_window()
        
    def test_write_name(self):
        """
        Write the name.
        """
        
        self.driver.find_element_by_id('firstName').send_keys('pepe')
        self.driver.find_element_by_id('lastName').send_keys('pizza')
        
        
    def test_write_username(self):
        """
        Write the username.
        """
        
        self.driver.find_element_by_id('username').send_keys('juju')
        
    def test_write_password(self):
        """
        Write the password.
        """
        
        self.driver.find_element_by_name('Passwd').send_keys('example')
        self.driver.find_element_by_name('ConfirmPasswd').send_keys('example')
    
    def test_create_account(self):
        """
        Click on the submit button for create
        the account.
        """
        
        self.driver.find_element_by_xpath(
            '//*[@id="accountDetailsNext"]/span/span'
        ).click()
        
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