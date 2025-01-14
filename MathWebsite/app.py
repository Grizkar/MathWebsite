from flask import Flask, render_template, request
from graph import plot_function
from solve import solve_polynomial, solve_rational, solve_trigonometric, solve_exponential, solve_logarithmic, solve_piecewise, solve_absolute_value, solve_square_root
from calculate import calculate
import sympy as sp

# Initialize the Flask app
app = Flask(__name__)

# Route for the homepage (index page)
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Route for the calculator page, handles both GET and POST requests
@app.route('/calculate', methods=['GET', 'POST'])
def calculate_route():
    result = None
    if request.method == 'POST':
        # Retrieve the expression entered by the user from the form
        expression = request.form['expression']
        # Pass the expression to the calculate function and get the result
        result = calculate(expression)
    # Render the calculate.html template, passing the result if available
    return render_template('calculate.html', result=result)

# Route for the graphing page, handles both GET and POST requests
@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
        # Retrieve the function type, function string, and range values from the form
        func_type = request.form.get('function_type')
        func_str = request.form.get('function')
        min_x = request.form.get('min_x', -10)
        max_x = request.form.get('max_x', 10)
        try:
            # Try to convert the range values to floats
            min_x = float(min_x)
            max_x = float(max_x)
        except ValueError:
            # If conversion fails, return an error message
            return render_template('graph.html', error="Invalid range values.")
        if func_type and func_str:
            # Call the plot_function to generate the graph HTML
            graph_html = plot_function(func_str, func_type, x_range=(min_x, max_x))
            # Render the graph.html template, passing the graph HTML and function string
            return render_template('graph.html', graph_html=graph_html, func_str=func_str)
        else:
            # If function type or function string is missing, show an error
            return render_template('graph.html', error="Both function type and function are required.")
    # Render the graph.html template for GET requests, with no graph or error
    return render_template('graph.html', graph_html=None, error=None)

# Route for the solving page, handles both GET and POST requests
@app.route('/solve', methods=['GET', 'POST'])
def solve():
    if request.method == 'POST':
        # Retrieve the function, operation, and evaluation values from the form
        function = request.form.get('function')
        operation = request.form.get('operation')
        evaluation = request.form.get('evaluation')
        function_type = request.form.get('function_type')
        if evaluation:
            try:
                # Try to convert the evaluation to a float, else use sympy to parse it
                evaluation = float(evaluation)
            except ValueError:
                evaluation = sp.sympify(evaluation)
        # Mapping of function types to corresponding solvers
        solvers = {
            'polynomial':solve_polynomial,
            'rational':solve_rational,
            'trigonometric':solve_trigonometric,
            'exponential':solve_exponential,
            'logarithmic':solve_logarithmic,
            'piecewise':solve_piecewise,
            'absolute_value':solve_absolute_value,
            'square_root':solve_square_root,
        }
        # Get the appropriate solver function based on the selected function type
        solver = solvers.get(function_type)
        if not solver:
            # If no solver found, display an error
            result = f"Error: Unsupported function type '{function_type}'."
        else:
            # Call the solver with the function, operation, and evaluation
            result = solver(function, operation, evaluation)
        # Render the solve.html template, passing necessary data including result
        return render_template('solve.html', function=function, operation=operation, evaluation=evaluation, result=result, function_type=function_type)
    # Render the solve.html template for GET requests, with no result
    return render_template('solve.html')

# Start the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)