from cal_score import cal_addition, cal_multiple

def test_addition():

    assert cal_addition(2, 4) == 6

def test_multiple():

    assert cal_multiple(2, 4) == 8