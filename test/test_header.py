from django.test import LiveServerTestCase
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#"https://doogking-testing.azurewebsites.net/"
class LogInTestCase(LiveServerTestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://localhost:8081/")
        return driver

    def testIcon(self):
        driver = self.setUp()
        icon = driver.find_element_by_id("icon")
        icon.click()
        driver.implicitly_wait(5)
        self.assertEqual(driver.current_url,"http://localhost:8081/")

    '''def testLogIn(self):
        driver = self.setUp()
        login = driver.find_element_by_id("login")
        login.click()
        driver.implicitly_wait(5)
        self.assertEqual(driver.current_url, "http://localhost:8081/login")
    def testRegiter(self):
        driver = self.setUp()
        register = driver.find_element_by_id("registrer")
        #register.click()
        driver.implicitly_wait(5)
        self.assertEqual(driver.current_url, "http://localhost:8081/register")'''

