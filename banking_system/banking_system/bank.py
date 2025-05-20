import csv
from pathlib import Path
from typing import Dict, List
from .account import Account
from .exceptions import AccountNotFoundError, InvalidAmountError

class Bank:
    def __init__(self):
        """Initialize a bank with an empty dictionary of accounts."""
        self.accounts: Dict[str, Account] = {}

    def create_account(self, account_id: str, name: str, initial_balance: float = 0.0) -> Account:
        """
        Create a new account and add it to the bank.
        
        Args:
            account_id: Unique identifier for the account
            name: Name of the account holder
            initial_balance: Starting balance (default 0.0)
            
        Returns:
            The newly created Account object
        """
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative")
            
        account = Account(account_id, name, initial_balance)
        self.accounts[account_id] = account
        return account

    def get_account(self, account_id: str) -> Account:
        """
        Retrieve an account by its ID.
        
        Args:
            account_id: The ID of the account to retrieve
            
        Returns:
            The Account object
            
        Raises:
            AccountNotFoundError: If the account doesn't exist
        """
        account = self.accounts.get(account_id)
        if account is None:
            raise AccountNotFoundError(f"Account with ID {account_id} not found")
        return account

    def deposit(self, account_id: str, amount: float) -> None:
        """Deposit money into an account."""
        account = self.get_account(account_id)
        account.deposit(amount)

    def withdraw(self, account_id: str, amount: float) -> None:
        """Withdraw money from an account."""
        account = self.get_account(account_id)
        account.withdraw(amount)

    def transfer(self, from_account_id: str, to_account_id: str, amount: float) -> None:
        """
        Transfer money between two accounts.
        
        Args:
            from_account_id: The account to transfer from
            to_account_id: The account to transfer to
            amount: The amount to transfer
        """
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        from_account.transfer_to(to_account, amount)

    def save_to_csv(self, file_path: str) -> None:
        """
        Save all accounts to a CSV file.
        
        Args:
            file_path: Path to the CSV file
        """
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['account_id', 'name', 'balance'])  # header
            for account in self.accounts.values():
                writer.writerow([account.account_id, account.name, account.balance])

    def load_from_csv(self, file_path: str) -> None:
        """
        Load accounts from a CSV file.
        
        Args:
            file_path: Path to the CSV file
        """
        path = Path(file_path)
        if not path.exists():
            return
            
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header
            self.accounts.clear()
            for row in reader:
                if len(row) == 3:  # account_id, name, balance
                    account = Account.from_csv(','.join(row))
                    self.accounts[account.account_id] = account

    def get_all_accounts(self) -> List[Account]:
        """Return a list of all accounts in the bank."""
        return list(self.accounts.values())