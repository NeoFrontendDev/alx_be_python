Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from class_static_methods_demo import Calculator
... 
... def main():
...     sum_result = Calculator.add(10, 5)
...     print(f"The sum is: {sum_result}")
... 
...     product_result = Calculator.multiply(10, 5)
...     print(f"The product is: {product_result}")
... 
... if __name__ == "__main__":
...     main()
