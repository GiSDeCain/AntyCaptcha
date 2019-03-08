from config import Config
import time
from seed import seed


def test_positive(fixture):
    step = fixture.common
    step.get_seed()
    step.open_exercise(1, seed)
    time.sleep(5)
    step.click_button(1)
    step.click_button(2)
    step.click_button(3)
    step.click_check_solution()
    #assert step.check_trail() == Config.test_pass_text
    step.back_to_main_page()


def test_negative(fixture):
    step = fixture.common
    step.open_exercise(1, seed)
    time.sleep(5)
    step.click_check_solution()
    #assert step.check_trail() == Config.test_fail_text
    step.back_to_main_page()


__author__ = 'GiSDeCain'
