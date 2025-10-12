from typing import Union

def safe_divide(numerator: Union[str, float, int], denominator: Union[str, float, int]) -> str:
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is {result}"
