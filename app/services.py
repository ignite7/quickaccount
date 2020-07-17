"""
Services
"""

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import TimeoutException

# Utilities
import time
import random
import string

# Modules
from .test_accounts import test_protonmail_account
from .test_accounts import test_hotmail_account
from .test_accounts import test_fastmail_account


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

    def __init__(self, proxy):
        """
        Initialize the web driver.
        """

        if proxy:
            PROXY = self.get_proxy()

            custom_proxy = Proxy()
            custom_proxy.proxy_type = ProxyType.MANUAL
            custom_proxy.ssl_proxy = PROXY

            capabilities = webdriver.DesiredCapabilities.CHROME
            custom_proxy.add_to_capabilities(capabilities)

            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                desired_capabilities=capabilities
            )

        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_proxy(self):
        """
        This method it going to take care
        of bring the proxy.
        """

        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://us-proxy.org/')

            https = driver.find_element_by_css_selector(
                '#proxylisttable > thead > tr > th.hx.sorting'
            ); https.click(); https.click()

            ip = driver.find_element_by_css_selector(
                '#proxylisttable > tbody > tr:nth-child(1) > td:nth-child(1)'
            ).text

            port = driver.find_element_by_css_selector(
                '#proxylisttable > tbody > tr:nth-child(1) > td:nth-child(2)'
            ).text

            joiner_proxy = '{}:{}'.format(ip, port)

        except TimeoutException:
            print('Proxy service does not working now, try later.')

        return joiner_proxy

    def get_data(self, **info):
        """
        This method will create random information
        about the account.
        """

        fastmail_domain_list = [
            'fastmail.com', 'fastmail.cn',
            'fastmail.co.uk', 'fastmail.com.au',
            'fastmail.de', 'fastmail.es',
            'fastmail.fm', 'fastmail.fr',
            'fastmail.im', 'fastmail.in',
            'fastmail.jp', 'fastmail.mx',
            'fastmail.net', 'fastmail.nl',
            'fastmail.org', 'fastmail.se',
            'fastmail.to', 'fastmail.tw',
            'fastmail.uk', 'fastmail.us'
        ]
        abc_lw = random.choices(string.ascii_lowercase, k=8)
        abc_up = random.choices(string.ascii_uppercase, k=6)
        number = random.choices(string.digits, k=4)
        fastmail_domain = random.choice(fastmail_domain_list)
        day = random.choice(range(1, 32))
        month = random.choice(range(1, 13))
        year = random.choice(range(1970, 2000))
        symbols = random.choices(
            '! ? - / _ " *'.split(' '),
            k=2
        )

        joiner_username = abc_lw + number
        joiner_password = abc_up + number + symbols + abc_lw

        self.data = {
            'service': info['service'],
            'r_username': ''.join(joiner_username),
            'r_password': ''.join(joiner_password),
            'c_username': info['username'],
            'c_password': info['password'],
            'c_first_name': info['first_name'],
            'c_last_name': info['last_name'],
            'c_recovery_email': info['recovery_email'],
            'c_domain': info['domain'],
            'f_domain': fastmail_domain,
            'r_day': str(day),
            'r_month': str(month),
            'r_year': str(year),
            'c_email': 'NOT'
        }

        if info['service'] == 'protonmail':
            self.driver.get('https://mail.protonmail.com/create/new?language=en')
            self.protonmail(self.data)

        elif info['service'] == 'hotmail':
            self.driver.get('https://signup.live.com/')
            self.hotmail(self.data)

        elif info['service'] == 'fastmail':
            self.driver.get('https://www.fastmail.com/signup/')
            self.fastmail(self.data)

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
            self.finish_setup_protonmail(data)

        except TimeoutException:
            # Finish setup
            resolve_captcha()
            self.finish_setup_protonmail(data)

    def finish_setup_protonmail(self, data):
        """
        This method it's going to take care
        of confirm the account was created
        correctly.
        """

        submit = '/html/body/div[2]/div/div/div/form/div/div/p[3]/button'

        try:
            # Click in create account
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.XPATH, submit)
                )
            ).click()

            print('Testing account...')
            time.sleep(10)
            test_protonmail_account(data, self.driver)

        except TimeoutException:
            print(
                'Procces interrupted by human intervention, ',
                'testing account...'
            )
            time.sleep(10)
            test_protonmail_account(data, self.driver)

    def hotmail(self, data):
        """
        This method copy the info in the DOM
        to create hotmail account.
        """

        email = '{}@{}'.format(
            data['c_username'] or data['r_username'],
            data['c_domain'] or 'hotmail.com'
        )
        data['c_email'] = email

        try:
            #Write username
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'MemberName')
                )
            ).send_keys(email)

            # Select domain
            domain = Select(self.driver.find_element_by_id('LiveDomainBoxList'))
            domain.select_by_value(data['c_domain'] or 'outlook.com')

            # Click Next
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'iSignupAction')
                )
            ).click()

            # Write password
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'PasswordInput')
                )
            ).send_keys(data['c_password'] or data['r_password'])

            # Deactivate email notification
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'iOptinEmail')
                )
            ).click()

            # Click Next
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'iSignupAction')
                )
            ).click()

            # Write first name
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'FirstName')
                )
            ).send_keys(data['c_first_name'] or data['r_username'])

            # Write last name
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'LastName')
                )
            ).send_keys(data['c_last_name'] or sorted(data['r_username']))

            # Click Next
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'iSignupAction')
                )
            ).click()

            # Select country
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#Country')
                )
            ).click()

            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#Country > option:nth-child(244)')
                )
            ).click()

            # Select birthday
            day = Select(self.driver.find_element_by_id('BirthDay'))
            day.select_by_value(data['r_day'])

            month = Select(self.driver.find_element_by_id('BirthMonth'))
            month.select_by_value(data['r_month'])

            year = Select(self.driver.find_element_by_id('BirthYear'))
            year.select_by_value(data['r_year'])

            # Click Next
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'iSignupAction')
                )
            ).click()

            # Finish setup
            resolve_captcha()

            try:
                # Click Next
                WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(
                        (By.ID, 'iSignupAction')
                    )
                ).click()

                print('Testing account...')
                time.sleep(10)
                test_hotmail_account(data, self.driver)

            except TimeoutException:
                print(
                    'Procces interrupted by human intervention, ',
                    'testing account...'
                )
                time.sleep(10)
                test_hotmail_account(data, self.driver)

        except TimeoutException:
            print('Username or password invalid.')

    def fastmail(self, data):
        """
        This method copy the info in the DOM
        to create hotmail account.
        """

        email = '{}@{}'.format(
            data['c_username'] or data['r_username'],
            data['c_domain'] or data['f_domain']
        )

        data['c_email'] = email

        try:
            # Write first name
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'name')
                )
            ).send_keys(data['c_first_name'] or sorted(data['r_username']))

            # Write username
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'email-localpart')
                )
            ).send_keys(data['c_username'] or data['r_username'])

            # Select domain
            domain = Select(
                self.driver.find_element_by_id(
                    'email-domain-fm'
                )
            )
            domain.select_by_value(
                data['c_domain'] or data['f_domain']
            )

            # Write password
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.ID, 'password')
                )
            ).send_keys(data['c_password'] or data['r_password'])

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

            catpcha = self.driver.find_element_by_id('phone-submit')

            if catpcha:
                resolve_captcha()

            # Finish setup
            print('Testing account...')
            time.sleep(5)
            test_fastmail_account(data, self.driver)

        except TimeoutException:
            print('Username or password invalid.')