import numpy as np
import sympy as sp
import plotly.graph_objects as go

# Function to parse the string representation of a mathematical function based on its type
def parse_function(func_str, func_type):
    x = sp.symbols('x')
    try:
        # Parse different types of functions based on the specified 'func_type'
        if func_type == 'polynomial':
            func = sp.sympify(func_str)  # Directly convert the string into a polynomial
        elif func_type == 'rational':
            func = sp.sympify(func_str)  # Directly convert the string into a rational function
        elif func_type == 'trigonometric':
            func = sp.sympify(func_str)  # Directly convert the string into a trigonometric function
        elif func_type == 'exponential':
            # For exponential functions, handle the base and exponent separately
            base, exponent = func_str.split('^')
            func = sp.exp(sp.sympify(base) * x)**sp.sympify(exponent)
        elif func_type == 'logarithmic':
            func = sp.log(x)  # Convert the function to a logarithmic form
        elif func_type == 'piecewise':
            func = sp.Piecewise(x)  # Handle piecewise functions (may need further refinement)
        elif func_type == 'absolute_value':
            func = sp.Abs(x)  # Convert to absolute value function
        elif func_type == 'square_root':
            func = sp.sqrt(x)  # Convert to square root function
        else:
            raise ValueError("Invalid function type")  # Raise an error if function type is invalid
        return func  # Return the parsed function
    except Exception as e:
        return f"Error: {str(e)}"  # Return error message in case of parsing failure

# Function to plot the graph of the parsed function
def plot_function(func_str, func_type, x_range=(-10, 10)):
    x = sp.symbols('x')  # Define the symbol for 'x'
    func = parse_function(func_str, func_type)  # Parse the function string into a usable function object
    if isinstance(func, str):  # Check if there was an error during parsing
        return func  # Return error message if function parsing failed
    
    # Generate x-values for the graph (500 points between the given range)
    x_vals = np.linspace(*x_range, 500)
    y_vals = []  # List to store y-values for plotting
    
    # Evaluate the function for each x-value
    for val in x_vals:
        try:
            y = func.evalf(subs={x: val})  # Evaluate the function for the current x-value
            y_vals.append(float(y))  # Add the result to the y-values list
        except (ZeroDivisionError, ValueError, TypeError):  # Handle possible errors during evaluation
            y_vals.append(None)  # Append None for invalid results (e.g., division by zero)
    
    # Create a Plotly figure to plot the graph
    fig = go.Figure()
    fig.add_scatter(x=x_vals, y=y_vals, mode='lines', name=func_str)  # Plot the function as a line chart
    fig.update_layout(
        title="Graph of the Function",  # Set the graph title
        xaxis_title="x",  # Set the x-axis label
        yaxis_title="f(x)",  # Set the y-axis label
        showlegend=True,  # Display legend
        plot_bgcolor='black',  # Set the background color of the plot area
        paper_bgcolor='#2a2a2a',  # Set the background color of the paper area
        font=dict(color='white'),  # Set the font color to white for visibility
        xaxis=dict(
            showgrid=True,  # Show grid lines on the x-axis
            gridcolor='#444',  # Set the grid line color
        ),
        yaxis=dict(
            showgrid=True,  # Show grid lines on the y-axis
            gridcolor='#444',  # Set the grid line color
        ),
        title_font=dict(size=20),  # Set the font size for the title
        margin=dict(l=50, r=50, t=50, b=50)  # Set the plot margins
    )
    
    # Return the plot as HTML to embed in a web page
    return fig.to_html(full_html=False)