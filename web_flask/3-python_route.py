#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """displays “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """displays “C ” followed by the value of the text variable"""
    return 'C ' + text.replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonis(text='is cool'):
    """displays “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')