class BankAccount:

    """
    A class that performs banking operations.
    """

    def __init__(self, account_balance=0):
        """Initialize account balance"""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Deposit amount to account balance"""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount from account balance.
        If insufficient balance, return False
        """
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Display current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")
