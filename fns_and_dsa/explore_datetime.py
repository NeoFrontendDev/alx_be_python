Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from datetime import datetime, timedelta
... 
... def display_current_datetime():
...     current_date = datetime.now()
...     print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
...     return current_date
... 
... def calculate_future_date(current_date, days_to_add):
...     future_date = current_date + timedelta(days=days_to_add)
...     print("Future date:", future_date.strftime("%Y-%m-%d"))
...     return future_date
... 
... def main():
...     current_date = display_current_datetime()
... 
...     try:
...         days = int(input("Enter the number of days to add to the current date: "))
...         calculate_future_date(current_date, days)
...     except ValueError:
...         print("Invalid input. Please enter an integer.")
... 
... if __name__ == "__main__":
...     main()
