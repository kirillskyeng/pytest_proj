from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_get_index_out_of_bounds():
    assert arrs.get([1, 2, 3], 5, "default") == "default"


def test_slice_negative_indices():
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]

def test_slice_out_of_bounds():
    assert arrs.my_slice([1, 2, 3], 1, 10) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -10, 2) == [1, 2]

def test_slice_empty_list():
    assert arrs.my_slice([], 0, 1) == []

def test_slice_none_indices():
    assert arrs.my_slice([1, 2, 3], None, None) == [1, 2, 3]