from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Python Operations with Flask Routing and Views")

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return render_template('print.html', param=param)

@app.route('/count/<int:param>')
def count(param):
    return render_template('count.html', numbers=range(1, param+1))

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation."

    return render_template('math.html', result=result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
