"""
Flask Web Application

This script sets up a Flask web application with multiple routes for different
messages and text display.

Routes:
    /: Display "Hello HBNB!"
    /hbnb: Display "HBNB"
    /c/<text>: Display "C " followed by the value of the text variable (replace
                underscore _ symbols with a space)

Usage:
    Run this script to start the Flask web application. Access the application
    by opening a web browser and navigating to different routes:
    - http://localhost:5000/ for "Hello HBNB!"
    - http://localhost:5000/hbnb for "HBNB"
    - http://localhost:5000/c/your_text_here for "C your text here"
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

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for URLs with the '/c/<text>' pattern.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The message "C " followed by the value of the text variable, with
             underscores (_) replaced by spaces.
    """
    return "C " + text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
