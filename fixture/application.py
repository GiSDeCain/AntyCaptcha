from selenium.webdriver.chrome.webdriver import WebDriver
from src.common import Common
from config import Config


class Application:

    def __init__(self, base_url=Config.main_page):
        self.driver = WebDriver()
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.common = Common(self)

    def destroy(self):
        self.driver.close()
        self.driver.quit()


__author__ = 'GiSDeCain'
