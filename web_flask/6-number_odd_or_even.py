#!/usr/bin/python3
"""script that starts a flash application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cis(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyis(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n: int):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_odd_even(n):
    odd_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
