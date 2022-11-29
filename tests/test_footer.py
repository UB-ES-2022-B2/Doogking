from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class FooterTest(StaticLiveServerTestCase):

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

    def test_about_us(self):
        self.selenium.get(self.live_server_url)
        about_us = self.selenium.find_element(By.LINK_TEXT, "About Us")
        firstDisplay = about_us.is_displayed()
        self.selenium.get(self.live_server_url+"/aboutUs")
        self.selenium.implicitly_wait(10)
        info_about_us = self.selenium.find_element(By.ID, "info_about_us")
        assert info_about_us.is_displayed() and firstDisplay

    def test_privacy_policy(self):
        self.selenium.get(self.live_server_url)
        privacy_policy = self.selenium.find_element(By.ID, "privacyPolicy")
        firstDisplay = privacy_policy.is_displayed()
        self.selenium.get(self.live_server_url + "/privacyPolicy")
        self.selenium.implicitly_wait(10)
        info_privacy_policy = self.selenium.find_element(
            By.ID, "privacy_policy_info")
        assert info_privacy_policy.is_displayed() and firstDisplay
