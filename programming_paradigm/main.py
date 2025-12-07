Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import sys
... from robust_division_calculator import safe_divide
... 
... def main():
...     if len(sys.argv) != 3:
...         print("Usage: python main.py <numerator> <denominator>")
...         sys.exit(1)
... 
...     numerator = sys.argv[1]
...     denominator = sys.argv[2]
... 
...     result = safe_divide(numerator, denominator)
...     print(result)
... 
... if __name__ == "__main__":
...     main()
