def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please provide numeric values for numerator and denominator."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    return f"Result: {num:g} / {den:g} = {result:g}"
