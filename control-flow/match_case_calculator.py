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
