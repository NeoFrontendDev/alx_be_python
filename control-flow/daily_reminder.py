Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
task = input("Enter your task: ")
Enter your task: Finish project report
>>> priority = input("Priority (high/medium/low): ").lower()
Priority (high/medium/low): high
>>> time_bound = input("Is it time-bound? (yes/no): ").lower()
Is it time-bound? (yes/no): yes
>>> 
>>> match priority:
...     case "high":
...         message = f"'{task}' is a high priority task"
...     case "medium":
...         message = f"'{task}' is a medium priority task"
...     case "low":
...         message = f"'{task}' is a low priority task"
...     case _:
...         message = f"'{task}' has an unknown priority level"
... 
...         
>>> if time_bound == "yes":
...     message += " that requires immediate attention today!"
... else:
...     message = f"Note: {message}. Consider completing it when you have free time."
... 
...     
>>> print("\nReminder:", message)

Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
