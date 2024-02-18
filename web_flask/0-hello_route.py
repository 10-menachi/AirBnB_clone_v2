#!/usr/bin/python3

"""
This is a simple Flask app that returns a string.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True)