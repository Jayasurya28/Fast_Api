import pytest
from app.calculations import add,subtract,multiply,divide,BankAccount


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

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount():
    bank_account = BankAccount()
    assert bank_account.balance  == 0

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(10)
    assert bank_account.balance == 40

def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(10)
    assert bank_account.balance == 60

def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55