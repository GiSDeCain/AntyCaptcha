import time


def test_positive(fixture):
    fixture.common.open_main_page()
    seed = fixture.common.get_seed()
    fixture.common.open_exercise(1, seed)
    sol = fixture.common.check_solution()
    print(str(sol))
    time.sleep(1)


__author__ = 'GiSDeCain'
