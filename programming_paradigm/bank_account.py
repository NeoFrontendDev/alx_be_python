>>> class BankAccount:
...     def __init__(self, initial_balance=0):
...         """Initialize account with an optional starting balance."""
...         self.account_balance = initial_balance
... 
...     def deposit(self, amount):
...         """Add money to the account."""
...         self.account_balance += amount
... 
...     def withdraw(self, amount):
...         """
...         Withdraw money if sufficient funds exist.
...         Return True if successful, otherwise False.
...         """
...         if amount <= self.account_balance:
...             self.account_balance -= amount
...             return True
...         return False
... 
...     def display_balance(self):
...         """Print the current balance in a friendly format."""
        print(f"Current Balance: ${self.account_balance}")
