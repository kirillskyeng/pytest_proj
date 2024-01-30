import pytest
from utils.arrs import my_slice


def test_my_slice():
    # Тест на извлечение среза от начала до конца
    assert my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Тест на извлечение среза с указанием начала и конца
    assert my_slice([1, 2, 3, 4, 5], start=1, end=4) == [2, 3, 4]

    # Тест на извлечение среза с отрицательными индексами
    assert my_slice([1, 2, 3, 4, 5], start=-3, end=-1) == [3, 4]

    # Тест на извлечение среза с несуществующими индексами
    assert my_slice([1, 2, 3, 4, 5], start=10, end=20) == []

    # Тест на пустой список
    assert my_slice([], start=1, end=3) == []

    # Тест на срез с началом и без конца
    assert my_slice([1, 2, 3, 4, 5], start=2) == [3, 4, 5]
