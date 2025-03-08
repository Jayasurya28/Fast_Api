import pytest
from app.calculations import add,subtract,multiply,divide


@pytest.mark.parametrize("num1,num2,expected",[
    (5,3,8),
    (9,4,13),
    (5,3,8),
    (9,3,12)
])

def test_add(num1,num2,expected):
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(9,4) == 5

def test_multiply():
    assert multiply(5,3) == 15

def test_divide():
    assert divide(9,3) == 3


