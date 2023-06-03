import pytest

from utils import dicts


@pytest.fixture
def dicts_fixture():
    return {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


@pytest.fixture
def dicts_fixture_zero():
    return {}


def test_get(dicts_fixture):
    assert dicts.get_val(dicts_fixture, 2, 'git') == 'two'
    assert dicts.get_val(dicts_fixture, 5, 'git') == 'git'


def test_get_zero(dicts_fixture_zero):
    assert dicts.get_val(dicts_fixture_zero, 3, 'git') == 'git'
    assert dicts.get_val(dicts_fixture_zero, 3, 'goods') == 'goods'
    assert dicts.get_val(dicts_fixture_zero, 1) == 'git'
