from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging as log
from config import Config


class Common:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        driver = self.app.driver
        driver.get(Config.main_page)
        assert driver.title == Config.main_page_title
        log.info('Page url: ' + Config.main_page)

    def get_seed(self):
        driver = self.app.driver
        seed = driver.find_element_by_css_selector('code>em')
        seed = seed.text
        log.info('Seed: ' + seed)
        return seed

    def write_seed_to_file(self):
        driver = self.app.driver
        seed = driver.find_element_by_css_selector('code>em').text
        file = open("../seed.py", "r+")
        try:
            file.writelines("seed = " + "'" + seed + "'")
            log.info('Seed write to file.')
        finally:
            file.close()

    def open_exercise(self, number, seed):
        driver = self.app.driver
        url = Config.main_page + Config.ex_url_sub_dir + str(number) + Config.ex_url_param + str(seed)
        driver.get(url)
        assert ('Exercise ' + str(number)) in driver.find_element_by_class_name('title').text
        log.info('Exercise ' + str(number) + ' opened successful')

    # def check_solution(self):  # This one is an experiment and it's not working yet.
    #     driver = self.app.driver
    #     table = driver.find_elements_by_xpath('//tbody/tr/td')
    #     len_tabel = len(table) / 3
    #     for i in range(int(len_tabel)):
    #         i += 2
    #         solution = driver.find_element_by_xpath('//tbody/tr[' + str(i) + ']/td[3]').text
    #         solution = solution[14:20]
    #         print(solution)  # I have no idea why it's print correctly but if I return it to method it gives "None"

    def click_button(self, step_number):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        btn = driver.find_element_by_xpath('//tbody/tr[' + str(step_number + 1) + ']/td[2]/code')
        btn1 = wait.until(EC.element_to_be_clickable((By.ID, 'btnButton1')))
        btn2 = wait.until(EC.element_to_be_clickable((By.ID, 'btnButton2')))
        if 'B1' in btn.text:
            btn1.click()
            log.info('Button 1 clicked')
        else:
            btn2.click()
            log.info('Button 2 clicked')

    def copy_text(self, step_number):
        driver = self.app.driver
        text_to_past = driver.find_element_by_xpath('//tbody/tr[' + str(step_number + 1) + ']/td[2]/code[1]').text
        return text_to_past

    def past_text(self, input_id, text_to_past):
        driver = self.app.driver
        textbox = driver.find_element_by_id(str(input_id))
        textbox.clear()
        textbox.send_keys(text_to_past)

    def click_check_solution(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, 'solution'))).click()
        log.info('Checking solution...')

    def check_trail(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        steps_table = driver.find_elements_by_xpath('//tbody/tr/td')
        len_tabel = len(steps_table) / 3
        solution_text = ''
        control_element = driver.find_element_by_class_name('wrap').text
        for i in range(int(len_tabel)):
            i += 2
            solution_text = driver.find_element_by_xpath('//tbody/tr[' + str(i) + ']/td[3]').text
            solution_text = solution_text[14:20]
        try:
            if solution_text == control_element:
                wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'wrap'), Config.test_pass_text))
            else:
                wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'wrap'), Config.test_fail_text))
        finally:
            return driver.find_element_by_class_name('wrap').text

    def back_to_main_page(self):
        Common.open_main_page(self)

    def click_button_ex2(self, step_number):
        driver = self.app.driver
        btn = driver.find_element_by_xpath('//tbody/tr[' + str(step_number + 1) + ']/td[2]/code')
        if "B1" in btn.text:
            driver.find_element_by_xpath('//*[@id="btnButton1"]').click()
        else:
            driver.find_element_by_xpath('//*[@id="btnButton2"]').click()


__author__ = 'GiSDeCain'
