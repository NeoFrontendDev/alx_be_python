Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num1 = float(input("Enter the first number: "))
Enter the first number: 10
>>> num2 = float(input("Enter the second number: "))
Enter the second number: 5
>>> operation = input("Choose the operation (+, -, *, /): ")
Choose the operation (+, -, *, /): *
>>> match operation:
...     case "*":
...         result = num1 * num2
...         print(f"The result is {result}.")
