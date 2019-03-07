import time


def test_positive(fixture):
    fixture.common.open_main_page()
    seed = fixture.common.get_seed()
    fixture.common.open_exercise(1, seed)
    print('dupa: ' + fixture.common.check_solution())
    time.sleep(1)


__author__ = 'GiSDeCain'
