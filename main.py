"""
Main 
"""

# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

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
            self.driver.get(
                'https://accounts.google.com/signup/v2/webcreateaccount?'
                'hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'
            )
            
            return print('OK') # Test
            
        elif provider == '2':
            pass
        
        elif provider == '3':
            pass
        
        elif provider == '4':
            pass
        
        elif provider == '5':
            pass
        
        #self.random_dom_elements()
        
    def random_dom_elements(self):
        first_name = self.driver.find_element_by_id('firstName')
        first_name.send_keys('Sergio')
        first_name.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        #random.choice(list(string.ascii_lowercase))
        
class CreateManuallyAccount:
    
    def manually_dom_elementsT(self):
        pass