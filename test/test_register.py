from django.test import LiveServerTestCase
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Create your tests here.
from webdriver_manager.core.utils import ChromeType


class PlayerFormTest(LiveServerTestCase):

    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://localhost:8081/register")
        return driver

    def test_form(self):
        driver = self.setUp()
        email = driver.find_element_by_id('inputEmail')
        username = driver.find_element_by_id('inputUsername')
        password = driver.find_element_by_id('inputPassword')
        street = driver.find_element_by_id('inputStreet')
        street_number = driver.find_element_by_id('inputStreetnum')

        email.send_keys('prova@gmail.com')
        username.send_keys('Usuari prova')
        password.send_keys('password1234')
        street.send_keys('Carrer Major')
        street_number.send_keys('23')
        submit = driver.find_element_by_name('createAccount')
        submit.send_keys(Keys.RETURN)
        assert (email.get_attribute('value'), 'prova@gmail.com')
        assert (username.get_attribute('value'), 'Usuari prova')
        assert (password.get_attribute('value'), 'password1234')
        assert (street.get_attribute('value'), 'Carrer Major')
        assert (street_number.get_attribute('value'), '23')
        #actions = ActionChains(driver);
        #actions.move_to_element(submit).click().perform();
        #driver.implicitly_wait(5)
        #assert driver.current_url, "http://localhost:8081/"
        driver.close()

    '''def test_cancel(self):
        driver = self.setUp()
        driver.implicitly_wait(5)

        login= driver.find_element_by_name("goToLogIn")
        login.click()
        driver.implicitly_wait(5)
        assert driver.current_url, "http://localhost:8081/login"'''
