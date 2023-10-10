#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        operation = f"{a} / {b} = {result}"
    except ZeroDivisionError:
        result = None
        operation = f"{a} / {b} is undefined (division by zero)"
    finally:
        print("Inside result: {}".format(result))
        if result is not None:
            print("{}".format(operation))

# Example usage:
a = 10
b = 2
safe_print_division(a, b)
