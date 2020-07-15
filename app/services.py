"""
Services 
"""

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Utilities
import time
import random
import string

# Modules
from .test_accounts import test_protonmail_account


def resolve_captcha():
    """
    Allows to the user resolve the 
    captcha.
    """
    
    confirm = input(
        'Enter "yes" or "y" when you finish the captcha to continue: '
    )
                
    while confirm != 'yes' and confirm != 'y' and confirm != 'YES' and \
        confirm != 'Y':
         
        confirm = input(
            '\nEnter "yes" or "y" when you finish the captcha to continue: '
        )  

        if confirm == 'yes' or confirm == 'y' or confirm == 'YES' or \
            confirm == 'Y':
                
                break
    
class CreateAccount:
    """
    It's gonna create random account for
    the user.
    """
    
    def __init__(self):
        """
        Initialize the web driver.
        """
        
        self.driver = webdriver.Chrome('./app/chromedriver')
 
    def get_data(self, **info):
        """
        This method will create random information
        about the account.
        """
        
        abc_lw = random.choices(string.ascii_lowercase, k=8)
        abc_up = random.choices(string.ascii_uppercase, k=6)
        number = random.choices(string.digits, k=4) 
        symbols = random.choices(
            '! ? - / _ " *'.split(' '),
            k=2
        )
        
        joiner_username = abc_lw + number
        joiner_password = abc_up + number + symbols + abc_lw
        
        self.data = {
            'service': info['service'],
            'r_username': ''.join(sorted(joiner_username)),
            'r_password': ''.join(sorted(joiner_password)),
            'c_username': info['username'],
            'c_password': info['password'],
            'c_first_name': info['first_name'],
            'c_last_name': info['last_name'],
            'c_recovery_email': info['recovery_email']
        }
        
        if info['service'] == 'protonmail':
            self.driver.get('https://mail.protonmail.com/create/new?language=en')
            self.protonmail(self.data)
            
        elif info['service'] == 'hotmail':
            self.driver.get('https://signup.live.com/')
            self.hotmail(self.data)
        
    def protonmail(self, data):
        """
        This method copy the info in the DOM 
        to create protonmail account.
        """
        
        try:
            # Write username 
            WebDriverWait(self.driver, 3).until(
                EC.frame_to_be_available_and_switch_to_it(
                    (By.CLASS_NAME, 'top')
                )
            )
        
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'username')
                )
            ).send_keys(data['c_username'] or data['r_username'])
            
            self.driver.switch_to.default_content()
            
            # Write password
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'password')
                )
            ).send_keys(data['c_password'] or data['r_password'])
            
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'passwordc')
                )
            ).send_keys(data['c_password'] or data['r_password'])
            
            # Write recovery email
            WebDriverWait(self.driver, 3).until(
                EC.frame_to_be_available_and_switch_to_it(
                    (By.CLASS_NAME, 'bottom')
                )
            )
            
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'notificationEmail')
                )
            ).send_keys(data['c_recovery_email'] or '')
        
            # Click in create account button
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.NAME, 'submitBtn')
                )
            ).click()
            
            self.driver.switch_to.default_content()
            
            # Click in submit modal button
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'confirmModalBtn')
                )
            ).click()
            
            # Finish setup
            resolve_captcha()
            self.finish_setup(data)
        
        except TimeoutException:
            # Finish setup
            resolve_captcha()
            self.finish_setup(data)
                
    def finish_setup(self, data):
        submit = '/html/body/div[2]/div/div/div/form/div/div/p[3]/button'
        
        try:
            # Click in create account 
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, submit)
                )
            ).click()
            
            print('Testing account...')
            time.sleep(5)
            test_protonmail_account(data)
                
        except TimeoutException:
            print(
                'Procces interrupted by human intervention, ',
                'testing account...'
            )
            time.sleep(5)
            test_protonmail_account(data)
            
    def hotmail(self, data):
        """
        This method copy the info in the DOM 
        to create hotmail account.
        """
        
        try:
            pass
        
        except TimeoutException:
            pass
            