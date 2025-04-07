from flask import Flask, render_template

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return """
    <h1>Python Operations with Flask Routing and Views</h1>
    """

# Print string view
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print to console
    return f"<p>{param}</p>"

# Count view
@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(1, param + 1))
    return f"<pre>{numbers}</pre>"

# Math view
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'plus':
        result = num1 + num2
    elif operation == 'minus':
        result = num1 - num2
    elif operation == 'times':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        result = num1 / num2
    elif operation == 'mod':
        result = num1 % num2
    else:
        return "Invalid operation."

    return f"<p>{num1} {operation} {num2} = {result}</p>"

if __name__ == '__main__':
    app.run(debug=True)
