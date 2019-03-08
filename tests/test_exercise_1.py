from config import Config
import time


def test_positive(fixture):
    fixture.common.open_main_page()
    seed = fixture.common.get_seed()
    fixture.common.open_exercise(1, seed)
    fixture.common.click_button(1)
    fixture.common.click_button(2)
    fixture.common.click_button(3)
    fixture.common.click_check_solution()
    time.sleep(1)
    assert fixture.common.check_trail() == Config.test_pass_text
    time.sleep(10)


__author__ = 'GiSDeCain'
