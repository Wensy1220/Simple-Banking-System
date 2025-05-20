


class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds for a withdrawal or transfer"""
    pass

class AccountNotFoundError(Exception):
    """Raised when an account is not found in the bank"""
    pass

class InvalidAmountError(Exception):
    """Raised when an invalid amount is provided (e.g., negative amount)"""
    pass

