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

    def click_btn_1(self):
        driver = self.app.driver
        driver.find_element_be_name("btnButton1").click()

    def click_btn_2(self):
        driver = self.app.driver
        driver.find_element_be_name("btnButton2").click()

    def check_solution(self):
        driver = self.app.driver
        table = driver.find_elements_by_xpath('//tbody/tr/td')
        lentabel = len(table) / 3
        for i in range(int(lentabel)):
            i += 2
            solution = driver.find_element_by_xpath('//tbody/tr[' + str(i) + ']/td[3]').text
            solution = solution[14:20]
            print(solution)

    def check_button(self):
        # driver = self.app.driver
        # btn1 = driver.find
        pass


__author__ = 'GiSDeCain'
