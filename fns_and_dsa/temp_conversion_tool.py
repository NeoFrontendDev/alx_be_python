Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
... CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
... 
... def convert_to_celsius(fahrenheit):
...     """Convert Fahrenheit to Celsius using global conversion factor."""
...     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
... 
... def convert_to_fahrenheit(celsius):
...     """Convert Celsius to Fahrenheit using global conversion factor."""
...     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
... 
... def main():
...     temp_input = input("Enter the temperature to convert: ")
... 
...     try:
...         temperature = float(temp_input)
...     except ValueError:
...         raise ValueError("Invalid temperature. Please enter a numeric value.")
... 
...     unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
... 
...     if unit == "F":
...         converted = convert_to_celsius(temperature)
...         print(f"{temperature}°F is {converted}°C")
... 
...     elif unit == "C":
...         converted = convert_to_fahrenheit(temperature)
...         print(f"{temperature}°C is {converted}°F")
... 
...     else:
...         raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
... 
... if __name__ == "__main__":
...     main()
