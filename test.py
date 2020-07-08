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
           
    def test_write_username(self):
        """
        Write the username.
        """
        
        WebDriverWait(self.driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CLASS_NAME, 'top')
            )
        )
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, 'username')
            )
        ).send_keys('pepe')
        
        self.driver.switch_to.default_content()
        
    def test_write_password(self):
        """
        Write the password.
        """
        
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
    
    def test_create_account(self):
        """
        Click on the submit button for create
        the account.
        """
        
        WebDriverWait(self.driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/form/div[2]/section/div/div[2]/iframe')
            )
        )
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/footer/button')
            )
        ).click()
        
        self.driver.switch_to.default_content()
        
    def test_modal_submit(self):
        """
        Last accept in a modal window.
        
        Note: the element in this point it will
        be invisible for the user.
        """
        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.ID, 'confirmModalBtn')
            )
        )
        
    def test_select_radio_button(self):
        """
        Select the email option to verified
        we're humans.
        
        Note: the element in this point it will
        be invisible for the user.
        """
        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, '#verification-panel > div.humanVerification-block-email > label')
            )
        )
        
    def test_write_email_verification(self):
        """
        Write the email verification.
        
        Note: the element in this point it will
        be invisible for the user.
        """
        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.ID, 'emailVerification')
            )
        )
        
        
    def test_send_email_verification(self):
        """
        Send the email verification.
        
        Note: the element in this point it will
        be invisible for the user.
        """
        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/div/div/form/div/div/form[1]/div[1]/div[2]/button')
            )
        )
        
    def test_finish_setup(self):
        """
        Finish setup
        
        Note: the element in this point it will
        be invisible for the user.
        """
        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/div/div/form/div/div/p[3]/button')
            )
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