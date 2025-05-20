class Account:
    def __init__(self, account_id: str, name: str, balance: float = 0.0):
        """
            account_id: Unique ID for the account
            name: Name of the account holder
            balance: Starting balance
        """
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount

    def transfer_to(self, other_account: 'Account', amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for transfer")
        
        self.balance -= amount
        other_account.balance += amount

    def __repr__(self) -> str:
        return f"Account(account_id='{self.account_id}', name='{self.name}', balance={self.balance})"

    def to_csv(self) -> str:
        """Convert account data to CSV format."""
        return f"{self.account_id},{self.name},{self.balance}"

    @classmethod
    def from_csv(cls, csv_string: str) -> 'Account':
        account_id, name, balance = csv_string.strip().split(',')
        return cls(account_id, name, float(balance))