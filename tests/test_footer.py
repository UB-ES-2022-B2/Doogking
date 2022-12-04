from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import action_builder
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
        about_us = self.selenium.find_element(By.ID, "aboutUs")
        self.selenium.execute_script("arguments[0].click();", about_us)
        self.selenium.implicitly_wait(100)
        info_about_us = self.selenium.find_element(By.ID, "info_about_us")
        assert info_about_us.is_displayed()

    def test_privacy_policy(self):
        self.selenium.get(self.live_server_url)
        privacy_policy = self.selenium.find_element(By.ID, "privacyPolicy")
        self.selenium.execute_script("arguments[0].click();", privacy_policy)
        self.selenium.implicitly_wait(100)
        info_privacy_policy = self.selenium.find_element(
            By.ID, "privacy_policy_info")
        assert info_privacy_policy.is_displayed()
