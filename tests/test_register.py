from django.test import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://doogking.azurewebsites.net/"


class PlayerFormTest(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.get(url + "register")
        return driver
