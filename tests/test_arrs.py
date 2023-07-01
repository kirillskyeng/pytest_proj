from utils.arrs import get, my_slice


def test_get():
    assert get([1,2,3,4,5,6], 2) == 3
    assert get([1,2,3,1,5,6], 0) == 1
    assert get([1,2,3,1,5,6], -1) == None


def test_my_slice():
    assert my_slice([], 2,4) == []
    assert my_slice([1,2,3,4,5,6,7,8,9,4,2,12,3,5,34,22,12,2,42334], 0,4) == [1,2,3,4]
    assert my_slice([1,2,3,4,5,6,7,8,9,4,2,12,3,5,34,22,12,2,42334], -23,4) == [1,2,3,4]
    assert my_slice([1,2,3,4,5,6,7,8,9,4,2,12,3,5,34,22,12,2,42334], 2,-23) == []