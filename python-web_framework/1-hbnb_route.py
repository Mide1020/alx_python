"""
Flask Web Application

This script sets up a simple Flask web application with two routes: one that
displays "Hello HBNB!" at the root URL ('/') and another that displays "HBNB"
at the '/hbnb' URL.

Routes:
    /: Display "Hello HBNB!"
    /hbnb: Display "HBNB"

Usage:
    Run this script to start the Flask web application. Access the application
    by opening a web browser and navigating to http://localhost:5000/ for
    "Hello HBNB!" or http://localhost:5000/hbnb for "HBNB".

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ('/').

    Returns:
        str: The message "Hello HBNB!" to be displayed in the browser.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' URL.

    Returns:
        str: The message "HBNB" to be displayed in the browser.
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
