Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
... 
... 
... class EBook(Book):
...     """Represents an electronic book."""
... 
...     def __init__(self, title, author, file_size):
...         super().__init__(title, author)
...         self.file_size = file_size  # in KB
... 
... 
... class PrintBook(Book):
...     """Represents a printed physical book."""
... 
...     def __init__(self, title, author, page_count):
...         super().__init__(title, author)
...         self.page_count = page_count
... 
... 
... class Library:
...     """Represents a library that stores various types of books."""
... 
...     def __init__(self):
...         self.books = []
... 
...     def add_book(self, book):
...         """Add a book of any type to the library."""
...         self.books.append(book)
... 
...     def list_books(self):
...         """Print details of each book in the library."""
...         for book in self.books:
...             if isinstance(book, EBook):
...                 print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
...             elif isinstance(book, PrintBook):
...                 print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
...             else:
...                 print(f"Book: {book.title} by {book.author}")
