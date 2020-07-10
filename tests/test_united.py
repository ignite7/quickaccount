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
        
        self.driver = webdriver.Chrome('./app/chromedriver')
        self.driver.get('https://mail.protonmail.com/create/new?language=en')
        self.driver.maximize_window()
           
    def test_create_username(self):
        """
        Create username.
        """
        
        # Write username
        WebDriverWait(self.driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CLASS_NAME, 'top')
            )
        )
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, 'username')
            )
        ).send_keys('sjdkjnankjdnajkdnaksjdnka')
        
        self.driver.switch_to.default_content()
        
        # Write password
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, 'password')
            )
        ).send_keys('example')
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, 'passwordc')
            )
        ).send_keys('example')
        
        WebDriverWait(self.driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/form/div[2]/section/div/div[2]/iframe')
            )
        )
        
        # Click in submit button
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/footer/button')
            )
        ).click()
        
        self.driver.switch_to.default_content()
        
        # Click in submit modal button 
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, 'confirmModalBtn')
            )
        ).click()
        
        time.sleep(100)
        
        # Click in finish setup
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div/div/div/form/div/div/p[3]/button')
            )
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
            output='united',
            report_name='test_united'
        )
    )