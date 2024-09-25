"""defines functions to convert temperatures between Celsius and Fahrenheit"""
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Converts a Fahrenheit temperature to Celsius.

    Args:
        fahrenheit_temperature (float): The Fahrenheit temperature to be converted.

    Returns:
        float: The equivalent Celsius temperature.
    """
    celsius_temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius_temperature


def convert_to_fahrenheit(celsius):
    """
    Converts a Celsius temperature to Fahrenheit.

    Args:
        celsius_temperature (float): The Celsius temperature to be converted.

    Returns:
        float: The equivalent Fahrenheit temperature.
    """
    fahrenheit_temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit_temperature


temp = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
unit = unit.upper()

# check if the input is numeric
if temp.isnumeric():
    temp = float(temp)
    if unit == "C":
        # convert to Fahrenheit
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif unit == "F":
        # convert to Celsius
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("Invalid temperature. Please enter a numeric value.")
