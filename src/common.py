from config import Config


class Common:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        driver = self.app.driver
        driver.get(Config.main_page)

    def get_seed(self):
        driver = self.app.driver
        seed = driver.find_element_by_css_selector('code>em')
        seed = seed.text
        return seed

    def open_exercise(self, number, seed):
        driver = self.app.driver
        url = Config.main_page + Config.ex_url_sub_dir + str(number) + Config.ex_url_param + str(seed)
        driver.get(url)

    def check_solution(self):
        driver = self.app.driver
        table = driver.find_elements_by_xpath('//tbody/tr/td')
        lentabel = len(table) / 3
        for i in range(int(lentabel)):
            i += 2
            solution = driver.find_element_by_xpath('//tbody/tr[' + str(i) + ']/td[3]').text
            solution = solution[14:20]
            print(solution)

    def click_button(self, step_number):
        driver = self.app.driver
        step_number += 1
        btn = driver.find_element_by_xpath('//tbody/tr[' + str(step_number) + ']/td[2]/code')
        btn1 = driver.find_element_by_name('btnButton1')
        btn2 = driver.find_element_by_name('btnButton2')
        if 'B1' in btn.text:
            btn1.click()
        else:
            btn2.click()

    def click_check_solution(self):
        driver = self.app.driver
        driver.find_element_by_id('solution').click()

    def check_trail(self):
        driver = self.app.driver
        text = driver.find_element_by_class_name('wrap').text
        return text


__author__ = 'GiSDeCain'
