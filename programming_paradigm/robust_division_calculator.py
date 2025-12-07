Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def safe_divide(numerator, denominator):
...     try:
...         num = float(numerator)
...         den = float(denominator)
... 
...         try:
...             result = num / den
...             return f"The result of the division is {result}"
...         except ZeroDivisionError:
...             return "Error: Cannot divide by zero."
... 
...     except ValueError:
...         return "Error: Please enter numeric values only."
