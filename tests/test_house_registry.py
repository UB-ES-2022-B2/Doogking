from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class HouseRegistryTest(StaticLiveServerTestCase):

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

    def test_house_registry_fields(self):
        self.selenium.get(self.live_server_url + "/login")
        self.selenium.find_element(By.ID, "email").send_keys("admin@doogking.com")
        self.selenium.get(self.live_server_url + "/houseRegistry")
        city_field = self.selenium.find_element(By.ID, "city").is_enabled()
        street_field = self.selenium.find_element(By.ID, "street_number").is_enabled()
        floor_field = self.selenium.find_element(By.ID, "floor").is_enabled()
        house_dimension_field = self.selenium.find_element(By.ID, "house_dimension").is_enabled()
        price_field = self.selenium.find_element(By.ID, "price").is_enabled()
        description_field = self.selenium.find_element(By.ID, "description").is_enabled()
        door_field = self.selenium.find_element(By.ID, "door").is_enabled()
        testPassed = city_field and street_field and floor_field and house_dimension_field \
                     and price_field and description_field and door_field

        assert testPassed

    def test_house_registry_fill(self):
        self.selenium.get(self.live_server_url + "/houseRegistry")
        city_field = self.selenium.find_element(By.ID, "city").is_enabled()
        street_field = self.selenium.find_element(By.ID, "street_number").is_enabled()
        floor_field = self.selenium.find_element(By.ID, "floor").is_enabled()
        house_dimension_field = self.selenium.find_element(By.ID, "house_dimension").is_enabled()
        price_field = self.selenium.find_element(By.ID, "price").is_enabled()
        description_field = self.selenium.find_element(By.ID, "description").is_enabled()
        door_field = self.selenium.find_element(By.ID, "door").is_enabled()
        testPassed = city_field and street_field and floor_field and house_dimension_field \
                     and price_field and description_field and door_field

        assert testPassed
