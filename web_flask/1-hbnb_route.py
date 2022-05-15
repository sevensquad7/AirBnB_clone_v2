#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug="true", host="0.0.0.0", port=5000)
