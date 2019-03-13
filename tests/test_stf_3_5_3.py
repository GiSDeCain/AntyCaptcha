from config import Config


def test_stf_3_5_3_pos(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-3', seed)
    btn_tag = fixture.stf.find_attribute()
    fixture.stf.click_button_by_tag_name(btn_tag)
    assert fixture.stf.stf_solution() == Config.test_pass_text
    fixture.common.back_to_main_page()


def test_stf_3_5_3_neg(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-3', seed)
    btn_tag = fixture.stf.find_attribute()
    fixture.stf.fake_click_button_by_tag_name(btn_tag)
    assert fixture.stf.stf_solution() == Config.test_fail_text
    fixture.common.back_to_main_page()


__author__ = 'GiSDeCain'
