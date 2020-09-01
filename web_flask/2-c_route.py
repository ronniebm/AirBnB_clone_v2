#!/usr/bin/python3
"""
starts a Flask web app.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """a script that starts a Flask
    web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route1():
    """a script that starts a Flask
    web application"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def route2(text):
    """It returns text passed by url"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
