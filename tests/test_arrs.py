from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_get_with_positive_index():
    assert arrs.get([1, 2, 3], 1, "test") == 2


def test_get_with_index_out_of_range():
    assert arrs.get([1, 2, 3], 5, "test") == "test"


def test_get_with_empty_list():
    assert arrs.get([], 0, "test") == "test"


def test_slice_with_negative_start():
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]


def test_slice_with_negative_end():
    assert arrs.my_slice([1, 2, 3, 4], end=-2) == [1, 2]


def test_slice_with_negative_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4], -2, -1) == [3]


def test_slice_with_start_and_end_out_of_range():
    assert arrs.my_slice([1, 2, 3, 4], 5, 10) == []


def test_slice_with_empty_list():
    assert arrs.my_slice([], 0, 2) == []
