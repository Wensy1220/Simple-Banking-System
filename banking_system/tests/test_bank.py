#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
import tempfile
from banking_system.bank import Bank
from banking_system.exceptions import AccountNotFoundError, InvalidAmountError

def test_create_account():
    bank = Bank()
    account = bank.create_account("123", "Wenxi Chen", 100.0)
    assert account.account_id == "123"
    assert account.name == "Wenxi Chen"
    assert account.balance == 100.0

def test_get_account():
    bank = Bank()
    bank.create_account("123", "Wenxi Chen")
    account = bank.get_account("123")
    assert account.account_id == "123"

def test_get_nonexistent_account():
    bank = Bank()
    with pytest.raises(AccountNotFoundError):
        bank.get_account("999")

def test_deposit():
    bank = Bank()
    bank.create_account("123", "Wenxi Chen")
    bank.deposit("123", 50.0)
    account = bank.get_account("123")
    assert account.balance == 50.0

def test_withdraw():
    bank = Bank()
    bank.create_account("123", "Wenxi Chen", 100.0)
    bank.withdraw("123", 50.0)
    account = bank.get_account("123")
    assert account.balance == 50.0

def test_transfer():
    bank = Bank()
    bank.create_account("123", "Wenxi Chen", 100.0)
    bank.create_account("456", "Haitao Jiang", 50.0)
    bank.transfer("123", "456", 30.0)
    account1 = bank.get_account("123")
    account2 = bank.get_account("456")
    assert account1.balance == 70.0
    assert account2.balance == 80.0

def test_save_and_load_csv():
    bank = Bank()
    bank.create_account("123", "Wenxi Chen", 100.0)
    bank.create_account("456", "Haitao Jiang", 50.0)
    
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmp_path = tmpfile.name
    
    try:
        bank.save_to_csv(tmp_path)
        
        new_bank = Bank()
        new_bank.load_from_csv(tmp_path)
        
        accounts = new_bank.get_all_accounts()
        assert len(accounts) == 2
        assert any(acc.account_id == "123" and acc.balance == 100.0 for acc in accounts)
        assert any(acc.account_id == "456" and acc.balance == 50.0 for acc in accounts)
    finally:
        import os
        os.unlink(tmp_path)

