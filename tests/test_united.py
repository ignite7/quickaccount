"""
Unit Test
"""

# Pytest
import unittest
from pyunitreport import HTMLTestRunner

# Selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

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

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_united_protonmail(self):
        """
        Test to create a protonmail
        account.
        """

        # Get the web page
        self.driver.get('https://mail.protonmail.com/create/new?language=en')
        self.driver.maximize_window()

        # Write username
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CLASS_NAME, 'top')
            )
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'username')
            )
        ).send_keys('example12348')

        self.driver.switch_to.default_content()

        # Write password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'password')
            )
        ).send_keys('Example1234!')

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'passwordc')
            )
        ).send_keys('Example1234!')

        # Click in submit button
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/form/div[2]/section/div/div[2]/iframe')
            )
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/footer/button')
            )
        ).click()

        self.driver.switch_to.default_content()

        # Click in submit modal button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'confirmModalBtn')
            )
        ).click()

    def test_united_hotmail(self):
        """
        Test to create a hotmail
        account.
        """

        # Get the web page
        self.driver.get('https://signup.live.com/')
        self.driver.maximize_window()

        #Write username
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'MemberName')
            )
        ).send_keys('example12563@hotmail.com')

        # Select domain
        domain = Select(self.driver.find_element_by_id('LiveDomainBoxList'))
        domain.select_by_value('hotmail.com')

        # Click Next
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'iSignupAction')
            )
        ).click()

        # Write password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'PasswordInput')
            )
        ).send_keys('Example1234!')

        # Deactivate email notification
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'iOptinEmail')
            )
        ).click()

        # Click Next
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'iSignupAction')
            )
        ).click()

        # Write first name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'FirstName')
            )
        ).send_keys('example')

        # Write last name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'LastName')
            )
        ).send_keys('last example')

        # Click Next
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'iSignupAction')
            )
        ).click()

        # Select country
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#Country')
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#Country > option:nth-child(244)')
            )
        ).click()

        # Select birthday
        day = Select(self.driver.find_element_by_id('BirthDay'))
        day.select_by_value('8')

        month = Select(self.driver.find_element_by_id('BirthMonth'))
        month.select_by_value('11')

        year = Select(self.driver.find_element_by_id('BirthYear'))
        year.select_by_value('1999')

        # Click Next
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'iSignupAction')
            )
        ).click()

    def test_united_fastmail(self):
        """
        Test to create a fatsmail
        account.
        """

        # Get the web page
        self.driver.get('https://www.fastmail.com/signup/')
        self.driver.maximize_window()

        # Write first name
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'name')
            )
        ).send_keys('pepe')

        # Write username
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'email-localpart')
            )
        ).send_keys('pepeusername')

        # Select domain
        domain = Select(
            self.driver.find_element_by_id(
                'email-domain-fm'
            )
        )
        domain.select_by_value('fastmail.com')

        # Write password
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'password')
            )
        ).send_keys('Example1234!')

        # Accept conditions
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'tos')
            )
        ).click()

        # Submit
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'main-submit')
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
            output='',
            report_name='unit_test'
        )
    )