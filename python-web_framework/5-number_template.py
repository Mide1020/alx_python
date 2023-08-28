"""
Flask Web Application

This script sets up a Flask web application with multiple routes for displaying
different messages and HTML content based on URL patterns.

Routes:
    /: Display "Hello HBNB!"
    /hbnb: Display "HBNB"
    /c/<text>: Display "C ", followed by the value of the text variable (replace
                underscore _ symbols with a space)
    /python/<text>: Display "Python ", followed by the value of the text variable
                    (replace underscore _ symbols with a space). If text is not
                    provided, the default value "is cool" is used.
    /number/<n>: Display "<n> is a number" only if n is an integer
    /number_template/<n>: Display an HTML page with the text "Number: n" inside
                          an H1 tag in the BODY, only if n is an integer.

Usage:
    Run this script to start the Flask web application. Access the application
    by opening a web browser and navigating to different routes:
    - http://localhost:5000/ for "Hello HBNB!"
    - http://localhost:5000/hbnb for "HBNB"
    - http://localhost:5000/c/your_text_here for "C your text here"
    - http://localhost:5000/python/your_text_here for "Python your text here"
    - http://localhost:5000/python/ for "Python is cool"
    - http://localhost:5000/number/42 for "42 is a number"
    - http://localhost:5000/number_template/42 for an HTML page with "Number: 42"

Note:
    Ensure that the 'number_template.html' file is located in the same directory
    as this script for correct rendering of the /number_template/<n> route.

"""

from flask import Flask, render_template

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

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route handler for URLs with the '/python/<text>' pattern.

    Args:
        text (str, optional): The text provided in the URL. If not provided, uses
                              the default value "is cool".

    Returns:
        str: The message "Python " followed by the value of the text variable, with
             underscores (_) replaced by spaces.
    """
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler for URLs with the '/number/<n>' pattern.

    Args:
        n (int): The number provided in the URL.

    Returns:
        str: The message "<n> is a number".
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for URLs with the '/number_template/<n>' pattern.

    Args:
        n (int): The number provided in the URL.

    Returns:
        str: An HTML page with an H1 tag containing "Number: n".
    """
    return render_template('number_template.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)