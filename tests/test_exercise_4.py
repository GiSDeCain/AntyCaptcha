from config import Config
import time


def test_positive(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(4, seed)
    step.select_radio_button(1, 'Beluga Brown')
    time.sleep(10)
    # for i in range(3):  # Counter for step iteration is from Zero. So range(3) == 4 iterations.
    #     text = step.copy_text(i+1)
    #     step.select_radio_button(i, text)
    #     i += 1
    step.click_check_solution()
    assert step.check_trail() == Config.test_pass_text
    step.back_to_main_page()


# def test_negative(fixture):
#     step = fixture.common
#     seed = step.get_seed()
#     step.open_exercise(4, seed)
#     step.click_check_solution()
#     assert step.check_trail() == Config.test_fail_text
#     step.back_to_main_page()


__author__ = 'GiSDeCain'
