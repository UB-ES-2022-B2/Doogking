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
        m = ''.join(chr(i) for i in range(128))
        for characters in m:
            card_number.send_keys(characters)
        check_code = card_number.get_attribute('value')
        assert check_code == "0123-4567-89__-____"

    def test_payment_options_card_right_input(self):
        self.selenium.get("https://doogking.azurewebsites.net/payment?house_id=1")
        card_number = self.selenium.find_element(By.ID, "cardNumber")
        card_number.send_keys("12345")
        check_code = card_number.get_attribute('value')
        assert check_code == "1234-5___-____-____"

    def test_cvc_good(self):
        self.selenium.get("https://doogking.azurewebsites.net/payment?house_id=1")
        card_number = self.selenium.find_element(By.ID, "cvc")
        card_number.send_keys("544")
        check_code = card_number.get_attribute('value')
        assert check_code == "544"

    def test_cvc_bad(self):
        self.selenium.get("https://doogking.azurewebsites.net/payment?house_id=1")
        card_number = self.selenium.find_element(By.ID, "cvc")
        m = ''.join(chr(i) for i in range(128))
        for characters in m:
            card_number.send_keys(characters)
        check_code = card_number.get_attribute('value')
        assert check_code == "012"

    def test_calendar(self):
        msg = "Expiry date has to be greater or equal than current date."
        self.selenium.get("https://doogking.azurewebsites.net/payment?house_id=1")
        calendar = self.selenium.find_element(By.ID, "expiryDate")
        calendar.send_keys("12/01/2022")
        assert True
