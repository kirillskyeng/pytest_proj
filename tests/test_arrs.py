from utils.arrs import my_slice, get


def test_get_existing_index():
    assert get([1, 2, 3], 0) == 1
    assert get([1, 2, 3], 1) == 2
    assert get([1, 2, 3], 2) == 3

def test_get_non_existing_index():
    assert get([1, 2, 3], 3) is None
    assert get([1, 2, 3], -1) is None

def test_get_with_default_value():
    assert get([1, 2, 3], 3, 'default') == 'default'
    assert get([1, 2, 3], -1, 'default') == 'default'
    assert get([], 0, 'default') == 'default'

def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], 0, 3) == [1, 2, 3]
    assert my_slice([1, 2, 3, 4, 5], 0, -1) == [1, 2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert my_slice([], 0, 1) == []

def test_my_slice():
    # Тест на пустой входной список
    assert my_slice([], 0, 1) == []

    # Тесты на извлечение всего списка
    assert my_slice([1, 2, 3], 0, 3) == [1, 2, 3]
    assert my_slice([1, 2, 3], 0, None) == [1, 2, 3]
    assert my_slice([1, 2, 3]) == [1, 2, 3]

    # Тесты на извлечение подмножества списка
    assert my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5], -3, None) == [3, 4, 5]

    # Тесты на отрицательные индексы
    assert my_slice([1, 2, 3], -1) == [3]
    assert my_slice([1, 2, 3], -2, -1) == [2]
    assert my_slice([1, 2, 3], -10, 1) == [1]




