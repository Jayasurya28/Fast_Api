from app.calculations import add,subtract,multiply,divide

def test_add():
    print("testing add function")
    assert add(5,3) == 8

def test_subtract():
    print("testing subtract function")
    assert subtract(9,4) == 5

def test_multiply():
    print("testing multiply function")
    assert multiply(5,3) == 15

def test_divide():
    print("testing divide function")
    assert divide(9,3) == 3


