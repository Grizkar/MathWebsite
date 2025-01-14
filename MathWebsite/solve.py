import sympy as sp

# Function to solve a polynomial equation (finding roots, derivatives, or evaluations)
def solve_polynomial(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        if operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(func, x)  # Find the roots of the polynomial
                return roots  # Return the roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(func, x)  # Differentiate the function
                return derivative  # Return the derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif type(evaluation) == int or type(evaluation) == float:  # If an evaluation point is given
            try:
                value = func.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve a rational function equation (handling roots, derivatives, or evaluations)
def solve_rational(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        numerator, denominator = sp.fraction(func)  # Separate the numerator and denominator
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(numerator, x)  # Find the roots of the numerator
                valid_roots = [r for r in roots if denominator.subs(x, r) != 0]  # Filter out roots where denominator is zero
                return valid_roots if valid_roots else "No valid roots found"  # Return valid roots or a message if no valid roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                numerator_derivative = sp.diff(numerator, x)  # Differentiate the numerator
                denominator_derivative = sp.diff(denominator, x)  # Differentiate the denominator
                derivative = (numerator_derivative * denominator - numerator * denominator_derivative) / denominator**2  # Apply the quotient rule
                return sp.simplify(derivative)  # Return the simplified derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif type(evaluation) == int or type(evaluation) == float:  # If an evaluation point is given
            try:
                if denominator.subs(x, evaluation) == 0:  # Check if denominator is zero at the evaluation point
                    return "Error: Denominator is zero at this point"  # Return an error if denominator is zero
                value = func.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve a trigonometric function equation (handling roots, derivatives, or evaluations)
def solve_trigonometric(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solveset(func, x, domain=sp.Interval(0, 2 * sp.pi))  # Find the roots within one period
                roots = [sp.simplify(r) for r in roots]  # Simplify the roots
                return list(roots) if roots else "No roots found"  # Return the roots or a message if no roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(func, x)  # Differentiate the function
                return derivative  # Return the derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif evaluation is not None:  # If an evaluation point is given
            try:
                value = func.evalf(subs={x: sp.N(evaluation)})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
        else:
            return "Error: Unsupported operation or missing evaluation point."  # Return an error if operation is unsupported or missing evaluation
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve an exponential function equation (handling roots, derivatives, or evaluations)
def solve_exponential(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(func, x)  # Find the roots of the exponential function
                return roots if roots else "No roots found"  # Return the roots or a message if no roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(func, x)  # Differentiate the function
                return derivative  # Return the derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif evaluation is not None:  # If an evaluation point is given
            try:
                value = func.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve a logarithmic function equation (handling roots, derivatives, or evaluations)
def solve_logarithmic(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(func, x)  # Find the roots of the logarithmic function
                return roots if roots else "No roots found"  # Return the roots or a message if no roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(func, x)  # Differentiate the function
                return derivative  # Return the derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif evaluation is not None:  # If an evaluation point is given
            try:
                value = func.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve a piecewise function equation (handling roots, derivatives, or evaluations)
def solve_piecewise(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(func, x)  # Find the roots of the piecewise function
                return roots if roots else "No roots found"  # Return the roots or a message if no roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(func, x)  # Differentiate the function
                return derivative  # Return the derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif evaluation is not None:  # If an evaluation point is given
            try:
                value = func.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve an absolute value function equation (handling roots, derivatives, or evaluations)
def solve_absolute_value(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        g = sp.Abs(func)  # Apply absolute value
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(func, x)  # Find the roots of the absolute value function
                return roots if roots else "No roots found"  # Return the roots or a message if no roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(g, x)  # Differentiate the absolute value function
                simplified_derivative = sp.simplify(derivative)  # Simplify the derivative
                return simplified_derivative  # Return the simplified derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif type(evaluation) == int or type(evaluation) == float:  # If an evaluation point is given
            try:
                value = g.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails

# Function to solve a square root function equation (handling roots, derivatives, or evaluations)
def solve_square_root(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')  # Define symbolic variable x
    try:
        func = sp.sympify(func_str)  # Convert the function string into a sympy expression
        if operation and operation.lower() == 'roots':  # If the operation is to find the roots
            try:
                roots = sp.solve(func, x)  # Find the roots of the square root function
                return roots if roots else "No roots found"  # Return the roots or a message if no roots
            except Exception as e:
                return f"Error finding roots: {e}"  # Return an error if finding roots fails
        elif operation and operation.lower() == 'derivative':  # If the operation is to find the derivative
            try:
                derivative = sp.diff(func, x) / (2 * sp.sqrt(func))  # Differentiate the square root function
                return derivative  # Return the derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"  # Return an error if differentiation fails
        elif type(evaluation) == int or type(evaluation) == float:  # If an evaluation point is given
            try:
                value = func.evalf(subs={x: evaluation})  # Evaluate the function at the given point
                return round(value, 2)  # Return the evaluated value rounded to 2 decimal places
            except Exception as e:
                return f"Error evaluating function: {e}"  # Return an error if evaluation fails
    except Exception as e:
        return f"Error parsing function: {e}"  # Return an error if the function parsing fails