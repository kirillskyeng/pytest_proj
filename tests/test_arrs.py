from utils import arrs


def test_get():
    from utils.arrs import get
    assert get([1, 2, 3], 0) == 1
    assert get([1, 2, 3], 1) == 2
    assert get([1, 2, 3], 2) == 3
    assert get([1, 2, 3], 3, "default") == "default"
    assert get([1, 2, 3], -1, "default") == "default"
    assert get([], 0, "default") == "default"
    assert get([1, 2, 3], 4) == None
    assert get([1, 2, 3], -1) == None

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
