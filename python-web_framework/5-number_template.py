from flask import Flask, render_template

# ... (Previous code)

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

# ... (Rest of the code)