from flask import Flask, render_template, request
from graph import plot_function
from solve import solve_polynomial, solve_rational, solve_trigonometric, solve_exponential, solve_logarithmic, solve_piecewise, solve_absolute_value, solve_square_root, solve_polynomial_with_exponent
import sympy as sp
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
        func_str = request.form.get('function')
        graph_html = plot_function(func_str)
        return render_template('graph.html', graph_html=graph_html, func_str=func_str)
    return render_template('graph.html', graph_html=None)

@app.route('/solve', methods=['GET', 'POST'])
def solve():
    if request.method == 'POST':
        function = request.form.get('function')
        operation = request.form.get('operation')
        evaluation = request.form.get('evaluation')
        function_type = request.form.get('function_type')
        if evaluation:
            try:
                evaluation = float(evaluation)
            except ValueError:
                evaluation = sp.sympify(evaluation)
        solvers = {
            'polynomial':solve_polynomial,
            'rational':solve_rational,
            'trigonometric':solve_trigonometric,
            'exponential':solve_exponential,
            'logarithmic':solve_logarithmic,
            'piecewise':solve_piecewise,
            'absolute_value':solve_absolute_value,
            'square_root':solve_square_root,
            'polynomial_with_exponent':solve_polynomial_with_exponent
        }
        solver = solvers.get(function_type)
        if not solver:
            result = f"Error: Unsupported function type '{function_type}'."
        else:
            result = solver(function, operation, evaluation)
        return render_template('solve.html', function=function, operation=operation, evaluation=evaluation, result=result, function_type=function_type)
    return render_template('solve.html')

if __name__ == "__main__":
    app.run(debug=True)