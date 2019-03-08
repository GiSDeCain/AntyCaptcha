from selenium.webdriver.chrome.webdriver import WebDriver
from src.common import Common
from config import Config


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(5)
        self.driver.get(Config.main_page)
        self.common = Common(self)

    def destroy(self):
        self.driver.close()
        self.driver.quit()


__author__ = 'GiSDeCain'
