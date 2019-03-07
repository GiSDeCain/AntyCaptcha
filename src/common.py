from config import Config


class Common:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        driver = self.app.driver
        driver.get(Config.main_page)

    def open_exercise(self, number):
        driver = self.app.driver
        url = Config.main_page + Config.ex_sub_dir + str(number)
        driver.get(url)


__author__ = 'GiSDeCain'
