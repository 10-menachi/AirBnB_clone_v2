#!/usr/bin/python3

"""
This is a simple Flask app that returns a string.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Returns a string
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    Returns a string
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    Displays n only if it is an integer
    """
    return '%d is a number' % int(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
