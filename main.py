"""
Main 
"""

# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Utilities
import time
import random
import string


class CreateRamdonAccount:
    """
    It's gonna create random account for
    the user.
    """
    
    def random_provider(self, provider):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        if provider == '1':
            self.driver.get('https://mail.protonmail.com/create/new?language=en')
            
            #return print('OK') # Test
            
        elif provider == '2':
            pass
        
        elif provider == '3':
            pass
        
        elif provider == '4':
            pass
        
        elif provider == '5':
            pass
            
        self.ramdom_data()
        
    def ramdom_data(self):
        """
        This method will create random information
        about the account.
        """
        
        abc = random.choices(string.ascii_letters, k=8)
        number = random.choices(string.digits, k=4) 
        symbols = random.choices(
            '! ? - / _ " *'.split(' '),
            k=2
        )
        
        joiner_username = abc + number
        joiner_password = abc + number + symbols
        
        data = {
            'username': ''.join(sorted(joiner_username)),
            'password': ''.join(sorted(joiner_password))
        }
        
        self.random_dom_elements(data)
        
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
        
        # Needs to be fixed!
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div/div/div/form/div/div/div[2]/label/div/input')
            )
        ).click()
        
        time.sleep(10)
        
        self.driver.close()
        self.driver.quit()
        
        
class CreateManuallyAccount:
    
    def manually_dom_elementsT(self):
        pass