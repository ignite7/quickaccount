"""
Main 
"""

# Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class CreateRamdonAccount:
    """
    It's gonna create random account for
    the user.
    """
    
    def __init__(self, service):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(
            'https://accounts.google.com/signup/v2/webcreateaccount?'
            'hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'
        )
        
        self.dom_elements()
        
    def dom_elements(self):
        first_name = self.driver.find_element_by_id('firstName')
        first_name.send_keys('Sergio')
        first_name.close()
        
        
class CreateManuallyAccount:
    pass