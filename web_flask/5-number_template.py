#!/usr/bin/python3
"""
starts a Flask web app.
"""
import numbers
from flask import Flask, render_template
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


@app.route("/python", strict_slashes=False)
def route3():
    """It returns text passed by url"""
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def route4(text):
    """It returns text passed by url"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def route5(n):
    """It returns text passed by url"""
    if isinstance(n, numbers.Number):
        return "{} is a number".format(n)
    pass


@app.route("/number_template/<int:n>", strict_slashes=False)
def route6(n):
    """It returns text passed by url"""
    if isinstance(n, numbers.Number):
        return render_template('5-number.html', num=n)
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
