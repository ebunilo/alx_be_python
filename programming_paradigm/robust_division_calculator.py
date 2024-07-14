def safe_divide(numerator, denominator):
    """Division calculator that handles errors like 
    division by zero and non-numeric inputs"""
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    return f"The result of the division is {result}"
