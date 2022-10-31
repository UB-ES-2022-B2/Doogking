from django.test import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


url = "https://doogking-testing.azurewebsites.net/"
#url = "http://localhost:8080/"
class LogInTestCase(LiveServerTestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url + "login")

        username = driver.find_element_by_id("inputUsername")
        password = driver.find_element_by_id("inputPassword")

        return driver, username, password

    def test_correctLogin(self):
        driver, username, password= self.setUp()
        username.send_keys("test@gmail.com")
        password.send_keys("password123")
        driver.find_element_by_name("signIn").click()
        driver.implicitly_wait(5)
        assert driver.current_url,url + "?username=aura&logged=true&token"
        driver.close()

    def test_incorrectLogin(self):
        driver, username, password= self.setUp()
        username.send_keys("test@gmail.com")
        password.send_keys("password123")
        driver.find_element_by_name("signIn").click()
        waiter = WebDriverWait(driver, 10)
        alert = waiter.until(EC.alert_is_present())
        assert 'Wrong username or password' in alert.text
        alert.accept()
        driver.close()

    def test_regiter(self):
        driver, username, password = self.setUp()
        driver.find_element_by_name("createAccount").click()
        driver.implicitly_wait(5)
        assert driver.current_url, url + "register"