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
        self.driver.get('https://mail.protonmail.com/create/new?language=en')
        self.driver.maximize_window()
    
    def test_username_short(self):
        # self.driver.implicitly_wait(3)   
        self.driver.switch_to_frame(self.driver.find_element_by_tag_name(
            'iframe'
        ))
           
    def test_write_username(self):
        """
        Write the username.
        """
        
        WebDriverWait(self.driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//div[@class='usernameWrap']//iframe[@title='Registration form']")
            )
        )
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='input' and @id='username']")
            )
        ).send_keys('hola')
        
    def test_write_password(self):
        """
        Write the password.
        """
        
        self.driver.find_element_by_name('password').send_keys('example')
        self.driver.find_element_by_name('passwordc').send_keys('example')
    
    def test_create_account(self):
        """
        Click on the submit button for create
        the account.
        """
        
        self.driver.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        
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