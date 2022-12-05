from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from rest_framework.test import RequestsClient


class MyHousesTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        cls.selenium = webdriver.Chrome(ChromeDriverManager().install(),
                                        chrome_options=options)
        cls.selenium.maximize_window()
        cls.selenium.implicitly_wait(500)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_profile_houses(self):
        # house_registry = self.selenium.find_element(By.NAME, "My houses").is_enabled()
        client = RequestsClient()
        headers = {'Access-Control-Allow-Origin': '*'}
        house_id = 1
        requests_passed = True
        while house_id < 8 and requests_passed:
            requests = client.get(
                'https://doogking.azurewebsites.net/api/housing_images/housing/' + str(house_id) + '/')
            requests_passed = requests.status_code == 200
            house_id += 1
        assert house_id == 8
