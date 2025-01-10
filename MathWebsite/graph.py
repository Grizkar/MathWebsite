import numpy as np
import sympy as sp
import plotly.graph_objects as go

def parse_function(func_str):
    """
    This function parses the function string into a sympy expression.
    """
    try:
        if 'piecewise' in func_str.lower():
            # Handle piecewise function parsing
            func = sp.sympify(func_str)
        else:
            func = sp.sympify(func_str)  # Convert string to a sympy expression
        return func
    except Exception as e:
        return f"Error: {str(e)}"

def plot_function(func_str, x_range=(-10, 10)):
    """
    This function plots the graph of the given function string.
    """
    x = sp.Symbol('x')
    func = parse_function(func_str)
    if isinstance(func, str):  # If there's an error in parsing
        return func

    x_vals = np.linspace(*x_range, 500)
    y_vals = []

    for val in x_vals:
        try:
            y = func.evalf(subs={x: val})  # Evaluate the function for each x value
            y_vals.append(float(y))
        except (ZeroDivisionError, ValueError):
            y_vals.append(None)

    fig = go.Figure()
    fig.add_scatter(x=x_vals, y=y_vals, mode='lines', name=func_str)
    fig.update_layout(
        title="Graph of the Function",
        xaxis_title="x",
        yaxis_title="y",
        showlegend=True
    )

    return fig.to_html(full_html=False)

def solve_function(func_str, solve_for=None):
    x = sp.Symbol('x')
    func = parse_function(func_str)
    if isinstance(func, str):
        return func
    if solve_for is None:
        return "Error: 'solve_for' value must be provided for evaluation."
    if isinstance(solve_for, str):
        solve_for = solve_for.lower()
        if solve_for == 'roots':
            try:
                roots = sp.solve(func, x)
                return roots
            except Exception as e:
                return f"Error finding roots: {e}"
        elif solve_for == 'derivative':
            try:
                derivative = sp.diff(func, x)
                return derivative
            except Exception as e:
                return f"Error calculating derivative: {e}"
        else:
            return "Error: 'solve_for' must be 'roots' or 'derivative'."
    try:
        solve_for_value = float(solve_for)
        y_val = func.evalf(subs={x: solve_for_value})
        rounded_y_val = round(y_val, 2)
        return rounded_y_val
    except ValueError:
        return "Error: 'solve_for' value is not a valid number."
    except Exception as e:
        return f"Error evaluating function: {e}"