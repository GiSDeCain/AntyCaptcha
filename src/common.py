from config import Config


class Common:

    def __init__(self, apka):
        self.apka = apka

    def open_main_page(self):
        driver = self.apka.driver
        driver.get(Config.main_page)


__author__ = 'GiSDeCain'
