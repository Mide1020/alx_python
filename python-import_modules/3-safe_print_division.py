#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        if result is not None:
            print("{} / {} = {}".format(a, b, result))

# Example usage:
a = 10
b = 2
safe_print_division(a, b)
