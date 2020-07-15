"""
Test Accounts.
"""

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Utilities
import getpass


def resume(data):
    """
    It going to shows the resume of the
    random data.
    """
    
    path = '/home/{}/quickaccount.txt'.format(
        getpass.getuser()
    )
    
    message = (
        '''
        {}\n{}\nUsername: {}\n Password: {}\nFirst Name: {}\n
        Last Name: {}\nRecovery Email: {}\n{}\n
        '''.format(
            '-' * 50,
            data['service'].upper(),
            data['c_username'] or data['r_username'],
            data['c_password'] or data['r_password'],
            data['c_first_name'] or 'NOT',
            data['c_last_name'] or 'NOT',
            data['c_recovery_email'] or 'NOT',
            '-' * 50
        )
    )
    
    with open(path, 'a+') as file:
        file.write(message)
        
    print(
        'The acccount has been created successfully, ',
        'you can find the account in:\n{}'.format(path) 
    )
    

def test_protonmail_account(data):
    """
    Test if protonmail account has
    passed or not.
    """
    
    driver = webdriver.Chrome('./app/chromedriver')
    driver.get('https://mail.protonmail.com/login')
                
    try:
        # Write username
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'username')
            )
        ).send_keys(data['c_username'] or data['r_username'])
        
        # Write password
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'password')
            )
        ).send_keys(data['c_password'] or data['r_password'])
        
        # Submit form
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'login_btn')
            )
        ).click()
        
        # Title contains 'Inbox'
        WebDriverWait(driver, 3).until(
            EC.title_contains('Inbox')
        )
        
    except TimeoutException:
        print(
            'Invalid captcha, he account wasn\'t ',
            'created succesfully.'
        )
    
    else:                    
        resume(data)
    
    driver.close()
    driver.quit()
    

