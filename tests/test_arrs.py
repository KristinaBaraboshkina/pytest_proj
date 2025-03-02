import pytest
from utils import arrs

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

# 🔹 Фикстура для пустого списка
@pytest.fixture
def empty_list():
    return []

# 🔹 Фикстура для значений по умолчанию
@pytest.fixture
def default_value():
    return "test"

def test_get(sample_list, empty_list, default_value):
    assert arrs.get(sample_list, 1, default_value) == 2
    assert arrs.get(empty_list, 0, default_value) == default_value
    assert arrs.get(empty_list, 1, default_value) == default_value

def test_slice(sample_list, empty_list):
    assert arrs.my_slice(sample_list, 1, 3) == [2, 3]
    assert arrs.my_slice(sample_list, 1) == [2, 3, 4, 5]
    assert arrs.my_slice(sample_list, 1, 1) == []
    assert arrs.my_slice(sample_list) == [1, 2, 3, 4, 5]
    assert arrs.my_slice(empty_list) == []