#!/usr/bin/python3
from flask import Flask
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

app = Flask(__name__)


@app.route('/')
def index():
    """Return Hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug="true",host="0.0.0.0", port=5000)
