def perform_operation(num1, num2, operation):
    """Performs basic arithmetic operations"""
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            return num1 / num2
        case _:
            raise ValueError(f"Invalid operation: {operation}")
