from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging as log
from config import Config


class Stf:

    def __init__(self, app):
        self.app = app

    def open_stf_exercise(self, number, seed):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        sub_locator = Config.stf_url_sub_dir + str(number) + Config.ex_url_param + str(seed)
        main_page_title = driver.find_element_by_xpath('//a[@href="/' + sub_locator + '"]').text
        url = Config.main_page + Config.stf_url_sub_dir + str(number) + Config.ex_url_param + str(seed)
        driver.get(url)
        stf_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))
        assert main_page_title.lower() in stf_title.text.lower()
        log.info('STF exercise ' + str(number) + ' opened successful')

    def open_solution_url(self, seed):
        driver = self.app.driver
        url = Config.main_page + Config.stf_url_sub_dir + '3-2-1/solution' + Config.ex_url_param + str(seed)
        driver.get(url)
        log.info('Opened solution page using url: ' + url)

    def stf_solution(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        trail = wait.until(EC.presence_of_element_located((By.ID, 'trail'))).text
        return trail
        log.info('Trail answer is: ' + trail)


__author__ = 'GiSDeCain'
