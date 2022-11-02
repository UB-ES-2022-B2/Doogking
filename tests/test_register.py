from django.test import LiveServerTestCase
from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create your tests here.
from webdriver_manager.core.utils import ChromeType

url = "https://doogking.azurewebsites.net/"
#url = "http://localhost:8080/"


class PlayerFormTest(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.get(url + "register")
        return driver

    '''def test_form(self):
        driver = self.setUp()
        email = driver.find_element_by_id('inputEmail')
        username = driver.find_element_by_id('inputUsername')
        password = driver.find_element_by_id('inputPassword')
        # street = driver.find_element_by_id('inputStreet')
        # street_number = driver.find_element_by_id('inputStreetnum')

        email.send_keys('prova2@gmail.com')
        username.send_keys('Usuari prova')
        password.send_keys('Password1234')

        submit = driver.find_element_by_name('createAccount')
        driver.maximize_window()
        time.sleep(2)
        submit.click()
        driver.implicitly_wait(5)
        assert driver.current_url, url
        driver.close()

    def test_cancel(self):
        driver = self.setUp()
        driver.implicitly_wait(5)
        login = driver.find_element_by_name("goToLogIn")
        driver.maximize_window()
        time.sleep(2)
        login.click()
        driver.implicitly_wait(5)
        assert driver.current_url, url + "login"
        driver.close()

    def test_form_wrong_email(self):
        driver = self.setUp()
        email = driver.find_element_by_id('inputEmail')
        username = driver.find_element_by_id('inputUsername')
        password = driver.find_element_by_id('inputPassword')
        # street = driver.find_element_by_id('inputStreet')
        # street_number = driver.find_element_by_id('inputStreetnum')

        email.send_keys('prova2gmailcom')
        username.send_keys('Usuari prova')
        password.send_keys('Password1234')
        submit = driver.find_element_by_name('createAccount')
        driver.maximize_window()
        time.sleep(5)
        submit.click()
        waiter = WebDriverWait(driver, 10)
        alert = waiter.until(EC.alert_is_present())
        assert 'Wrong username or password' in alert.text
        alert.accept()
        driver.close()'''