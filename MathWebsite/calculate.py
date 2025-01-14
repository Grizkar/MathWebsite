import math

# Function to evaluate a mathematical expression
def calculate(expression):
    try:
        # Define the allowed characters to ensure the input is safe
        allowed_characters = "0123456789+-*/().^sqrt"
        
        # Replace '^' with '**' for Python-style exponentiation
        expression = expression.replace('^', '**')
        
        # Replace 'sqrt' with 'math.sqrt' to use the math module's square root function
        expression = expression.replace('sqrt', 'math.sqrt')
        
        # Check if the expression contains any invalid characters (not in allowed list)
        if any(c not in allowed_characters and not c.isalpha() for c in expression):
            return "Error: Invalid characters in expression"
        
        # Evaluate the expression safely using eval() and return the result
        result = eval(expression)
        return result
    except ZeroDivisionError:
        # Return an error message for division by zero
        return "Error: Cannot divide by zero"
    except Exception as e:
        # Return any other error messages that might occur during evaluation
        return f"Error: {e}"