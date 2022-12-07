from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class FilteringHousesTest(StaticLiveServerTestCase):

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

    '''
    def test_house_registry_fields(self):
        self.selenium.get(self.live_server_url)
        house_registry = self.selenium.find_element(By.ID, "houseRegistry")
        self.selenium.execute_script("arguments[0].click();", house_registry)
        self.selenium.implicitly_wait(100)
        city_field = self.selenium.find_element(By.NAME, "City").is_enabled()
        street_field = self.selenium.find_element(By.NAME, "Street number").is_enabled()
        floor_field = self.selenium.find_element(By.NAME, "Floor").is_enabled()
        house_dimension_field = self.selenium.find_element(By.NAME, "House dimension").is_enabled()
        price_field = self.selenium.find_element(By.NAME, "Price").is_enabled()
        description_field = self.selenium.find_element(By.NAME, "Description").is_enabled()
        testPassed = city_field and street_field and floor_field and house_dimension_field \
                     and price_field and description_field

        assert testPassed
    '''

    def test_filtering(self):
        self.selenium.get(self.live_server_url)
        checkin_field = self.selenium.find_element(By.ID, "check_in")
        checkout_field = self.selenium.find_element(By.ID, "check_out")
        search_button = self.selenium.find_element(By.ID, "searchButton")
        #yyyy-mm-dd
        checkin_field.send_keys("12/07/2022")
        checkout_field.send_keys("12/07/2022")
        self.selenium.execute_script("arguments[0].click();", search_button)
        self.selenium.implicitly_wait(100)
        assert self.selenium.find_element(By.ID, "confirmPopup").is_enabled()
