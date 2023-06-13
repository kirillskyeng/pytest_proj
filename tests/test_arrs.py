from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, 2) == 2
    assert arrs.get([], -1, 0) == 0


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
