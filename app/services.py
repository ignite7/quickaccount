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
import getpass


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


def resume(data):
    """
    It going to shows the resume of the
    random data.
    """
    
    path = '/home/{}/quickaccount.txt'.format(
        getpass.getuser()
    )
        
    with open(path, 'a+') as file:
        file.write(
            '\nQUICKACCOUNT\n{}\nUsername: {}\n Password: {}\n {}\n'.format(
                '-' * 50,
                data['custom_username'] or data['random_username'],
                data['custom_password'] or data['random_password'],
                '-' * 50
            )
        )
        
    print(
        'The acccount has been created successfully, ',
        'you can find the account in: \n{}'.format(path) 
    )
    
    
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
 
    def get_data(self, service, username, password):
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
            'random_username': ''.join(sorted(joiner_username)),
            'random_password': ''.join(sorted(joiner_password)),
            'custom_username': username,
            'custom_password': password
        }
        
        if service == 'protonmail':
            self.driver.get('https://mail.protonmail.com/create/new?language=en')
            self.protonmail(self.data)
            
        elif service == 'hotmail':
            self.driver.get('https://signup.live.com/')
            self.hotmail(self.data)
        
    def protonmail(self, data):
        """
        This method copy the info in the DOM 
        to create protonmail account.
        """
        
        try:
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
            ).send_keys(data['custom_username'] or data['random_username'])
            
            self.driver.switch_to.default_content()
            
            # Write password
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, 'password')
                )
            ).send_keys(data['custom_password'] or data['random_password'])
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, 'passwordc')
                )
            ).send_keys(data['custom_password'] or data['random_password'])
            
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
            
            # Resolve captcha
            resolve_captcha()
            
            try:
                # Click in finish setup
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[2]/div/div/div/form/div/div/p[3]/button')
                    )
                ).click()
                    
                self.driver.close()
                self.driver.quit()
                    
                # Finish
                resume(data)
                    
            except TimeoutException:
                print(
                    'Invalid captcha',
                    'or proccess interrupted',
                    'by human interaction.'
                )   
                
                self.driver.close()
                self.driver.quit()
                
                #Finish
                resume(data)    
        
        except TimeoutException:
            print(
                'Username already used',
                'or weak password.'
            )
            
            self.driver.close()
            self.driver.quit() 
            
    def hotmail(self, data):
        """
        This method copy the info in the DOM 
        to create hotmail account.
        """
        
        try:
            pass
        
        except TimeoutException:
            pass
            