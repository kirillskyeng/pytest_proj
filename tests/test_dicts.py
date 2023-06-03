from utils import dicts


def test_get():
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three', 4: 'four'}, 2, 'git') == 'two'
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three', 4: 'four'}, 5, 'git') == 'git'
    assert dicts.get_val({}, 3, 'git') == 'git'
    assert dicts.get_val({}, 3, 'goods') == 'goods'
    assert dicts.get_val({}, 1) == 'git'

