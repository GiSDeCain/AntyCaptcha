from selenium.webdriver.chrome.webdriver import WebDriver
from src.common import Common


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(5)
        self.common = Common

    def destroy(self):
        self.driver.close()
        self.driver.quit()


__author__ = 'GiSDeCain'
