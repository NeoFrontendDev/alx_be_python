Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import sys
from bank_account import BankAccount

def main():
...     account = BankAccount(100)
... 
...     if len(sys.argv) < 2:
...         print("Usage: python main-0.py <command>:<amount>")
...         print("Commands: deposit, withdraw, display")
...         sys.exit(1)
... 
...     command, *params = sys.argv[1].split(':')
...     amount = float(params[0]) if params else None
... 
...     if command == "deposit" and amount is not None:
...         account.deposit(amount)
...         print(f"Deposited: ${amount}")
... 
...     elif command == "withdraw" and amount is not None:
...         if account.withdraw(amount):
...             print(f"Withdrew: ${amount}")
...         else:
...             print("Insufficient funds.")
... 
...     elif command == "display":
...         account.display_balance()
... 
...     else:
...         print("Invalid command.")
... 
... if __name__ == "__main__":
...     main()
