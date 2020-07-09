"""
Main 
"""

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Utilities
import time
import random
import string
import getpass


class CreateRamdonAccount:
    """
    It's gonna create random account for
    the user.
    """
    
    def __init__(self, provider, recovery_email):
        self.driver = webdriver.Chrome('./app/chromedriver')
        
        if provider == 'protonmail':
            self.driver.get('https://mail.protonmail.com/create/new?language=en')
            self.ramdom_data()
            
        elif provider == 'temporary_email':
            self.driver.get('https://temp-mail.org/en/')
        
    def ramdom_data(self):
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
            'username': ''.join(sorted(joiner_username)),
            'password': ''.join(sorted(joiner_password))
        }
        
        self.random_dom_elements(self.data)
        
    def random_dom_elements(self, data):
        """
        This method copy the info in the DOM.
        """
        
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CLASS_NAME, 'top')
            )
        )
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'username')
            )
        ).send_keys(data['username'])
        
        self.driver.switch_to.default_content()
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'password')
            )
        ).send_keys(data['password'])
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'passwordc')
            )
        ).send_keys(data['password'])
        
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
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'confirmModalBtn')
            )
        ).click()
        
        print('You have 1 minute to fisnish the verification\n')
        
        for seconds in range(1, 61):
            time.sleep(seconds)
            
            if seconds == 1:
                print('{} Second\n'.format(seconds))
            
            else:
                print('{} Seconds\n'.format(seconds))
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div/div/div/form/div/div/p[3]/button')
            )
        ).click()
         
        self.driver.close()
        self.driver.quit()
        
        self.random_resume_data(data)
        
    def random_resume_data(self, data):
        """
        It going to shows the resume of the
        random data.
        """
        
        path = '/home/{}/protonmail_account.txt'.format(
            getpass.getuser()
        )
        
        with open(path, 'a+') as file:
            file.write(
                'PROTON MAIL ACCOUNTS:\n Username: {}\n Password: {}\n'.format(
                    data['username'],
                    data['password']
                )
            )
        
        print(
            'The acccount has been created successfully, ',
            'you can find the account in: {}'.format(path) 
        )
        
class CreateManuallyAccount:
    
    def manually_dom_elementsT(self):
        pass