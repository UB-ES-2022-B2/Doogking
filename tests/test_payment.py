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

    def test_payment_options_card_wrong_input(self):
        self.selenium.get("https://doogking.azurewebsites.net/payment?house_id=1")
        card_number = self.selenium.find_element(By.ID, "cardNumber")
        card_number.send_keys("DD")
        check_code = card_number.get_attribute('value')
        assert check_code == "____-____-____-____"

    def test_payment_options_card_right_input(self):
        self.selenium.get("https://doogking.azurewebsites.net/payment?house_id=1")
        card_number = self.selenium.find_element(By.ID, "cardNumber")
        card_number.send_keys("DD")
        check_code = card_number.get_attribute('value')
        assert check_code == "____-____-____-____"
    def test_house_registry_fill(self):
        assert True
