Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> monthly_income = float(input("Enter your monthly inncome: "))
Enter your monthly inncome: 5000
>>> monthly_expenses = float(input("Enter your total monthly expenses: "))
Enter your total monthly expenses: 4000
>>> monthly_savings = monthly_income - monthly_expenses
>>> projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
>>> print(f"Your monthly savings are ${monthly_savings:.2f}.")
Your monthly savings are $1000.00.
>>> print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
Projected savings after one year, with interest, is: $12600.00.
