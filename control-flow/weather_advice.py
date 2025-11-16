Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> weather = input("What's the weather like today? (sunny/rainy/cold): ")
What's the weather like today? (sunny/rainy/cold): rainy
>>> 
>>> if weather == "sunny":
...     print("Wear a t-shirt and sunglasses.")
... elif weather == "rainy":
...     print("Don't forget your umbrella and a raincoat.")
... elif weather == "cold":
...     print("Make sure to wear a warm coat and a scarf.")
... else:
