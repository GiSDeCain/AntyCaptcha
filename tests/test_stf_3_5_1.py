from config import Config


def test_stf_3_2_1_pos(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-1', seed)
    btn_id = fixture.stf.find_id()
    fixture.stf.click_button_by_id(btn_id)
    fixture.common.click_check_solution()
    assert fixture.common.check_trail() == Config.test_pass_text
    fixture.common.back_to_main_page()


def test_stf_3_2_1_neg(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-1', seed)
    fixture.common.click_check_solution()
    assert fixture.common.check_trail() == Config.test_pass_text
    fixture.common.back_to_main_page()


__author__ = 'GiSDeCain'
