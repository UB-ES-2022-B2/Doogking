from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class HousingView(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        cls.selenium = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=options)
        cls.selenium.maximize_window()
        cls.selenium.implicitly_wait(500)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_housing_views(self):
        self.selenium.get(self.live_server_url)
        grid = self.selenium.find_element(
            By.ID, "buttonViewGrid").is_enabled()
        assert grid

    def test_housing_price(self):
        self.selenium.get(self.live_server_url)
        container = self.selenium.find_element(
            By.ID, "priceContainer").is_enabled()
        assert container

    def test_housing_view_house(self):
        self.selenium.get(self.live_server_url)
        button_grid = self.selenium.find_element(
            By.ID, "favButtonGrid").is_enabled()
        assert button_grid
