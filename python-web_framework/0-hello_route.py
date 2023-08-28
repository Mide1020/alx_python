"""
Flask Web Application

This script sets up a simple Flask web application with a single route
that displays "Hello HBNB!" when accessed.

Routes:
    /: Display "Hello HBNB!"

Usage:
    Run this script to start the Flask web application. Access the application
    by opening a web browser and navigating to http://localhost:5000/.

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ('/')

    Returns:
        str: The message "Hello HBNB!" to be displayed in the browser.
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
