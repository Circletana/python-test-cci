from cal_score import cal_addition, cal_multiple
import pytest

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (3, 5, 8), (5, 8, 13)])
def test_addition(a, b, expected):

    assert cal_addition(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (3, 5, 15), (5, 8, 40)])
def test_multiple(a, b, expected):

    assert cal_multiple(a, b) == expected