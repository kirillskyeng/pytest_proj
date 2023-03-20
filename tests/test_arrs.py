from utils import arrs
import pytest


@pytest.mark.parametrize("a, b, c, expected_result", [([1, 2, 3], 2, "test", 3), ([], 0, "test", "test")])
def test_get(a, b, c, expected_result):
    assert arrs.get(a, b, c) == expected_result


# @pytest.mark.parametrize()


@pytest.mark.parametrize("coll, start, end, expected_result", [([1, 2, 3, 4], 1, 3, [2, 3]), ([1, 2, 3], 1, None, [2, 3])])
def test_slice(coll, start, end, expected_result):
    assert arrs.my_slice(coll, start, end) == expected_result
