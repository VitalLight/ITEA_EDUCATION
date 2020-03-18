from test.for_unit_test import parol


def test_variable_ans ():
    pa = parol()
    assert bool(pa) == False, "Len is True"