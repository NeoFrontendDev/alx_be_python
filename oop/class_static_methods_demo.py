Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Calculator:
...     calculation_type = "Arithmetic Operations"
... 
...     @staticmethod
...     def add(a, b):
...         return a + b
... 
...     @classmethod
...     def multiply(cls, a, b):
...         print(f"Calculation type: {cls.calculation_type}")
...         return a * b
