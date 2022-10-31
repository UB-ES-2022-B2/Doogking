from django.test import LiveServerTestCase
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://doogking.azurewebsites.net/"
#url = "http://localhost:8080/"
class LogInTestCase(LiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        driver.get(url)
        return driver

   ''' def testIcon(self):
        driver = self.setUp()
        icon = driver.find_element_by_id("icon")
        icon.click()
        driver.implicitly_wait(5)
        self.assertEqual(driver.current_url,url)
        driver.close()'''


        ''' def testLogIn(self):
        driver = self.setUp()
        login = driver.find_element_by_id("login")
        login.click()
        driver.implicitly_wait(5)
        self.assertEqual(driver.current_url, url +"login")
    def testRegiter(self):
        driver = self.setUp()
        register = driver.find_element_by_id("registrer")
        #register.click()
        driver.implicitly_wait(5)
        self.assertEqual(driver.current_url, url + "register")'''

