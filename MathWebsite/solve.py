import sympy as sp

def solve_polynomial(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        if operation.lower() == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation.lower() == 'derivative':
            try:
                derivative = sp.diff(func, x)
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif type(evaluation) == int or type(evaluation) == float:
            try:
                value = func.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"
    
def solve_rational(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        numerator, denominator = sp.fraction(func)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solve(numerator, x)
                valid_roots = [r for r in roots if denominator.subs(x, r) != 0]
                return valid_roots if valid_roots else "No valid roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation and operation.lower() == 'derivative':
            try:
                numerator_derivative = sp.diff(numerator, x)
                denominator_derivative = sp.diff(denominator, x)
                derivative = (numerator_derivative * denominator - numerator * denominator_derivative) / denominator**2
                return sp.simplify(derivative)
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif type(evaluation) == int or type(evaluation) == float:
            try:
                if denominator.subs(x, evaluation) == 0:
                    return "Error: Denominator is zero at this point"
                value = func.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"

def solve_trigonometric(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solveset(func, x, domain=sp.Interval(0, 2 * sp.pi))
                roots = [sp.simplify(r) for r in roots]
                return list(roots) if roots else "No roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation and operation.lower() == 'derivative':
            try:
                derivative = sp.diff(func, x)
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif evaluation is not None:
            try:
                value = func.evalf(subs={x: sp.N(evaluation)})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
        else:
            return "Error: Unsupported operation or missing evaluation point."
    except Exception as e:
        return f"Error parsing function: {e}"

def solve_exponential(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots if roots else "No roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation and operation.lower() == 'derivative':
            try:
                derivative = sp.diff(func, x)
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif evaluation is not None:
            try:
                value = func.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"
    
def solve_logarithmic(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots if roots else "No roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        
        elif operation and operation.lower() == 'derivative':
            try:
                derivative = sp.diff(func, x)
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif evaluation is not None:
            try:
                value = func.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"
    
def solve_piecewise(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots if roots else "No roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation and operation.lower() == 'derivative':
            try:
                derivative = sp.diff(func, x)
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif evaluation is not None:
            try:
                value = func.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"

def solve_absolute_value(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        g = sp.Abs(func)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots if roots else "No roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation and operation.lower() == 'derivative':
            try:
                derivative = sp.diff(g, x)
                simplified_derivative = sp.simplify(derivative)
                return simplified_derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif type(evaluation) == int or type(evaluation) == float:
            try:
                value = g.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"

def solve_square_root(func_str, operation=None, evaluation=None):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        if operation and operation.lower() == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots if roots else "No roots found"
            except Exception as e:
                return f"Error finding roots: {e}"
        elif operation and operation.lower() == 'derivative':
            try:
                derivative = sp.diff(func, x) / (2 * sp.sqrt(func))
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        elif type(evaluation) == int or type(evaluation) == float:
            try:
                value = func.evalf(subs={x: evaluation})
                return round(value, 2)
            except Exception as e:
                return f"Error evaluating function: {e}"
    except Exception as e:
        return f"Error parsing function: {e}"