def calculate(expression):
    try:
        allowed_characters = "0123456789+-*/().^"
        expression = expression.replace('^', '**')
        if any(c not in allowed_characters for c in expression):
            return "Error: Invalid characters in expression"
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception as e:
        return f"Error: {e}"