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
        {}\n{}\nEmail: {}\nUsername: {}\nPassword: {}\nFirst Name: {}\n
        Last Name: {}\nRecovery Email: {}\n{}\n
        '''.format(
            '-' * 50,
            data['service'].upper(),
            data['c_email'] or 'NOT',
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


# Driver
driver = webdriver.Chrome(ChromeDriverManager().install())


def test_protonmail_account(data):
    """
    Test if protonmail account has
    passed or not.
    """

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
            'Invalid captcha, the account wasn\'t ',
            'created succesfully, try later.'
        )

    else:
        resume(data)

    driver.close()
    driver.quit()


def test_hotmail_account(data):
    """
    Test if hotmail account has
    passed or not.
    """

    driver.get('https://outlook.live.com/owa/?nlp=1')

    try:
        # Write username
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.NAME, 'loginfmt')
            )
        ).send_keys(data['c_email'])

        # Click next
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'idSIButton9')
            )
        ).click()

        # Write password
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.NAME, 'passwd')
            )
        ).send_keys(data['c_password'] or data['r_password'])

        # Click next
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.ID, 'idSIButton9')
            )
        ).click()

        # Title contains 'Outlook'
        WebDriverWait(driver, 3).until(
            EC.title_contains('Outlook')
        )

    except TimeoutException:
        print(
            'Invalid captcha, the account wasn\'t ',
            'created succesfully, try later.'
        )

    else:
        resume(data)

    driver.close()
    driver.quit()


def test_fastmail_account(data):
    """
    Test if fastmail account has
    passed or not.
    """

    driver.get('https://www.fastmail.com/login/')

    try:
        # Write username
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.NAME, 'username')
            )
        ).send_keys(data['c_email'])

        # Write password
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.NAME, 'password')
            )
        ).send_keys(data['c_password'] or data['r_password'])

        # Submit
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#v14 > div > p.u-alignRight > button')
            )
        ).click()

        # Title contains 'Outlook'
        WebDriverWait(driver, 3).until(
            EC.title_contains('Inbox')
        )

    except TimeoutException:
        print(
            'Invalid account, the account wasn\'t ',
            'created succesfully, try later.'
        )

    else:
        resume(data)

    driver.close()
    driver.quit()