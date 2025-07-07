def reverse_text(text: str) -> str:
    """
    Reverses the input text.
    
    Args:
        text (str): The input text to reverse.
    
    Returns:
        str: The reversed text.
    """
    return text[::-1]

def simple_calculator(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic calculations.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform (+, -, *, /).
    
    Returns:
        float: The result of the operation.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Example usage:
print(reverse_text("Hello"))  # Output: olleH
print(simple_calculator(10, 2, '+'))  # Output: 12
print(simple_calculator(10, 2, '-'))  # Output: 8
print(simple_calculator(10, 2, '*'))  # Output: 20
print(simple_calculator(10, 2, '/'))  # Output: 5.0
print(simple_calculator(10, 0, '/'))  # Output: Cannot divide by zero
