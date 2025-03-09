import pytest
from app.calculations import add,subtract,multiply,divide,BankAccount,InsufficientFunds

@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


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

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance  == 0

def test_withdraw(bank_account):
    bank_account.withdraw(10)
    assert bank_account.balance == 40

def test_deposit(bank_account):
    bank_account.deposit(10)
    assert bank_account.balance == 60

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55


@pytest.mark.parametrize("deposited,withdraw,expected",[
    (200,100,100),
    (50,10,40),
    (1200,300,900)
])

def test_bank_transaction(zero_bank_account,deposited,withdraw,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)

