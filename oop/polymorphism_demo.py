Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
... 
... class Shape:
...     def area(self):
...         raise NotImplementedError("Subclasses must override this method.")
... 
... class Rectangle(Shape):
...     def __init__(self, length, width):
...         self.length = length
...         self.width = width
... 
...     def area(self):
...         return self.length * self.width
... 
... class Circle(Shape):
...     def __init__(self, radius):
...         self.radius = radius
... 
...     def area(self):
...         return math.pi * (self.radius ** 2)
