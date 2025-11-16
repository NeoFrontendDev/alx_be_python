Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> size = int(input("Enter the size of the pattern: "))
Enter the size of the pattern: 4
>>> 
>>> row = 0
>>> 
>>> while row < size:
...     for i in range(size):
...         print("*", end="")
...     print()
...     row += 1
