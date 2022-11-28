from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class HeaderTest(StaticLiveServerTestCase):

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

    def test_icon(self):
        self.selenium.get(self.live_server_url)
        logo = self.selenium.find_element(By.ID, "main_logo")
        assert logo.is_enabled()

    def test_homepage_link(self):
        self.selenium.get(self.live_server_url)
        homepage = self.selenium.find_element(By.ID, "main_homepage")
        assert homepage.is_enabled()
