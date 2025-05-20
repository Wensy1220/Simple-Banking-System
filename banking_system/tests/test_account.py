#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest
from banking_system.account import Account
from banking_system.exceptions import InsufficientFundsError, InvalidAmountError

def test_account_creation():
    account = Account("123", "Wenxi Chen", 100.0)
    assert account.account_id == "123"
    assert account.name == "Wenxi Chen"
    assert account.balance == 100.0

def test_deposit():
    account = Account("123", "Wenxi Chen")
    account.deposit(50.0)
    assert account.balance == 50.0

def test_deposit_negative_amount():
    account = Account("123", "Wenxi Chen")
    with pytest.raises(InvalidAmountError):
        account.deposit(-10.0)

def test_withdraw():
    account = Account("123", "Wenxi Chen", 100.0)
    account.withdraw(50.0)
    assert account.balance == 50.0

def test_withdraw_insufficient_funds():
    account = Account("123", "Wenxi Chen", 30.0)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(50.0)

def test_withdraw_negative_amount():
    account = Account("123", "Wenxi Chen", 100.0)
    with pytest.raises(InvalidAmountError):
        account.withdraw(-10.0)

def test_transfer():
    account1 = Account("123", "Wenxi Chen", 100.0)
    account2 = Account("456", "Haitao Jiang", 50.0)
    account1.transfer_to(account2, 30.0)
    assert account1.balance == 70.0
    assert account2.balance == 80.0

def test_transfer_insufficient_funds():
    account1 = Account("123", "Wenxi Chen", 20.0)
    account2 = Account("456", "Haitao Jiang", 50.0)
    with pytest.raises(InsufficientFundsError):
        account1.transfer_to(account2, 30.0)

def test_csv_serialization():
    account = Account("123", "Wenxi Chen", 100.0)
    csv_str = account.to_csv()
    new_account = Account.from_csv(csv_str)
    assert new_account.account_id == "123"
    assert new_account.name == "Wenxi Chen"
    assert new_account.balance == 100.0


# In[ ]:




