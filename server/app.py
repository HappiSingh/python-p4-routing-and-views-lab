#!/usr/bin/env python3
import ipdb
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    nums = ""
    for num in range(parameter):
        nums = nums + str(num) + '\n'
    return nums
    
    

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    ans = 0
    if operation == '+':
        ans = num1 + num2
    elif operation == '-':
        ans = num1 - num2
    elif operation == '*':
        ans = num1 * num2
    elif operation == 'div':
        ans = num1 / num2
    elif operation == '%':
        ans = num1 % num2

    return str(ans)