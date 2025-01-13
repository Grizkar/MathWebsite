import numpy as np
import sympy as sp
import plotly.graph_objects as go

def parse_function(func_str, func_type):
    x = sp.symbols('x')
    try:
        if func_type == 'polynomial':
            func = sp.sympify(func_str)
        elif func_type == 'rational':
            func = sp.sympify(func_str)
        elif func_type == 'trigonometric':
            func = sp.sympify(func_str)
        elif func_type == 'exponential':
            base, exponent = func_str.split('^')
            func = sp.exp(sp.sympify(base) * x)**sp.sympify(exponent)
        elif func_type == 'logarithmic':
            func = sp.log(x)
        elif func_type == 'piecewise':
            func = sp.Piecewise((x, x > 0), (-x, x <= 0))
        elif func_type == 'absolute_value':
            func = sp.Abs(x)
        elif func_type == 'square_root':
            func = sp.sqrt(x)
        else:
            raise ValueError("Invalid function type")
        return func
    except Exception as e:
        return f"Error: {str(e)}"
    
def plot_function(func_str, func_type, x_range=(-10, 10)):
    x = sp.symbols('x')
    func = parse_function(func_str, func_type)
    if isinstance(func, str):
        return func
    x_vals = np.linspace(*x_range, 500)
    y_vals = []
    for val in x_vals:
        try:
            y = func.evalf(subs={x: val})
            y_vals.append(float(y))
        except (ZeroDivisionError, ValueError, TypeError):
            y_vals.append(None)
    fig = go.Figure()
    fig.add_scatter(x=x_vals, y=y_vals, mode='lines', name=func_str)
    fig.update_layout(
        title="Graph of the Function",
        xaxis_title="x",
        yaxis_title="f(x)",
        showlegend=True,
        plot_bgcolor='black',
        paper_bgcolor='#2a2a2a',
        font=dict(color='white'),
        xaxis=dict(
            showgrid=True,
            gridcolor='#444',
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#444',
        ),
        title_font=dict(size=20),
        margin=dict(l=50, r=50, t=50, b=50)
    )
    return fig.to_html(full_html=False)