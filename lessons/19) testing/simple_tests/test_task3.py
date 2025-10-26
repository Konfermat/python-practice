from task3 import add
import pytest

@pytest.mark.parametrize('a,b,expected', [
    (1, 2, 3),
    (100, 200, 300),
])

def test_add_positive(a, b, expected):
    actual = add(a, b)
    assert actual == expected, (f'ожидалось {expected}, получено {actual}, для {a}+{b}')


