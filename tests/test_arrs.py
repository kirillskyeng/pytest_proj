from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, int) == 2
    assert arrs.get([1, 2, 3], 0, int) == 1
    assert arrs.get([1, 2, 3], 2, int) == 3
    assert arrs.get(["test", 1, 2], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -3, int) == int



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], 1, -2) == []
    assert arrs.my_slice([-1, -2, -3], 0) == [-1, -2, -3]
    assert arrs.my_slice([], ) == []
    assert arrs.my_slice([], 0, -1) == []
    assert arrs.my_slice([-6], -2) == [-6]