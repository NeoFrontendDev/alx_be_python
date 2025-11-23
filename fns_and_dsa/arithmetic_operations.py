Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def perform_operation(num1, num2, operation):
...     if operation == "add":
...         return num1 + num2
...     elif operation == "subtract":
...         return num1 - num2
...     elif operation == "multiply":
...         return num1 * num2
...     elif operation == "divide":
...         if num2 == 0:
...             return "Error: Cannot divide by zero"
...         return num1 / num2
...     else: return "Error: Invalid operation"
... 
...     
