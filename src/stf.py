from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging as log
from config import Config


class Stf:

    def __init__(self, app):
        self.app = app

    def open_stf_exercise(self, number, seed):
        driver = self.app.driver
        url = Config.main_page + Config.stf_url_sub_dir + str(number) + Config.ex_url_param + str(seed)
        driver.get(url)
        title = driver.find_element_by_link_text(Config.stf_url_sub_dir + str(number + Config.ex_url_param) + str(seed))
        stf_title = driver.find_element_by_class_name('title').text
        assert title.text in stf_title
        log.info('STF exercise ' + str(number) + ' opened successful')


__author__ = 'GiSDeCain'
