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
        sub_locator = Config.stf_url_sub_dir + str(number) + Config.ex_url_param + str(seed)  # It is a string for main_page_title xpath locator.
        main_page_title = driver.find_element_by_xpath('//a[@href="/' + sub_locator + '"]').text  # find anchor text using anchor href. It is title of exercise on main page for later assertion.
        url = Config.main_page + Config.stf_url_sub_dir + str(number) + Config.ex_url_param + str(seed)  # Exercise URL
        driver.get(url)
        stf_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))  # Exercise title on exercise page. collected for assertion.
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
        log.info('Trail answer is: ' + trail)
        return trail

    def find_id(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        btn_id = wait.until(EC.presence_of_element_located((By.XPATH, '//ol/li[1]/em')))
        log.info('Button id is: ' + btn_id.text)
        return btn_id.text

    def click_button_by_id(self, btn_id):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        btn = wait.until(EC.element_to_be_clickable((By.ID, btn_id))).click()
        log.info('Text of located button is: ' + btn.text)


__author__ = 'GiSDeCain'
